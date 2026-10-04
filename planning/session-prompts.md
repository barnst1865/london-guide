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
> Goal for launch: **at least 5 public places in each theme**, both theme intros, and the **WMD Tour trail** for its London stops (Salisbury and Aldermaston go in the trail text or later as day trips). Treat every claim in my WMD draft as unverified; §8 lists known errors. Apply §3 strictly: no house numbers for private homes; describe active government and military sites only from public sources; and keep the tone serious about victims. Interview me first, then propose, sort, research and write as in §10.3. Set `visibility: public` only on places I've approved that have `last_verified`. Finish by logging the session, updating both backlog rows, and listing the files you changed so I can run `npm run check`, then commit and push.

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
> 2. **Write a listing file**: `depth: listing`, the type and themes from the triage, `badge: favourite` only where the triage says favourite, sensible tags, a summary (≤160 chars) in our voice built on the family's angle in the triage notes, and optionally one or two sentences plus an **Our tip:** line if the notes have one. Fill in `sources` and `last_verified`. Follow §3 for location precision (private homes and film exteriors are street-level only) and §7 for legends.
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
