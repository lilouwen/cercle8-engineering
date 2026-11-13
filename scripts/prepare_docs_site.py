#!/usr/bin/env python3
"""Stage allowlisted public documentation for MkDocs without duplicating source content."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / ".site-docs"
ALLOW_DIRS = ("docs", "architecture", "engineering-decisions", "development-journal", "assets")
ALLOW_ROOT = ("README.md", "SECURITY.md", "CONTRIBUTING.md")


def main() -> None:
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)
    copied = 0
    for name in ALLOW_ROOT:
        shutil.copy2(ROOT / name, OUTPUT / name)
        copied += 1
    for folder in ALLOW_DIRS:
        for source in sorted((ROOT / folder).rglob("*.md")):
            if source.is_symlink():
                raise ValueError(f"Symlink refused: {source}")
            target = OUTPUT / source.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            copied += 1

    shutil.copy2(ROOT / "site-content" / "index.md", OUTPUT / "index.md")
    style = OUTPUT / "stylesheets" / "extra.css"
    style.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "site-content" / "extra.css", style)
    print(f"Staged {copied} public Markdown documents + website landing page.")


if __name__ == "__main__":
    main()
