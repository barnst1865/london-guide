# Kickoff prompts for the launch sessions

Start each one as a new Cowork session in the **London Guide** project, with the **LondonGuide** folder connected, and paste the prompt. Sessions 2–6 can run in parallel. After each one finishes: run `npm run check`, then commit and push.

## Shared opening (already included in each prompt below)

> We're working on Where We'd Take You in London. Read `CLAUDE.md`, `PROJECT_INSTRUCTIONS.md`, `planning/launch-plan.md`, `planning/backlog.md`, `planning/requests.md` and `planning/ideas.md` in the connected LondonGuide folder, and list `content/places/` before creating anything. If a place file already exists (another session may have written it), add your theme to it instead of duplicating it. Note: `sources/triage/handoff.md` was written before the badge change. `favourite` is now the only badge, it's optional, and the schema already allows it (§5.4).

---

## Session 2: Historic Pubs & Restaurants (+ City pub crawl trail)

> We're working on Where We'd Take You in London. Read `CLAUDE.md`, `PROJECT_INSTRUCTIONS.md`, `planning/launch-plan.md`, `planning/backlog.md`, `planning/requests.md` and `planning/ideas.md` in the connected LondonGuide folder, and list `content/places/` before creating anything. If a place file already exists (another session may have written it), add your theme to it instead of duplicating it. Note: `sources/triage/handoff.md` was written before the badge change. `favourite` is now the only badge, it's optional, and the schema already allows it (§5.4).
>
> This is **Session 2: the `historic-pubs` theme (Historic Pubs & Restaurants)**. Sources: the `historic-pubs` section of `sources/triage/handoff.md` (95 rows), the office pub list in `sources/docs/London Restaurants.docx`, and the 5 seed drafts already in `content/places/`. Ideas #10 (City pub crawl) and #22 (historic pubs essay) in `planning/ideas.md` belong to this theme.
>
> Goal for launch: **15–20 public places**, with favourites and the best stories first, plus the theme intro, 3–4 `featured` places, and a **City of London pub crawl trail**. Draft the rest in later rounds. Start by showing me the 95 grouped by area, with favourites marked, and help me pick the launch set. Then research (age claims, the 75-year rule, still open, address and coordinates geocoded from the address), write the place files in our voice (§7; label unverifiable stories as legend), and set `visibility: public` only on places I've approved that have `last_verified`. Also verify the term "desi pub" before using it (open request). Finish by logging the session in `planning/sessions/`, updating the backlog row, and listing the files you changed so I can run `npm run check`, then commit and push.

## Session 3: Spies & Cold War + Wartime London (+ WMD Tour)

> We're working on Where We'd Take You in London. Read `CLAUDE.md`, `PROJECT_INSTRUCTIONS.md`, `planning/launch-plan.md`, `planning/backlog.md`, `planning/requests.md` and `planning/ideas.md` in the connected LondonGuide folder, and list `content/places/` before creating anything. If a place file already exists (another session may have written it), add your theme to it instead of duplicating it. Note: `sources/triage/handoff.md` was written before the badge change. `favourite` is now the only badge, it's optional, and the schema already allows it (§5.4).
>
> This is **Session 3: the `spies-cold-war` and `wartime-london` themes, plus the WMD Tour trail**. Sources: my WMD tour draft (`sources/docs/UK WMD Tour - Fleshed OUt.docx`), the `spies-cold-war` and `wartime-london` sections of `sources/triage/handoff.md`, the 11 deferred spy sites (GM104–GM115) in `sources/triage/google-maps-triage.csv` (I'll tell you what I decided after checking my book), the 6 seed drafts in `content/places/`, and idea #9 (Blitz scars walk).
>
> Goal for launch: **at least 5 public places in each theme**, both theme intros, and the **WMD Tour trail** for its London stops (Salisbury and Aldermaston go in the trail text or later as day trips). Treat every claim in my WMD draft as unverified; §8 lists known errors. Apply §3 strictly: house numbers only where the family has chosen to identify the building; describe active government and military sites only from public sources; and keep the tone serious about victims. Interview me first, then propose, sort, research and write as in §10.3. Set `visibility: public` only on places I've approved that have `last_verified`. Finish by logging the session, updating both backlog rows, and listing the files you changed so I can run `npm run check`, then commit and push.

## Session 4: Where We Eat (finish)

> We're working on Where We'd Take You in London. Read `CLAUDE.md`, `PROJECT_INSTRUCTIONS.md`, `planning/launch-plan.md`, `planning/backlog.md`, `planning/requests.md` and `planning/ideas.md` in the connected LondonGuide folder, and list `content/places/` before creating anything. If a place file already exists (another session may have written it), add your theme to it instead of duplicating it. Note: `sources/triage/handoff.md` was written before the badge change. `favourite` is now the only badge, it's optional, and the schema already allows it (§5.4).
>
> This is **Session 4: the `eat` theme (Where We Eat)**. Sources: the `eat` section of `sources/triage/handoff.md`, the office restaurant list in `sources/docs/London Restaurants.docx`, our Google reviews (already in the triage), the 16 restaurant research drafts in `content/places/` (see `planning/research/value-restaurants.md` and `criteria.md`), and the selection rules in §7 ("What earns a place"). Use the `quick-bite` type for ice cream, bakeries and desserts.
>
> Goal for launch: **15–20 public places** across cuisines, budgets and parts of town, plus the theme intro and 3–4 `featured`. Start by asking which of the 16 research drafts we or trusted friends have now tried. Publish those in our voice, and leave the rest as drafts (§2.3, §5.4). Then go through the handoff's eat list with me. Verify each place is still open, check its address, and geocode it. Verify the term "desi pub" before using it. Finish by logging the session, updating the backlog row, and listing the files you changed so I can run `npm run check`, then commit and push.

## Session 5: Practical London guides

> We're working on Where We'd Take You in London. Read `CLAUDE.md`, `PROJECT_INSTRUCTIONS.md` (especially §5.6, §6.5, §6.6, §7), `planning/launch-plan.md`, `planning/backlog.md` and `planning/ideas.md` (#17) in the connected LondonGuide folder.
>
> This is **Session 5: write the four Practical London guides**: `content/guides/getting-around.md`, `pub-etiquette.md`, `eating-out.md` and `britishisms.md` (their outlines are already there). Interview me for our own experience and tips first; that's the value. Then write each guide in our voice for American visitors. Link to official sources (TfL, etc.) for fares, rules and anything that changes, rather than restating it. Link to places with `[name](place:slug)` only if the place file exists. Include a short explanation of jellied eels and other oddities in the glossary. Set `visibility: public` and `last_verified` only on guides I approve. Finish by logging the session, updating the Guides backlog row, and listing the files you changed so I can run `npm run check`, then commit and push.

## Session 6: Fifth launch theme

> We're working on Where We'd Take You in London. Read `CLAUDE.md`, `PROJECT_INSTRUCTIONS.md`, `planning/launch-plan.md`, `planning/backlog.md`, `planning/requests.md` and `planning/ideas.md` in the connected LondonGuide folder, and list `content/places/` before creating anything. If a place file already exists (another session may have written it), add your theme to it instead of duplicating it. Note: `sources/triage/handoff.md` was written before the badge change. `favourite` is now the only badge, it's optional, and the schema already allows it (§5.4).
>
> This is **Session 6: the fifth launch theme, [`kids` (With Kids) OR `wild-london` (Parks, Walks & Wild London, plus the Thames Path trail from idea #24)]**. Sources: that theme's section of `sources/triage/handoff.md`, plus [for wild-london: idea #24's route and stops]. Goal for launch: **at least 5–8 public places**, the theme intro, 3–4 `featured`, [and for wild-london: the Thames Path trail, using segments, optional stops, waypoints for bridge crossings, and short and long variants (§6.3)]. Interview me first, then propose, sort, research and write as in §10.3. Set `visibility: public` only on places I've approved that have `last_verified`. Finish by logging the session, updating the backlog row, and listing the files you changed so I can run `npm run check`, then commit and push.

---

# Quick-listing sessions (after launch)

These put the ~140 remaining London places from the Google Maps triage on the site as **quick listings** (`depth: listing`, §6.1): verified facts and a one-line summary, with full write-ups later as each theme is built out. Three sessions, which can run in parallel. Day-trip rows, the deferred spy rows and whole streets (e.g. Brick Lane, which becomes an area guide) are out of scope.

## Shared prompt (fill in the [brackets])

> We're working on Where We'd Take You in London. Read `CLAUDE.md`, `PROJECT_INSTRUCTIONS.md` (especially §3, §6.1 "Quick listings", §7, §8), `planning/backlog.md` and `planning/requests.md` in the connected LondonGuide folder, and list `content/places/`.
>
> This is a **quick-listing session for [THEMES]**. Source: `sources/triage/google-maps-triage.csv`, rows where `decision` is `include`, `scope` is `london`, and the first theme in `proposed_themes` is one of [THEMES]. Skip any row that already has a place file (check by name; some names differ, e.g. "The Red Lion, Mayfair" is `red-lion-duke-of-york-street`). Skip whole streets or districts (§5.6).
>
> For each place:
> 1. **Verify** that it's still open and at that address (recent reviews, its website, press), then find the nearest station and the official website. Geocode the coordinates from the address; don't use the triage's approximate coords.
> 2. **Write a listing file**: `depth: listing`, the type and themes from the triage, `badge: favourite` only where the triage says favourite, sensible tags, a summary (≤160 chars) in our voice built on the family's angle in the triage notes, and optionally one or two sentences plus an **Our tip:** line if the notes have one. Fill in `sources` and `last_verified`. Follow §3 for location precision (private homes are street-level only, and no house numbers unless the family has chosen them) and §7 for legends.
> 3. Set `visibility: public` once facts are verified. If a place has closed or moved, or you can't verify it, leave it as a draft and say why in a comment.
>
> Work in **batches of about 15**. Before writing each batch, show me a short table (name, type, area, open status, one-line summary) so I can drop or correct anything. After writing, record each new slug in a `place_file` column of the triage CSV.
>
> Finish by logging the session in `planning/sessions/`, updating the backlog rows for these themes, and listing the files you changed so I can run `npm run check`, then commit and push.

## The three sessions

| Session | [THEMES] | About how many |
|---|---|---|
| Listings A | `historic-pubs`, `drinks` | ~48 |
| Listings B | `eat`, `markets-food-shops` | ~49 |
| Listings C | `on-screen-on-record`, `kids`, `science-curious`, `transit-hidden-city`, `writers-artists-makers`, `only-in-london`, `play-games-music`, `medieval-old-london`, `wild-london` | ~36 |


---

# Post-review sessions (2026-10-04)

An outside review of the live site led to a batch of site fixes by the master session (see `planning/sessions/2026-10-04-master-review-fixes.md`) and these sessions. They can run in parallel: the pin check touches coordinates and trail waypoints, and the occasions session touches `occasions:` only.

## Pin check

> We're working on Where We'd Take You in London. Read `CLAUDE.md`, `PROJECT_INSTRUCTIONS.md` (especially §3, §5.3a "How the map draws a trail", §6.1, §6.3 and §8), `planning/backlog.md` and `planning/requests.md` in the connected LondonGuide folder.
>
> This is the **pin check**. Many public places are marked `location_precision: exact` but are pinned to a postcode centroid, so the pin can sit a street or more from the door. Directions now search Google Maps by name and address, so the job is to make the **map pins** honest.
>
> **Scope, in this order:**
> 1. Public places marked `exact` whose comments mention a postcode centroid, an approximate pin or a pin to check (about 66; list them first with a script).
> 2. Other public restaurants, cafés, quick bites, pubs, bars and shops marked `exact`.
> 3. Large or awkward sites: parks and gardens (pin the entrance most visitors use, such as a named gate), canal-side places (pin the towpath access) and big museums (pin the main visitor entrance).
>
> **Method:** take coordinates only from a source that shows the actual building or entrance: the OpenStreetMap object for the venue or its entrance, a Historic England listing for listed buildings, or the venue's own map or contact page. If this session can't reach map services, use the built-in browser on my computer to look at openstreetmap.org, or give me a batch list and I'll drop pins in Google Maps and paste the coordinates back. Never guess or nudge coordinates by eye.
>
> **For each place:**
> - **Confirmed:** update `coords` (5 decimals), keep `exact`, replace the centroid comment with `<!-- Pin checked YYYY-MM-DD: source -->`, and make sure `address` is complete with a postcode.
> - **Can't confirm:** set `location_precision: street` and say why in a comment. Directions still work from the address.
> - **Large sites:** if the right entrance isn't obvious, name it in the **Our tip:** line.
>
> **Trails:** preview each of the four trail maps in `npm run dev`. Where the straight line cuts across the river or through blocks in a way that misleads, add `path_only` waypoints (§6.3) with coordinates checked on OpenStreetMap. On the Thames Path, look at Dukes Meadows, the Mortlake towpath, Chiswick Bridge to the National Archives, and the National Archives to Kew Bridge branch.
>
> Work in **batches of about 20**. Before writing each batch, show me a table: place, the problem, the new coordinates, the source, and how far the pin moved. Don't change descriptions except to fix a wrong fact you notice (flag it). Don't edit `src/`; put any code requests in `planning/requests.md`. Finish by logging the session, adding a "Pin check" row to the backlog, and listing the files you changed so I can run `npm run check`, then commit and push.

## Eating by occasion

> We're working on Where We'd Take You in London. Read `CLAUDE.md`, `PROJECT_INSTRUCTIONS.md` (especially §2.7 browse-first, §6.1 `occasions`, §7 and §8), `planning/backlog.md`, `planning/requests.md` and `content/themes/eat.md` in the connected LondonGuide folder.
>
> This is the **eating-by-occasion session**. Theme pages now show a "Pick by occasion" section built from each place's `occasions` field. The allowed values are `breakfast-brunch`, `quick-lunch`, `cheap-cheerful`, `dinner-with-friends`, `sunday-roast`, `afternoon-tea` and `special-occasion`. Nothing is tagged yet.
>
> **Scope:** public places in `eat` and `drinks`, plus any pub in `historic-pubs` that serves food we'd send people for (a Sunday roast especially).
>
> **Steps:**
> 1. **Interview me first.** For each occasion, ask which places we'd actually send people to. That's the value.
> 2. **Propose a table:** place, area, suggested occasions, and the fact behind each. Only tag what's true now: `sunday-roast` only if the current menu shows one, `afternoon-tea` only if it's served, `breakfast-brunch` only if it opens for it, `special-occasion` for places worth dressing up and booking for. Most places get one or two occasions, three at most. Aim for about 4–10 places per occasion, spread across areas and prices.
> 3. **Write** the `occasions:` field into the files I approve. Don't change anything else, except optionally one sentence in the `eat` intro pointing to "Pick by occasion".
>
> If an occasion we need is missing from the list, ask for it in `planning/requests.md` rather than editing `src/`. Finish by logging the session, updating the `eat` and `drinks` backlog rows, and listing the files you changed so I can run `npm run check`, then commit and push.

## Home-page favourites (short; can be done in any session or by hand)

> We're working on Where We'd Take You in London. Read `CLAUDE.md` and §6.7 of `PROJECT_INSTRUCTIONS.md`. Help me pick about six places for `homeFavourites` in `content/site.yaml`, from the places with `badge: favourite`. Aim for a spread of areas and kinds of place, and for each one ask me for, or help me word, one line in our voice on why it's ours. Write the list into `site.yaml`, then list the files you changed so I can run `npm run check`, then commit and push.
