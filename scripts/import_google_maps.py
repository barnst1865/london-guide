"""Import and categorize scraped Google Maps list data into CSV."""

import csv
import json
import os
import pathlib
import re

PROJ = pathlib.Path(__file__).resolve().parent.parent
LISTS_DIR = PROJ / "data" / "google_maps_lists"
EXISTING_CSV = PROJ / "data" / "sites.csv"
CSV_OUT = PROJ / "data" / "google_maps_raw.csv"

FIELDNAMES = [
    "id", "name", "lat", "lon", "category", "subcategory", "neighborhood",
    "address", "summary", "price_range", "kid_friendly", "visited", "rating",
    "website", "google_maps_url", "tags", "notes",
]

# ---- Type-to-category/subcategory mapping ----
TYPE_MAP = {
    # Restaurants & Food
    "Restaurant": ("restaurants", "restaurant"),
    "Pub": ("restaurants", "pub"),
    "Gastropub": ("restaurants", "gastropub"),
    "Cafe": ("restaurants", "cafe"),
    "Coffee shop": ("restaurants", "cafe"),
    "Coffee stand": ("restaurants", "cafe"),
    "Tea house": ("restaurants", "cafe"),
    "Bakery": ("restaurants", "bakery"),
    "Patisserie": ("restaurants", "bakery"),
    "Bagel shop": ("restaurants", "bakery"),
    "Cocktail bar": ("restaurants", "cocktail-bar"),
    "Bar": ("restaurants", "cocktail-bar"),
    "Blues club": ("restaurants", "cocktail-bar"),
    "Wine bar": ("restaurants", "wine-bar"),
    "Market": ("restaurants", "market"),
    "Flea market": ("restaurants", "market"),
    "Food court": ("restaurants", "street-food"),
    "Food producer": ("restaurants", "market"),
    "Cheese shop": ("restaurants", "market"),
    "Cheese manufacturer": ("restaurants", "market"),
    "Butcher shop": ("restaurants", "market"),
    "Farm shop": ("restaurants", "market"),
    "Grocery store": ("restaurants", "market"),
    "Deli": ("restaurants", "market"),
    "Ice Cream": ("restaurants", "ice-cream"),
    "Brewery": ("restaurants", "pub"),
    "Irish pub": ("restaurants", "pub"),
    "Inn": ("restaurants", "pub"),
    "Grill": ("restaurants", "restaurant"),
    "Seafood": ("restaurants", "restaurant"),
    "Italian": ("restaurants", "restaurant"),
    "French": ("restaurants", "restaurant"),
    "Indian": ("restaurants", "restaurant"),
    "British": ("restaurants", "restaurant"),
    "Modern British": ("restaurants", "restaurant"),
    "Modern European restaurant": ("restaurants", "restaurant"),
    "Modern European": ("restaurants", "restaurant"),
    "Mediterranean": ("restaurants", "restaurant"),
    "Mexican": ("restaurants", "restaurant"),
    "Middle Eastern": ("restaurants", "restaurant"),
    "Japanese": ("restaurants", "restaurant"),
    "Indonesian": ("restaurants", "restaurant"),
    "Portuguese": ("restaurants", "restaurant"),
    "Bangladeshi": ("restaurants", "restaurant"),
    "Punjabi": ("restaurants", "restaurant"),
    "Shawarma restaurant": ("restaurants", "restaurant"),
    "Pizza": ("restaurants", "restaurant"),
    "Fish and Chips": ("restaurants", "restaurant"),
    "Country food restaurant": ("restaurants", "restaurant"),
    "Pie shop": ("restaurants", "restaurant"),
    "Buffet": ("restaurants", "restaurant"),
    "Diner": ("restaurants", "restaurant"),
    "Beer store": ("restaurants", "pub"),
    "Steak house": ("restaurants", "restaurant"),
    # Attractions & Museums
    "Museum": ("attractions", "museum"),
    "Art museum": ("attractions", "gallery"),
    "History museum": ("attractions", "museum"),
    "National museum": ("attractions", "museum"),
    "Natural history museum": ("attractions", "museum"),
    "Archaeological museum": ("attractions", "museum"),
    "Army museum": ("attractions", "museum"),
    "War museum": ("attractions", "museum"),
    "Maritime museum": ("attractions", "museum"),
    "Rail museum": ("attractions", "museum"),
    "Open air museum": ("attractions", "museum"),
    "Children's museum": ("attractions", "museum"),
    "Local history museum": ("attractions", "museum"),
    "Historical place museum": ("attractions", "museum"),
    "Tourist attraction": ("attractions", "landmark"),
    "Cultural landmark": ("attractions", "landmark"),
    "Park": ("attractions", "park"),
    "Garden": ("attractions", "garden"),
    "Zoo": ("attractions", "zoo"),
    "Wildlife and safari park": ("attractions", "zoo"),
    "Soccer club": ("attractions", "football"),
    "Baseball field": ("attractions", "sports"),
    "Sculpture": ("attractions", "landmark"),
    "Bridge": ("attractions", "landmark"),
    "Event venue": ("attractions", "landmark"),
    "Visitor center": ("attractions", "landmark"),
    "Tour agency": ("attractions", "landmark"),
    "Boat rental service": ("attractions", "landmark"),
    "College": ("attractions", "landmark"),
    "Academic department": ("attractions", "landmark"),
    # Historic Sites
    "Castle": ("historic-sites", "castle"),
    "Cathedral": ("historic-sites", "medieval"),
    "Church": ("historic-sites", "medieval"),
    "Anglican church": ("historic-sites", "medieval"),
    "Episcopal church": ("historic-sites", "medieval"),
    "Cemetery": ("historic-sites", "memorial"),
    "Monument": ("historic-sites", "memorial"),
    "Memorial": ("historic-sites", "memorial"),
    "Memorial park": ("historic-sites", "memorial"),
    "Historical landmark": ("historic-sites", "memorial"),
    "Historical place": ("historic-sites", "memorial"),
    "Quarry": ("historic-sites", "memorial"),
    # Day Trips
    "National park": ("day-trips", "national-park"),
    "Nature preserve": ("day-trips", "countryside"),
    "Mountain peak": ("day-trips", "countryside"),
    "Ravine": ("day-trips", "countryside"),
    "Beach": ("day-trips", "coast"),
    "Bay": ("day-trips", "coast"),
    "Rock": ("day-trips", "coast"),
    "Scenic spot": ("day-trips", "coast"),
    "Hiking area": ("day-trips", "countryside"),
    "Woods": ("day-trips", "countryside"),
    "Bird watching area": ("day-trips", "countryside"),
    # Kid Friendly
    "Amusement park": ("kid-friendly", "theme-park"),
    "Theme park": ("kid-friendly", "theme-park"),
    "Paintball center": ("kid-friendly", "outdoor-adventure"),
    "Rock climbing gym": ("kid-friendly", "sports"),
    "Pick your own farm produce": ("kid-friendly", "farm"),
}

# Types to skip entirely
SKIP_TYPES = {
    "Permanently closed",
    "Supermarket",
    "Shoe store",
    "Shoe repair shop",
    "Clothing store",
    "Jewelry designer",
    "International airport",
    "K-12 school",
    "International school",
    "Apartment complex",
    "Non-profit organization",
    "Grammar school",
    "Self-catering accommodation",
    "Holiday home",
    "Spa",
}

# Hotel patterns to skip
HOTEL_PATTERN = re.compile(r"\d-star hotel", re.IGNORECASE)

# UK postcode pattern to detect address-as-type entries
UK_POSTCODE = re.compile(r"[A-Z]{1,2}\d[A-Z\d]?\s*\d[A-Z]{2}", re.IGNORECASE)
ADDRESS_INDICATORS = ["United Kingdom", "London ", "England"]


def slugify(text):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower().strip())
    return slug.strip("-")


def is_address_type(type_val):
    """Check if the type field actually contains an address instead of a type."""
    if not type_val:
        return False
    if any(ind in type_val for ind in ADDRESS_INDICATORS):
        return True
    if UK_POSTCODE.search(type_val):
        return True
    return False


def is_coordinate_name(name):
    """Check if name is actually coordinates or a raw address."""
    if re.match(r'^[\d\.\-,\s\xb0\'"NSEW]+$', name):
        return True
    if re.match(r"^\d+\s+\w+\s+(St|Rd|Ln|Ave|Dr|Pl|Ct|Walk)", name):
        return True
    return False


def normalize_name(name):
    """Normalize name for dedup matching."""
    n = name.lower().strip()
    n = re.sub(r"^the\s+", "", n)
    n = re.sub(r"[^a-z0-9\s]", "", n)
    n = re.sub(r"\s+", " ", n).strip()
    return n


def categorize(place, source_list):
    """Map a Google Maps place to our category/subcategory schema."""
    name = place.get("name", "").strip()
    gtype = place.get("type", "").strip()
    rating = place.get("rating", "")
    reviews = place.get("reviews", "")
    price = place.get("price", "")

    # Skip coordinate names and raw addresses
    if is_coordinate_name(name):
        return None

    # Skip if name is empty or too short
    if not name or len(name) < 2:
        return None

    # Handle address-as-type entries
    address = ""
    if is_address_type(gtype):
        address = gtype
        gtype = ""

    # Skip hotels
    if HOTEL_PATTERN.search(gtype):
        return None

    # Skip unwanted types
    if gtype in SKIP_TYPES:
        return None

    # Look up category/subcategory
    category = ""
    subcategory = ""
    if gtype in TYPE_MAP:
        category, subcategory = TYPE_MAP[gtype]
    elif gtype:
        # Try partial match
        for type_key, (cat, subcat) in TYPE_MAP.items():
            if type_key.lower() in gtype.lower() or gtype.lower() in type_key.lower():
                category, subcategory = cat, subcat
                break

    # Default: uncategorized
    if not category:
        category = "attractions"
        subcategory = "landmark"

    # Normalize price to our schema
    price_map = {
        "$$$$": "$$$$",
        "$$$": "$$$",
        "$$": "$$",
        "Very expensive": "$$$$",
        "Moderately priced": "$$",
        "Inexpensive": "$",
    }
    price_range = ""
    if price in price_map:
        price_range = price_map[price]
    elif price.startswith("£"):
        # Convert £ ranges to $ symbols roughly
        if "100" in price:
            price_range = "$$$$"
        elif "20" in price or "30" in price:
            price_range = "$$"
        elif "10" in price:
            price_range = "$"
        elif "1" in price:
            price_range = "$"

    return {
        "id": slugify(name),
        "name": name,
        "lat": "",
        "lon": "",
        "category": category,
        "subcategory": subcategory,
        "neighborhood": "",
        "address": address,
        "summary": "",
        "price_range": price_range,
        "kid_friendly": "",
        "visited": "",
        "rating": "",
        "website": "",
        "google_maps_url": "",
        "tags": f"source:{source_list}",
        "notes": f"Google rating: {rating}/5 ({reviews} reviews)" if rating else "",
    }


def load_existing_ids():
    """Load existing site IDs from sites.csv for dedup."""
    ids = set()
    names = set()
    if EXISTING_CSV.exists():
        with open(EXISTING_CSV, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("id"):
                    ids.add(row["id"])
                if row.get("name"):
                    names.add(normalize_name(row["name"]))
    return ids, names


def main():
    existing_ids, existing_names = load_existing_ids()
    all_entries = []
    seen_ids = set()
    seen_names = set()

    # Process each JSON file
    json_files = sorted(LISTS_DIR.glob("*.json"))
    print(f"Found {len(json_files)} Google Maps list files")

    for json_file in json_files:
        with open(json_file, encoding="utf-8") as f:
            data = json.load(f)

        list_name = data.get("listName", json_file.stem)
        places = data.get("places", [])
        imported = 0
        skipped = 0
        dupes = 0

        for place in places:
            entry = categorize(place, list_name)
            if entry is None:
                skipped += 1
                continue

            # Dedup against existing data
            norm = normalize_name(entry["name"])
            if entry["id"] in existing_ids or norm in existing_names:
                dupes += 1
                continue

            # Dedup within this import
            if entry["id"] in seen_ids or norm in seen_names:
                dupes += 1
                continue

            seen_ids.add(entry["id"])
            seen_names.add(norm)
            all_entries.append(entry)
            imported += 1

        print(f"  {list_name}: {len(places)} total, {imported} imported, {skipped} skipped, {dupes} dupes")

    # Write output
    with open(CSV_OUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(all_entries)

    # Summary by category
    cats = {}
    for e in all_entries:
        cat = e["category"]
        cats[cat] = cats.get(cat, 0) + 1

    print(f"\nTotal imported: {len(all_entries)}")
    print("By category:")
    for cat, count in sorted(cats.items()):
        print(f"  {cat}: {count}")


if __name__ == "__main__":
    main()
