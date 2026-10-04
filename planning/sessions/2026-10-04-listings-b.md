# Session log: Listings B (eat and markets-food-shops quick listings)

Date: 2026-10-04. Scope: London triage rows whose first theme is `eat` or `markets-food-shops`, written as `depth: listing` files per §6.1. Triage IDs and slugs are in `sources/triage/listings-B.md` (private, git-ignored). The triage CSV was not edited.

## Result

47 place files: 42 public, 5 drafts. Worked in three batches (15, 15, 17), each shown as a table and approved before any file was written.

- Batch 1 (markets and shops, 15): 14 public, 1 draft (`the-deli-warehouse`). Favourites: `daunt-books-marylebone`, `hampstead-butcher-and-providore`. `hedonism-wines` and `grays-antique-market` are paired.
- Batch 2 (restaurants, 15): all public. Six carry `historic-pubs` (M. Manze, J Sheekey, Mon Plaisir, Rock & Sole Plaice, Simpson's in the Strand, Palm Court at The Langham).
- Batch 3 (cafes, quick-bites, pubs, 17): 13 public, 4 drafts.

## Held as drafts, and why

- `the-deli-warehouse`: two websites give different addresses and the best dated press item is 2024; the business changed hands in 2024. Phone or check socials, then settle the address.
- `ginger-natural-food`: only a food business called "Ginger Cafe" is recorded at the address (inspected April 2026); no source uses the longer name, no reviews or menu found.
- `finsbury-park-cafe`: newest dated evidence is March 2025, its own site was last updated in 2022, and the pin is a park postcode.
- `original-dubai-shawarma`: the operating company applied for strike-off in April 2026 and was dissolved in July 2026; no 2026 review found.
- `the-hut-by-the-heath`: no 2026 trading evidence, no named operator, and the Heath-area cafe concessions changed hands this year.

## Calls made during the session (all approved)

- `tamil-crown` is type `restaurant` with no `historic-pubs` theme: the pub site dates from 1839 but it is unconfirmed that the present building is the original. It pairs with `tamil-prince`.
- `the-botanist-kew` is type `pub` with no `historic-pubs` theme (building age unverified) and is not described as a chain (ownership unconfirmed).
- `dunns-bakery-crouch-end` is the original shop; the 1820 founding date is attributed to the bakery because a trade source says 1850. Muswell Hill is mentioned in passing only.
- `forno-hackney` is paired with `columbia-road-flower-market`; the bakery now has three sites.
- `fortitude-bakehouse`: corrected to 35 Colonnade (not Lamb's Conduit Street); opened 2018.
- Facts left out because they could not be confirmed: founding years for Caffè Tropea and the Soho Italian Bear shop, the Cheese Barge's vessel name, Ottolenghi Richmond's opening date, Belle Epoque's garden, Ginger & White's egg dish.
- Websites deliberately omitted where the site was dead or stale: Maggie Jones's, La Patagonia, Schnitzel Heaven, The Hut by the Heath, Original Dubai Shawarma kept its site (draft).
- Places that already had a file, and whole streets or districts such as Brick Lane (§5.6), were skipped.

## Method and caveats

- Each place was checked for open status with dated evidence (reviews, the venue's site, press, and for several the Food Standards Agency and Companies House records), then given an official website and nearest stations.
- Coordinates are postcode centroids from postcodes.io. Other geocoders were blocked from this environment. Each file's coords comment says to spot-check the pin. Weakest pins: Camden Market (Humble Crumble), Kew Green (The Botanist), Russell Square (Caffè Tropea), Finsbury Park Cafe (draft), Palm Court at The Langham, and the Cheese Barge (two postcodes about 80 m apart).
- Station walking times are estimates, not sourced.
- `npm run check` was not run (no shell on the device). Files were validated against the schema fields, tag and type vocabularies, summary length, `pair_with` targets and place links by a local script.
- Several entries rest on one source or moderate evidence (marked in each file's comment): Reenie's, Belle Epoque (newest evidence November 2025), Ottolenghi Richmond, The Botanist, Taste Croatia, Kappacasein. Schnitzel Heaven's earlier company entities were dissolved; the venue is public with that flag in its comment.
- Several entries are plain recommendations the team has not visited; they follow §7 but are not first-hand write-ups.

## Follow-ups

- Run `npm run check`, spot-check the pins above, then review and push.
- `tamil-prince`: add `pair_with: [tamil-crown]` and update its comment (it says the Tamil Crown is not yet a place file). Not changed here because it belongs to another session.
- Confirm the five drafts before publishing.
- Café Japan: its listed hours conflict between sources; the file gives none.
