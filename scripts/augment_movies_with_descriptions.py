import argparse
import json
import os
import re
import urllib.parse
import urllib.request
from pathlib import Path


FILE_PATH = Path(__file__).resolve().parents[1] / "docs" / "fun" / "movies.md"
CACHE_PATH = Path(__file__).resolve().parent / ".omdb_cache.json"


def split_row(line: str) -> list[str]:
    # Split markdown table row into cells, trimming whitespace
    parts = [p.strip() for p in line.strip().strip("|").split("|")]
    return parts


def join_row(cells: list[str]) -> str:
    return "| " + " | ".join(cells) + " |\n"


def generate_desc(year: str, genre: str) -> str:
    year = year.strip()
    genre = genre.strip()
    # Keep it short, neutral, and original to avoid copyright issues
    if year and genre:
        return f"Erschienen {year}; Genre: {genre}."
    if year:
        return f"Erschienen {year}."
    if genre:
        return f"Genre: {genre}."
    return "Kurzbeschreibung folgt."


def is_generic(desc: str) -> bool:
    if not desc:
        return True
    lowered = desc.lower().strip()
    return lowered.startswith("erschienen") or lowered.startswith("genre:") or lowered.startswith("kurzbeschreibung folgt")


def load_cache(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save_cache(path: Path, cache: dict) -> None:
    path.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def shorten_plot(plot: str, max_len: int = 200) -> str:
    if len(plot) <= max_len:
        return plot
    trimmed = plot[: max_len - 1].rsplit(" ", 1)[0].rstrip(".,;:!?")
    return f"{trimmed}…"


def fetch_omdb_plot(title: str, year: str, api_key: str, cache: dict, requests_made: int, max_requests: int | None) -> tuple[str | None, int]:
    cache_key = f"{title.lower()}|{year}"
    if cache_key in cache:
        return cache[cache_key], requests_made

    if max_requests is not None and requests_made >= max_requests:
        return None, requests_made

    params = {
        "t": title,
        "y": year,
        "plot": "short",
        "r": "json",
        "apikey": api_key,
    }
    url = "http://www.omdbapi.com/?" + urllib.parse.urlencode(params)

    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception:
        return None, requests_made

    requests_made += 1

    if str(data.get("Response", "")).lower() != "true":
        return None, requests_made

    plot = str(data.get("Plot", "")).strip()
    if not plot or plot.lower() == "n/a":
        return None, requests_made

    short_plot = shorten_plot(plot)
    cache[cache_key] = short_plot
    return short_plot, requests_made


def process_table(lines: list[str], api_key: str | None, max_requests: int | None, force: bool) -> tuple[list[str], dict]:
    out = []
    in_table = False
    header_done = False
    cache = load_cache(CACHE_PATH)
    requests_made = 0

    for i, line in enumerate(lines):
        if line.strip().startswith("|") and line.strip().endswith("|"):
            # Inside a markdown table row
            cells = split_row(line)

            # Detect header: expect at least Titel, Jahr, Genre
            if not header_done and len(cells) >= 3 and cells[0].lower() == "titel" and cells[1].lower() == "jahr" and cells[2].lower().startswith("genre"):
                in_table = True
                header_done = True
                # Add Beschreibung column if missing
                if len(cells) < 4 or cells[3].lower() != "beschreibung":
                    cells = cells[:3] + ["Beschreibung"] + cells[3:]
                out.append(join_row(cells))
                continue

            # Separator row (---)
            if in_table and re.fullmatch(r"\|\s*-+\s*(\|\s*-+\s*)+\|", line.strip()):
                sep_cells = split_row(line)
                # Ensure separator has 4 columns
                if len(sep_cells) < 4:
                    sep_cells = sep_cells[:3] + ["----"] + sep_cells[3:]
                out.append(join_row(["-" * max(4, len(c)) for c in sep_cells]))
                continue

            # Data rows
            if in_table and len(cells) >= 3:
                year = cells[1] if len(cells) > 1 else ""
                genre = cells[2] if len(cells) > 2 else ""

                # Ensure at least 4 columns by adding description
                if len(cells) < 4:
                    desc = generate_desc(year, genre)
                    cells = cells[:3] + [desc] + cells[3:]

                desc_cell = cells[3].strip() if len(cells) > 3 else ""

                if api_key and (force or is_generic(desc_cell)):
                    fetched, requests_made = fetch_omdb_plot(cells[0], year, api_key, cache, requests_made, max_requests)
                    if fetched:
                        cells[3] = fetched
                    elif not desc_cell:
                        cells[3] = generate_desc(year, genre)
                elif not desc_cell:
                    cells[3] = generate_desc(year, genre)

                out.append(join_row(cells))
                continue

        # Non-table lines or outside the table
        out.append(line)

    return out, cache


def main() -> None:
    parser = argparse.ArgumentParser(description="Augment movies table with descriptions.")
    parser.add_argument("--omdb-api-key", dest="api_key", default=None, help="OMDb API key (or set OMDB_API_KEY env var)")
    parser.add_argument("--max-requests", type=int, default=0, help="Limit OMDb lookups (0 = no limit)")
    parser.add_argument("--force", action="store_true", help="Override existing non-generic descriptions")
    args = parser.parse_args()

    home_key_path = Path.home().joinpath(".omdb_api_key")
    file_key = home_key_path.read_text(encoding="utf-8").strip() if home_key_path.exists() else None
    api_key = args.api_key or os.getenv("OMDB_API_KEY") or file_key

    max_requests = None if args.max_requests == 0 else max(0, args.max_requests)

    text = FILE_PATH.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    new_lines, cache = process_table(lines, api_key=api_key, max_requests=max_requests, force=args.force)
    FILE_PATH.write_text("".join(new_lines), encoding="utf-8")

    if api_key:
        save_cache(CACHE_PATH, cache)


if __name__ == "__main__":
    main()
