#!/usr/bin/env python3
"""Initialize a research workspace and run lightweight toolkit checks."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCAFFOLD = ROOT / "templates" / "workspace"
ROOT_FILES = ("WORKFLOW.md", "QUALITY_CONTROL.md")
REQUIRED_TOOLKIT_PATHS = (
    "README.md",
    "AGENTS.md",
    "WORKFLOW.md",
    "QUALITY_CONTROL.md",
    "LICENSE",
    "templates/workspace/README.md",
    "templates/workspace/AGENTS.md",
    "methods/README.md",
    "methods/regression/README.md",
    "examples/minimal_quarto/manuscript.qmd",
)
REQUIRED_WORKSPACE_PATHS = (
    "README.md",
    "AGENTS.md",
    ".gitignore",
    "WORKFLOW.md",
    "QUALITY_CONTROL.md",
    "index/workspace_catalog.md",
    "index/workspace_memory.md",
    "index/workspace_structure_text.md",
    "shared/templates/ARTICLE_STATE_template.md",
    "shared/templates/analysis_plan_template.md",
)
DATA_SUFFIXES = {
    ".csv",
    ".tsv",
    ".xlsx",
    ".xls",
    ".sav",
    ".por",
    ".dta",
    ".sas7bdat",
    ".rds",
    ".rdata",
    ".dat",
    ".parquet",
    ".feather",
    ".gh5",
}
TEXT_SUFFIXES = {".md", ".qmd", ".py", ".yml", ".yaml", ".txt", ".bib", ".tex"}
PERSONAL_PATH_PATTERNS = (
    re.compile(r"/Users/[^/\s]+/"),
    re.compile(r"/home/[^/\s]+/"),
    re.compile(r"[A-Za-z]:\\Users\\"),
)


def install_workspace(target: Path) -> None:
    if target.exists() and any(target.iterdir()):
        raise ValueError(f"Target directory is not empty: {target}")

    target.mkdir(parents=True, exist_ok=True)
    for source in SCAFFOLD.iterdir():
        destination = target / source.name
        if source.is_dir():
            shutil.copytree(source, destination)
        else:
            shutil.copy2(source, destination)
    for name in ROOT_FILES:
        shutil.copy2(ROOT / name, target / name)


def repository_files() -> list[Path]:
    try:
        result = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", "--cached", "--others", "--exclude-standard"],
            check=True,
            capture_output=True,
            text=True,
        )
        return [ROOT / line for line in result.stdout.splitlines() if line]
    except (FileNotFoundError, subprocess.CalledProcessError):
        return [path for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts]


def run_checks() -> list[str]:
    errors: list[str] = []

    for relative in REQUIRED_TOOLKIT_PATHS:
        if not (ROOT / relative).exists():
            errors.append(f"Missing required toolkit path: {relative}")

    method_entries = sorted(
        path.name
        for path in (ROOT / "methods").iterdir()
        if path.name != "README.md"
        and (path.is_file() or any(child.is_file() for child in path.rglob("*")))
    )
    if method_entries != ["regression"]:
        errors.append(f"Methods example must contain only regression; found: {method_entries}")

    for path in repository_files():
        if path.suffix.lower() in DATA_SUFFIXES:
            errors.append(f"Data-like file is tracked or pending: {path.relative_to(ROOT)}")
        if path.resolve() == Path(__file__).resolve():
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES or not path.is_file():
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if any(pattern.search(content) for pattern in PERSONAL_PATH_PATTERNS):
            errors.append(f"Personal absolute path found in: {path.relative_to(ROOT)}")
        if "analysis_spec.md" in content:
            errors.append(f"Obsolete analysis_spec.md reference found in: {path.relative_to(ROOT)}")

    with tempfile.TemporaryDirectory(prefix="research-workflow-check-") as temp_dir:
        installed = Path(temp_dir) / "workspace"
        install_workspace(installed)
        for relative in REQUIRED_WORKSPACE_PATHS:
            if not (installed / relative).exists():
                errors.append(f"Installed workspace is missing: {relative}")

    return errors


def init_command(target_value: str) -> int:
    target = Path(target_value).expanduser().resolve()
    try:
        install_workspace(target)
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2

    print(f"Workspace created at: {target}")
    print("Next: read README.md and AGENTS.md, review .gitignore, then record local preferences in index/workspace_memory.md.")
    return 0


def check_command() -> int:
    errors = run_checks()
    if errors:
        print("Toolkit check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Toolkit check passed: core files, method scope, portability, data boundary, and scaffold installation are valid.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    init_parser = subparsers.add_parser("init", help="Create a workspace from the bundled scaffold")
    init_parser.add_argument("target", help="New or empty target directory")
    subparsers.add_parser("check", help="Run lightweight repository and scaffold checks")
    args = parser.parse_args()

    if args.command == "init":
        return init_command(args.target)
    return check_command()


if __name__ == "__main__":
    raise SystemExit(main())
