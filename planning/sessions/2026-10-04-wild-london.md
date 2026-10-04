# Session 6: Parks, Walks & Wild London + Thames Path (2026-10-04)

**Goal:** launch set for `wild-london`: 5–8 public places, theme intro, 3–4 featured places, and the Thames Path trail from idea #24 (segments, optional stops, waypoints, variants).

## Sources used

- `sources/triage/handoff.md`, wild-london section (5 rows), plus related rows filed under other themes (the Dove, the Spaniards, Fuller's, the William Morris Society, Kew pubs and tearoom, Diana Memorial Playground).
- Idea #24's route and stops (now marked accepted in `ideas.md`).
- Interview with the family; no first-hand anecdotes this round (plain recommendations; the family will add voice at review).

## Decisions (with the family)

- **Route:** north bank from Hammersmith Bridge to Barnes Bridge, cross on the bridge footway, south-bank towpath, then leave the river by the National Archives for Kew Gardens station. The long version stays on the towpath to Kew Bridge and Kew Green.
- **Favourites:** the Blue Anchor and Kew Gardens (plus the Dove and the Spaniards, already favourites from Session 2).
- **Other walks for launch:** Hampstead Heath, Regent's Canal (Little Venice to Camden), Kensington Gardens with the Diana Memorial Playground, and Richmond Park.
- **Held back:** all 5 wild-london handoff rows (Clifton Nurseries and its café, the Garden Museum, Alexandra Palace; Kew's Palm House is folded into Kew Gardens). The Botanist on Kew Green was skipped (chain, §7).
- **Pubs under 75 years** carry `wild-london` only (just the Tap on the Line).
- **Featured:** Kew Gardens, Hampstead Heath, Regent's Canal, Richmond Park.

## Added or changed

**New, public (16, all `last_verified: 2026-10-04`):**
- Thames Path stops: `blue-anchor-hammersmith` (★), `rutland-arms-hammersmith`, `william-morris-society`, `old-ship-hammersmith`, `black-lion-hammersmith`, `fullers-griffin-brewery`, `white-hart-barnes`, `tap-on-the-line`, `original-maids-of-honour`, `kew-gardens` (★), `rose-and-crown-kew`
- Parks and walks: `hampstead-heath`, `regents-canal-walk`, `kensington-gardens`, `diana-memorial-playground`, `richmond-park`

**Existing (Session 2's files), theme added:** `the-dove-hammersmith` and `spaniards-inn` now also carry `wild-london`. Their `pair_with` was filled in; nothing else changed.

**Theme:** `content/themes/wild-london.md`: intro written, blurb tweaked, `featured` set.

**Trail:** `content/trails/thames-path-hammersmith-to-kew.md`, public and featured. It has:
- 18 stops: 13 places (4 optional) and 5 waypoints (Hammersmith Bridge, St Nicholas Church, Barnes Bridge, Chiswick Bridge, and the National Archives exit).
- 3 segments.
- 4 variants: Black Lion, White Hart, Kew Gardens, and the Rose & Crown via Kew Bridge.
- The draft `first-v2-staveley-road` as an optional detour. It stays hidden until the wartime session publishes it.

## How facts were checked

- **Age:** every pub checked against the 75-year rule. Earliest documented dates:
  - Black Lion: 1754
  - The Old Ship: 1795
  - White Hart: 1822
  - Blue Anchor: 1843 (the pub claims 1722, labelled as its claim)
  - Rutland: 1849
  - Rose & Crown: 1860
  - Maids of Honour: Kew Road shop 1887; Newens business 1850
  - Tap on the Line: a pub only since about the 1980s, so no `historic-pubs`
- **Sources:** Historic England list entries, CAMRA, pubs-history sources, the Survey of London, Richmond Local Studies, Royal Parks, City of London, Canal & River Trust, and Kew. All are recorded in each file's `sources:`.
- **Open status:** every venue checked against 2025–26 sources. All trading. The Rose & Crown reopened under its old name in 2025, and the Diana Playground reopened in August 2026 after renewal.
- **Coordinates:** Nominatim was blocked, so coordinates come from Historic England list-entry points, CAMRA and venue listings, and GLA view-assessment points (Parliament Hill, King Henry's Mound).
- **Legends labelled as such:** Holst at the Blue Anchor, the Fuller's wisteria, the Maids of Honour and Henry VIII, King Henry's Mound and Anne Boleyn, and the Little Venice name.
- **Route facts:**
  - Hammersmith Bridge is open on foot (closed to vehicles).
  - The Barnes Bridge footway is on the downstream side.
  - Chiswick Mall and the Mortlake towpath flood at high spring tides.
  - Kew Gardens admits **assistance dogs only**. The trail and Kew's file say so prominently.

## To check when previewing (`npm run dev`)

- **Old Ship pin:** sources disagreed slightly.
- **Diana Playground pin:** two sources about 80 m apart.
- **Two estimated waypoints:** Hammersmith Bridge (north end) and the National Archives exit. The footpath link from the towpath to Ruskin Avenue wasn't confirmed on a map.
- **Trail distances are approximate:** about 2 miles to Barnes Bridge and about 4 miles to Kew Gardens.

## Open

- **Two new requests in `planning/requests.md`:**
  - Themes with placeholder intros (`kids`, `writers-artists-makers`, `drinks`, `eat`) now have public places and will show on the live site.
  - A date check on the Dove's "licensed by 1740" line.
- **Next rounds:**
  - Clifton Nurseries, the Garden Museum and Alexandra Palace.
  - The Narrowboat, Word on the Water and the Canal Museum, which could extend the canal walk east of Camden.
  - Idea #8 (lost rivers walk).
  - A Richmond riverside walk (the White Cross is in the historic-pubs handoff).
- **Not run:** `npm run check` (no shell on the linked computer). The family runs it before pushing.
