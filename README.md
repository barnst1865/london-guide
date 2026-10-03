# Where We'd Take You in London

A personal guide to London for our visiting friends and family: themes, a map, and trails, built with [Astro](https://astro.build) and [Leaflet](https://leafletjs.com) and published with GitHub Pages.

Project rules, content schema and workflow: **[PROJECT_INSTRUCTIONS.md](PROJECT_INSTRUCTIONS.md)**.

## Run it locally

Needs [Node.js](https://nodejs.org) 22 or newer.

```bash
npm install
npm run dev      # http://localhost:4321/london-guide/ (shows drafts, with a yellow banner)
npm run check    # full build; fails on any invalid content file
npm run stale    # places and guides whose facts haven't been checked in 12+ months
```

## Add a place

1. Copy any file in `content/places/` to `content/places/<new-slug>.md` (lowercase, hyphens).
2. Fill in the front matter (see PROJECT_INSTRUCTIONS.md §6.1) and write the description.
3. Leave `visibility: draft` until it's checked; then set `visibility: public` and `last_verified: <today>`.
4. `npm run check`, commit, push. Pushing to `main` publishes the site.

## Folder map

| Folder | What's in it |
|---|---|
| `content/places/` | One Markdown file per place |
| `content/themes/` | One file per theme (title, colour, intro) |
| `content/trails/` | Ordered routes through several places |
| `content/site.yaml` | Site settings (`showWishlist`, home-page `startHere` themes) |
| `content/guides/` | Written guides and essays (Practical London, Around town, Essays, Living here) |
| `src/` | Site code (layouts, pages, map) |
| `planning/` | Backlog, session logs, change requests |
| `sources/` | Private raw material (git-ignored) |
| `tools/` | Helper scripts |
