"""Tag historic restaurants/pubs with subcategory='historic' and add missing ones."""

import csv
import pathlib
import re

PROJ = pathlib.Path(__file__).resolve().parent.parent
CSV_PATH = PROJ / "data" / "sites.csv"

FIELDNAMES = [
    "id", "name", "lat", "lon", "category", "subcategory", "neighborhood",
    "address", "summary", "price_range", "kid_friendly", "visited", "rating",
    "website", "google_maps_url", "tags", "notes",
]

# Known historic pubs/restaurants to tag (by normalized name)
HISTORIC_NAMES = {
    "ye olde cheshire cheese",
    "ye olde mitre",
    "ye olde mitre, holborn",
    "the mayflower pub",
    "prospect of whitby",
    "the grapes",
    "gordon's wine bar",
    "gordons wine bar",
    "rules",
    "the french house",
    "the ship tavern",
    "the olde wine shades",
}

# Missing historic entries to add
MISSING_HISTORIC = [
    {"name": "The Ship Tavern", "neighborhood": "Holborn", "subcategory": "historic",
     "summary": "Hidden gem near Lincoln's Inn Fields, dating back centuries. Popular with lawyers and locals."},
    {"name": "The French House", "neighborhood": "Soho", "subcategory": "historic",
     "summary": "Legendary Soho pub famous as the French Resistance HQ in WWII. De Gaulle drafted his 'Appeal of 18 June' here. No pints served - only halves."},
    {"name": "The Grapes", "neighborhood": "Limehouse", "subcategory": "historic",
     "summary": "Historic riverside pub in Limehouse, part-owned by Sir Ian McKellen. Dating from 1720, it featured in Dickens' Our Mutual Friend."},
    {"name": "Prospect of Whitby", "neighborhood": "Wapping", "subcategory": "historic",
     "summary": "London's oldest riverside pub (1520). Famous for its hanging noose over the Thames where pirates were executed. Samuel Pepys and Charles Dickens drank here."},
    {"name": "Gordon's Wine Bar", "neighborhood": "Embankment", "subcategory": "historic",
     "summary": "London's oldest wine bar, in a candlelit cellar near Embankment. Rudyard Kipling once lived upstairs. Famous for its atmospheric cave-like interior."},
    {"name": "Rules", "neighborhood": "Covent Garden", "subcategory": "historic",
     "summary": "London's oldest restaurant, established 1798. Classic British game and traditional dishes. Dickens, H.G. Wells, and Charlie Chaplin were regulars."},
    {"name": "The George Inn, Norton St Philip", "neighborhood": "Somerset", "subcategory": "historic",
     "summary": "One of England's oldest inns, dating from 1397. The Duke of Monmouth used it as HQ during the 1685 rebellion. Samuel Pepys stayed here."},
]


def slugify(text):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower().strip())
    return slug.strip("-")


def main():
    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    existing_ids = {r.get("id") for r in rows}
    tagged = 0

    # Tag entries from the historic list source
    for row in rows:
        tags = row.get("tags", "")
        name_lower = row.get("name", "").lower().strip()

        should_tag = False

        # Tag if source is the historic list
        if "source:London Historic Restaurants and Pubs" in tags:
            should_tag = True

        # Tag if name matches known historic places
        if name_lower in HISTORIC_NAMES:
            should_tag = True

        if should_tag and row.get("category") == "restaurants":
            row["subcategory"] = "historic"
            tagged += 1

    # Add missing historic entries
    added = 0
    for entry in MISSING_HISTORIC:
        site_id = slugify(entry["name"])
        if site_id in existing_ids:
            continue

        row = {k: "" for k in FIELDNAMES}
        row["id"] = site_id
        row["name"] = entry["name"]
        row["category"] = "restaurants"
        row["subcategory"] = "historic"
        row["neighborhood"] = entry.get("neighborhood", "")
        row["summary"] = entry.get("summary", "")
        row["tags"] = "source:manual-historic"
        rows.append(row)
        added += 1

    # Write back
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for row in rows:
            clean = {k: row.get(k, "") for k in FIELDNAMES}
            writer.writerow(clean)

    print(f"Tagged {tagged} entries as historic")
    print(f"Added {added} new historic entries")
    print(f"Total rows: {len(rows)}")


if __name__ == "__main__":
    main()
