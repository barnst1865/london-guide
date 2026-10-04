# Listings C: smaller themes, quick listings (2026-10-04)

**Goal:** `depth: listing` files (§6.1) for the triage rows with decision include, scope london, and a first proposed theme in on-screen-on-record, kids, science-curious, transit-hidden-city, writers-artists-makers, only-in-london, play-games-music, medieval-old-london or wild-london.

## Added

**39 listings: 38 public, 1 draft.** All `last_verified: 2026-10-04`. Three favourites (London Transport Museum, the V&A, Hamleys), as the triage says.

- Museums and sights (batch 1, 15): `brunel-museum`, `foundling-museum`, `postal-museum`, `london-transport-museum` (★), `ragged-school-museum`, `museum-of-the-home`, `cutty-sark`, `london-canal-museum`, `crystal-palace-museum` (seasonal), `william-morris-gallery`, `garden-museum`, `charles-dickens-museum`, `young-v-and-a`, `victoria-and-albert-museum` (★), `sherlock-holmes-museum`
- Old London, science, shops, music and pubs (batch 2, 14): `tyburn-tree-plaque`, `royal-observatory-prime-meridian` (**draft**), `the-monument`, `enderby-wharf-cable-gear`, `alexandra-palace`, `peter-pan-statue`, `richmond-palace-gatehouse`, `battle-of-barnet-monument`, `lock-and-co-hatters`, `hamleys` (★), `annabels`, `sounds-of-the-universe`, `aint-nothin-but`, `sherlock-holmes-pub`
- Film, TV, music and makers (batch 3, 10): `abbey-road-crossing`, `rickroll-arches-freston-road`, `oval-road-henson-creature-shop`, `jim-henson-blue-plaque`, `westbourne-terrace-happiness-hotel`, `holland-park-highbrow-street`, `chesham-place-lady-holiday`, `admirals-walk`, `benedict-arnold-gloucester-place`, `william-blake-south-molton-street`

Extra `pair_with` links on the new files: Lock & Co. to Berry Bros. & Rudd, the Monument to Leadenhall Market, and the Museum of the Home to Columbia Road Flower Market (all public, from Listings A and B). I did not edit other sessions' files.

The triage ID to slug mapping is in `sources/triage/listings-C.md` (git-ignored). The triage CSV was not touched.

## Decisions

- **Observatory is a draft.** The Royal Observatory's meridian courtyard is closed from 2 Nov 2026 and is due back in summer 2027 (decision 15: temporarily closed means draft). The file has a comment saying so. **When the courtyard reopens:** set it public and add `royal-observatory-prime-meridian` to `cutty-sark`'s `pair_with`.
- **§3 exception, owner-approved.** The three Great Muppet Caper buildings (`westbourne-terrace-happiness-hotel`, `holland-park-highbrow-street`, `chesham-place-lady-holiday`) carry full building addresses in the name and address. The owner walked past them and confirmed the addresses. Each is labelled as a viewing from the street. Pins stay at street or terrace precision except Holland Park, which is exact. See `requests.md`.
- **Berwick Street dropped** (GM186) as a whole street (§5.6).
- **Admiral's Walk** keeps `on-screen-on-record` and `kids`, and the text says plainly that the film connection is thin.
- **Caper trivia** is labelled with "fan sources" or legend wording (§7) where it can't be checked.
- **Folded or already covered:** GM251 (Brunel tunnel) into `brunel-museum`; GM257 is the existing `william-morris-society`; GM289 is the existing `diana-memorial-playground`; GM151 (Palm House) is folded into `kew-gardens`; GM294 is covered by `clifton-nurseries-cafe`.

## How facts were checked

- Eight research agents each checked existence, opening, booking, the nearest station and the official site, writing to JSON. I reviewed their output and rewrote any summary I couldn't support.
- **Claims softened or dropped:** Enderby Wharf's gear is telephone-cable era, not Victorian telegraph; the Diana and Prince Charles Annabel's story was dropped; Lock & Co.'s "oldest" is attributed to the firm; the Foundling "first" claim is softened; the Ragged School lesson is first Sundays only; the Monument's kids' certificate was dropped; Henson's unverified "lived here from 1979" was dropped; Rickroll walking directions were dropped.
- **Coordinates:** Nominatim and Photon were blocked, so pins come from postcodes.io (postcode centroids, no-space postcodes), British Listed Buildings coordinates, and Historic England grid references converted locally. Floor of four decimals on every pin.
- **Privacy (§3):** private-home and film sites use street or area precision with no house numbers, apart from the Caper exception above.

## Coordinate caveats

- **Crystal Palace Museum:** single source.
- **Rickroll arch** (Freston Road): approximate street pin.
- **Westbourne Terrace and Chesham Place:** terrace-centroid pins.
- **Alexandra Palace, Peter Pan statue, Richmond Palace, Battle of Barnet monument:** Historic England grid references.

## To check when previewing (`npm run dev`)

- **William Morris Gallery:** the two pin sources differ by about 145 m.
- **Royal Observatory:** confirm the draft status and closure dates against the official site.
- **Sounds of the Universe:** the shop is a third-party business (Soul Jazz Records); check it still trades.
- **William Blake, South Molton Street:** redevelopment nearby; check news before relying on it.
- **Ragged School:** sources conflict on opening days.
- **Foundling Museum and Garden Museum:** both have had closures; recheck before the family goes.

## Open

- **Berwick Street / Soho:** area-guide candidate (§5.6). Sister Ray, Sounds of the Universe and Ain't Nothin' But could all be cited there.
- **Caper wording:** the family may want to tidy the "fan sources" phrasing.
- **Not run:** `npm run check` (no shell on the linked computer).
