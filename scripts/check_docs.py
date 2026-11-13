#!/usr/bin/env python3
"""Check local Markdown and HTML links without dependencies or external requests."""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MD_LINK = re.compile(r"\]\(([^)\n]+)\)")
MD_REFERENCE = re.compile(r"(?m)^\s{0,3}\[[^\]]+\]:\s*(\S+)")
EXTERNAL = ("http:", "https:", "mailto:", "tel:", "data:", "//")


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.items: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag not in {"a", "img", "source"}:
            return
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.items.append(value)


def strip_code_blocks(body: str) -> str:
    lines: list[str] = []
    fence = False
    for line in body.splitlines():
        if line.strip().startswith("~~~"):
            fence = not fence
        elif not fence:
            lines.append(line)
    return "\n".join(lines)


def destination(source: Path, target: str) -> Path | None:
    target = target.strip().strip("<>")
    if not target or target.startswith(("#", *EXTERNAL)):
        return None
    if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
        return None
    target = re.split(r"\s+[\"']", target, maxsplit=1)[0]
    path = unquote(urlsplit(target).path)
    if not path:
        return None
    return ((ROOT / path.lstrip("/")) if path.startswith("/") else (source.parent / path)).resolve()


def main() -> int:
    errors: list[str] = []
    count = 0
    docs = sorted(ROOT.rglob("*.md"))
    for source in docs:
        if ".git" in source.parts:
            continue
        body = strip_code_blocks(source.read_text(encoding="utf-8"))
        parser = Links()
        parser.feed(body)
        for url in MD_LINK.findall(body) + MD_REFERENCE.findall(body) + parser.items:
            path = destination(source, url)
            if path is None:
                continue
            count += 1
            try:
                path.relative_to(ROOT)
            except ValueError:
                errors.append(f"{source.relative_to(ROOT)}: outside repository: {url}")
                continue
            if not path.exists():
                errors.append(f"{source.relative_to(ROOT)}: missing link: {url}")
    print(f"Checked {len(docs)} Markdown documents and {count} local links.")
    for error in errors:
        print("ERROR:", error, file=sys.stderr)
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
