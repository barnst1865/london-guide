# 2026-10-04: Master — favourite-only badges

Request from the Google Maps triage session (family decision): keep only the `favourite` badge.

- Schema: `badge` is optional, and `favourite` is its only allowed value. `like`, `tip` and `wishlist` now fail `npm run check` with a clear message.
- Site code: cards, place pages and map popups show a badge only for favourites. The map's "Favourites only" filter and the home page's "Family favourites" row are unchanged.
- Retired the `showWishlist` switch in `content/site.yaml` and the code that hid wishlist places. Places we haven't vetted stay at `visibility: draft` instead.
- Migrated all 27 place files: removed the `badge:` line (none were favourites). All still `visibility: draft`.
- Docs: PROJECT_INSTRUCTIONS.md §2.3, §5, §5.4, §6.1, §6.7, §6.8, §9.2, §10.3, §11, §13; README; launch plan; backlog.
- Proposed (awaiting confirmation): how to stay honest about places we haven't visited (see `planning/requests.md`).
- Then decided with the user: recommendations come from us and trusted friends and colleagues, without claiming we've visited everything (§2.3); `markets-food-shops` retitled "Markets & Shops"; streets and districts become "Around town" area guides (§5.6). Footer text updated to match. Two day-trip questions stay open until after launch.
