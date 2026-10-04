# 2026-10-04: Master, fixes from the site review

An outside review of the live site made six priority recommendations and some smaller ones. This session made the site-side fixes and drafted prompts for the rest (`planning/session-prompts.md`, "Post-review sessions").

## Done

- **Trail maps.**
  - The line now runs only through required stops and waypoints.
  - Optional stops within 1.5 km get a dotted spur from the previous main-route stop; ones further out are marked but not joined.
  - Alternative endings get a dashed line from their new `branches_at` stop. On the Thames Path, the long version now branches at the National Archives instead of joining Kew Gardens to Kew Green.
  - Markers are numbered to match the stop list, and each map has a caption saying the line is a rough guide.
  - New `path_only` waypoints let trail sessions bend the line along the real path (§5.3a, §6.3).
- **Directions.**
  - The link now searches Google Maps by the place's name and address instead of our pin, so a postcode-centroid pin no longer sends people to the wrong door.
  - Places at `street` precision with an address now get directions too; `area` places still don't.
- **Map filters.**
  - The theme dropdown lists only themes that have public places.
  - An empty result says so.
  - A line under the map points to the list views.
  - The empty Spies map from the review doesn't happen with the current build (21 places show); it was probably an older deploy.
- **Old London.** The blurb now matches what's there (a Saxon arch, a Tudor gatehouse, the Great Fire and the gallows) instead of promising Roman walls and Templar churches.
- **Getting around.** Added a "Traveling with kids?" paragraph near the top, checked against TfL's Visitor Shop comparison page:
  - under-11s travel free;
  - 11–15s get the Young Visitor discount (half price for 14 days) only on a Visitor Oyster, added by staff after arrival;
  - everyone 11 and over needs their own card or phone.

  The "skip the Oyster" advice is now for adults only.
- **Narrow phones.** Card grids can shrink below their minimum width (`minmax(min(…, 100%), 1fr)`). Checked at 320 px: no horizontal scroll.
- **Navigation and home.**
  - The first nav item is now "Home".
  - The home page has quick links under the welcome: Explore the map, Before you visit, Walks and trails, and Moving here once a Living here guide is public.
- **Family favourites.**
  - New `homeFavourites` list in `site.yaml` (`place` + `why`), with the current favourites listed in a comment.
  - Until the family fills it in, the home page falls back to the first six favourites.
  - Added an "All favourites on the map" link.
- **Accessibility.** Visible keyboard focus outlines and a "Skip to content" link.
- **Occasions.**
  - New optional `occasions` field on places: `breakfast-brunch`, `quick-lunch`, `cheap-cheerful`, `dinner-with-friends`, `sunday-roast`, `afternoon-tea` and `special-occasion`.
  - Theme pages show a "Pick by occasion" section once places use it. Nothing is tagged yet; that's the eating-by-occasion session.

## Not done, on purpose

- **Closure badges on cards and markers.** Our rule moves temporarily closed places to draft (decision 15), so nothing closed shows on cards or the map.
- **Real walking routes.** No routing service is reachable from the cloud workspace. `path_only` waypoints are the manual route instead.

## Checks

- The build passes (272 pages).
- Screenshots of the Thames and WMD trail maps, the Spies map filter and the home page at 320 px all look right. Map tiles don't load in the cloud workspace, so the screenshots show lines and markers only.
- An occasions test render worked and was reverted.

## Next

- **Sessions:**
  - The pin check, which also adds `path_only` waypoints to the trails.
  - Eating by occasion.
  - Home-page favourites (short).
- **Family:**
  - Fill in `homeFavourites`.
  - Review the theme intros and the home-page welcome.
