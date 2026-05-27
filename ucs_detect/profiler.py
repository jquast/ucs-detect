"""Resource profiling for terminal test runs.

Samples CPU% and RSS memory of a process tree at regular intervals,
saves CSV data, and generates per-terminal matplotlib graphs.
"""
from __future__ import annotations

import csv
import threading
import time
from pathlib import Path


class ProfileSession:
    """Samples CPU% and RSS of a process tree during a terminal test."""

    def __init__(self, sw_name: str, pid: int, interval: float = 1.0,
                 program: str | None = None):
        self._sw_name = sw_name
        self._pid = pid
        self._interval = interval
        self._program = program  # if set, only profile processes matching this name
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

    def _sample_process_tree(self, root) -> tuple[float, float]:
        """Sum CPU% and RSS across *root* and matching descendants.

        If ``_program`` is set, only processes whose ``name()`` equals
        ``_program`` are included; the root process itself is always
        excluded when ``_program`` is set (the root is the launcher, not
        the terminal)."""
        import psutil  # type: ignore[import-untyped]
        cpu_total = 0.0
        rss_total = 0.0

        try:
            procs = [root] + root.children(recursive=True)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return 0.0, 0.0

        for proc in procs:
            if self._program and proc.pid == self._pid:
                continue  # skip launcher, only profile the named child
            try:
                name = proc.name()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
            if self._program and name != self._program:
                continue
            try:
                with proc.oneshot():
                    cpu_total += proc.cpu_percent(interval=None)
                    rss_total += proc.memory_info().rss
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        return cpu_total, rss_total / (1024 * 1024)

    def _sample_loop(self) -> None:
        import psutil  # type: ignore[import-untyped]
        t0 = time.monotonic()
        try:
            root = psutil.Process(self._pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return

        # Initialize cpu_percent baselines for all tracked processes
        try:
            procs = [root] + root.children(recursive=True)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            procs = [root]
        for proc in procs:
            if self._program and proc.pid == self._pid:
                continue
            if self._program:
                try:
                    if proc.name() != self._program:
                        continue
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            try:
                proc.cpu_percent(interval=None)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        while not self._stop_event.is_set():
            elapsed = time.monotonic() - t0
            try:
                cpu, rss_mb = self._sample_process_tree(root)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                break  # process tree vanished, stop sampling
            self._samples.append((elapsed, cpu, rss_mb))
            self._stop_event.wait(self._interval)

    def samples(self) -> list[tuple[float, float, float]]:
        """Return collected samples (elapsed_seconds, cpu_pct, rss_mb).

        Trailing entries with zero RSS (process-exit artifacts) are stripped."""
        result = list(self._samples)
        # drop trailing zero-RSS entries from process termination cliff
        while result and result[-1][2] <= 0.0:
            result.pop()
        return result

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
    """Generate per-terminal CPU and memory graphs with shared log scales.

    Writes ``{safe}_cpu.png`` and ``{safe}_rss.png`` for each terminal,
    plus aggregate ``all_cpu.png`` and ``all_rss.png`` showing all
    terminals overlaid.  All graphs share the same Y-axis range (log
    scale) and the same X-axis range (log scale, determined by the
    slowest terminal).  A red crosshair marks the global mean of both
    axes with a "---- mean average" label.
    """
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt  # type: ignore[import-untyped]
    except ImportError:
        return

    if not profiles:
        return

    safe_map = {}
    all_cpu_vals: list[float] = []
    all_rss_vals: list[float] = []
    all_durations: list[float] = []
    terminal_data: list[tuple[str, list[float], list[float], list[float]]] = []

    for sw_name, session in profiles.items():
        samples = session.samples()
        if not samples:
            continue
        elapsed = [s[0] for s in samples]
        cpu = [s[1] for s in samples]
        rss = [s[2] for s in samples]
        safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in sw_name)
        safe_map[sw_name] = safe
        all_durations.append(elapsed[-1])
        all_cpu_vals.extend(cpu)
        all_rss_vals.extend(rss)
        terminal_data.append((sw_name, elapsed, cpu, rss))

    if not terminal_data:
        return

    time_max = max(all_durations)
    time_mean = sum(all_durations) / len(all_durations)
    cpu_min = min(all_cpu_vals) if all_cpu_vals else 0.0
    cpu_max_val = max(all_cpu_vals) if all_cpu_vals else 100.0
    rss_min = min(all_rss_vals) if all_rss_vals else 0.0
    rss_max_val = max(all_rss_vals) if all_rss_vals else 100.0
    cpu_mean = sum(all_cpu_vals) / len(all_cpu_vals) if all_cpu_vals else 0.0
    rss_mean = sum(all_rss_vals) / len(all_rss_vals) if all_rss_vals else 0.0

    cpu_ymin = max(0, cpu_min - 0.5)
    cpu_ymax = cpu_max_val * 1.10 if cpu_max_val > 0 else 100
    rss_ymin = max(0, rss_min - 1)
    rss_ymax = rss_max_val * 1.10 if rss_max_val > 0 else 100

    output_dir.mkdir(parents=True, exist_ok=True)

    for sw_name, elapsed, cpu_vals, rss_vals in terminal_data:
        safe = safe_map[sw_name]
        xmin = max(elapsed[0], 0.1)

        for label, vals, ymin, ymax, color in [
            ("cpu", cpu_vals, cpu_ymin, cpu_ymax, "#2563eb"),
            ("rss", rss_vals, rss_ymin, rss_ymax, "#16a34a"),
        ]:
            fig, ax = plt.subplots(figsize=(10, 5))
            fig.suptitle(f"{sw_name} \u2014 {label.upper()} Profile",
                         fontsize=12, fontweight="bold")

            ax.plot(elapsed, vals, color=color, linewidth=1.0)
            ax.set_ylabel("CPU %" if label == "cpu" else "RSS (MB)")
            ax.set_xlabel("Time (seconds, log scale)")
            ax.set_xscale("log")
            ax.set_xlim(left=xmin, right=time_max)
            ax.set_ylim(bottom=ymin, top=ymax)
            ax.grid(True, alpha=0.3, which="both")

            mean_y = cpu_mean if label == "cpu" else rss_mean
            if mean_y > 0:
                ax.axhline(y=mean_y, color="red", linestyle="--",
                           linewidth=0.8, alpha=0.9)
                ax.text(time_max * 0.95, mean_y * 0.8,
                        "---- mean average", color="red", fontsize=7,
                        ha="right", va="top", alpha=0.7)
            ax.axvline(x=time_mean, color="red", linestyle="--",
                       linewidth=0.8, alpha=0.9)
            ax.text(time_mean * 1.05, ymax * 0.95,
                    "---- mean average", color="red", fontsize=7,
                    ha="left", va="top", alpha=0.7, rotation=90)

            plt.tight_layout()
            png_path = output_dir / f"{safe}_{label}.png"
            fig.savefig(str(png_path), dpi=100)
            plt.close(fig)

    cmap = plt.get_cmap("tab20")
    for label, ymin, ymax, ymean in [
        ("cpu", cpu_ymin, cpu_ymax, cpu_mean),
        ("rss", rss_ymin, rss_ymax, rss_mean),
    ]:
        fig, ax = plt.subplots(figsize=(14, 8))
        fig.suptitle(
            f"All Terminals \u2014 {label.upper()} Profile",
            fontsize=14, fontweight="bold")

        data_sorted = sorted(
            terminal_data,
            key=lambda t: max(t[2 if label == "cpu" else 3]),
            reverse=True,
        )

        for i, (sw_name, elapsed, cpu_vals, rss_vals) in enumerate(data_sorted):
            vals = cpu_vals if label == "cpu" else rss_vals
            peak = max(vals)
            color = cmap(i % 20)
            ax.plot(elapsed, vals, color=color, linewidth=0.8)
            ax.text(elapsed[-1] * 1.02, peak,
                    f"{sw_name} ({peak:.0f}{'%' if label == 'cpu' else 'MB'})",
                    color=color, fontsize=6, va="center")

        ax.set_ylabel("CPU %" if label == "cpu" else "RSS (MB)")
        ax.set_xlabel("Time (seconds, log scale)")
        ax.set_xscale("log")
        ax.set_xlim(left=0.1, right=time_max * 1.15)
        ax.set_ylim(bottom=ymin, top=ymax)
        ax.grid(True, alpha=0.3)

        if ymean > 0:
            ax.axhline(y=ymean, color="red", linestyle="--",
                       linewidth=0.8, alpha=0.9)
            ax.text(time_max * 1.05, ymean * 0.8,
                    "---- mean average", color="red", fontsize=7,
                    ha="right", va="top", alpha=0.7)
        ax.axvline(x=time_mean, color="red", linestyle="--",
                   linewidth=0.8, alpha=0.9)
        ax.text(time_mean * 1.05, ymax * 0.7,
                "---- mean average", color="red", fontsize=7,
                ha="left", va="top", alpha=0.7, rotation=90)

        plt.tight_layout()
        png_path = output_dir / f"all_{label}.png"
        fig.savefig(str(png_path), dpi=150)
        plt.close(fig)


def compute_resource_scores(
    profiles: dict[str, ProfileSession],
) -> dict[str, float]:
    """Return a 0--100 resource score for each terminal.

    Each terminal's mean CPU%, mean RSS (MB), and total run duration are
    scored individually so that the global minimum maps to 100, the global
    mean to 50, and the global maximum to 0.  The three sub-scores are
    averaged to produce a composite Resources score.
    """
    if len(profiles) < 2:
        return {name: 50.0 for name in profiles}

    metrics: dict[str, tuple[float, float, float]] = {}
    for name, session in profiles.items():
        samples = session.samples()
        if not samples:
            continue
        cpu_vals = [s[1] for s in samples]
        rss_vals = [s[2] for s in samples]
        duration = samples[-1][0]
        metrics[name] = (
            sum(cpu_vals) / len(cpu_vals),
            sum(rss_vals) / len(rss_vals),
            duration,
        )

    if len(metrics) < 2:
        return {name: 50.0 for name in metrics}

    cpu_all = [m[0] for m in metrics.values()]
    rss_all = [m[1] for m in metrics.values()]
    dur_all = [m[2] for m in metrics.values()]

    def _sub_score(values, val):
        lo, hi, mid = min(values), max(values), sum(values) / len(values)
        span_lo = mid - lo
        span_hi = hi - mid
        if val <= mid:
            return 50.0 + 50.0 * (mid - val) / span_lo if span_lo > 0 else 50.0
        return 50.0 - 50.0 * (val - mid) / span_hi if span_hi > 0 else 50.0

    scores: dict[str, float] = {}
    for name, (cpu_m, rss_m, dur) in metrics.items():
        scores[name] = (
            _sub_score(cpu_all, cpu_m)
            + _sub_score(rss_all, rss_m)
            + _sub_score(dur_all, dur)
        ) / 3.0

    return scores
