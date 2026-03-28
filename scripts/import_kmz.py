"""Parse London Football Teams.kmz into CSV rows for sites.csv."""

import csv
import pathlib
import re
import zipfile
from xml.etree import ElementTree as ET

PROJ = pathlib.Path(__file__).resolve().parent.parent
KMZ = PROJ / "Google-maps" / "extracted" / "Takeout" / "My Maps" / "London Football Teams.kmz"
CSV_OUT = PROJ / "data" / "football_raw.csv"


def slugify(text):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower().strip())
    return slug.strip("-")


def parse_kmz(kmz_path):
    entries = []
    ns = {"kml": "http://www.opengis.net/kml/2.2"}

    with zipfile.ZipFile(kmz_path) as z:
        kml_data = z.read("doc.kml").decode("utf-8")

    root = ET.fromstring(kml_data)

    for pm in root.iter("{http://www.opengis.net/kml/2.2}Placemark"):
        name_el = pm.find("kml:name", ns)
        name = name_el.text.strip() if name_el is not None else ""
        if not name:
            continue

        coords_el = pm.find(".//kml:coordinates", ns)
        if coords_el is None:
            continue

        coords_text = coords_el.text.strip()
        parts = coords_text.split(",")
        if len(parts) < 2:
            continue

        lon, lat = float(parts[0]), float(parts[1])

        # Extract description (may contain stadium name, tier, URL)
        desc_el = pm.find("kml:description", ns)
        desc_html = desc_el.text if desc_el is not None else ""
        # Strip HTML tags
        desc_text = re.sub(r"<[^>]+>", " ", desc_html).strip() if desc_html else ""

        entries.append({
            "id": slugify(name),
            "name": name,
            "lat": str(lat),
            "lon": str(lon),
            "category": "attractions",
            "subcategory": "football",
            "neighborhood": "London",
            "address": "",
            "summary": f"Football club in London",
            "price_range": "",
            "kid_friendly": "true",
            "visited": "",
            "rating": "",
            "website": "",
            "google_maps_url": "",
            "tags": "sports|football",
            "notes": desc_text[:200] if desc_text else "",
        })

    return entries


def main():
    entries = parse_kmz(KMZ)

    fieldnames = [
        "id", "name", "lat", "lon", "category", "subcategory", "neighborhood",
        "address", "summary", "price_range", "kid_friendly", "visited", "rating",
        "website", "google_maps_url", "tags", "notes",
    ]

    with open(CSV_OUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(entries)

    print(f"Wrote {len(entries)} football clubs to {CSV_OUT}")


if __name__ == "__main__":
    main()
