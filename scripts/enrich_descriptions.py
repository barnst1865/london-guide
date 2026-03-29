"""Enrich sites.csv entries with descriptions via DuckDuckGo web search."""

import csv
import json
import os
import pathlib
import sys
import time

# Fix Windows console encoding
if sys.platform == "win32":
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

PROJ = pathlib.Path(__file__).resolve().parent.parent
CSV_PATH = PROJ / "data" / "sites.csv"
CACHE_PATH = PROJ / "data" / "enrichment_cache.json"

FIELDNAMES = [
    "id", "name", "lat", "lon", "category", "subcategory", "neighborhood",
    "address", "summary", "price_range", "kid_friendly", "visited", "rating",
    "website", "google_maps_url", "tags", "notes",
]


def load_cache():
    if CACHE_PATH.exists():
        with open(CACHE_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_cache(cache):
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)


def search_description(name, category, subcategory):
    """Search DuckDuckGo for a description of the place."""
    try:
        from duckduckgo_search import DDGS
    except ImportError:
        print("  Install duckduckgo-search: pip install duckduckgo-search")
        return ""

    # Build a contextual query
    if category == "restaurants":
        query = f'"{name}" London restaurant pub review'
    elif category == "wmd-sites":
        query = f'"{name}" history nuclear chemical weapons site'
    elif category == "historic-sites":
        query = f'"{name}" UK history heritage site'
    elif category == "day-trips":
        query = f'"{name}" UK visit tourist attraction'
    elif category == "movie-sites":
        query = f'"{name}" London filming location movie'
    elif category == "kid-friendly":
        query = f'"{name}" London family children activities'
    else:
        query = f'"{name}" London UK visit attraction'

    try:
        results = DDGS().text(query, max_results=3)
        if results:
            # Take the best snippet, clean it up
            for r in results:
                body = r.get("body", "").strip()
                if body and len(body) > 30 and name.split()[0].lower() in body.lower():
                    # Truncate to ~200 chars at a sentence boundary
                    if len(body) > 200:
                        cut = body[:200].rfind(".")
                        if cut > 100:
                            body = body[: cut + 1]
                        else:
                            body = body[:200] + "..."
                    return body

            # Fallback: use first result even if name not in body
            body = results[0].get("body", "").strip()
            if body and len(body) > 20:
                if len(body) > 200:
                    cut = body[:200].rfind(".")
                    if cut > 100:
                        body = body[: cut + 1]
                    else:
                        body = body[:200] + "..."
                return body
    except Exception as e:
        print(f"  Search error for '{name}': {e}")

    return ""


def main():
    cache = load_cache()

    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    enriched = 0
    cached_hits = 0
    failed = 0
    skipped = 0

    for row in rows:
        # Skip if already has a summary
        if row.get("summary", "").strip():
            skipped += 1
            continue

        site_id = row.get("id", "")
        name = row.get("name", "")

        if not name or not site_id:
            continue

        # Check cache
        if site_id in cache:
            cached = cache[site_id]
            if cached:
                row["summary"] = cached
                cached_hits += 1
            else:
                failed += 1
            continue

        category = row.get("category", "")
        subcategory = row.get("subcategory", "")

        print(f"Searching: {name} ({category}/{subcategory})...")
        desc = search_description(name, category, subcategory)

        if desc:
            row["summary"] = desc
            cache[site_id] = desc
            enriched += 1
            print(f"  -> {desc[:80]}...")
        else:
            cache[site_id] = ""
            failed += 1
            print(f"  -> NO RESULT")

        # Rate limit
        time.sleep(1.5)

    # Write back
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for row in rows:
            clean = {k: row.get(k, "") for k in FIELDNAMES}
            writer.writerow(clean)

    save_cache(cache)
    print(f"\nEnriched: {enriched}, Cached: {cached_hits}, Failed: {failed}, Already had summary: {skipped}")


if __name__ == "__main__":
    main()
