// Lets content link to other pages without worrying about the site's base path:
//   [the Cheshire Cheese](place:ye-olde-cheshire-cheese)   [pubs](theme:historic-pubs)
//   [the WMD Tour](trail:wmd-tour)                         [pub etiquette](guide:pub-etiquette)
// The build fails if the target file doesn't exist (§6.8).
// Also strips <!-- comments --> from Markdown bodies so research notes stay in the repo only.
import fs from 'node:fs';
import path from 'node:path';

const KINDS = { place: 'places', theme: 'themes', trail: 'trails', guide: 'guides' };
// `astro build` = production; `astro dev` keeps every link so drafts can be previewed.
const PRODUCTION = process.argv.includes('build');

/** True if the target file would appear on the published site. */
function isLive(file) {
  const fm = fs.readFileSync(file, 'utf8').match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!fm) return true;
  const vis = fm[1].match(/^visibility:\s*(\w+)/m);
  const status = fm[1].match(/^status:\s*([\w-]+)/m);
  if (vis && vis[1] !== 'public') return false;
  if (status && status[1] === 'closed') return false;
  return true;
}

export default function remarkInternalLinks({ base = '/' } = {}) {
  const prefix = base.replace(/\/$/, '');
  return (tree, file) => {
    const walk = (node) => {
      if (node.type === 'link' && typeof node.url === 'string') {
        const m = node.url.match(/^(place|theme|trail|guide):([a-z0-9-]+)$/);
        if (m) {
          const [, kind, id] = m;
          const dir = KINDS[kind];
          const target = path.join(process.cwd(), 'content', dir, `${id}.md`);
          if (!fs.existsSync(target)) {
            throw new Error(`Broken link "${node.url}" in ${file.path ?? 'content'}: content/${dir}/${id}.md does not exist`);
          }
          node.url = `${prefix}/${dir}/${id}/`;
          // In a production build, a link to a draft (or closed place) would 404, so render it as plain text.
          if (PRODUCTION && !isLive(target)) {
            node.type = 'emphasis'; // keep the words, drop the link
            delete node.url;
            console.warn(`[links] ${path.basename(file.path ?? '')}: "${kind}:${id}" is not public, so it's shown as plain text`);
          }
        }
      }
      (node.children || []).forEach(walk);
    };
    walk(tree);
    // Strip HTML comments (research notes) so they never reach the published pages.
    const strip = (node) => {
      if (!node.children) return;
      node.children = node.children.filter((c) => !(c.type === 'html' && /^\s*<!--[\s\S]*-->\s*$/.test(c.value)));
      node.children.forEach(strip);
    };
    strip(tree);
  };
}
