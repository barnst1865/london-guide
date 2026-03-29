"""Validate geocoded coordinates — flag entries that look wrong."""

import csv
import math
import pathlib

PROJ = pathlib.Path(__file__).resolve().parent.parent
CSV_PATH = PROJ / "data" / "sites.csv"
FLAGGED_OUT = PROJ / "data" / "location_flagged.csv"

FIELDNAMES = [
    "id", "name", "lat", "lon", "category", "subcategory", "neighborhood",
    "address", "summary", "price_range", "kid_friendly", "visited", "rating",
    "website", "google_maps_url", "tags", "notes",
]

# Greater London bounding box (generous)
LONDON_BBOX = {
    "lat_min": 51.28,
    "lat_max": 51.69,
    "lon_min": -0.51,
    "lon_max": 0.33,
}

# UK bounding box
UK_BBOX = {
    "lat_min": 49.8,
    "lat_max": 60.9,
    "lon_min": -8.2,
    "lon_max": 1.8,
}

# London center for distance checks
LONDON_CENTER = (51.509, -0.118)

# Categories expected to be in London
LONDON_CATEGORIES = {"restaurants", "wmd-sites", "kid-friendly", "movie-sites", "neighborhoods"}

# Categories that can be anywhere in UK
UK_CATEGORIES = {"day-trips", "historic-sites", "attractions"}


def distance_km(lat1, lon1, lat2, lon2):
    """Approximate distance in km using Haversine."""
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    return R * 2 * math.asin(math.sqrt(a))


def in_bbox(lat, lon, bbox):
    return bbox["lat_min"] <= lat <= bbox["lat_max"] and bbox["lon_min"] <= lon <= bbox["lon_max"]


def validate(row):
    """Return a reason string if the entry is suspicious, or None if OK."""
    lat = row.get("lat", "").strip()
    lon = row.get("lon", "").strip()
    if not lat or not lon:
        return None  # No coordinates to validate

    try:
        lat_f, lon_f = float(lat), float(lon)
    except ValueError:
        return "INVALID_COORDS: lat/lon not numeric"

    # Check for null island (0, 0)
    if lat_f == 0 and lon_f == 0:
        return "NULL_ISLAND: coordinates are 0,0"

    category = row.get("category", "")
    neighborhood = row.get("neighborhood", "").lower()
    name = row.get("name", "")

    # Check if outside UK entirely
    if not in_bbox(lat_f, lon_f, UK_BBOX):
        return f"OUTSIDE_UK: ({lat_f:.4f}, {lon_f:.4f}) is not in the UK"

    # For London-expected categories, check if within London
    if category in LONDON_CATEGORIES:
        if not in_bbox(lat_f, lon_f, LONDON_BBOX):
            dist = distance_km(lat_f, lon_f, *LONDON_CENTER)
            return f"OUTSIDE_LONDON: {name} is {dist:.0f}km from London center ({lat_f:.4f}, {lon_f:.4f})"

    # For any category: if neighborhood mentions London but coords are far away
    if "london" in neighborhood or neighborhood in ("whitehall", "soho", "mayfair", "chelsea", "covent garden", "pimlico", "marylebone", "belgravia"):
        if not in_bbox(lat_f, lon_f, LONDON_BBOX):
            dist = distance_km(lat_f, lon_f, *LONDON_CENTER)
            return f"NEIGHBORHOOD_MISMATCH: neighborhood='{row.get('neighborhood')}' but coords are {dist:.0f}km from London ({lat_f:.4f}, {lon_f:.4f})"

    return None


def main():
    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    flagged = []
    for row in rows:
        reason = validate(row)
        if reason:
            flagged.append({**row, "flag_reason": reason})

    if flagged:
        flag_fields = FIELDNAMES + ["flag_reason"]
        with open(FLAGGED_OUT, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=flag_fields)
            writer.writeheader()
            writer.writerows(flagged)

        print(f"Flagged {len(flagged)} entries → {FLAGGED_OUT}")
        for entry in flagged:
            print(f"  [{entry['flag_reason']}] {entry['name']}")
    else:
        print("All coordinates look valid!")

    print(f"\nTotal rows checked: {len(rows)}")
    with_coords = sum(1 for r in rows if r.get("lat") and r.get("lon"))
    print(f"With coordinates: {with_coords}")
    print(f"Without coordinates: {len(rows) - with_coords}")


if __name__ == "__main__":
    main()
