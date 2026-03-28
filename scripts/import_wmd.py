"""Parse UK WMD Tour - Fleshed OUt.docx into CSV rows for sites.csv."""

import csv
import pathlib
import re
import zipfile
from xml.etree import ElementTree as ET

PROJ = pathlib.Path(__file__).resolve().parent.parent
DOCX = PROJ / "Misc-sources" / "UK WMD Tour - Fleshed OUt.docx"
CSV_OUT = PROJ / "data" / "wmd_raw.csv"

SECTION_KEYWORDS = {
    "nuclear": "nuclear",
    "radiological": "radiological",
    "chemical": "chemical",
    "biological": "biological",
    "missile": "missile",
    "activism": "activism",
}


def extract_text(docx_path):
    paragraphs = []
    with zipfile.ZipFile(docx_path) as z:
        xml = z.read("word/document.xml")
        root = ET.fromstring(xml)
        ns = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
        for para in root.iter(f"{{{ns}}}p"):
            text = "".join(r.text or "" for r in para.iter(f"{{{ns}}}t"))
            if text.strip():
                # Replace smart quotes and dashes
                text = text.replace("\u2013", "-").replace("\u2014", "-")
                text = text.replace("\u2018", "'").replace("\u2019", "'")
                text = text.replace("\u201c", '"').replace("\u201d", '"')
                paragraphs.append(text.strip())
    return paragraphs


def slugify(text):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower().strip())
    return slug.strip("-")


def detect_section(line):
    lower = line.lower().strip()
    for keyword, subcat in SECTION_KEYWORDS.items():
        if lower.startswith(keyword) and len(lower) < 30:
            return subcat
    return None


def parse_wmd(paragraphs):
    entries = []
    current_subcat = "nuclear"
    current_name = ""
    current_location = ""
    current_desc_lines = []

    def flush():
        if current_name:
            desc = " ".join(current_desc_lines).strip()
            entries.append({
                "id": slugify(current_name),
                "name": current_name,
                "lat": "",
                "lon": "",
                "category": "wmd-sites",
                "subcategory": current_subcat,
                "neighborhood": current_location,
                "address": "",
                "summary": desc[:200] if desc else "",
                "price_range": "",
                "kid_friendly": "",
                "visited": "",
                "rating": "",
                "website": "",
                "google_maps_url": "",
                "tags": "",
                "notes": desc[200:] if len(desc) > 200 else "",
            })

    for line in paragraphs:
        # Detect section headers
        new_section = detect_section(line)
        if new_section:
            flush()
            current_subcat = new_section
            current_name = ""
            current_desc_lines = []
            continue

        # Detect site names (bold lines, often with location in parens)
        # Sites typically start with a name and may have (Location) after
        name_match = re.match(r"^(?:\d+\.\s*)?(.+?)(?:\s*\(([^)]+)\))?\s*$", line)

        # Heuristic: if line is short and looks like a title (no period in first 40 chars)
        if len(line) < 80 and "." not in line[:40] and not line.startswith("Once") and not line.startswith("A ") and not line.startswith("The ") and not line.startswith("During"):
            # Could be a site name
            if name_match:
                flush()
                current_name = name_match.group(1).strip()
                current_location = name_match.group(2) or ""
                current_desc_lines = []
                continue

        # Check if this is a sub-site (e.g., Litvinenko locations starting with place name)
        if " - " in line[:50] and len(line) > 50:
            flush()
            parts = line.split(" - ", 1)
            current_name = parts[0].strip()
            current_location = ""
            current_desc_lines = [parts[1].strip()] if len(parts) > 1 else []
            continue

        # Otherwise it's description text
        if current_name:
            current_desc_lines.append(line)

    flush()
    return entries


def main():
    paragraphs = extract_text(DOCX)
    entries = parse_wmd(paragraphs)

    # Deduplicate
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

    print(f"Wrote {len(unique)} WMD sites to {CSV_OUT}")


if __name__ == "__main__":
    main()
