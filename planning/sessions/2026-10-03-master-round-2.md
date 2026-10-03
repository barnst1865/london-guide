# 2026-10-03: Master — site build round 2

Built from the family ideas list (`planning/ideas.md`):

- **Browse-first home page** (#14–#16): "Start here" themes (set by `startHere` in `content/site.yaml`), the other themes as a compact list, featured trails, featured guides, a map teaser with type chips, and family favourites. Principle added as §2.7.
- **Guides section** (#17, #19–#22): new `content/guides/` collection (§5.6, §6.5) in four groups: Practical London, Around town, Essays, Living here. Seven draft outlines added. `/practical/` now redirects to the Guides page. The nav item "Practical London" became "Guides".
- **Internal links** (§6.6): `[text](place:slug)` and similar, checked at build time.
- **"Our kids" quote** (#3): optional `kids_say` on places.
- **Richer trails** (#24): segments, optional stops, waypoints and variants (§6.3).
- **New theme** `only-in-london` (#13).
- Checked the 16 `eat` research drafts: they all pass validation. They're `wishlist`, so they stay hidden until visited.
- `npm run stale` now covers guides too.
- PROJECT_INSTRUCTIONS.md is now v0.4.

## Housekeeping for the user (Claude can't delete files on this computer)
- Delete `content/practical.md` (replaced by the guides).
- Delete the `setup/` folder (the workflow file now lives in `.github/workflows/`).

## Next candidates
- Theme sessions: historic-pubs (5 seeds), spies-cold-war (WMD tour), and finish verifying the eat drafts.
- Write the Practical London guides (quick wins with high value for visitors).
- Parked features: "near me", search, printable trails, photos.
