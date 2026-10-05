# Where We'd Take You in London — Project Instructions

**Version:** 0.4 · **Last updated:** 2026-10-01 · **Owner:** master planning session

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

Secondary audience: **people moving to London**. They're served by the "Living here" guides (§5.6), worded generically ("people moving here"), with no employer or posting references (§3).

---

## 2. Guiding principles

1. **Our voice, our opinions.** Write as "we": personal, warm, and a bit wry. Say *why we love it*, not just what it is. A short anecdote beats a Wikipedia summary.
2. **Beyond the obvious.** Big-name sites are included only when we have a specific angle on them, such as the best entrance, the room most people miss, or what to pair it with. Default to the less-known.
3. **Confident recommendations.** The guide gathers recommendations from our family and from trusted friends and colleagues who have been there. If a place is on the site, we're confident it's worth a visit, but we don't claim to have personally visited everything. The only badge is ★ Family favourite, for places we've been to more than once and actively send people to (§5.4). Describe first-hand experiences ("we sat by the fire…") only where they're ours; otherwise recommend plainly ("friends who live nearby swear by it" is fine, but not required).
4. **Accurate.** Historical claims are fact-checked against reliable sources before publishing (§8).
5. **Useful on the ground.** Give the nearest station, whether to book, whether it's good for kids, and what's nearby to pair it with.
6. **Durable.** Avoid details that go stale fast, such as exact opening hours, prices and named staff. Link to the venue's site instead. For rules, fees and charges (transport, pets, driving), link to the official source; our value is experience and tacit advice.
7. **Browse-first.** The site is for browsing: themes, trails, guides and the map. No interactive planners, quizzes, checklists or "build my day" tools (family decision; see `planning/ideas.md` #4–#6, #15).

---

## 3. Privacy and safety rules (hard rules — apply to everything committed to the repo)

The site is public, so these rules apply to every file in the repository, not just the visible pages.

- **No identifying family details.** No surnames, no first names of the kids, no photos showing our faces or the kids' faces, and no mention of our employers, jobs, posting or work locations. "Our family" / "we" is the voice.
- **No home location.** Nothing that reveals where we live: no "our local", no "around the corner from us", no neighbourhood-of-residence hints, and no kids' schools or clubs. A place can be a favourite without saying why it's convenient for us.
- **No work-derived framing.** Anything from work-sourced lists (e.g., the office restaurant list) is rewritten from scratch for visitors. References to official functions, specific government buildings' staff habits ("full of X folks"), or colleagues' preferences are removed.
- **House numbers: the family decides.** If the family chooses to include a specific house number, the building is noteworthy enough to be publicly identified (a blue-plaque house, a famous film exterior, a historic address), so give the full address and pin it as precisely as the coordinates allow. Sessions don't add house numbers on their own initiative: for history at a private home the family hasn't chosen to identify (e.g., Litvinenko's house, Skripal's former house), use `location_precision: area` or `street`, describe the site in text, and prefer a nearby public landmark as the pin. Either way, private buildings are described as seen from the street, and nothing may reveal where we or our friends live (see above).
- **Active government and military sites** (e.g., Thames House, Vauxhall Cross, RAF Northolt, AWE Aldermaston) are included only as things visible from public places, described from public sources. No advice on photographing them, approaching their perimeters, or anything about their security.
- **Respect for victims.** The spy and WMD material involves real people who died or were injured, including bystanders (e.g., Dawn Sturgess). The tone there is curious and serious, never jokey.
- **Robots.** The site ships with `noindex` meta tags and a `robots.txt` that disallows crawling. The link is shared directly with friends and family.
- **Address.** The site lives at `london.dckoiks.com` (decision 18). The family chose its own domain knowing it can point back to us; the content rules above still apply in full, so the domain is no reason to add names or details.
- **Private material stays private.** Raw source files (Google Takeout, office lists, notes) live in `sources/`, which is **git-ignored** and never published.

---

## 4. Scope

- **Core:** Greater London.
- **Day Trips:** places roughly ≤2 hours by train from central London, done as a return trip (e.g., Salisbury, Bletchley Park, IWM Duxford, Windsor, Dover, Canterbury, Oxford, Cambridge, Portsmouth). Day trips are a *type* (`day-trip`) and can also carry themes (e.g., Salisbury → Spies & Cold War).
- **Out of scope:** longer UK weekends (Cotswolds, Dorset, Scotland, and so on). This could become a separate section later.

---

## 5. How content is organized

There are four ways to cut the content. A place has **one type**, **one or more themes**, **any number of tags**, and optionally the **favourite** badge.

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
| `historic-pubs` | **Historic Pubs & Restaurants** (id unchanged). Rule: any pub or restaurant **75+ years old** that we include carries this theme | Ye Olde Cheshire Cheese, Ye Olde Mitre, Cittie of Yorke, Olde Wine Shades, Mayflower, Prospect of Whitby, The Grapes, The Harp, French House, Seven Stars |
| `eat` | **Where We Eat** (by occasion and cuisine) | Dishoom, Punjab, Barbary, Sichuan spots, Indian (Cinnamon Club, Quilon, Kutir), Rules (angle), Brasserie Zédel, Dumplings' Legend |
| `drinks` | **Bars, Cocktails & Wine** | Gordon's Wine Bar, Duke's, Connaught Bar, Mr Fogg's, Radio Rooftop |
| `markets-food-shops` | **Markets & Shops**: markets, food shops and specialist shops (antiques, maps, books, toys) | Borough, Maltby Street, Columbia Road, Neal's Yard Dairy, Gelateria La Romana |
| `sport` | **Sport**: watch it, tour it, run it | Lord's (incl. Eton v Harrow), The Oval, football from Premier League to non-league groundhopping (from our Football Teams map), Wimbledon, Twickenham, Marathon viewing spots |
| `play-games-music` | **Play, Games & Live Music** | Arcade Battersea, board-game cafés, retro arcades, Flight Club, live-music venues in the rock and Americana tradition |
| `wild-london` | **Parks, Walks & Wild London** (including foraging, canals and the Thames) | Hampstead Heath, Richmond Park, Regent's Canal walk, Walthamstow Wetlands, Crystal Palace dinosaurs, Thames foreshore (note PLA permit rules) |
| `kids` | **With Kids** (and teens) | Horniman, Science Museum Wonderlab, Mudchute Farm, Diana Memorial Playground, Cutty Sark, Crystal Palace dinosaurs |
| `day-trips` | **Day Trips** | See §4 |
| `only-in-london` | **Only in London**: British oddities | Places and experiences that are odd in themselves (idea #13). How-to-get-by advice belongs in the Practical London guides |
| `on-screen-on-record` | **On Screen & On Record**: film, TV and music landmarks | Great Muppet Caper locations, Abbey Road crossing, the Oasis album-cover street, Leadenhall Market. Many exteriors are private buildings: street-level only (§3) |
| `writers-artists-makers` | **Writers, Artists & Makers** | Charles Dickens Museum, William Blake sites, William Morris Gallery and Society, Foundling Museum, Sherlock Holmes Museum |

Theme files live in `content/themes/<id>.md` (§6.2).

**Themes are a living list.** Adding a theme or reworking an existing one is expected, not exceptional:

- **New theme:** any session may create `content/themes/<new-id>.md` with `visibility: draft` and add a row to `planning/backlog.md`. The master session reviews it for overlap with existing themes, assigns menu `order`, and publishes it.
- **Updating a theme:** any session may revise a theme's intro, featured list or places. Renaming a theme's *title* is fine; changing its *id* is a master-session job, because place files reference it.
- **Merging or retiring a theme:** master session only. Retired themes keep their file with `visibility: draft` so nothing breaks.

### 5.2 Types (one per place, "what kind of place is it?")

Types drive map marker icons and the "Browse by type" menus.

`historic-site` · `museum` · `church` · `pub` · `bar` · `restaurant` · `cafe` · `quick-bite` (ice cream, bakeries, desserts: not a sit-down meal) · `market-shop` · `park-walk` · `entertainment` · `sport-venue` · `viewpoint` · `tour` · `day-trip`

### 5.3 Trails (ordered routes)

A trail is an ordered sequence of places with walking or transport notes between them, drawn as a route on the map. Examples: the **WMD Tour**, a **City of London historic pub crawl**, and a **Cold War walk around Whitehall**. Trails reference places by slug and don't duplicate place content.

### 5.3a Trail structure

Trails can have **named segments** (e.g. "Hammersmith to Barnes"), **optional stops** (detours, shown dashed), **waypoints** (a named point that isn't a place, like a bridge crossing, used to shape the route), and **variants** (shorter or longer ways to do it, optionally naming the stop where a variant ends). See §6.3.

**How the map draws a trail** (since 2026-10-04): a solid line through the required stops and waypoints in order; a dotted spur from the previous main-route stop to each optional stop within 1.5 km (optional stops further away are marked but not joined); and a dashed line for each alternative ending, from its `branches_at` stop. Markers are numbered to match the stop list. The line is straight between points, so the map is captioned as a rough guide. To make it follow the real path (round a river bend, along a towpath), add `path_only` waypoints with coordinates you've checked on a map.

### 5.4 The favourite badge (optional)

| badge | Label shown | Meaning |
|---|---|---|
| `favourite` | ★ Family favourite | We've been more than once and actively send people there |
| *(none)* | *(nothing shown)* | Recommended: we're confident it's worth a visit |

There are no other badges (decided 2026-10-04; `like`, `tip` and `wishlist` were retired and now fail the build). A place goes public when we're confident recommending it, from our own visit or a trusted friend's or colleague's. Places found only through research (e.g. the restaurant research drafts) stay at `visibility: draft` until someone we trust has been. The map's "Favourites only" filter and the home page's "Family favourites" row use this badge.

### 5.5 Tags (controlled vocabulary; add new ones via the master session)

`kid-friendly` · `teen-appeal` · `dog-friendly` · `free` · `booking-essential` · `rainy-day` · `outdoors` · `step-free` · `late-night` · `seasonal` · `quick-visit` (<1 hr) · `half-day` · `group-friendly` · `sunday` (good on a Sunday)

Price uses `price: 1–4` (£ to ££££) for food and drink, and `£0` / `£` / `££` / `£££` for attractions. Use the scale only, never actual prices.

---

### 5.6 Guides (standalone written pages)

Guides are written pages that aren't about a single place: how-to advice, essays, area mini-guides. Each is one file in `content/guides/<id>.md`, in one of four groups:

| group | Label shown | For |
|---|---|---|
| `practical` | Practical London | Getting around, pub etiquette, eating out, glossary |
| `area` | Around town | What's actually good in the busiest districts (idea #25) |
| `essay` | Essays | Longer reads, e.g. historic pubs and restaurants |
| `living-here` | Living here | For people moving to London: dogs, cars, and so on |

**Streets and districts** (Brick Lane, Carnaby Street, and so on) are handled as `area` guides linking to their standout places, not as place files. A single-spot sight on a street (e.g. the Abbey Road crossing) is still a place file.

A guide can list `places` (shown as cards and on a map at the end) and link to anything inline with the internal link syntax (§6.6). The old Practical London page now redirects to the Guides page. Any session may draft a guide; new groups are a master-session change.

## 6. Data model

All content lives in plain Markdown files with YAML front matter. **One place = one file.** This keeps sessions from colliding and makes additions trivial.

### 6.1 Place file — `content/places/<slug>.md`

Slug: lowercase, hyphenated, unique, stable (e.g., `ye-olde-cheshire-cheese`). Never rename a slug once published, because trails and links depend on it.

```yaml
---
name: Ye Olde Cheshire Cheese
type: pub
themes: [historic-pubs, medieval-old-london]
badge: favourite                # optional; the only allowed value
tags: [rainy-day, group-friendly]
occasions: [quick-lunch, dinner-with-friends]   # optional, mainly eat/drinks: breakfast-brunch, quick-lunch, cheap-cheerful, dinner-with-friends, sunday-roast, afternoon-tea, special-occasion. Theme pages group places by these under "Pick by occasion"
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

**Quick listings.** `depth: listing` marks a short entry: all the usual front matter (verified address, coordinates, station, status, `last_verified`, sources) and a summary in our voice, but little or no body. Listings appear on the map, on type pages and in a compact "More places we recommend" list at the end of their theme page; the place page says a fuller write-up is coming. When a theme session writes one up properly, it removes `depth: listing` (the default is `full`). Listings let every place we recommend reach the map before it gets a full page.

Optional: `kids_say: "..."` (≤140 chars), a one-line quote from our kids, shown on the place page as "Our kids". No names or ages (§3).

**Required:** `name`, `type`, `themes` (≥1), `summary`, `area`, `coords`, `location_precision`, `status`, `visibility`. `last_verified` is required before a place can be `public`; the build refuses public places without it.
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
title: Thames Path from Hammersmith
summary: A riverside walk with pub stops, great with kids and dogs.   # ≤200 chars
themes: [wild-london, historic-pubs]
mode: walk                       # walk | transit | mixed
duration: Half day
tags: [kid-friendly, dog-friendly, outdoors]
featured: true                   # show on the home page
stops:
  - place: blue-anchor           # a place, by slug
    segment: Hammersmith to Chiswick   # optional: starts a named section
    note: Start on the north bank...
  - waypoint: Hammersmith Bridge # a point that isn't a place file
    coords: [51.4883, -0.2302]
    note: Cross here if the bridge is open to pedestrians.
  - place: william-morris-society
    optional: true               # a detour, shown dashed
  - waypoint: Dukes Meadows bend # shapes the map line only: no marker, not listed
    coords: [51.4790, -0.2560]   # illustrative only: check real coordinates on a map
    path_only: true
variants:
  - name: Short version
    description: Finish after the White Hart.
    ends_at: white-hart-barnes   # optional: must be a stop on this trail
  - name: Long version
    description: Stay on the towpath to Kew Bridge.
    ends_at: rose-and-crown-kew  # an optional stop = an alternative ending...
    branches_at: National Archives (leave the river)   # ...drawn from here (a place slug or waypoint name)
visibility: draft
---
Introduction to the trail.
```

Each stop has either `place`, or `waypoint` + `coords`. A trail is hidden if any required stop isn't public; optional stops that aren't public are simply left out.

### 6.5 Guide file — `content/guides/<id>.md`

```yaml
---
title: Pub etiquette
summary: Order at the bar, rounds, last orders...   # ≤200 chars
group: practical                 # practical | area | essay | living-here
order: 2                         # order within the group
themes: [historic-pubs]          # related themes (linked at the end)
places: [ye-olde-cheshire-cheese]  # shown as cards and on a map at the end
featured: false                  # show on the home page
visibility: draft
last_verified: 2026-10-03        # required once public
sources: []
---
Body in our voice, with ## headings.
```

### 6.6 Internal links

In any Markdown body, link to other pages with `[text](place:slug)`, `[text](theme:id)`, `[text](trail:id)` or `[text](guide:id)`. The build turns these into correct links and **fails if the target doesn't exist**. On the published site, a link to a draft (or closed) target is shown as plain italic text instead of a dead link. `<!-- comments -->` in bodies are for research notes: they stay in the repo but are stripped from published pages (the repo is still public, so keep §3 in mind). Don't write `/places/...` paths by hand, because the site lives under a base path.

### 6.7 Site settings — `content/site.yaml`

`title`, `tagline`, `startHere` (up to three theme ids shown large at the top of the home page), `minThemePlaces` (a theme appears on the published home page only once it has at least this many public places; currently 3) and `homeFavourites` (the hand-picked "Family favourites" on the home page: a list of `{ place, why }`, where `why` is one line in our voice; while it's empty the home page shows the first six favourites alphabetically). (The old `showWishlist` switch was retired with the wishlist badge.)

### 6.8 Validation

The site build validates every file against this schema and **fails loudly** on errors: missing required fields, unknown theme, type or tag, any badge other than `favourite`, malformed coordinates, a trail, guide or variant pointing to a non-existent slug, a broken internal link (§6.6), or a duplicate slug. Running `npm run check` before finishing any session is mandatory.

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
- **Legends:** a good story we can't verify may be included if it's clearly labelled as such ("apocryphally…", "the story goes…"). Never state it as fact.
- **What earns a place (restaurants, cafés, bars):** prefer places that are long-established, good value, quirky or one-of-a-kind, or unexpectedly good. Skip the mediocre, the trendy-new, chains and the overpriced, unless we have a specific reason (e.g. a kid-friendly stop on a river walk, or good non-alcoholic options).
- **Kids:** say honestly what works for which ages ("teens will love it; under-8s will be bored after 20 minutes").

---

## 8. Fact-checking and freshness

- **Every factual claim** (dates, "oldest", "only", who did what where) is checked against at least one reliable source. Anything we can't verify is either cut or labelled as legend (§7): the venue's own site, Historic England, the museum, reputable press, or official inquiry reports (e.g., the Litvinenko and Dawn Sturgess inquiries). Record the URLs in `sources:`.
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
| Map | **Leaflet** + OpenStreetMap tiles (no API key; CARTO now needs one) + marker clustering | Free, no API key, works well on mobile |
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
│   ├── guides/<id>.md
│   └── site.yaml                ← site-wide settings (title, tagline, startHere)
├── src/                         ← Astro site code (master session only)
├── public/                      ← static assets: icons, our own photos, robots.txt
├── .github/workflows/deploy.yml ← builds and publishes on push to main
├── planning/
│   ├── backlog.md               ← status of every theme and workstream
│   ├── ideas.md                 ← brainstormed features and content ideas (family input)
│   ├── sessions/YYYY-MM-DD-<topic>.md   ← one log per working session
│   ├── launch-plan.md           ← what's needed to go live, and which sessions do it
│   └── requests.md              ← schema or site change requests from theme sessions
├── tools/                       ← import, geocode, validate and stale scripts
└── sources/                     ← GIT-IGNORED raw inputs (Takeout, office list, old drafts)
```

### 9.3 Pages

- **Home (browse-first):** a short welcome with quick links (Explore the map, Before you visit, Walks and trails, and Moving here once a Living here guide is public); a "Start here" row of up to three themes (`startHere` in `site.yaml`); the remaining themes as a compact list; featured trails; featured guides; a map teaser with browse-by-type chips; family favourites (`homeFavourites`). The first nav item is "Home". On the published site, themes appear only once they have a public place.
- **Map:** full-screen map with markers styled by type; filters for theme, type, favourites and key tags (kid-friendly, free, rainy-day), offering only themes and types that have public places; clustering; popups linking to place pages. Filters are kept in the URL, so a filtered map can be linked.
- **Theme pages:** intro essay, featured places, places grouped by type, trails in the theme, and a mini-map.
- **Browse by type:** Eat, Drink, Museums, Historic sites, and so on.
- **Place pages:** description, "Our kids" quote (optional), our tip, practical box with directions (the link searches Google Maps by name and address, not by our pin, so it works at `exact` or `street` precision; `area` places get none), mini-map, "pair with", and the themes it belongs to.
- **Trail pages:** summary, route map (numbered markers, main line, detours and alternative endings; see §5.3a) with a caption, "Ways to do it" variants, and stops grouped by segment.
- **Guides:** an index grouped as Practical London, Around town, Essays and Living here, plus one page per guide, with its places on a map at the end.

**Later (parked ideas):** "Near me" (geolocation), search, a printable or offline trail view, photos.

### 9.4 Images

Version 1 has no photos, which keeps it simple and safe. If added later, use **only our own photos (no people's faces)** or openly licensed images (e.g., Wikimedia Commons) with attribution. Never hotlink or scrape venue images.

---

## 10. How we work: master session and topic sessions

### 10.1 Roles

**Master session** (the Cowork "London Guide" planning session):

- Owns this file, the schema, the theme, type and tag lists, the site code (`src/`), `planning/backlog.md`, and deploys.
- Reviews output from topic sessions for consistency, duplicates, privacy and style.
- Processes `planning/requests.md`.

**Ideas session** (an ongoing brainstorm with the family):

- Captures feature and content ideas in `planning/ideas.md`, with a kind, a source role (never names) and a status.
- Doesn't build anything. Ideas move on only when the master session accepts them into `backlog.md` or `requests.md`, or when a theme session picks up a content idea.
- Every other session should skim `planning/ideas.md` at the start, and theme sessions should pick up `content` ideas for their theme.

**Topic sessions** (one per theme, or per workstream such as "Google Maps triage"):

- Start a new Cowork session **in the same claude.ai Project, with the same folder connected**.
- Work only in `content/` and `planning/sessions/`. **Do not edit `src/`, the schema, or this file.** Propose changes in `planning/requests.md`.
- May add their theme to an existing place's `themes:` list instead of creating a duplicate place. That's encouraged.
- May create a new draft theme or update an existing theme's file (see §5.1).

### 10.2 Topic-session kickoff prompt (copy and paste)

> We're working on the London Guide. Read `PROJECT_INSTRUCTIONS.md` and `planning/backlog.md` in the connected London-Guide folder, then the theme file for **[THEME ID]** and the list of existing places. This session's job is to build out the **[THEME NAME]** theme. Start by interviewing me about what we love in this theme, then propose candidates (including less-obvious ones), and we'll triage together before you research and write anything.

### 10.3 Topic-session workflow

1. **Orient.** Read this file, the backlog, `planning/ideas.md` (for ideas tagged with this theme), the theme file, and the existing places (by name, type and themes) to avoid duplicates.
2. **Interview.** Ask what we've done, what we loved, stories worth telling, and which places from the source material belong here.
3. **Propose.** Suggest a candidate list mixing our known places and beyond-the-obvious ideas, each with a one-line pitch.
4. **Triage with the user.** For each candidate, decide include or skip, a type, and whether it's a family favourite. Places we haven't been to yet but want to vet stay as drafts.
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

All raw sources live in the private, git-ignored `sources/` folder (see `sources/README.md`). Never quote list names, notes or addresses from them into `content/` or `planning/`.

| Source | Location | Handling |
|---|---|---|
| **Google Maps triage results** | `sources/triage/google-maps-triage.csv` | **Start here for any theme.** 503 rows (London and day trips) with `decision` (include/skip), `proposed_type`, `proposed_themes`, `proposed_badge` (only `favourite` is meaningful now; anything else is ignored), notes with the family's angle, and approximate coords (re-geocode from the address; don't trust the decoded coords). |
| WMD tour draft | `sources/docs/UK WMD Tour - Fleshed OUt.docx` | Goes to the `spies-cold-war` and `wartime-london` themes plus the **WMD Tour** trail. Full fact-check and privacy pass (§3, §8); known errors are listed in §8. |
| Office restaurant and pub list | `sources/docs/London Restaurants.docx` | Goes to `eat`, `historic-pubs` and `drinks`. Include only places we're confident recommending; mark `favourite` where it applies. Rewrite from scratch with no work framing. Verify each is still open. |
| OneNote export | `sources/docs/UK Tour Guide - 8 June 2025.pdf` | Duplicate of the two documents above; reference only. |
| Our 5-star Google reviews | `sources/google-maps/takeout/Reviews.json` | Already folded into the triage. |
| London Football Teams map | `sources/google-maps/takeout/London Football Teams.kmz` | `sport` theme (possibly a groundhopping trail). |
| Raw Google saved lists | `sources/google-maps/saved/` | Already triaged; consult only for detail the triage notes lack. |
| Historic England list | `sources/National_Heritage_List_for_England_NHLE_*.csv` | Fact-checking listing grades and dates. |

---

## 12. Roadmap

| Phase | What | Where |
|---|---|---|
| **0. Foundations** | Agree these instructions; decide the open items in §13; create the repo; re-export Google saved lists | Master |
| **1. Skeleton** | Build the Astro site, schema, map, theme and place pages, and the deploy workflow, using about 10 seed places (pubs plus WMD) to prove it end to end | Master |
| **2. First themes** | Suggested order: Pubs with History → Spies & Cold War (WMD tour) → Where We Eat → Wartime London → Transit & Hidden City | Topic sessions |
| **3. Google Maps triage** | Done 2026-10-03 (a handful still to research); results in `sources/triage/` | Topic session |
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
| 5 | **Badges** | Decided 2026-10-04: `favourite` is the only badge and is optional. `like`, `tip`, `wishlist` and the `showWishlist` switch were retired. Unvetted places stay as drafts (§5.4) |
| 6 | **Themes** | Decided: themes are a living list. Sessions can add draft themes and update existing ones; the master session approves and orders them (§5.1). The starter list in §5.1 stands until a session changes it |
| 7 | **Browse-first** | Decided: no planners, quizzes or checklists (§2.7) |
| 8 | **Guides** | Decided: a Guides section of standalone pages, grouped as Practical London, Around town, Essays and Living here (§5.6). Practical London became guides |
| 9 | **People moving here** | Decided: served by the "Living here" guide group, worded generically (§1) |
| 10 | **New theme** | Added `only-in-london` (idea #13) |
| 11 | **More themes** | Added `on-screen-on-record` (film, TV, music landmarks) and `writers-artists-makers` (2026-10-03). Both post-launch |
| 12 | **Whose recommendations** | Decided 2026-10-04: the guide gathers recommendations from the family and trusted friends and colleagues who've been; it doesn't claim we've visited everything. Research-only finds stay as drafts until someone we trust has been (§2.3, §5.4) |
| 13 | **Markets & Shops** | `markets-food-shops` retitled "Markets & Shops" to include specialist non-food shops (id unchanged) |
| 14 | **Streets and districts** | Handled as "Around town" area guides, not place files (§5.6) |
| 15 | **Pre-launch review** | 2026-10-04: themes need 3+ public places to appear on the home page; links to drafts render as plain text; research-note comments are stripped from pages; temporarily closed places go back to draft |
| 16 | **Quick listings** | 2026-10-04: remaining triage places go on the site first as `depth: listing` entries (verified facts and a one-line summary), then become full pages as themes are built out (§6.1) |
| 17 | **House numbers** | Decided 2026-10-04: the blanket no-house-numbers rule is replaced. A house number the family chooses to include means the building is noteworthy enough to be identified; sessions don't add them on their own (§3). First used for the three Great Muppet Caper buildings |
| 18 | **Custom domain** | Decided 2026-10-05: the site moved from `barnst1865.github.io/london-guide/` to **`london.dckoiks.com`** (a CNAME at Squarespace; custom domain set in the repo's Pages settings). The base path is now `/`; old `/london-guide/...` links are forwarded by the 404 page |
