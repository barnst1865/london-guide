# 2026-10-04: Master, quick-listings integration

Checked and integrated the output of Listings A, B and C.

## Results

- **Build:** passes. 253 place files, 229 public; 271 pages built.
- **Triage CSV:** the `place_file` column is now filled for every `include` row with London scope (140 rows filled this session: 92 from `listings-B.md` / `listings-C.md`, 48 matched to place files written before the listing sessions). Every other column is unchanged; BOM and CRLF kept.
- **Coverage gaps:**
  - Hijazi Corner (GM191, scope `london?`, trading unconfirmed) has no place file. Listings B only took rows with scope `london`.
  - Brick Lane (GM502) and Berwick Street (GM186) are whole streets, so they wait for area guides (§5.6).
- **Theme intros:** seven themes now have 3+ public places, so they appear on the home page. Each was showing the "still writing" placeholder, so the master drafted a short intro for each from its public places. Family to edit:
  - `markets-food-shops`
  - `on-screen-on-record`
  - `only-in-london`
  - `play-games-music`
  - `science-curious`
  - `transit-hidden-city`
  - `writers-artists-makers`

  `day-trips` and `sport` still have no places and stay off the home page.

## Audit

- **Privacy scan of the new files:** clean. The hits were place and street names (St Mary's, St John's Wood, the Ragged School and so on).
- **Placeholders:** none in public places. Review comments are stripped from pages at build time.
- **Shared pins** (both expected; the map clusters them):
  - The Prince's Head and the Cricketers share one Richmond Green postcode centroid.
  - The American Bar and Simpson's in the Strand are both in the Savoy building.
- **Caper addresses:** the three Great Muppet Caper files are public with full building addresses. That is against the default rule in §3. Listings C says the owner approved it (see `requests.md`). The master has not written an exception into PROJECT_INSTRUCTIONS.md and is asking the owner to confirm directly.

## Open

- Owner: confirm or reverse the Caper address exception.
- Family: review the seven new intros, plus the three from the pre-launch review and the home-page welcome.
- Hijazi Corner: confirm it is trading, then add a quick listing.
