# Launch plan

**Status on 2026-10-03 (after housekeeping):** site built and deployed (browse-first home, map, themes, trails, guides). **Nothing is public yet:** 27 draft places (11 unverified seeds and 16 restaurant research picks on the wishlist), 7 outline guides, 1 draft trail, 15 themes with no intros.

## Launch bar (what "ready to share" means)

1. **5 launch themes** with at least 5 public places each, a written intro and 3–4 featured places. Suggested: Historic Pubs & Restaurants, Spies & Cold War, Wartime London, Where We Eat, plus one more we know well (Parks & walks or With kids).
2. **2 public trails:** the WMD Tour (London stops) and one walk (the City pub crawl or the Thames Path).
3. **4 Practical London guides** written: getting around, pub etiquette, eating out, Britishisms.
4. **Home page** welcome text rewritten in our voice; `startHere` set to three launch themes.
5. **Pre-launch review passed** (master session): privacy sweep (§3), fact and freshness spot-check (§8), broken links, mobile check, and the map with real pins.

Everything else (other themes, Living here guides, essays, area guides, parked features) is post-launch. The site grows by adding files.

## Sessions

Work through the sessions in this order; sessions 1–5 can run in parallel. Start each one in the London Guide project with the LondonGuide folder connected, using the kickoff prompt below.

| # | Session | Produces | Depends on |
|---|---|---|---|
| 0 | **Housekeeping** | **Done 2026-10-03.** Sources and triage results are in `sources/` (private); triage requests processed | — |
| 1 | **Google Maps triage: finish and hand off** | The last few rows researched and decided in `sources/triage/google-maps-triage.csv` | 0 |
| 2 | **Theme: Historic Pubs & Restaurants** (+ City pub crawl trail) | ~8–12 public places, theme intro, 1 trail | 1 helps |
| 3 | **Themes: Spies & Cold War + Wartime London** (+ WMD Tour) | ~10–15 public places, both intros, WMD Tour trail (London part) | 0 (WMD doc) |
| 4 | **Theme: Where We Eat** (finish) | Our own restaurants (Google reviews, office list, triage), research drafts we've now tried rewritten and published, intro | 1 helps |
| 5 | **Guides: Practical London** | 4 guides written and public | — |
| 6 | **Fifth theme** (Parks & walks + Thames Path, or With kids) | ~5–8 places, intro, optionally the Thames Path trail | 1 helps |
| 7 | **Master: pre-launch review** (this coordinating session) | Fixes, home text, launch checklist ticked, then share the link | 2–6 |

## Kickoff prompt (fill in the [brackets])

> We're working on Where We'd Take You in London. Read `CLAUDE.md`, `PROJECT_INSTRUCTIONS.md`, `planning/launch-plan.md`, `planning/backlog.md` and `planning/ideas.md` in the connected LondonGuide folder, and list `content/places/` so you don't duplicate anything. This session is **[session name from the table]**. Its goal: **[the "Produces" column]**. Use these sources: `sources/triage/google-maps-triage.csv` (rows where `decision` is include and `proposed_themes` matches), [any `sources/docs/` file], and the existing seed drafts. Start by interviewing me about what we've actually done and loved, then propose candidates and sort through them with me before researching and writing. Verify facts (§8), write in our voice (§7), follow the privacy rules (§3), and only set `visibility: public` on places I've approved and that have `last_verified`. Finish by logging the session in `planning/sessions/`, updating `planning/backlog.md`, and telling me which files changed so I can commit and push.

## Tips

- **Commit and push after every session.** Drafts never show, so pushing is safe.
- **Sessions on this computer can't run `npm run check`** (no command line), so they hand off to you: run `npm run check` in the LondonGuide folder before pushing, and `npm run dev` to preview drafts at http://localhost:4321/london-guide/. If a push ever breaks the build, the live site stays on the last good version and the Actions tab shows why.
- **The restaurant research drafts:** these stay as drafts until we're confident recommending them, usually after a visit. Then rewrite the "It's on our list because…" text in our own voice, add `badge: favourite` if it earned it, set `last_verified`, and set `visibility: public`. You can do this by hand or in any session.
