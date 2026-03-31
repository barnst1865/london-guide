"""Remove garbage entries from sites.csv (description fragments from restaurant parser)."""

import csv
import pathlib

PROJ = pathlib.Path(__file__).resolve().parent.parent
CSV_PATH = PROJ / "data" / "sites.csv"

FIELDNAMES = [
    "id", "name", "lat", "lon", "category", "subcategory", "neighborhood",
    "address", "summary", "price_range", "kid_friendly", "visited", "rating",
    "website", "google_maps_url", "tags", "notes",
]

# Entries to remove by exact ID (confirmed garbage from restaurant parser)
REMOVE_IDS = {
    "a-hefty-bill-1f-everyone-orders-the-fancy-steaks-no-private-room-but-can-seat-8",
    "and-woodhouse-brewery",
    "are-the-only-food",
    "book-good-set-menus-for-a-larger-dinner",
    "cancellation-policy-british-food",
    "by-or-on-whitehall",
    "by-thames-house",
    "corinthla-also-does-a-very-nice-afternoon-tea-expensive-and-fancy",
    "cittle-of-york-huge-and-inexpensive-also-a-sam-smiths",
    "excellent-food-nice-ambiance",
    "further-east",
    "in-trafalgar-square",
    "in-a-category-all-its-own",
    "in-the-old-city-of-london",
    "north-of-whitehall-st-james",
    "entrees-are-30",
    "from-heddon-st-kitchen",
    "has-plenty-of-beer-and-the-cheapest-pint-in-all-of-london-great-tapas",
    "here-not-too-expensive",
    "hours-prior-partial-cover-and-heating-if-it-rains-no-option",
    "house",
    "is-very-good",
    "line-so-best-to-plan-ahead-if-you-have-a-group",
    "lunch-not-expensive",
    "main-dining-room",
    "nice-private-room-for-a-group",
    "notice",
    "nutmeg",
    "one-or-very-small-group-but-a-classic-british-experience",
    "room-available",
    "slower",
    "table-companions",
    "that-is-quaint-drink-in-the-alleyway-behind-too",
    "to-13-really-nice-set-menu-of-shared-small-plates-for-a-group-lots-of-food",
    "totally-break-the-bank",
    "will-seat-8-later-at-night-there-s-a-dj-so-beware-that-vibe",
    "windows-the-route-from-the-tube-takes-you-on-a-walk-through-a-neighborhood",
    "would-call-a-boozer",
    # Neighborhood headers captured as entries
    "chinatown",
    "28",  # Just the number "28"
}

# Also remove entries where name starts with lowercase (strong signal of fragment)
# but NOT legitimate entries like "de" prefixes


def is_garbage(row):
    """Return True if this entry should be removed."""
    site_id = row.get("id", "")
    name = row.get("name", "").strip()

    # Explicit removal list
    if site_id in REMOVE_IDS:
        return True

    # Name starts with lowercase and is a restaurant (fragment from doc parser)
    if name and name[0].islower() and row.get("category") == "restaurants":
        return True

    # Very short meaningless names
    if len(name) < 3:
        return True

    return False


def main():
    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    kept = []
    removed = []
    for row in rows:
        if is_garbage(row):
            removed.append(row)
        else:
            kept.append(row)

    # Write cleaned CSV
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for row in kept:
            clean = {k: row.get(k, "") for k in FIELDNAMES}
            writer.writerow(clean)

    print(f"Removed {len(removed)} garbage entries, kept {len(kept)}")
    print("\nRemoved entries:")
    for r in sorted(removed, key=lambda x: x.get("name", "")):
        print(f"  - {r.get('name', '')[:70]}")


if __name__ == "__main__":
    main()
