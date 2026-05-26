"""Verify dockered terminal binaries are callable."""
import subprocess
import sys
import yaml


def main() -> int:
    with open("terminals.yaml") as f:
        data = yaml.safe_load(f)

    for name, cfg in sorted(data["terminals"].items(), key=lambda kv: kv[0].lower()):
        launch = cfg.get("launch_docker") or cfg.get("launch")
        if not launch or cfg.get("skip_docker") or "program" not in launch:
            continue
        prog = launch["program"]
        try:
            r = subprocess.run([prog, "--version"], capture_output=True, text=True, timeout=3)
            line = (r.stderr + r.stdout).strip().split("\n")[0][:70]
            print(f"OK    {name:25s}  exit={r.returncode}  {line}")
        except FileNotFoundError:
            print(f"MISS  {name:25s}  {prog}")
        except subprocess.TimeoutExpired:
            print(f"HANG  {name:25s}  {prog}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
