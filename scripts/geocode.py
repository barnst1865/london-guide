"""Geocode sites in sites.csv that are missing lat/lon using Nominatim."""

import csv
import json
import pathlib
import time
import urllib.request
import urllib.parse

PROJ = pathlib.Path(__file__).resolve().parent.parent
CSV_PATH = PROJ / "data" / "sites.csv"
CACHE_PATH = PROJ / "data" / "geocode_cache.json"

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
USER_AGENT = "KoikFamilyLondonGuide/1.0"

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


def _nominatim_query(query):
    """Execute a single Nominatim query."""
    params = urllib.parse.urlencode({
        "q": query,
        "format": "json",
        "limit": 1,
        "countrycodes": "gb",
    })
    url = f"{NOMINATIM_URL}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if data:
                return float(data[0]["lat"]), float(data[0]["lon"])
    except Exception:
        pass
    return None, None


def geocode(name, neighborhood="", address="", category=""):
    """Query Nominatim with multiple fallback strategies."""
    # Strategy 1: address if available
    if address:
        lat, lon = _nominatim_query(f"{name}, {address}")
        if lat: return lat, lon

    # Strategy 2: name + neighborhood + London
    if neighborhood and "london" not in neighborhood.lower():
        lat, lon = _nominatim_query(f"{name}, {neighborhood}, London, UK")
        if lat: return lat, lon

    # Strategy 3: name + London (for restaurants/attractions)
    if category in ("restaurants", "movie-sites", "kid-friendly", "wmd-sites"):
        lat, lon = _nominatim_query(f"{name}, London")
        if lat: return lat, lon

    # Strategy 4: just name + UK (for day-trips and historic sites)
    lat, lon = _nominatim_query(f"{name}, UK")
    if lat: return lat, lon

    # Strategy 5: name + category hint
    type_hints = {
        "restaurants": "restaurant",
        "attractions": "museum",
        "historic-sites": "castle",
    }
    hint = type_hints.get(category, "")
    if hint:
        lat, lon = _nominatim_query(f"{name} {hint}, London")
        if lat: return lat, lon

    return None, None


def main():
    cache = load_cache()

    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    geocoded = 0
    failed = 0

    for row in rows:
        lat = row.get("lat", "").strip()
        lon = row.get("lon", "").strip()
        if lat and lon:
            continue

        name = row.get("name", "")
        site_id = row.get("id", "")

        # Check cache first
        if site_id in cache:
            cached = cache[site_id]
            if cached["lat"]:
                row["lat"] = str(cached["lat"])
                row["lon"] = str(cached["lon"])
                geocoded += 1
                continue
            else:
                failed += 1
                continue

        neighborhood = row.get("neighborhood", "")
        address = row.get("address", "")

        category = row.get("category", "")
        print(f"Geocoding: {name} ({category}/{neighborhood})...")
        lat_val, lon_val = geocode(name, neighborhood, address, category)

        if lat_val is not None:
            row["lat"] = str(lat_val)
            row["lon"] = str(lon_val)
            cache[site_id] = {"lat": lat_val, "lon": lon_val}
            geocoded += 1
            print(f"  -> {lat_val}, {lon_val}")
        else:
            cache[site_id] = {"lat": None, "lon": None}
            failed += 1
            print(f"  -> NOT FOUND")

        # Rate limit: 1 request per second
        time.sleep(1.1)

    # Write back
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for row in rows:
            clean = {k: row.get(k, "") for k in FIELDNAMES}
            writer.writerow(clean)

    save_cache(cache)
    print(f"\nGeocoded: {geocoded}, Failed: {failed}, Total rows: {len(rows)}")


if __name__ == "__main__":
    main()
