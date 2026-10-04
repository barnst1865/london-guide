# 2026-10-04: Quick listings A, pubs and drinks

**Themes:** `historic-pubs`, `drinks` · **Source:** `sources/triage/google-maps-triage.csv`, rows with `decision` include, `scope` london and a first proposed theme of `historic-pubs` or `drinks`.

## What we did

- **Scope:** 68 matching rows. About 21 already had place files (matched by name, e.g. The George is `george-inn-southwark`, Fuller's shop is `fullers-griffin-brewery`, The Red Lion, Mayfair is `red-lion-duke-of-york-street`) and were skipped. None of the rest was a street or district. That left **47 quick listings**, worked in three batches (15, 16, 16) and shown to the family as tables before writing.
- **Result:** 47 new `depth: listing` files. **46 are public** with `last_verified: 2026-10-04`; **1 is a draft** (`cloth-cornhill`). No badges: nothing in this set is marked favourite in the triage.
  - `historic-pubs`: 42 (4 also carry `eat`: Guinea Grill, Veeraswamy, Wiltons, Bentley's; 3 also carry `drinks`: American Bar, El Vino, Berry Bros.).
  - `drinks` only: 4 (Milroy's of Soho, Le Beaujolais, Cahoots Underground, The Lucky Saint). The Vintage House carries `drinks` and `markets-food-shops`.
- **Verification (§8):** each place was checked on 2026-10-04 for open status, address, nearest stations and official website, using dated 2025–26 evidence where possible. Sources are in each file. Triage notes were mostly research rather than family angles, so the summaries are built on the verified facts, not on visits we haven't made (§2.3).
- **Claims:** age claims that only the venue makes are labelled as claims. Legends are labelled (Turpin at the Flask, the Great Train Robbery at the Star Tavern, the Morpeth Arms tunnel, the Grenadier's ghost, Pembroke "Camden Castles"). Dropped for lack of a source: the Grazing Goat's "1776", the Pembroke's 2014 rename, and the Red Lion & Sun's "Swearing on the Horns" claim. Churchill Arms "1750" is shown as the pub's own claim.
- **Coordinates:** postcode centroids from postcodes.io (geocoders other than postcodes.io weren't reachable from this session), not rooftop. The triage CSV's own approximate coordinates are flagged unreliable and were not used. **Spot-check the pins in `npm run dev`.**
- **Triage CSV:** new `place_file` column (last column) with each new slug. The 21 rows that already had files are left blank. The file's BOM and CRLF line endings are preserved.

## Decisions made with the family

- **Cahoots Underground:** strictly 21+, so not a family place. Kept as a public listing with that stated in the text.
- **Berry Bros. & Rudd:** pinned at the walk-in Wine Shop, 63 Pall Mall. The Grade II* original at 3 St James's Street is the company's HQ, not a public shop, so it appears in the text only.
- **Cloth Cornhill (formerly Simpson's Tavern):** reopening was set for 1 Oct 2026 but no post-opening report was found, and it keeps weekday hours, so it stays `visibility: draft` with a comment. Re-check on a weekday, then set `visibility: public` and add `last_verified`. The old name can't be used, so it is listed as Cloth Cornhill.
- **Veeraswamy:** public. It is in a lease dispute with the Crown Estate (hearing postponed July 2026, no outcome found). The text takes no side and has a review comment; re-check before sharing the site widely.

## Check before sharing

- **Pins that overlap or are approximate:** the Prince's Head and the Cricketers share one postcode centroid on Richmond Green, so their pins sit on top of each other. The Narrowboat's old postcode (N1 8PZ) is terminated and was replaced by a current one. Berry Bros., Cadogan Arms (no Tube on that stretch of the King's Road) and the Flask (uphill from Highgate station) are worth a look on the map.
- **No website field (none confirmed):** The Prince's Head, The Hand & Marigold, The Pride of Spitalfields, The Plimsoll.
- **Recently reopened or changed:** Hand & Marigold (reopened March 2025), Bald Faced Stag (reopened August 2025), Cadogan Arms (2021), Parakeet (2023), Queens (Young's refurbishment, 2025). Re-check at each sweep.
- **Old and new names:** the Grazing Goat (was the Bricklayers Arms, renamed 2011) and the Pembroke Castle (also trades as the Pembroke) are listed under their current names.

## Not done / next rounds

- Full write-ups of these places as the family visits them.
- Theme intros and featured places for `drinks` (not started) and `markets-food-shops`.
- Listings B (eat and shops) and C (everything else) are still to run.
- Historic-pubs `pair_with` links were added only where both places exist: Star Tavern with Grenadier, Prince's Head with Cricketers, Pembroke Castle with Queens, Berry Bros. with Wiltons, Morpeth Arms with Tate Britain, Narrowboat with Regent's Canal walk.

## Check

`npm run check` was not run: this session's computer link has no shell. The front matter was validated by a script against the schema rules: slug format, type, themes, tags, badge, summary length of 160 or less, coordinate ranges and London bounds, `last_verified` on public places, `pair_with` targets, stations and sources.

## Files changed

- `content/places/` new (47, `.md`): `american-bar-savoy`, `bald-faced-stag-east-finchley`, `barley-mow-marylebone`, `bentleys-oyster-bar-and-grill`, `berry-bros-and-rudd`, `black-dog-beer-house-brentford`, `blue-posts-berwick-street`, `cadogan-arms-chelsea`, `cahoots-underground`, `churchill-arms-kensington`, `cloth-cornhill` (draft), `cricketers-richmond`, `dog-and-duck-soho`, `el-vino-fleet-street`, `faltering-fullback-finsbury-park`, `flask-highgate`, `grazing-goat-marylebone`, `grenadier-belgravia`, `guinea-grill`, `hand-and-marigold-bermondsey`, `holly-bush-hampstead`, `lamb-and-flag-covent-garden`, `le-beaujolais`, `lucky-saint-pub`, `milroys-of-soho`, `morpeth-arms-pimlico`, `mr-foggs-tavern`, `narrowboat-islington`, `parakeet-kentish-town`, `pembroke-castle-primrose-hill`, `pineapple-kentish-town`, `plimsoll-finsbury-park`, `pride-of-spitalfields`, `prince-alfred-maida-vale`, `princes-head-richmond`, `punch-and-judy-covent-garden`, `queens-primrose-hill`, `red-lion-and-sun-highgate`, `ship-tavern-holborn`, `sir-colin-campbell-kilburn`, `star-tavern-belgravia`, `the-harp-covent-garden`, `veeraswamy`, `vintage-house-soho`, `washington-belsize-park`, `white-cross-richmond`, `wiltons`
- `sources/triage/google-maps-triage.csv` (new `place_file` column)
- `planning/backlog.md`
- `planning/sessions/2026-10-04-listings-a.md` (this file)
