#!/usr/bin/env python3
"""Keep page frontmatter in sync with git history and content.

Sets/updates these frontmatter keys on every markdown page in docs/:

- date:        first commit date of the file (creation)
- modified:    last commit date of the file (update)
- description: first paragraph of the page, trimmed to ~155 chars (--all only)
- tags:        derived from the directory the page lives in (--all only)

The date/modified values feed the mkdocs-rss-plugin (feed_rss_created.xml /
feed_rss_updated.xml) without any git calls at build time. So that only real
page edits bump the "modified" date (and thus the RSS feed), two kinds of
commits are ignored: commits whose message contains [rss-skip], and bulk
commits touching more than BULK_COMMIT_THRESHOLD markdown files at once
(mass formatting/metadata sweeps).

Usage:
    python scripts/update_frontmatter.py --dates   # refresh dates only (CI)
    python scripts/update_frontmatter.py --all     # also fill missing description/tags
"""

import argparse
import re
import subprocess
import sys
from datetime import date as date_type
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

RSS_SKIP_MARKER = "[rss-skip]"
# Commits touching more markdown files than this are treated as bulk/mechanical
# changes and do not bump the "modified" date (only real page edits should).
BULK_COMMIT_THRESHOLD = 25
DESCRIPTION_MAX_LEN = 155

# Small, deliberately coarse tag vocabulary mapped from directory prefixes.
# First match wins, so keep more specific prefixes on top.
TAG_MAP = [
    ("tech/ai", ["Tech", "AI"]),
    ("tech/art", ["Tech", "Art"]),
    ("tech/cloud", ["Tech", "Cloud"]),
    ("tech/hack", ["Tech", "Security"]),
    ("tech/hardware", ["Tech", "Hardware"]),
    ("tech/scripts", ["Tech", "Scripting"]),
    ("tech/standards", ["Tech", "Standards"]),
    ("tech/tools", ["Tech", "Tools"]),
    ("tech", ["Tech"]),
    ("make/art", ["Making", "Art"]),
    ("make/boxes", ["Making", "DIY"]),
    ("make/food", ["Making", "Food"]),
    ("make/gadget", ["Making", "DIY"]),
    ("make/games", ["Making", "Games"]),
    ("make/hid", ["Making", "Hardware"]),
    ("make/music", ["Making", "Music"]),
    ("make", ["Making"]),
    ("fun/culture", ["Fun", "Culture"]),
    ("fun/games", ["Fun", "Games"]),
    ("fun/media", ["Fun", "Media"]),
    ("fun", ["Fun"]),
    ("about", ["Personal"]),
]

# Pages that should not carry tags (meta pages).
UNTAGGED = {"index.md", "tags.md"}


def git_dates() -> dict[str, tuple[str, str]]:
    """Return {relative_posix_path: (created_iso, modified_iso)} for docs/**/*.md.

    Walks the whole history once (newest to oldest) and follows renames so a
    moved file keeps its original creation date.
    """
    out = subprocess.run(
        # core.quotepath=false keeps non-ASCII paths (e.g. "prömpeln") unescaped
        ["git", "-c", "core.quotepath=false", "log", "--name-status", "--format=@@@%aI%x09%s", "--", "docs"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=True,
    ).stdout

    created: dict[str, str] = {}
    modified: dict[str, str] = {}
    # Maps historical path -> current (canonical) path, built while walking
    # backwards through renames.
    alias: dict[str, str] = {}

    def canonical(path: str) -> str:
        seen = set()
        while path in alias and path not in seen:
            seen.add(path)
            path = alias[path]
        return path

    def apply_commit(date: str, skip: bool, paths: list[str]) -> None:
        # Commits touching many pages at once are mechanical (mass formatting,
        # metadata sweeps) - they must not count as an "edit" for the RSS feed.
        bulk = len(paths) > BULK_COMMIT_THRESHOLD
        for path in paths:
            created[path] = date  # oldest occurrence wins (overwritten)
            if path not in modified and not skip and not bulk:
                modified[path] = date

    current_date = ""
    current_skip = False
    current_paths: list[str] = []
    for line in out.splitlines():
        if line.startswith("@@@"):
            apply_commit(current_date, current_skip, current_paths)
            current_date, _, subject = line[3:].partition("\t")
            current_skip = RSS_SKIP_MARKER in subject
            current_paths = []
            continue
        if not line or "\t" not in line:
            continue
        parts = line.split("\t")
        status = parts[0]
        if status.startswith("R") and len(parts) == 3:
            old, new = parts[1], parts[2]
            target = canonical(new)
            alias[old] = target
            path = target
        else:
            path = canonical(parts[-1])
        if path.endswith(".md"):
            current_paths.append(path)
    apply_commit(current_date, current_skip, current_paths)

    result = {}
    for path, created_iso in created.items():
        result[path] = (created_iso, modified.get(path, created_iso))
        # Windows filesystems are case-insensitive, so on-disk casing may
        # differ from the casing recorded in git history.
        result.setdefault(path.casefold(), result[path])
    return result


def split_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body). Body excludes the frontmatter block."""
    if text.startswith("---"):
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.DOTALL)
        if match:
            try:
                data = yaml.safe_load(match.group(1)) or {}
            except yaml.YAMLError:
                data = {}
            if isinstance(data, dict):
                return data, text[match.end():]
    return {}, text


def extract_description(body: str) -> str:
    """First real text paragraph, markdown stripped, trimmed to ~155 chars."""
    lines = []
    in_code = False
    for raw in body.splitlines():
        line = raw.strip()
        if line.startswith("```") or line.startswith("~~~"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if not line:
            if lines:
                break
            continue
        # Skip headings, images, badges, html, tables, list-only intros
        if line.startswith(("#", "<", "|", "!", "[![", ">")):
            if lines:
                break
            continue
        lines.append(line)
    text = " ".join(lines)
    # Strip markdown syntax
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)  # images
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)  # links -> text
    text = re.sub(r"[`*_~]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > DESCRIPTION_MAX_LEN:
        cut = text[:DESCRIPTION_MAX_LEN]
        if " " in cut:
            cut = cut.rsplit(" ", 1)[0]
        text = cut.rstrip(",;:.") + " ..."
    return text


def tags_for(rel_path: str) -> list[str]:
    name = rel_path.rsplit("/", 1)[-1]
    if name in UNTAGGED and "/" not in rel_path:
        return []
    if name == "tags.md":
        return []
    for prefix, tags in TAG_MAP:
        if rel_path.startswith(prefix + "/") or rel_path == prefix + ".md":
            return list(tags)
    return []


def parse_iso_date(value: str):
    return datetime.fromisoformat(value).astimezone(timezone.utc).date()


class _NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def dump_frontmatter(data: dict) -> str:
    return yaml.dump(
        data,
        Dumper=_NoAliasDumper,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
        width=1000,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dates", action="store_true", help="update date/modified only")
    mode.add_argument("--all", action="store_true", help="also fill missing description/tags")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    dates = git_dates()
    today = date_type.today()
    changed = 0

    for md_file in sorted(DOCS.rglob("*.md")):
        rel = md_file.relative_to(ROOT).as_posix()
        rel_docs = md_file.relative_to(DOCS).as_posix()
        text = md_file.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        original = dict(fm)

        created_iso, modified_iso = dates.get(rel) or dates.get(rel.casefold()) or ("", "")
        fm["date"] = parse_iso_date(created_iso) if created_iso else today
        fm["modified"] = parse_iso_date(modified_iso) if modified_iso else today

        if args.all:
            if not fm.get("description"):
                description = extract_description(body)
                if description:
                    fm["description"] = description
            if not fm.get("tags"):
                tags = tags_for(rel_docs)
                if tags:
                    fm["tags"] = tags

        # Stable key order: date, modified, description, tags, then the rest.
        ordered = {}
        for key in ("date", "modified", "description", "tags"):
            if key in fm:
                ordered[key] = fm[key]
        for key, value in fm.items():
            if key not in ordered:
                ordered[key] = value

        if ordered != original:
            md_file.write_text(
                "---\n" + dump_frontmatter(ordered) + "---\n\n" + body.lstrip("\n"),
                encoding="utf-8",
                newline="\n",
            )
            changed += 1
            if not args.quiet:
                print(f"updated {rel}")

    print(f"{changed} file(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
