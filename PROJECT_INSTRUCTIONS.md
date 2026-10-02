# Where We'd Take You in London — Project Instructions

**Version:** 0.3 · **Last updated:** 2026-10-01 · **Owner:** master planning session

This is the single source of truth for the project. **Every Claude session working on the guide reads this file first.** If something here is wrong or missing, raise it with the master session rather than working around it.

---

## 1. What we're building

A personal, opinionated guide to London for friends and family who visit us. It steers people **past the obvious tourist circuit** toward the places we love: historic sites, odd museums, pubs, restaurants, bars, entertainment, and the hidden corners that match our interests.

It is:

- **A website** built from a git repository and published on the web (GitHub Pages).
- **Organized by theme and by type**, so a visitor can follow their own interests ("I like spy stuff", "where should we eat tonight?").
- **Map-first.** Every place is on an interactive map that works well on a phone in the street.
- **Modular.** Places, themes and trails are separate small files, so new material can be added at any time without touching the site code.

Audience: adults and families (including kids and teens) visiting from the US, mostly first- or second-time London visitors. They have already heard of the British Museum and the Tower, and they're looking to us for what they wouldn't find on their own.

---

## 2. Guiding principles

1. **Our voice, our opinions.** Write as "we": personal, warm, and a bit wry. Say *why we love it*, not just what it is. A short anecdote beats a Wikipedia summary.
2. **Beyond the obvious.** Big-name sites are included only when we have a specific angle on them, such as the best entrance, the room most people miss, or what to pair it with. Default to the less-known.
3. **Honest about what we've done.** Every place carries a badge saying whether we've been and how much we liked it (§5.4).
4. **Accurate.** Historical claims are fact-checked against reliable sources before publishing (§8).
5. **Useful on the ground.** Give the nearest station, whether to book, whether it's good for kids, and what's nearby to pair it with.
6. **Durable.** Avoid details that go stale fast, such as exact opening hours, prices and named staff. Link to the venue's site instead.

---

## 3. Privacy and safety rules (hard rules — apply to everything committed to the repo)

The site is public, so these rules apply to every file in the repository, not just the visible pages.

- **No identifying family details.** No surnames, no first names of the kids, no photos showing our faces or the kids' faces, and no mention of our employers, jobs, posting or work locations. "Our family" / "we" is the voice.
- **No home location.** Nothing that reveals where we live: no "our local", no "around the corner from us", no neighbourhood-of-residence hints, and no kids' schools or clubs. A place can be a favourite without saying why it's convenient for us.
- **No work-derived framing.** Anything from work-sourced lists (e.g., the office restaurant list) is rewritten from scratch for visitors. References to official functions, specific government buildings' staff habits ("full of X folks"), or colleagues' preferences are removed.
- **No private residences pinned.** Where history happened at a private home (e.g., Litvinenko's house, Skripal's former house, Amesbury), use `location_precision: area` or `street`, describe the site in text, and never give a house number. Prefer a nearby public landmark as the map pin.
- **Active government and military sites** (e.g., Thames House, Vauxhall Cross, RAF Northolt, AWE Aldermaston) are included only as things visible from public places, described from public sources. No advice on photographing them, approaching their perimeters, or anything about their security.
- **Respect for victims.** The spy and WMD material involves real people who died or were injured, including bystanders (e.g., Dawn Sturgess). The tone there is curious and serious, never jokey.
- **Robots.** The site ships with `noindex` meta tags and a `robots.txt` that disallows crawling. The link is shared directly with friends and family.
- **Private material stays private.** Raw source files (Google Takeout, office lists, notes) live in `sources/`, which is **git-ignored** and never published.

---

## 4. Scope

- **Core:** Greater London.
- **Day Trips:** places roughly ≤2 hours by train from central London, done as a return trip (e.g., Salisbury, Bletchley Park, IWM Duxford, Windsor, Dover, Canterbury, Oxford, Cambridge, Portsmouth). Day trips are a *type* (`day-trip`) and can also carry themes (e.g., Salisbury → Spies & Cold War).
- **Out of scope:** longer UK weekends (Cotswolds, Dorset, Scotland, and so on). This could become a separate section later.

---

## 5. How content is organized

There are four ways to cut the content. A place has **one type**, **one or more themes**, **one badge**, and **any number of tags**.

### 5.1 Themes (curated, cross-cutting, "what are you into?")

Themes are the heart of the guide. Each has its own page with an intro written in our voice, a mini-map, and its places. A place can appear in several themes.

**Draft theme list.** The seed ideas are prompts for the theme sessions, not commitments. All must be verified.

| id | Theme | Seed ideas (to discuss and verify) |
|---|---|---|
| `spies-cold-war` | **Spies, Secrets & the Cold War**, including the WMD tour | Churchill War Rooms (angle), Litvinenko and Markov sites, Brompton Oratory dead drop, Kelvedon Hatch bunker (day trip), Bletchley Park (day trip), Salisbury (day trip), BT Tower |
| `wartime-london` | **Wartime London**: WWII and military history | V1/V2 strike sites, Battle of Britain Bunker (Uxbridge), Bentley Priory, RAF Museum Hendon, HMS Belfast, National Army Museum, Guards Museum, Blitz damage on buildings, IWM Duxford (day trip) |
| `medieval-old-london` | **Medieval & Old London** | Temple Church, St Bartholomew the Great, Southwark Cathedral, London Wall remnants, Guildhall Roman amphitheatre, Charterhouse, Eltham Palace, Westminster Abbey Chapter House |
| `transit-hidden-city` | **Transit & the Hidden City** (engineering, infrastructure, under the streets) | Hidden London tours, LT Museum Acton Depot open days, Brunel Museum, Postal Museum & Mail Rail, Crossness Pumping Station, Elizabeth line architecture, Thames Clipper, Kew Bridge Steam Museum |
| `science-curious` | **Science, Medicine & the Curious** (including geology) | Hunterian Museum, Old Operating Theatre, Grant Museum of Zoology, Wellcome Collection, Sir John Soane's Museum, Horniman, Royal Observatory, NHM geology galleries, Broad Street pump |
| `historic-pubs` | **Pubs with History** | Ye Olde Cheshire Cheese, Ye Olde Mitre, Cittie of Yorke, Olde Wine Shades, Mayflower, Prospect of Whitby, The Grapes, The Harp, French House, Seven Stars |
| `eat` | **Where We Eat** (by occasion and cuisine) | Dishoom, Punjab, Barbary, Sichuan spots, Indian (Cinnamon Club, Quilon, Kutir), Rules (angle), Brasserie Zédel, Dumplings' Legend |
| `drinks` | **Bars, Cocktails & Wine** | Gordon's Wine Bar, Duke's, Connaught Bar, Mr Fogg's, Radio Rooftop |
| `markets-food-shops` | **Markets & Food Shopping** | Borough, Maltby Street, Columbia Road, Neal's Yard Dairy, Gelateria La Romana |
| `sport` | **Sport**: watch it, tour it, run it | Lord's (incl. Eton v Harrow), The Oval, football from Premier League to non-league groundhopping (from our Football Teams map), Wimbledon, Twickenham, Marathon viewing spots |
| `play-games-music` | **Play, Games & Live Music** | Arcade Battersea, board-game cafés, retro arcades, Flight Club, live-music venues in the rock and Americana tradition |
| `wild-london` | **Parks, Walks & Wild London** (including foraging, canals and the Thames) | Hampstead Heath, Richmond Park, Regent's Canal walk, Walthamstow Wetlands, Crystal Palace dinosaurs, Thames foreshore (note PLA permit rules) |
| `kids` | **With Kids** (and teens) | Horniman, Science Museum Wonderlab, Mudchute Farm, Diana Memorial Playground, Cutty Sark, Crystal Palace dinosaurs |
| `day-trips` | **Day Trips** | See §4 |

Theme files live in `content/themes/<id>.md` (§6.2).

**Themes are a living list.** Adding a theme or reworking an existing one is expected, not exceptional:

- **New theme:** any session may create `content/themes/<new-id>.md` with `visibility: draft` and add a row to `planning/backlog.md`. The master session reviews it for overlap with existing themes, assigns menu `order`, and publishes it.
- **Updating a theme:** any session may revise a theme's intro, featured list or places. Renaming a theme's *title* is fine; changing its *id* is a master-session job, because place files reference it.
- **Merging or retiring a theme:** master session only. Retired themes keep their file with `visibility: draft` so nothing breaks.

### 5.2 Types (one per place, "what kind of place is it?")

Types drive map marker icons and the "Browse by type" menus.

`historic-site` · `museum` · `church` · `pub` · `bar` · `restaurant` · `cafe` · `market-shop` · `park-walk` · `entertainment` · `sport-venue` · `viewpoint` · `tour` · `day-trip`

### 5.3 Trails (ordered routes)

A trail is an ordered sequence of places with walking or transport notes between them, drawn as a route on the map. Examples: the **WMD Tour**, a **City of London historic pub crawl**, and a **Cold War walk around Whitehall**. Trails reference places by slug and don't duplicate place content.

### 5.4 Badges (exactly one per place)

| badge | Label shown | Meaning |
|---|---|---|
| `favourite` | ★ Family favourite | We've been more than once and actively send people there |
| `like` | We like it | We've been and would recommend it |
| `tip` | Trusted tip | We haven't been, but someone we trust recommends it |
| `wishlist` | On our list | We want to go. **Hidden for now.** Controlled by one switch, `showWishlist`, in `content/site.yaml`; flipping it to `true` shows these places site-wide with no other changes |

### 5.5 Tags (controlled vocabulary; add new ones via the master session)

`kid-friendly` · `teen-appeal` · `dog-friendly` · `free` · `booking-essential` · `rainy-day` · `outdoors` · `step-free` · `late-night` · `seasonal` · `quick-visit` (<1 hr) · `half-day` · `group-friendly` · `sunday` (good on a Sunday)

Price uses `price: 1–4` (£ to ££££) for food and drink, and `£0` / `£` / `££` / `£££` for attractions. Use the scale only, never actual prices.

---

## 6. Data model

All content lives in plain Markdown files with YAML front matter. **One place = one file.** This keeps sessions from colliding and makes additions trivial.

### 6.1 Place file — `content/places/<slug>.md`

Slug: lowercase, hyphenated, unique, stable (e.g., `ye-olde-cheshire-cheese`). Never rename a slug once published, because trails and links depend on it.

```yaml
---
name: Ye Olde Cheshire Cheese
type: pub
themes: [historic-pubs, medieval-old-london]
badge: favourite
tags: [rainy-day, group-friendly]
price: 1
summary: >-                     # ≤160 chars; shown on cards and map popups
  A warren of dark, firelit rooms rebuilt right after the Great Fire — the pub we take everyone to first.
area: Fleet Street / City        # neighbourhood label for visitors
address: 145 Fleet Street, London EC4A 2BU
coords: [51.5144, -0.1074]      # [lat, lng], WGS84, 4–5 decimals
location_precision: exact       # exact | street | area  (see §3)
stations: [Chancery Lane, City Thameslink, Blackfriars]
website: https://...
google_maps_url: https://maps.google.com/?cid=...
pair_with: [ye-olde-mitre, temple-church]   # slugs of nearby places worth combining
status: open                    # open | seasonal | closed | temporarily-closed
visibility: draft               # draft | public  — only `public` builds
last_verified: 2026-10-01       # date facts and open status were last checked (required once public)
sources:                        # where historical claims came from (not displayed by default)
  - https://...
---

Body: 80–200 words in our voice (see §7).

**Our tip:** one practical line (e.g., "Sam Smith's pub: no phones at the bar, cash-light prices, go downstairs").
```

**Required:** `name`, `type`, `themes` (≥1), `badge`, `summary`, `area`, `coords`, `location_precision`, `status`, `visibility`. `last_verified` is required before a place can be `public`; the build refuses public places without it.
**Optional:** everything else.

### 6.2 Theme file — `content/themes/<id>.md`

```yaml
---
title: Spies, Secrets & the Cold War
short: Spies & Cold War          # for menus
order: 1                         # menu order
icon: binoculars                 # icon name from the site's icon set
color: "#5b6b8c"                 # theme accent (site may override for accessibility)
featured: [churchill-war-rooms, brompton-oratory]   # 3–6 slugs shown first
blurb: One line (≤140 chars) shown on the home-page tile
visibility: public               # draft | public
---
Intro essay, 150–300 words, in our voice: why we love this theme, and how to approach it in a visit.
```

### 6.3 Trail file — `content/trails/<id>.md`

```yaml
---
title: The WMD Tour
themes: [spies-cold-war]
mode: mixed                      # walk | transit | mixed
duration: Full day
stops:
  - place: broad-street-pump
    note: Start in Soho...
  - place: millennium-hotel-mayfair
    note: 15-minute walk west...
visibility: draft
---
Introduction to the trail.
```

### 6.4 Validation

The site build validates every file against this schema and **fails loudly** on errors: missing required fields, unknown theme, type, tag or badge, malformed coordinates, a trail pointing to a non-existent slug, or a duplicate slug. Running `npm run check` before finishing any session is mandatory.

**Previewing drafts:** `npm run dev` shows draft places, themes and trails (with a yellow banner) so they can be reviewed locally; the published build never includes them. On the published home page, themes appear only once they have at least one public place.

---

## 7. Writing style guide

- **Voice:** first-person plural ("we", "our kids love…" is fine; names are not). Conversational, specific, and a little dry. Think of a well-travelled friend writing you a note, not a guidebook.
- **Lead with the hook:** the first sentence says why this place is worth your time. History comes second, practicalities last.
- **Summary (≤160 chars):** a single vivid sentence that works on its own in a map popup.
- **Body (80–200 words):** what it is, why we love it, what to look for, and who it suits.
- **"Our tip:"** one practical line, such as when to go, what to order, which entrance to use, or what to book.
- **Spelling:** American spelling for our prose (the audience is American). Keep British proper names as they are ("Theatre", "Centre"). Explain Britishisms on first use or link to the site glossary.
- **Avoid:** exact hours, exact prices, superlatives we can't stand behind ("best in London" only if we mean it and say it's our opinion), "hidden gem", "nestled", "boasts", and clichés generally.
- **Sensitive history:** factual and respectful (see §3). It's fine to be fascinated, but never flippant about victims.
- **Kids:** say honestly what works for which ages ("teens will love it; under-8s will be bored after 20 minutes").

---

## 8. Fact-checking and freshness

- **Every factual claim** (dates, "oldest", "only", who did what where) is checked against at least one reliable source: the venue's own site, Historic England, the museum, reputable press, or official inquiry reports (e.g., the Litvinenko and Dawn Sturgess inquiries). Record the URLs in `sources:`.
- **Known issues in the existing WMD draft to correct:** PINDAR's construction date (1980s, operational about 1992), the Broad Street pump framing (epidemiology, not "biological warfare research"), RAF Northolt's "nuclear bomber" role (likely wrong), BT Tower's "built to withstand nuclear attack" claim (check), Markov's hospital (St James' Balham, which has since closed and is not the same as St George's), and the "Ryu Sushi" reference (verify the venue name). Treat every claim in that draft as unverified.
- **Open/closed status:** restaurants and bars change constantly. Before a place goes `public`, confirm it's still trading and at that address. Several entries on the office list may have moved or closed.
- **Coordinates:** take them from the venue's own location or a Google Maps or OpenStreetMap lookup, then spot-check on the map. For `street` or `area` precision, place the pin on a public landmark.
- **Freshness:** `last_verified` is updated whenever a place is checked. A script (`npm run stale`) lists places not verified in 12+ months, for an annual sweep or a check before a known visit.

---

## 9. Website architecture

### 9.1 Stack (proposed)

| Concern | Choice | Why |
|---|---|---|
| Site generator | **Astro** (static output) | Content collections give schema validation on our Markdown files; fast static pages; easy to run on Windows |
| Map | **Leaflet** + OpenStreetMap or CARTO tiles + marker clustering | Free, no API key, works well on mobile |
| Search | **Pagefind** (phase 4) | Static, client-side search with no server |
| Hosting | **GitHub Pages** via a GitHub Actions workflow on push to `main` | Free; the build runs validation automatically |
| Styling | Hand-written CSS with a small design system (light/dark, mobile-first) | No framework lock-in |

The alternative we rejected is Jekyll (native to GitHub Pages, but it has no schema validation and needs Ruby on Windows). We can revisit this if needed.

### 9.2 Repository layout

```
london-guide/
├── PROJECT_INSTRUCTIONS.md      ← this file
├── CLAUDE.md                    ← short pointer to this file for Claude Code sessions
├── README.md                    ← how to run, build and add a place (for humans)
├── content/
│   ├── places/<slug>.md
│   ├── themes/<id>.md
│   ├── trails/<id>.md
│   ├── site.yaml                ← site-wide settings (title, showWishlist, …)
│   └── practical.md             ← the Practical London page
├── src/                         ← Astro site code (master session only)
├── public/                      ← static assets: icons, our own photos, robots.txt
├── .github/workflows/deploy.yml ← builds and publishes on push to main
├── planning/
│   ├── backlog.md               ← status of every theme and workstream
│   ├── sessions/YYYY-MM-DD-<topic>.md   ← one log per working session
│   └── requests.md              ← schema or site change requests from theme sessions
├── tools/                       ← import, geocode, validate and stale scripts
└── sources/                     ← GIT-IGNORED raw inputs (Takeout, office list, old drafts)
```

### 9.3 Pages (MVP)

- **Home:** a short welcome in our voice, theme tiles, "If you only have one day / a weekend" picks, and a map teaser.
- **Map:** full-screen map with markers styled by type; filters for theme, type, badge and key tags (kid-friendly, free, rainy-day); clustering; popups linking to place pages; a "Directions" button that opens Google or Apple Maps.
- **Theme pages:** intro essay, featured places, all places, and a mini-map.
- **Browse by type:** Eat, Drink, Museums, Historic sites, and so on.
- **Place pages:** description, our tip, practical box, mini-map, "pair with", and the themes it belongs to.
- **Trail pages:** ordered stops, route on the map, and leg notes.
- **Practical London:** getting around (contactless, Citymapper), booking culture, tipping, Sundays, a pub etiquette primer, and a glossary of Britishisms.

**Later:** "Near me" (geolocation), search, a printable or offline trail view, photos.

### 9.4 Images

Version 1 has no photos, which keeps it simple and safe. If added later, use **only our own photos (no people's faces)** or openly licensed images (e.g., Wikimedia Commons) with attribution. Never hotlink or scrape venue images.

---

## 10. How we work: master session and topic sessions

### 10.1 Roles

**Master session** (the Cowork "London Guide" planning session):

- Owns this file, the schema, the theme, type and tag lists, the site code (`src/`), `planning/backlog.md`, and deploys.
- Reviews output from topic sessions for consistency, duplicates, privacy and style.
- Processes `planning/requests.md`.

**Topic sessions** (one per theme, or per workstream such as "Google Maps triage"):

- Start a new Cowork session **in the same claude.ai Project, with the same folder connected**.
- Work only in `content/` and `planning/sessions/`. **Do not edit `src/`, the schema, or this file.** Propose changes in `planning/requests.md`.
- May add their theme to an existing place's `themes:` list instead of creating a duplicate place. That's encouraged.
- May create a new draft theme or update an existing theme's file (see §5.1).

### 10.2 Topic-session kickoff prompt (copy and paste)

> We're working on the London Guide. Read `PROJECT_INSTRUCTIONS.md` and `planning/backlog.md` in the connected London-Guide folder, then the theme file for **[THEME ID]** and the list of existing places. This session's job is to build out the **[THEME NAME]** theme. Start by interviewing me about what we love in this theme, then propose candidates (including less-obvious ones), and we'll triage together before you research and write anything.

### 10.3 Topic-session workflow

1. **Orient.** Read this file, the backlog, the theme file, and the existing places (by name, type and themes) to avoid duplicates.
2. **Interview.** Ask what we've done, what we loved, stories worth telling, and which places from the source material belong here.
3. **Propose.** Suggest a candidate list mixing our known places and beyond-the-obvious ideas, each with a one-line pitch.
4. **Triage with the user.** For each candidate, decide include / wishlist / skip, plus a badge and a type.
5. **Research and verify.** Check facts, open status, address, coordinates and station (§8).
6. **Draft.** Write place files with `visibility: draft`, plus the theme intro and an optional trail.
7. **Review.** The user reads the drafts, edits voice and adds anecdotes, then the place is flipped to `public`.
8. **Check.** Run `npm run check` (once available) and fix any errors.
9. **Log.** Write `planning/sessions/YYYY-MM-DD-<theme>.md` (what was added, what's pending, open questions) and update the theme's row in `planning/backlog.md`.

### 10.4 Git

- One commit per session, with a clear message (e.g., `content: historic-pubs — 12 places, City pub crawl trail`).
- Sessions commit locally when they can; **the user pushes** (GitHub Desktop or VS Code). Pushing to `main` publishes the site, so the push is the review gate. Draft-visibility content never builds, so pushing drafts is safe.
- If a session's computer link has no shell, it writes files only and the user commits and pushes.

---

## 11. Source material and how to process it

| Source | Status | Handling |
|---|---|---|
| `UK WMD Tour - Fleshed OUt.docx` | Draft WMD tour (nuclear, radiological, chemical, biological, missiles, activism) | Goes to the `spies-cold-war` and `wartime-london` themes plus a **WMD Tour** trail. Full fact-check and privacy pass (§3, §8). |
| `London Restaurants.docx` | Office list: restaurants, pubs and bars around Whitehall, Covent Garden, Mayfair and the City | Goes to the `eat`, `historic-pubs` and `drinks` themes. Places we've been get `favourite` or `like`; the rest get `tip`. Descriptions are rewritten from scratch with no work framing. Verify that each place is still open. |
| `UK Tour Guide - 8 June 2025.pdf` | OneNote export of the two documents above | Reference only (duplicate). |
| Google Takeout: `Saved Places.json` | 26 starred places, mostly US and Europe | London-relevant ones only (very few). |
| Google Takeout: `Reviews.json` | 10 reviews; London 5-star reviews include Oliver's Village Café, Punjab, Mon Plaisir, Gelateria La Romana, Dishoom Battersea, Arcade Battersea | Strong `favourite` or `like` candidates. |
| Google Takeout: `London Football Teams.kmz` | Map of London clubs, tiers 1–7 | Goes to the `sport` theme (possibly a "groundhopping" trail). |
| **Google Takeout: Saved lists (MISSING)** | Not in the current export. The main list is the shared list **"UK 2023"** (co-owned). Its share link can't be read automatically, because Google blocks automated fetching. | **Re-export** (see below). This is the main "hodgepodge" to triage. If "UK 2023" doesn't appear in your export, the list's owner exports it from their own account. |

**Re-exporting the Google Maps saved lists:** go to takeout.google.com, choose "Deselect all", then tick **Saved** (this holds your lists: Favourites, Want to go, Starred, and custom lists). Optionally also tick "Maps (your places)" again. Export, and put the zip in `sources/google-maps/`. Each list arrives as a CSV of names, notes and Google Maps URLs, without coordinates, so a triage session will resolve locations.

**Google Maps triage workstream** (its own topic session): extract London and day-trip entries into `planning/triage/google-maps-triage.csv` with columns name / list / url / proposed type / proposed theme(s) / proposed badge / decision / notes. Work through it with the user in batches of 25–40, then hand accepted places to the relevant theme sessions (or write them directly if the theme is already in progress).

---

## 12. Roadmap

| Phase | What | Where |
|---|---|---|
| **0. Foundations** | Agree these instructions; decide the open items in §13; create the repo; re-export Google saved lists | Master |
| **1. Skeleton** | Build the Astro site, schema, map, theme and place pages, and the deploy workflow, using about 10 seed places (pubs plus WMD) to prove it end to end | Master |
| **2. First themes** | Suggested order: Pubs with History → Spies & Cold War (WMD tour) → Where We Eat → Wartime London → Transit & Hidden City | Topic sessions |
| **3. Google Maps triage** | Process the saved lists and distribute to themes | Topic session |
| **4. Polish and launch** | Practical London page, glossary, trails, search, home-page picks, a mobile check, then share with friends and family | Master |
| **5. Ongoing** | Add places at any time; annual `stale` sweep; new themes as interests grow | Any |

---

## 13. Decisions

| # | Decision | Status |
|---|---|---|
| 1 | **Site name** | Decided: **Where We'd Take You in London**. Repo: `london-guide` |
| 2 | **Repo location** | Decided: a dedicated folder on the desktop's C: drive, outside OneDrive. Raw sources get copied into its git-ignored `sources/` so sessions only need this one folder |
| 3 | **GitHub** | Decided: the user's existing GitHub account (connected to Claude). Repo named once the site is named. Default flow: sessions commit locally and **the user pushes** (pushing = publishing, so this is the review gate). Revisit if direct pushes from sessions turn out to be easy |
| 4 | **Spelling** | Decided: American spelling for our prose; British proper names unchanged |
| 5 | **Wishlist visibility** | Decided: hidden for now, behind the `showWishlist` switch in `content/site.yaml` |
| 6 | **Themes** | Decided: themes are a living list. Sessions can add draft themes and update existing ones; the master session approves and orders them (§5.1). The starter list in §5.1 stands until a session changes it |
