// @ts-check
import { defineConfig } from 'astro/config';

// Published at https://barnst1865.github.io/london-guide/
// If you move to a custom domain, set `site` to it and remove `base`.
export default defineConfig({
  site: 'https://barnst1865.github.io',
  base: '/london-guide',
  trailingSlash: 'always',
  devToolbar: { enabled: false },
});
