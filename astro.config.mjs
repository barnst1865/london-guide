// @ts-check
import { defineConfig } from 'astro/config';
import remarkInternalLinks from './src/lib/remark-internal-links.mjs';

// Published at https://barnst1865.github.io/london-guide/
// If you move to a custom domain, set `site` to it and change `base` to '/'.
const base = '/london-guide';

export default defineConfig({
  site: 'https://barnst1865.github.io',
  base,
  trailingSlash: 'always',
  devToolbar: { enabled: false },
  markdown: {
    remarkPlugins: [[remarkInternalLinks, { base }]],
  },
});
