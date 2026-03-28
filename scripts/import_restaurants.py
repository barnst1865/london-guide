"""Parse London Restaurants.docx into CSV rows for sites.csv."""

import csv
import pathlib
import re
import zipfile
from xml.etree import ElementTree as ET

PROJ = pathlib.Path(__file__).resolve().parent.parent
DOCX = PROJ / "Misc-sources" / "London Restaurants.docx"
CSV_OUT = PROJ / "data" / "restaurants_raw.csv"

# Subcategory keywords
PUB_KEYWORDS = ["pub", "tavern", "arms", "inn", "ale", "brewery", "boar"]
BAR_KEYWORDS = ["bar", "wine bar", "cocktail"]
CAFE_KEYWORDS = ["cafe", "café", "coffee", "bakery", "breakfast"]


def extract_text(docx_path):
    """Extract paragraphs from a .docx file."""
    paragraphs = []
    with zipfile.ZipFile(docx_path) as z:
        xml = z.read("word/document.xml")
        root = ET.fromstring(xml)
        ns = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
        for para in root.iter(f"{{{ns}}}p"):
            text = "".join(
                r.text or ""
                for r in para.iter(f"{{{ns}}}t")
            )
            if text.strip():
                paragraphs.append(text.strip())
    return paragraphs


def classify_subcategory(name, text):
    """Guess subcategory from name and description."""
    combined = (name + " " + text).lower()
    if any(kw in combined for kw in PUB_KEYWORDS):
        return "pub"
    if any(kw in combined for kw in BAR_KEYWORDS):
        return "wine-bar"
    if any(kw in combined for kw in CAFE_KEYWORDS):
        return "cafe"
    return "restaurant"


def slugify(text):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower().strip())
    return slug.strip("-")


def parse_restaurants(paragraphs):
    """Parse the document into restaurant entries."""
    entries = []
    current_neighborhood = ""
    section = ""

    for line in paragraphs:
        # Skip the document title
        if line == "Restaurants":
            continue

        # Detect neighborhood headers (lines ending with colon)
        if line.endswith(":") and len(line) < 60:
            current_neighborhood = line.rstrip(":").strip()
            # Clean up neighborhood names
            current_neighborhood = re.sub(r"^(North of|South of|By|In the old|Further)\s+", "", current_neighborhood)
            continue

        # Detect section headers
        if line.startswith("Restaurants with outside") or line.startswith("Recent suggestions") or \
           line.startswith("Breakfast") or line.startswith("Pubs") or line.startswith("Not pubs"):
            section = line.split("\n")[0].strip()
            continue

        # Parse bullet entries (start with bullet char or restaurant name)
        # Remove bullet characters
        clean = re.sub(r"^[\uf0b7\u2022\u25cf\-\*]+\s*", "", line).strip()
        if not clean:
            continue

        # Try to split name from description at first dash or colon
        match = re.match(r"^([^–\-:]+?)\s*[–\-:]\s*(.+)$", clean)
        if match:
            name = match.group(1).strip()
            description = match.group(2).strip()
        else:
            # Just a name with no description
            name = clean.split("(")[0].strip()
            description = clean if clean != name else ""

        # Skip lines that look like headers or non-restaurant text
        if len(name) > 80 or name.startswith("FYI") or name.startswith("Senior Rep"):
            continue

        # Remove trailing punctuation from names
        name = re.sub(r"[\.\,]+$", "", name).strip()

        if not name or len(name) < 2:
            continue

        # Determine subcategory
        subcat = classify_subcategory(name, description)

        # Override neighborhood from section if applicable
        neigh = current_neighborhood
        if section == "Pubs" and not neigh:
            neigh = "City of London"
        if section == "Breakfast":
            subcat = "cafe"

        entries.append({
            "id": slugify(name),
            "name": name,
            "lat": "",
            "lon": "",
            "category": "restaurants",
            "subcategory": subcat,
            "neighborhood": neigh,
            "address": "",
            "summary": description[:200] if description else "",
            "price_range": "",
            "kid_friendly": "",
            "visited": "",
            "rating": "",
            "website": "",
            "google_maps_url": "",
            "tags": "",
            "notes": "",
        })

    return entries


def main():
    paragraphs = extract_text(DOCX)
    entries = parse_restaurants(paragraphs)

    # Deduplicate by id
    seen = set()
    unique = []
    for e in entries:
        if e["id"] not in seen:
            seen.add(e["id"])
            unique.append(e)

    fieldnames = [
        "id", "name", "lat", "lon", "category", "subcategory", "neighborhood",
        "address", "summary", "price_range", "kid_friendly", "visited", "rating",
        "website", "google_maps_url", "tags", "notes",
    ]

    with open(CSV_OUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(unique)

    print(f"Wrote {len(unique)} restaurants to {CSV_OUT}")


if __name__ == "__main__":
    main()
