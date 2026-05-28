"""Resource profiling for terminal test runs.

Samples CPU% and RSS memory of a process tree at regular intervals,
saves CSV data, and generates per-terminal matplotlib graphs.
"""
from __future__ import annotations

import csv
import colorsys
import os
import threading
import time
from pathlib import Path


class ProfileSession:
    """Samples CPU% and RSS of a process tree during a terminal test."""

    def __init__(self, sw_name: str, pid: int, interval: float = 1.0,
                 program: str | None = None,
                 extra_programs: list[str] | None = None,
                 exclude_names: set[str] | None = None):
        self._sw_name = sw_name
        self._pid = pid
        self._interval = interval
        self._program = program  # if set, only profile processes matching this name
        self._extra = extra_programs or []  # additional process names to capture
        self._exclude_names = exclude_names or {"ucs-detect", "re-run.py"}
        self._recovered = False  # True after root PID died and was re-discovered by name
        self._stop_event = threading.Event()
        self._thread: threading.Thread | None = None
        self._samples: list[tuple[float, float, float]] = []
        self._proc_cache: dict[int, object] = {}  # pid -> psutil.Process, for cpu_percent priming

    @staticmethod
    def _find_process_by_name(name: str):
        """Return the first process matching *name*, excluding the current process."""
        import psutil  # type: ignore[import-untyped]
        my_pid = os.getpid()
        for proc in psutil.process_iter(["name", "pid"]):
            try:
                if proc.info["name"] == name and proc.info["pid"] != my_pid:
                    return proc
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return None

    def _find_process_by_candidates(self):
        """Try to find the terminal process using program basename and extra names.

        Returns (process, name_that_matched) or (None, None).
        """
        prog_basename = os.path.basename(self._program) if self._program else None
        candidates = [prog_basename] if prog_basename else []
        candidates.extend(self._extra)
        for name in candidates:
            proc = self._find_process_by_name(name)
            if proc is not None:
                return proc, name
        return None, None

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

    def _get_or_prime_child(self, child):
        """Return a cached Process for *child*, priming cpu_percent if new."""
        import psutil  # type: ignore[import-untyped]
        pid = child.pid
        if pid in self._proc_cache:
            return self._proc_cache[pid]
        try:
            child.cpu_percent(interval=None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return None
        self._proc_cache[pid] = child
        return child

    def _sample_process_tree(self, root) -> tuple[float, float]:
        """Sum CPU% and RSS across *root* and all descendants.

        Processes whose name or first argument matches ``_exclude_names``
        (e.g. ``ucs-detect``, ``re-run.py``) are skipped so the test
        harness CPU is not attributed to the terminal."""
        import psutil  # type: ignore[import-untyped]
        cpu_total = 0.0
        rss_total = 0.0

        try:
            raw_children = root.children(recursive=True)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return 0.0, 0.0

        procs = [root]
        for child in raw_children:
            cached = self._get_or_prime_child(child)
            if cached is not None:
                procs.append(cached)

        for proc in procs:
            try:
                name = proc.name()
                if name in self._exclude_names:
                    continue
                cmdline = proc.cmdline()
                if cmdline and len(cmdline) > 1:
                    arg1 = os.path.basename(cmdline[1])
                    if arg1 in self._exclude_names:
                        continue
                cpu_total += proc.cpu_percent(interval=None)
                rss_total += proc.memory_info().rss
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                self._proc_cache.pop(proc.pid, None)
        return cpu_total, rss_total / (1024 * 1024)

    def _sample_loop(self) -> None:
        import psutil  # type: ignore[import-untyped]
        t0 = time.monotonic()

        def _init_baselines(process):
            """Prime cpu_percent() for all processes under *process*."""
            try:
                procs = [process] + process.children(recursive=True)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                procs = [process]
            for proc in procs:
                try:
                    proc.cpu_percent(interval=None)
                    if proc.pid != self._pid:
                        self._proc_cache[proc.pid] = proc
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

        root = None
        try:
            root = psutil.Process(self._pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            root, _found_name = self._find_process_by_candidates()
            if root is not None:
                self._recovered = True
            else:
                return

        _init_baselines(root)

        while not self._stop_event.is_set():
            elapsed = time.monotonic() - t0
            try:
                cpu, rss_mb = self._sample_process_tree(root)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                root, _found_name = self._find_process_by_candidates()
                if root is not None:
                    self._recovered = True
                    _init_baselines(root)
                    continue
                break
            self._samples.append((elapsed, cpu, rss_mb))
            self._stop_event.wait(self._interval)

    def samples(self) -> list[tuple[float, float, float]]:
        """Return collected samples (elapsed_seconds, cpu_pct, rss_mb).

        The first sample (initialization artifact) and trailing entries
        with zero RSS (process-exit artifacts) are stripped."""
        result = list(self._samples)
        if result:
            result.pop(0)
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


def hardware_info() -> dict:
    """Return a dict describing the host hardware for resource profile context."""
    import os as _os
    info: dict = {}

    info["cpu_count"] = _os.cpu_count()

    try:
        with open("/proc/cpuinfo") as f:
            for line in f:
                if line.startswith("model name"):
                    info["cpu_model"] = line.split(":", 1)[1].strip()
                    break
    except OSError:
        pass

    try:
        with open("/proc/meminfo") as f:
            for line in f:
                if line.startswith("MemTotal"):
                    val = line.split(":", 1)[1].strip().split()[0]
                    info["ram_total_kb"] = int(val)
                    break
    except OSError:
        pass

    return info


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
        all_cpu_vals.extend(cpu)
        all_rss_vals.extend(rss)
        terminal_data.append((sw_name, elapsed, cpu, rss))

    if not terminal_data:
        return

    cpu_min = min(all_cpu_vals) if all_cpu_vals else 0.0
    cpu_max_val = max(all_cpu_vals) if all_cpu_vals else 100.0
    rss_min = min(all_rss_vals) if all_rss_vals else 0.0
    rss_max_val = max(all_rss_vals) if all_rss_vals else 100.0
    cpu_mean = sum(all_cpu_vals) / len(all_cpu_vals) if all_cpu_vals else 0.0
    rss_mean = sum(all_rss_vals) / len(all_rss_vals) if all_rss_vals else 0.0

    cpu_ymin = max(0, cpu_min - 0.5)
    cpu_ymax = min(cpu_max_val * 1.10, 210) if cpu_max_val > 0 else 100
    rss_ymin = max(0, rss_min - 1)
    rss_ymax = rss_max_val * 1.10 if rss_max_val > 0 else 100

    output_dir.mkdir(parents=True, exist_ok=True)

    scatter_data = []
    for sw_name, elapsed, cpu_vals, rss_vals in terminal_data:
        mean_cpu = sum(cpu_vals) / len(cpu_vals)
        peak_rss = max(rss_vals)
        scatter_data.append((sw_name, mean_cpu, peak_rss))

    cpu_sorted = sorted(scatter_data, key=lambda t: t[1], reverse=True)
    rss_sorted = sorted(scatter_data, key=lambda t: t[2], reverse=True)

    n_terminals = len(terminal_data)
    positions = list(range(n_terminals))

    for label, data_sorted, ymin, ymax, ymean in [
        ("cpu", cpu_sorted, cpu_ymin, cpu_ymax, cpu_mean),
        ("rss", rss_sorted, rss_ymin, rss_ymax, rss_mean),
    ]:
        # Per-terminal: all others grey, this terminal red
        unit = "%" if label == "cpu" else "MB"
        for idx, (sw_name, mean_cpu_val, peak_rss_val) in enumerate(data_sorted):
            safe = safe_map[sw_name]
            yval = mean_cpu_val if label == "cpu" else peak_rss_val

            fig, ax = plt.subplots(figsize=(12, 5))
            fig.suptitle(f"{sw_name} -- {label.upper()} Profile",
                         fontsize=12, fontweight="bold")

            # All terminals in grey
            names = []
            for j, (other_name, other_cpu, other_rss) in enumerate(data_sorted):
                other_y = other_cpu if label == "cpu" else other_rss
                color = "#cccccc"
                ax.scatter(j, other_y, color=color, s=20, zorder=1)
                names.append(other_name)

            # Current terminal in red
            ax.scatter(idx, yval, color="#dc2626", s=60, zorder=2)
            ax.text(idx + 0.3, yval + 2, f"{yval:.0f}",
                    color="black", fontsize=8, va="bottom", ha="left")

            ax.set_xticks(positions)
            ax.set_xticklabels(names, rotation=90, fontsize=6, ha="center")
            ax.set_ylabel("CPU %" if label == "cpu" else "RSS (MB)")
            ax.set_ylim(bottom=ymin, top=ymax)
            ax.grid(True, alpha=0.3, axis="y")

            if ymean > 0:
                ax.axhline(y=ymean, color="red", linestyle="--",
                           linewidth=0.8, alpha=0.7)
                ax.text(n_terminals - 0.5, ymean,
                        f"mean ({ymean:.0f})", color="red", fontsize=7,
                        ha="right", va="bottom", alpha=0.7)

            plt.tight_layout()
            png_path = output_dir / f"{safe}_{label}.png"
            fig.savefig(str(png_path), dpi=100)
            plt.close(fig)

        # Aggregate: all terminals colored by HSV rank
        fig, ax = plt.subplots(figsize=(16, 8))
        fig.suptitle(
            f"All Terminals -- {label.upper()} Profile",
            fontsize=14, fontweight="bold")

        names = []
        for i, (sw_name, mean_cpu_val, peak_rss_val) in enumerate(data_sorted):
            yval = mean_cpu_val if label == "cpu" else peak_rss_val
            hue = (i / max(n_terminals - 1, 1) * 0.833) % 1.0
            r, g, b = colorsys.hsv_to_rgb(hue, 0.7, 0.9)
            color = (r, g, b)
            ax.scatter(i, yval, color=color, s=40, zorder=2,
                       label=f"{sw_name} ({yval:.0f}{unit})")
            dy = 2 if i % 2 == 0 else -2
            va = "bottom" if i % 2 == 0 else "top"
            ax.text(i + 0.5, yval + dy, f"{yval:.0f}",
                    color="black", fontsize=6, va=va, ha="left")
            names.append(sw_name)

        ax.set_xticks(positions)
        ax.set_xticklabels(names, rotation=90, fontsize=6, ha="center")
        ax.set_ylabel("CPU %" if label == "cpu" else "RSS (MB)")
        ax.set_ylim(bottom=ymin, top=ymax)
        ax.grid(True, alpha=0.3, axis="y")

        metric_name = "CPU %" if label == "cpu" else "RSS MB"
        ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5),
                  fontsize=6, framealpha=0.8, ncol=1,
                  title=f"Terminals (mean {metric_name})" if label == "cpu"
                  else f"Terminals (peak {metric_name})")

        if ymean > 0:
            ax.axhline(y=ymean, color="red", linestyle="--",
                       linewidth=0.8, alpha=0.7)
            ax.text(n_terminals - 0.5, ymean,
                    f"mean ({ymean:.0f})", color="red", fontsize=7,
                    ha="right", va="bottom", alpha=0.7)

        plt.tight_layout()
        png_path = output_dir / f"all_{label}.png"
        fig.savefig(str(png_path), dpi=150)
        plt.close(fig)

    # CPU vs Time scatter: trade-off between CPU% and duration
    cpu_time_data = []
    for sw_name, elapsed, cpu_vals, _rss_vals in terminal_data:
        mean_cpu = sum(cpu_vals) / len(cpu_vals)
        duration = elapsed[-1]
        cpu_time_data.append((sw_name, mean_cpu, duration))

    cpu_time_data.sort(key=lambda t: t[2])

    n_ct = len(cpu_time_data)

    # Per-terminal CPU vs Time: all others grey, this terminal red
    for idx, (sw_name, mean_cpu_val, duration_val) in enumerate(cpu_time_data):
        safe = safe_map[sw_name]
        fig, ax = plt.subplots(figsize=(12, 5))
        fig.suptitle(f"{sw_name} -- CPU % vs Duration",
                     fontsize=12, fontweight="bold")

        for j, (other_name, other_cpu, other_dur) in enumerate(cpu_time_data):
            ax.scatter(other_dur, min(other_cpu, 200), color="#cccccc", s=20,
                       zorder=1)

        ax.scatter(duration_val, min(mean_cpu_val, 200), color="#dc2626", s=60,
                   zorder=2)
        ax.text(duration_val, min(mean_cpu_val, 200) + 3,
                f"{sw_name} ({min(mean_cpu_val, 200):.0f}%, {duration_val:.0f}s)",
                color="black", fontsize=8, va="bottom", ha="left")

        ax.set_xlabel("Duration (seconds)")
        ax.set_ylabel("Mean CPU %")
        ax.set_xscale("log")
        ax.set_ylim(bottom=0, top=210)
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        png_path = output_dir / f"{safe}_cpu_vs_time.png"
        fig.savefig(str(png_path), dpi=100)
        plt.close(fig)

    # Aggregate CPU vs Time: all terminals colored by rank
    fig, ax = plt.subplots(figsize=(14, 10))
    fig.suptitle("All Terminals -- CPU % vs Duration",
                 fontsize=14, fontweight="bold")

    for i, (sw_name, mean_cpu_val, duration_val) in enumerate(cpu_time_data):
        hue = (1 - i / max(n_ct - 1, 1)) * 0.333
        r, g, b = colorsys.hsv_to_rgb(hue, 0.7, 0.9)
        color = (r, g, b)
        cpu_clamped = min(mean_cpu_val, 200)
        ax.scatter(duration_val, cpu_clamped, color=color, s=60, zorder=2,
                   label=f"{sw_name} ({cpu_clamped:.0f}%, {duration_val:.0f}s)")
        dy = 3 if i % 2 == 0 else -3
        va = "bottom" if i % 2 == 0 else "top"
        ax.text(duration_val, cpu_clamped + dy,
                f"{sw_name}", color="black", fontsize=6, va=va, ha="left")

    ax.set_xlabel("Duration (seconds)")
    ax.set_ylabel("Mean CPU %")
    ax.set_xscale("log")
    ax.set_ylim(bottom=0, top=210)
    ax.grid(True, alpha=0.3)

    ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5),
              fontsize=6, framealpha=0.8, ncol=1,
              title="Terminals (mean CPU %, duration)")

    plt.tight_layout()
    png_path = output_dir / "all_cpu_vs_time.png"
    fig.savefig(str(png_path), dpi=150)
    plt.close(fig)

    # Time-only horizontal bar charts: terminals sorted by duration
    time_data = sorted(cpu_time_data, key=lambda t: t[2])
    n_td = len(time_data)
    max_dur_td = max(d[2] for d in time_data)

    # Per-terminal time bars
    for idx, (sw_name, _mean_cpu_val, duration_val) in enumerate(time_data):
        safe = safe_map[sw_name]
        fig, ax = plt.subplots(figsize=(12, 5))
        fig.suptitle(f"{sw_name} -- Duration",
                     fontsize=12, fontweight="bold")

        names = []
        for j, (other_name, _oc, other_dur) in enumerate(time_data):
            color = "#dc2626" if other_name == sw_name else "#cccccc"
            z = 2 if other_name == sw_name else 1
            size = 60 if other_name == sw_name else 20
            ax.barh(j, other_dur, color=color, zorder=z, height=0.6)
            if other_name == sw_name:
                ax.text(other_dur * 1.05, j, f"{sw_name} ({other_dur:.0f}s)",
                        color="black", fontsize=8, va="center", ha="left")
            names.append(other_name)

        ax.set_yticks(range(n_td))
        ax.set_yticklabels(names, fontsize=6)
        ax.set_xlabel("Duration (seconds)")
        ax.set_xscale("log")
        ax.grid(True, alpha=0.3, axis="x")
        ax.invert_yaxis()

        plt.tight_layout()
        png_path = output_dir / f"{safe}_time.png"
        fig.savefig(str(png_path), dpi=100)
        plt.close(fig)

    # Aggregate time bars: all terminals colored by rank
    fig, ax = plt.subplots(figsize=(14, 10))
    fig.suptitle("All Terminals -- Duration",
                 fontsize=14, fontweight="bold")

    names = []
    for i, (sw_name, _mean_cpu_val, duration_val) in enumerate(time_data):
        hue = (1 - i / max(n_td - 1, 1)) * 0.333
        r, g, b = colorsys.hsv_to_rgb(hue, 0.7, 0.9)
        color = (r, g, b)
        ax.barh(i, duration_val, color=color, zorder=2, height=0.6,
                label=f"{sw_name} ({duration_val:.0f}s)")
        names.append(sw_name)

    ax.set_yticks(range(n_td))
    ax.set_yticklabels(names, fontsize=6)
    ax.set_xlabel("Duration (seconds)")
    ax.set_xscale("log")
    ax.grid(True, alpha=0.3, axis="x")
    ax.invert_yaxis()

    ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5),
              fontsize=6, framealpha=0.8, ncol=1,
              title="Terminals (duration)")

    plt.tight_layout()
    png_path = output_dir / "all_time.png"
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
