"""Verify all expected terminals are installed and executable in the Docker image."""
import subprocess
import sys
import yaml


def main() -> int:
    with open("terminals.yaml") as f:
        config = yaml.safe_load(f)

    terminals = config["terminals"]
    failed = []

    for name, data in sorted(terminals.items(), key=lambda x: x[0].lower()):
        launch = data.get("launch")
        if not launch:
            continue
        if data.get("skip_docker"):
            continue
        if "program" not in launch:
            continue

        program = launch["program"]
        try:
            result = subprocess.run(
                [program, "--version"],
                capture_output=True, text=True, timeout=10,
            )
        except FileNotFoundError:
            failed.append((name, program, "not found"))
            print(f"  FAIL  {name:20s} ({program}) — not found")
            continue
        except Exception as e:
            failed.append((name, program, str(e)))
            print(f"  FAIL  {name:20s} ({program}) — {e}")
            continue

        output = "\n".join([result.stderr.strip(), result.stdout.strip()]).strip()
        version_line = output.split("\n")[0] if output else "(no output)"
        if version_line:
            print(f"  OK    {name:20s} ({program}) — {version_line[:70]}")
        else:
            failed.append((name, program, f"exit={result.returncode} no output"))
            print(f"  FAIL  {name:20s} ({program}) exit={result.returncode} — no output")

    print(f"\n{len(terminals)} terminals total, {len(failed)} failures")
    if failed:
        print("\nFailures:")
        for name, prog, reason in failed:
            print(f"  {name}: {prog} — {reason}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
