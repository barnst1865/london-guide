# 2026-10-04: Master — pre-launch review (launch plan step 7)

## State
- 120 places: **102 public** (15 favourites), 18 drafts (the untried restaurant research picks, Mayflower and two other pubs held back, Lahore Kebab House).
- Public by theme: historic pubs 34, wartime 27, eat 25, spies 21, parks & walks 19, kids 12, drinks 6, old London 3, science 1, writers & artists 1.
- Trails public: City pub crawl, Thames Path (Hammersmith to Kew), Blitz scars walk, WMD Tour. Guides public: getting around, pub etiquette, eating out, Britishisms.
- `npm run check`: passes (144 pages).

## Checks run
- **Privacy (§3):** scanned all content and planning text for names, work references and home-area hints. No family names, employers or "our local" language found. Private homes on the spy pages (Bentinck Street, Carlyle Square, Greyswood Street) are street- or area-level with no house numbers. Working government sites are described from the public record only. Research-note comments contain nothing private, but they were showing up in page source, so they're now stripped from published pages.
- **Facts:** 18 high-risk claims spot-checked against independent sources: 14 correct, 4 with small caveats, none wrong. Fixed: All Hallows "founded around 675" and the Dove's date ("first recorded in 1790"). Left as is: Punjab "Neal Street since 1951" (the eat session had sources; the restaurant's own site gives no year for the move).
- **Placeholders:** none on public places, trails or guides.
- **Style:** no clichés found. The only British spellings are inside Visit London URLs.

## Changes made
- Links to draft or closed pages now render as plain text on the live site (Session 5 request).
- Themes appear on the home page only with 3+ public places (`minThemePlaces` in `site.yaml`). Science & Curious and Writers & Artists are hidden for now.
- Drafted short intros for `kids`, `drinks` and `medieval-old-london` (family to edit).
- Lahore Kebab House moved back to draft while it's temporarily closed.
- "Start here" row is now Spies, Historic pubs and Where we eat.

## For the family before sharing
- Read the three drafted intros and the home-page welcome; adjust in your own words.
- WMD Tour intro: rewritten as a general introduction to the topic (the "friend who works on arms control" line is gone).
- Several neighborhood cafés and pubs cluster in one part of north-west London. Each is a fine recommendation on its own; just be aware the cluster exists.
