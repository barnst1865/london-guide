# Session 2: Historic Pubs & Restaurants (2026-10-04)

**Goal:** launch set for `historic-pubs`: 15–20 public places, theme intro, 3–4 featured places and the City of London pub crawl (idea #10).

## Sources used

- `sources/triage/handoff.md`, historic-pubs section (95 rows: 78 in London, 17 in parked day-trip towns).
- The restaurant and pub list in `sources/docs/` (added Cittie of Yorke and the Olde Wine Shades, which weren't in the triage). Rewritten from scratch, no source wording.
- The 5 seed drafts (Cheshire Cheese, Mitre, Prospect of Whitby, Grapes, Mayflower): updated in place, slugs unchanged.

## Decisions (with the family)

- **Launch set (18):** the 8 historic-pubs favourites plus 10 more. Punjab was dropped from this round and left to the `eat` session; Gordon's stays in (it also carries `drinks`).
- **Voice:** first-person only on favourites; the others recommend plainly.
- **Featured:** Ye Olde Cheshire Cheese, The George Inn, The French House, Jamaica Wine House.
- **Trail:** the full west-to-east route, Mitre to Jamaica Wine House.

## Added or changed

**Public (18, all `last_verified: 2026-10-04`):**
- Favourites (8): `ye-olde-cheshire-cheese`, `jamaica-wine-house`, `french-house`, `the-dove-hammersmith`, `spaniards-inn`, `hole-in-the-wall-waterloo`, `gordons-wine-bar`, `lore-of-the-land`
- Recommended (10): `ye-olde-mitre`, `cittie-of-yorke`, `seven-stars`, `the-black-friar`, `olde-wine-shades`, `old-bell-tavern`, `george-inn-southwark`, `prospect-of-whitby`, `the-grapes-limehouse`, `rules`

**Draft (3, researched, not in the launch set):** `mayflower-pub` (rewritten), `george-and-vulture` and `hoop-and-grapes-aldgate` (optional crawl stops, so they drop out of the published trail until public).

**Theme:** intro written; `featured` set. **Trail:** `content/trails/city-pub-crawl.md`, public and featured: 7 stops, 3 optional, 2 segments.

## How facts were checked

- Every place's age checked against the 75-year rule. All 21 clear it; dates come from Historic England list entries, CAMRA heritage inventories and pub-history sources, recorded in each file's `sources:`.
- Open status checked for every place (CAMRA, venue sites, 2025–26 news). All trading.
- Coordinates geocoded from each address with OpenStreetMap Nominatim (building-level matches, not postcode centroids).
- Venue claims stated as claims; unverifiable stories labelled as legend. Corrections made to the seed drafts: the Prospect's noose is modern and Execution Dock was upriver; the Mayflower's interior is from 1957 and its 1620 links are loose; the Grapes' McKellen purchase was 2011.
- "Desi pub" verified and logged in `requests.md` (not used in this theme's text).

## Things to know

- **Hole in the Wall** changed hands in December 2025 (a London brewery took over and plans a more modern feel). It's still a favourite in the file, but worth a revisit.
- **Lore of the Land** no longer pours Guy Ritchie's own beer (his brewery stopped in 2024), so the text doesn't mention it.
- **Weekday-only:** the Olde Wine Shades, the Jamaica Wine House and usually George and Vulture; the trail says so. The Mitre is closed on Sundays.
- The theme intro links the `pub-etiquette` guide, which Session 5 published while this session was running. That guide lists `mayflower-pub` in its `places`, and the Mayflower is still a draft, so it won't appear there until it's published.

## Open / next rounds

- About 60 London rows from the handoff are still to triage with the family. Likely next: the Lamb & Flag, the Harp, the Dog and Duck, the Ship Tavern, the Barley Mow, the Prince Alfred, the Holly Bush and the Flask; and the old restaurants shared with `eat` (Sweetings, J Sheekey, Simpson's in the Strand, Wiltons, Scott's).
- Essay `historic-pubs-and-restaurants` (idea #22): not started; now has public places to link.
- Thames Path trail (#24): the Dove exists now; other stops still needed.
- The 17 day-trip pubs stay parked.
- `npm run check` not run here (no shell on the linked computer): the family runs it before pushing.
