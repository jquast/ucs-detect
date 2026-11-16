"""Load wcwidth from a local source checkout when configured."""

from __future__ import annotations

# std imports
import os
import sys
import subprocess
import importlib.util
from pathlib import Path

SOURCE_ENV = "UCS_DETECT_WCWIDTH_SOURCE"

#: Seconds allowed for each git query made by :func:`provenance`.
GIT_TIMEOUT = 2.0


def _source_root():
    configured = os.environ.get(SOURCE_ENV)
    if configured is not None:
        if not configured:
            return None
        root = Path(configured).expanduser()
    elif Path("/.dockerenv").exists():
        root = Path("/wcwidth")
    else:
        return None
    if not root.is_absolute():
        root = (Path.cwd() / root).resolve()
    if not (root / "wcwidth" / "__init__.py").is_file():
        return None
    return root


def install():
    """Load the configured wcwidth checkout before the installed package."""
    if "wcwidth" in sys.modules:
        return
    root = _source_root()
    if root is None:
        return
    package = root / "wcwidth"
    spec = importlib.util.spec_from_file_location(
        "wcwidth",
        package / "__init__.py",
        submodule_search_locations=[str(package)],
    )
    if spec is None or spec.loader is None:
        return
    module = importlib.util.module_from_spec(spec)
    sys.modules["wcwidth"] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        del sys.modules["wcwidth"]
        raise


def _git(root, *arguments):
    """Return stripped standard output of a git query, or an empty string."""
    try:
        result = subprocess.run(
            ("git", "-C", str(root), *arguments),
            capture_output=True, text=True, timeout=GIT_TIMEOUT, check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    return result.stdout.strip() if result.returncode == 0 else ""


def provenance():
    """Return the path, branch, commit and dirty state of the imported wcwidth."""
    module = sys.modules.get("wcwidth")
    path = getattr(module, "__file__", None)
    if not path:
        return {}
    package = Path(path).resolve().parent
    found = {"wcwidth_path": str(package)}
    root = package.parent
    if not (root / ".git").exists():
        return found
    commit = _git(root, "rev-parse", "--short=7", "HEAD")
    if not commit:
        return found
    branch = _git(root, "symbolic-ref", "--short", "-q", "HEAD")
    if branch:
        found["wcwidth_branch"] = branch
    found["wcwidth_commit"] = commit
    found["wcwidth_dirty"] = bool(_git(root, "status", "--porcelain"))
    return found
