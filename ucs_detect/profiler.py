"""Resource profiling for terminal test runs.

Samples CPU% and RSS memory of a process tree at regular intervals,
saves CSV data, and generates per-terminal matplotlib graphs.
"""
from __future__ import annotations

import csv
import threading
import time
from pathlib import Path

import psutil  # type: ignore[import-untyped]


class ProfileSession:
    """Samples CPU% and RSS of a process tree during a terminal test."""

    def __init__(self, sw_name: str, pid: int, interval: float = 1.0):
        self._sw_name = sw_name
        self._pid = pid
        self._interval = interval
        self._stop_event = threading.Event()
        self._thread: threading.Thread | None = None
        self._samples: list[tuple[float, float, float]] = []

    def start(self) -> None:
        """Begin sampling in a background thread."""
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._sample_loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        """Stop sampling and join the background thread."""
        self._stop_event.set()
        if self._thread is not None:
            self._thread.join(timeout=5)

    def _sample_loop(self) -> None:
        t0 = time.monotonic()
        try:
            proc = psutil.Process(self._pid)
            proc.cpu_percent(interval=None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return

        while not self._stop_event.is_set():
            elapsed = time.monotonic() - t0
            try:
                with proc.oneshot():
                    cpu = proc.cpu_percent(interval=None)
                    rss_mb = proc.memory_info().rss / (1024 * 1024)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                cpu = 0.0
                rss_mb = 0.0
            self._samples.append((elapsed, cpu, rss_mb))
            self._stop_event.wait(self._interval)

    def samples(self) -> list[tuple[float, float, float]]:
        """Return collected samples as (elapsed_seconds, cpu_pct, rss_mb)."""
        return list(self._samples)

    def write_csv(self, path: Path) -> None:
        """Write samples to CSV file."""
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["elapsed_s", "cpu_pct", "rss_mb"])
            writer.writerows(self._samples)

    def to_dict(self) -> dict:
        """Return samples as a dict suitable for YAML embedding."""
        return {
            "elapsed_s": [s[0] for s in self._samples],
            "cpu_pct": [s[1] for s in self._samples],
            "rss_mb": [s[2] for s in self._samples],
        }


def generate_graphs(
    profiles: dict[str, ProfileSession],
    output_dir: Path,
) -> None:
    """Generate per-terminal CPU and memory graphs with shared scales."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt  # type: ignore[import-untyped]
        import matplotlib.ticker as ticker  # type: ignore[import-untyped]
    except ImportError:
        return

    if not profiles:
        return

    all_cpu_max = 0.0
    all_mem_min = float("inf")
    all_mem_max = 0.0
    all_durations: list[float] = []

    for session in profiles.values():
        samples = session.samples()
        if not samples:
            continue
        duration = samples[-1][0]
        all_durations.append(duration)
        for _, cpu, rss in samples:
            if cpu > all_cpu_max:
                all_cpu_max = cpu
            if rss < all_mem_min:
                all_mem_min = rss
            if rss > all_mem_max:
                all_mem_max = rss

    if not all_durations:
        return

    time_max = max(all_durations)
    time_mean = sum(all_durations) / len(all_durations)

    if all_cpu_max <= 0:
        all_cpu_max = 100.0
    if all_mem_max <= 0:
        all_mem_max = 100.0
    if all_mem_min >= all_mem_max:
        all_mem_min = 0.0

    cpu_ymax = all_cpu_max * 1.1
    mem_ymin = max(0, all_mem_min * 0.9)
    mem_ymax = all_mem_max * 1.1

    output_dir.mkdir(parents=True, exist_ok=True)

    for sw_name, session in profiles.items():
        samples = session.samples()
        if not samples:
            continue

        elapsed = [s[0] for s in samples]
        cpu_vals = [s[1] for s in samples]
        mem_vals = [s[2] for s in samples]

        safe_name = "".join(c if c.isalnum() or c in "-_" else "_" for c in sw_name)

        fig, (ax_cpu, ax_mem) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
        fig.suptitle(f"{sw_name} \u2014 Resource Profile", fontsize=12, fontweight="bold")

        ax_cpu.plot(elapsed, cpu_vals, color="#2563eb", linewidth=1.0)
        ax_cpu.set_ylabel("CPU %")
        ax_cpu.set_ylim(0, cpu_ymax)
        ax_cpu.axvline(x=time_mean, color="red", linestyle="--", linewidth=0.8,
                       alpha=0.7)
        ax_cpu.grid(True, alpha=0.3)
        ax_cpu.set_xscale("log")
        ax_cpu.xaxis.set_major_formatter(ticker.ScalarFormatter())

        ax_mem.plot(elapsed, mem_vals, color="#16a34a", linewidth=1.0)
        ax_mem.set_ylabel("RSS (MB)")
        ax_mem.set_xlabel("Time (seconds, log scale)")
        ax_mem.set_ylim(mem_ymin, mem_ymax)
        ax_mem.axvline(x=time_mean, color="red", linestyle="--", linewidth=0.8,
                       alpha=0.7)
        ax_mem.grid(True, alpha=0.3)
        ax_mem.set_xscale("log")
        ax_mem.xaxis.set_major_formatter(ticker.ScalarFormatter())

        ax_cpu.set_xlim(left=max(elapsed[0], 0.1), right=time_max)
        ax_mem.set_xlim(left=max(elapsed[0], 0.1), right=time_max)

        plt.tight_layout()
        png_path = output_dir / f"{safe_name}_profile.png"
        fig.savefig(str(png_path), dpi=100)
        plt.close(fig)
