# Claude: read this first

This repo is **Where We'd Take You in London**, a family guide to London for visiting friends and family.

**Before doing anything, read `PROJECT_INSTRUCTIONS.md`.** It's the single source of truth: privacy rules (§3), content schema (§6), writing style (§7), fact-checking (§8), and how master vs. topic sessions divide the work (§10).

Quick rules:
- One place = one file in `content/places/<slug>.md`; guides live in `content/guides/`. New content starts with `visibility: draft`.
- Link between pages with `[text](place:slug)`, `theme:`, `trail:` or `guide:`, never hand-written paths (§6.6).
- The site is browse-first: no planners, quizzes or checklists (§2).
- Topic sessions edit `content/` and `planning/` only, never `src/` or the schema; put requests in `planning/requests.md`.
- Never commit anything identifying our family, where we live, or our work (§3). Raw sources go in git-ignored `sources/`.
- Run `npm run check` before finishing; it fails on invalid content.
- Skim `planning/ideas.md` at the start. Log each session in `planning/sessions/` and update `planning/backlog.md`.
