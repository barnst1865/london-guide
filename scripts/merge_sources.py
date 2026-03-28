"""Merge all *_raw.csv files into the master data/sites.csv."""

import csv
import pathlib

PROJ = pathlib.Path(__file__).resolve().parent.parent
DATA_DIR = PROJ / "data"
MASTER_CSV = DATA_DIR / "sites.csv"

FIELDNAMES = [
    "id", "name", "lat", "lon", "category", "subcategory", "neighborhood",
    "address", "summary", "price_range", "kid_friendly", "visited", "rating",
    "website", "google_maps_url", "tags", "notes",
]


def load_existing():
    """Load existing master CSV entries by id."""
    existing = {}
    if MASTER_CSV.exists():
        with open(MASTER_CSV, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("id"):
                    existing[row["id"]] = row
    return existing


def main():
    existing = load_existing()
    new_count = 0

    # Find all *_raw.csv files
    raw_files = sorted(DATA_DIR.glob("*_raw.csv"))
    print(f"Found {len(raw_files)} raw CSV files: {[f.name for f in raw_files]}")

    for raw_file in raw_files:
        with open(raw_file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                site_id = row.get("id", "").strip()
                if not site_id:
                    continue
                if site_id not in existing:
                    existing[site_id] = row
                    new_count += 1

    # Write merged output
    with open(MASTER_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for site_id in sorted(existing.keys()):
            row = existing[site_id]
            clean = {k: row.get(k, "") for k in FIELDNAMES}
            writer.writerow(clean)

    total = len(existing)
    print(f"Master CSV: {total} total sites ({new_count} new)")


if __name__ == "__main__":
    main()
