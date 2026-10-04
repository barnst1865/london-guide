# 2026-10-04: Google Maps triage, finish and hand off (launch plan Session #1)

Worked only in the private triage file and a private handoff note in `sources/triage/`. No place files were written.

## Done

- **Area labels:** all 108 flagged labels checked and the flags cleared; about half needed a new label. Broad bucket labels on another 110 or so included rows were replaced with the actual neighbourhood. Coordinates are still approximate: geocode from the address when writing a place file (§8).
- **Deferred spy sites:** the 11 rows stay undecided for the Spies & Cold War session. Each now has a §3 note saying whether it is a private home (area or street level only), an official building, or a public venue.
- **Themes:** the film and music landmark rows moved to the new `on-screen-on-record` theme, and the literary and artistic ones to `writers-artists-makers`, as the master session decided. Exteriors that are private homes or offices carry a street-level-only note. The few remaining unthemed rows were placed in existing themes.
- **Badges:** family decision that the only badge is `favourite`. 17 places are confirmed favourites; every other included place has no badge. The old values are kept in the private notes, because they record whether we have been.
- **Last two unthemed rows settled:** a members-only club stays in as a walk-by with a note on its history (now in `only-in-london`); a touristy shopping street is skipped.
- **Tidying:** type and theme values in the triage file now match the ids in §5.1 and §5.2.
- **Handoff:** `sources/triage/handoff.md` (private) lists every included row under each of its themes, with type, area, our angle and things to check, plus open questions per theme. `historic-pubs` and `eat` come first.

## Counts

503 rows: 205 include, 157 skip, 141 undecided on purpose (130 day trips, 11 spy sites).

## Not done, on purpose

- **Day trips are parked** until the site is live. Nothing was decided; a first batch was discussed but not agreed.
- Whether we have visited each historic pub was left to the Historic Pubs & Restaurants session.

## For the master session

Six new requests in `planning/requests.md`. The first matters before any theme session writes place files: the schema still requires one of four badges, and the family now wants `favourite` only.

## Files changed

- `sources/triage/google-maps-triage.csv` (private, git-ignored)
- `sources/triage/handoff.md` (private, git-ignored, new)
- `planning/requests.md`
- `planning/backlog.md`
- `planning/sessions/2026-10-04-google-maps-triage-handoff.md` (this file)
