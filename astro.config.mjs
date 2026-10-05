// @ts-check
import { defineConfig } from 'astro/config';
import remarkInternalLinks from './src/lib/remark-internal-links.mjs';

// Published at https://london.dckoiks.com/ (GitHub Pages custom domain, set in the repo's
// Settings → Pages; DNS is a CNAME at Squarespace pointing to barnst1865.github.io).
// Until 2026-10-05 the site lived at https://barnst1865.github.io/london-guide/; the 404 page
// forwards old /london-guide/... links to the same page here.
const base = '/';

export default defineConfig({
  site: 'https://london.dckoiks.com',
  base,
  trailingSlash: 'always',
  devToolbar: { enabled: false },
  markdown: {
    remarkPlugins: [[remarkInternalLinks, { base }]],
  },
});
