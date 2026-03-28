"""Convert sites.csv to sites.geojson for the Leaflet map."""

import csv
import json
import pathlib
import shutil

DATA_DIR = pathlib.Path(__file__).resolve().parent.parent / "data"
CSV_PATH = DATA_DIR / "sites.csv"
GEOJSON_PATH = DATA_DIR / "sites.geojson"
DOCS_GEOJSON = pathlib.Path(__file__).resolve().parent.parent / "docs" / "data" / "sites.geojson"

FIELDS = [
    "id", "name", "category", "subcategory", "neighborhood", "address",
    "summary", "price_range", "kid_friendly", "visited", "rating",
    "website", "google_maps_url", "tags", "notes",
]


def csv_to_geojson(csv_path: pathlib.Path) -> dict:
    features = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            lat = row.get("lat", "").strip()
            lon = row.get("lon", "").strip()
            if not lat or not lon:
                continue
            try:
                lat_f, lon_f = float(lat), float(lon)
            except ValueError:
                continue

            properties = {}
            for field in FIELDS:
                val = row.get(field, "").strip()
                if field in ("kid_friendly", "visited"):
                    val = val.lower() in ("true", "yes", "1")
                elif field == "rating":
                    val = int(val) if val else None
                properties[field] = val

            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon_f, lat_f],
                },
                "properties": properties,
            }
            features.append(feature)
    return {"type": "FeatureCollection", "features": features}


def main():
    geojson = csv_to_geojson(CSV_PATH)
    with open(GEOJSON_PATH, "w", encoding="utf-8") as f:
        json.dump(geojson, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(geojson['features'])} features to {GEOJSON_PATH}")

    DOCS_GEOJSON.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(GEOJSON_PATH, DOCS_GEOJSON)
    print(f"Copied to {DOCS_GEOJSON}")


if __name__ == "__main__":
    main()
