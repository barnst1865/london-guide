# 2026-10-05: Master, move to london.dckoiks.com

- **Domain:** the family chose `london.dckoiks.com`.
  - DNS is a CNAME at Squarespace pointing to `barnst1865.github.io`.
  - The domain is verified in the GitHub account and set as the custom domain in the repo's Pages settings, which the family did.
  - HTTPS is waiting for GitHub's certificate. Tick "Enforce HTTPS" once it's offered.
- **Code:**
  - `astro.config.mjs` now has `site: https://london.dckoiks.com` and `base: '/'`.
  - `404.astro` forwards old `/london-guide/...` paths (which arrive via GitHub's github.io redirect) to the same page without the prefix. Tested in preview.
  - With the site at the domain root, `robots.txt` now sits where crawlers look for it.
- **Docs:**
  - README dev URL updated.
  - PROJECT_INSTRUCTIONS §3 has an "Address" note, plus decision 18.
  - Backlog Site build row updated.
- **Privacy:** discussed before the move. The domain can point back to the family; the family accepted that. The content rules in §3 are unchanged.
