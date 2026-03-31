"""Add London filming locations to sites.csv, organized by film universe."""

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

MOVIE_SITES = [
    # ---- Harry Potter ----
    {"name": "Leadenhall Market", "lat": "51.5131", "lon": "-0.0838",
     "subcategory": "harry-potter", "neighborhood": "City of London",
     "summary": "The covered Victorian market doubled as Diagon Alley in Harry Potter and the Philosopher's Stone. The entrance to The Leaky Cauldron was filmed at 42 Bull's Head Passage.",
     "kid_friendly": "true"},
    {"name": "Australia House (Gringotts)", "lat": "51.5135", "lon": "-0.1170",
     "subcategory": "harry-potter", "neighborhood": "Strand",
     "summary": "The grand marble interior of the Australian High Commission was used as Gringotts Wizarding Bank. The ornate banking hall with its chandeliers is unmistakable.",
     "kid_friendly": "true"},
    {"name": "King's Cross Platform 9 3/4", "lat": "51.5322", "lon": "-0.1240",
     "subcategory": "harry-potter", "neighborhood": "King's Cross",
     "summary": "The famous platform where Hogwarts students catch the Express. A photo opportunity with a trolley disappearing into the wall is set up in the station concourse.",
     "kid_friendly": "true"},
    {"name": "Millennium Bridge", "lat": "51.5095", "lon": "-0.0985",
     "subcategory": "harry-potter", "neighborhood": "Southwark",
     "summary": "The pedestrian bridge was spectacularly destroyed by Death Eaters in Harry Potter and the Half-Blood Prince. Connects St Paul's to Tate Modern.",
     "kid_friendly": "true"},
    {"name": "Reptile House, London Zoo", "lat": "51.5353", "lon": "-0.1534",
     "subcategory": "harry-potter", "neighborhood": "Regent's Park",
     "summary": "Where Harry first discovers he can talk to snakes in Philosopher's Stone. He accidentally sets a Burmese python free by making the glass vanish.",
     "kid_friendly": "true"},
    {"name": "St Pancras Renaissance Hotel", "lat": "51.5312", "lon": "-0.1260",
     "subcategory": "harry-potter", "neighborhood": "King's Cross",
     "summary": "The stunning Gothic exterior was used for exterior shots of King's Cross Station. Ron and Harry fly the Ford Anglia past it in Chamber of Secrets.",
     "kid_friendly": "true"},
    {"name": "Lambeth Bridge", "lat": "51.4952", "lon": "-0.1229",
     "subcategory": "harry-potter", "neighborhood": "Westminster",
     "summary": "The Knight Bus squeezes between two red double-deckers on this bridge in Prisoner of Azkaban.",
     "kid_friendly": "true"},
    {"name": "Piccadilly Circus", "lat": "51.5100", "lon": "-0.1348",
     "subcategory": "harry-potter", "neighborhood": "West End",
     "summary": "Harry, Ron, and Hermione apparate into Piccadilly Circus in Deathly Hallows Part 1, nearly getting hit by a bus on Shaftesbury Avenue.",
     "kid_friendly": "true"},

    # ---- James Bond ----
    {"name": "MI6 Building (SIS)", "lat": "51.4875", "lon": "-0.1244",
     "subcategory": "james-bond", "neighborhood": "Vauxhall",
     "summary": "The distinctive green and cream headquarters of the Secret Intelligence Service on the Thames. Featured in GoldenEye, The World Is Not Enough, and Skyfall (where it gets blown up).",
     },
    {"name": "Treasury Building, Whitehall", "lat": "51.5025", "lon": "-0.1276",
     "subcategory": "james-bond", "neighborhood": "Westminster",
     "summary": "The view from M's office in several Bond films looks out over Horse Guards Parade. The building itself doubles as MI6 interiors.",
     },
    {"name": "Old Royal Naval College", "lat": "51.4834", "lon": "-0.0064",
     "subcategory": "james-bond", "neighborhood": "Greenwich",
     "summary": "Featured in multiple Bond films and also The Crown, Thor: The Dark World, and Les Miserables. The Painted Hall is one of London's most spectacular interiors.",
     },
    {"name": "Somerset House", "lat": "51.5113", "lon": "-0.1174",
     "subcategory": "james-bond", "neighborhood": "Strand",
     "summary": "Used in Tomorrow Never Dies and Goldeneye. The grand neoclassical courtyard with its fountains has also appeared in Sherlock Holmes and many other films.",
     },
    {"name": "Tower Bridge", "lat": "51.5055", "lon": "-0.0754",
     "subcategory": "james-bond", "neighborhood": "Tower Hamlets",
     "summary": "Bond drives a speedboat under the bridge in The World Is Not Enough and it appears in Die Another Day. One of London's most iconic landmarks.",
     "kid_friendly": "true"},
    {"name": "Barbican Centre", "lat": "51.5200", "lon": "-0.0937",
     "subcategory": "james-bond", "neighborhood": "City of London",
     "summary": "The brutalist arts complex doubled as Shanghai in Skyfall. Its distinctive architectural style has made it a popular filming location.",
     },
    {"name": "Natural History Museum", "lat": "51.4967", "lon": "-0.1764",
     "subcategory": "james-bond", "neighborhood": "South Kensington",
     "summary": "Featured in Spectre where Bond chases Mr. Hinx. Also a Paddington filming location. One of London's finest free museums with dinosaur galleries.",
     "kid_friendly": "true"},

    # ---- Sherlock Holmes ----
    {"name": "Speedy's Cafe", "lat": "51.5255", "lon": "-0.1388",
     "subcategory": "sherlock", "neighborhood": "Euston",
     "summary": "The cafe next door to 221B Baker Street in BBC's Sherlock. Located at 187 North Gower Street, it became a pilgrimage site for fans of the Benedict Cumberbatch series.",
     },
    {"name": "St Bartholomew's Hospital", "lat": "51.5180", "lon": "-0.1003",
     "subcategory": "sherlock", "neighborhood": "City of London",
     "summary": "Where Sherlock fakes his death by jumping from the roof in 'The Reichenbach Fall' (BBC Sherlock). Also where Watson and Holmes first meet in Conan Doyle's original stories.",
     },
    {"name": "The Criterion Restaurant", "lat": "51.5098", "lon": "-0.1340",
     "subcategory": "sherlock", "neighborhood": "Piccadilly",
     "summary": "Where Dr Watson meets Stamford in A Study in Scarlet, leading to his introduction to Sherlock Holmes. The ornate Neo-Byzantine interior is stunning.",
     },
    {"name": "Portland Place", "lat": "51.5214", "lon": "-0.1448",
     "subcategory": "sherlock", "neighborhood": "Marylebone",
     "summary": "Used as the exterior of 221B Baker Street in BBC's Sherlock. The grand Georgian terrace provided the perfect backdrop for the famous front door.",
     },

    # ---- The Crown ----
    {"name": "Lancaster House", "lat": "51.5034", "lon": "-0.1405",
     "subcategory": "crown", "neighborhood": "St James's",
     "summary": "Doubles as Buckingham Palace interiors in The Crown. Its lavish state rooms with gilded ceilings are even grander than the real palace. Open for occasional public tours.",
     },
    {"name": "Knebworth House", "lat": "51.8692", "lon": "-0.2109",
     "subcategory": "crown", "neighborhood": "Hertfordshire",
     "summary": "Used as various royal estates in The Crown, and also as the Happiness Hotel in The Great Muppet Caper. A stunning Gothic Tudor mansion with beautiful gardens.",
     "kid_friendly": "true"},
    {"name": "Wilton House", "lat": "51.0807", "lon": "-1.8619",
     "subcategory": "crown", "neighborhood": "Wiltshire",
     "summary": "The Double Cube Room doubles as Buckingham Palace in The Crown. Also used in Pride and Prejudice, Sense and Sensibility, and Emma. Magnificent Palladian architecture.",
     },

    # ---- Paddington ----
    {"name": "Paddington Station", "lat": "51.5154", "lon": "-0.1755",
     "subcategory": "paddington", "neighborhood": "Paddington",
     "summary": "Where the Brown family discovers Paddington Bear sitting on his suitcase. Brunel's grand iron and glass trainshed. There's a bronze Paddington statue on Platform 1.",
     "kid_friendly": "true"},
    {"name": "Chalcot Crescent (Browns' House)", "lat": "51.5399", "lon": "-0.1669",
     "subcategory": "paddington", "neighborhood": "Primrose Hill",
     "summary": "The pastel-coloured terraced street in Primrose Hill where the Brown family home is located in the Paddington films. Number 30 is the famous blue door.",
     "kid_friendly": "true"},
    {"name": "Tower of London", "lat": "51.5081", "lon": "-0.0759",
     "subcategory": "paddington", "neighborhood": "Tower Hamlets",
     "summary": "Featured in Paddington 2 during the thrilling chase scene. Nearly 1000 years of history as a royal palace, prison, and home of the Crown Jewels.",
     "kid_friendly": "true"},
    {"name": "St Paul's Cathedral", "lat": "51.5138", "lon": "-0.0984",
     "subcategory": "paddington", "neighborhood": "City of London",
     "summary": "Features in Paddington 2 and countless other films. Wren's masterpiece survived the Blitz. Climb 528 steps to the Golden Gallery for panoramic views.",
     "kid_friendly": "true"},

    # ---- Muppets (supplement existing Great Muppet Caper entries) ----
    {"name": "Battersea Power Station", "lat": "51.4819", "lon": "-0.1458",
     "subcategory": "muppets", "neighborhood": "Battersea",
     "summary": "Featured in The Great Muppet Caper. Now a major redevelopment with shops, restaurants, and apartments. The iconic four chimneys are a London landmark.",
     "kid_friendly": "true"},

    # ---- Notting Hill ----
    {"name": "The Travel Bookshop (Notting Hill)", "lat": "51.5140", "lon": "-0.2012",
     "subcategory": "other-film", "neighborhood": "Notting Hill",
     "summary": "The inspiration for Hugh Grant's bookshop in Notting Hill (1999). The original shop at 13 Blenheim Crescent is now a different business but the blue door at 280 Westbourne Park Road remains famous.",
     },
    {"name": "Kenwood House", "lat": "51.5717", "lon": "-0.1677",
     "subcategory": "other-film", "neighborhood": "Hampstead",
     "summary": "The bench where Hugh Grant and Julia Roberts have their final scene in Notting Hill. A beautiful neoclassical villa on Hampstead Heath with free entry and a stunning art collection.",
     "kid_friendly": "true"},

    # ---- Bridget Jones ----
    {"name": "Borough Market", "lat": "51.5055", "lon": "-0.0910",
     "subcategory": "other-film", "neighborhood": "Southwark",
     "summary": "Bridget Jones's flat is above the Globe pub in Borough Market. London's oldest food market (1014) with incredible street food, artisan produce, and a vibrant atmosphere.",
     "kid_friendly": "true"},
    {"name": "Royal Exchange", "lat": "51.5134", "lon": "-0.0874",
     "subcategory": "other-film", "neighborhood": "City of London",
     "summary": "Where Mark Darcy works in Bridget Jones. The grand colonnaded building near Bank station now houses luxury shops and restaurants.",
     },

    # ---- Kingsman ----
    {"name": "Black Prince Pub", "lat": "51.4903", "lon": "-0.1103",
     "subcategory": "other-film", "neighborhood": "Kennington",
     "summary": "Doubles as the Black Prince pub in Kingsman: The Secret Service. The real pub is a local favourite in Kennington, near the Imperial War Museum.",
     },
    {"name": "Huntsman Savile Row", "lat": "51.5109", "lon": "-0.1400",
     "subcategory": "other-film", "neighborhood": "Mayfair",
     "summary": "The Kingsman tailor shop is inspired by the real Huntsman at 11 Savile Row. The famous street has been the home of bespoke tailoring since the 1730s.",
     },

    # ---- Mission Impossible ----
    {"name": "Tate Modern", "lat": "51.5076", "lon": "-0.0994",
     "subcategory": "other-film", "neighborhood": "Southwark",
     "summary": "Featured in Mission: Impossible - Fallout during a tense chase scene. The former Bankside Power Station is now one of the world's most visited modern art galleries. Free entry.",
     "kid_friendly": "true"},
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
    added = 0
    skipped = 0

    for site in MOVIE_SITES:
        site_id = slugify(site["name"])
        if site_id in existing_ids:
            skipped += 1
            continue

        row = {k: "" for k in FIELDNAMES}
        row["id"] = site_id
        row["name"] = site["name"]
        row["lat"] = site.get("lat", "")
        row["lon"] = site.get("lon", "")
        row["category"] = "movie-sites"
        row["subcategory"] = site["subcategory"]
        row["neighborhood"] = site.get("neighborhood", "")
        row["summary"] = site.get("summary", "")
        row["kid_friendly"] = site.get("kid_friendly", "")
        row["tags"] = "source:manual-movie-sites"
        rows.append(row)
        existing_ids.add(site_id)
        added += 1

    # Write back
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for row in rows:
            clean = {k: row.get(k, "") for k in FIELDNAMES}
            writer.writerow(clean)

    # Summary by subcategory
    subcats = {}
    for site in MOVIE_SITES:
        sub = site["subcategory"]
        subcats[sub] = subcats.get(sub, 0) + 1

    print(f"Added {added} movie sites, skipped {skipped} duplicates")
    print(f"Total rows: {len(rows)}")
    print("\nBy film universe:")
    for sub, count in sorted(subcats.items()):
        print(f"  {sub}: {count}")


if __name__ == "__main__":
    main()
