# Requests for the master session

Topic sessions: add schema, vocabulary (types/tags), site-code or theme-structure requests here instead of editing `src/`.

| Date | From session | Request | Status |
|---|---|---|---|
| 2026-10-02 | Google Maps triage | Broaden `historic-pubs` to cover historic restaurants; any pub or restaurant 75+ years old carries it | **Done 2026-10-03.** Title is now "Historic Pubs & Restaurants"; the id `historic-pubs` is unchanged. Rule in §5.1 |
| 2026-10-02 | Google Maps triage | Allow hard-to-verify claims if labelled as apocryphal | **Done.** §7 "Legends" and §8 |
| 2026-10-02 | Google Maps triage | A "UK oddities" page (e.g. explaining jellied eels) | **Covered.** Places go in the `only-in-london` theme; explanations go in the `britishisms` guide or a new Practical London guide |
| 2026-10-02 | Google Maps triage | Privacy: the triage CSV shouldn't be in the public repo | **Done.** Moved to `sources/triage/` (git-ignored); `planning/triage/` holds only a pointer |
| 2026-10-03 | Google Maps triage | New place type `quick-bite` for ice cream, bakeries and desserts | **Done.** Added to the types (§5.2) |
| 2026-10-03 | Google Maps triage | Selection criteria for restaurants, cafés and bars | **Done.** §7 "What earns a place" |
| 2026-10-03 | Google Maps triage | Verify the term "desi pub" before using it in text | Open, for the `eat` / `historic-pubs` sessions |
| 2026-10-03 | Google Maps triage (Session #1) | New "movies" theme for film locations; also unthemed literary/artistic places | **Done.** New themes `on-screen-on-record` (film, TV and music landmarks) and `writers-artists-makers`. One-offs such as Lock & Co. go to `only-in-london` |
| 2026-10-04 | Google Maps triage (Session #1) | **Badges: keep only `favourite`.** Family decision: no separate like, tip or wishlist; if a place is on the map, we're confident it's worth a visit. Needs: `badge` made optional with `favourite` as its only value (§5.4, §6.1, validation); §2.3 reworded; the `showWishlist` switch retired or repurposed; existing draft places re-badged; the launch-plan tip about re-badging after visits updated. Until this is done, `npm run check` still demands one of the four badges on every place | Open |
| 2026-10-04 | Google Maps triage (Session #1) | Honesty without badges: place text is first person, but some included places are ones we haven't visited yet. Decide how a page says so (a line in the text, a tag, or hold those places back until visited) | Open |
| 2026-10-04 | Google Maps triage (Session #1) | `markets-food-shops` now holds specialist non-food shops as well (antiques, maps, books, toys). Confirm the theme covers them, and retitle it if so | Open |
| 2026-10-04 | Google Maps triage (Session #1) | Whole streets saved as places: should a street or district be a place file (which type?) or an "Around town" area guide (§5.6)? | Open |
| 2026-10-04 | Google Maps triage (Session #1) | Places outside London: §4 makes `day-trip` a type, but a place has one type, so a historic pub in a day-trip town can't be both `pub` and `day-trip`. Suggest such places keep their own type and carry the `day-trips` theme | Open; needed when day trips resume |
| 2026-10-04 | Google Maps triage (Session #1) | Day trips (parked until after launch): decide whether a destination town is one place with its sights folded in, or one place per sight | Open; post-launch |
