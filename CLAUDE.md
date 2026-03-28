# London Guide

Family London travel guide website deployed to londonguide.dckoiks.com via GitHub Pages.

## Architecture
- Static site: HTML/CSS/JS in `docs/` (GitHub Pages root)
- Data: `data/sites.csv` → `data/sites.geojson` → `docs/data/sites.geojson`
- Python scripts in `scripts/` for data import and processing
- Leaflet.js interactive map with category-based filtering

## Content Categories
restaurants, attractions, neighborhoods, day-trips, wmd-sites, movie-sites, kid-friendly, historic-sites

## Key Commands
- `python scripts/csv_to_geojson.py` — regenerate GeoJSON from CSV
- `python scripts/geocode.py` — fill missing lat/lon coordinates

## Style
London-themed: navy (#1B2A4A), red (#C8102E), cream (#F7F5F0)
Fonts: DM Serif Display (headings) + Inter (body)
