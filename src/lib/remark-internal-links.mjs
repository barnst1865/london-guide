// Lets content link to other pages without worrying about the site's base path:
//   [the Cheshire Cheese](place:ye-olde-cheshire-cheese)   [pubs](theme:historic-pubs)
//   [the WMD Tour](trail:wmd-tour)                         [pub etiquette](guide:pub-etiquette)
// The build fails if the target file doesn't exist (§6.8).
import fs from 'node:fs';
import path from 'node:path';

const KINDS = { place: 'places', theme: 'themes', trail: 'trails', guide: 'guides' };

export default function remarkInternalLinks({ base = '/' } = {}) {
  const prefix = base.replace(/\/$/, '');
  return (tree, file) => {
    const walk = (node) => {
      if (node.type === 'link' && typeof node.url === 'string') {
        const m = node.url.match(/^(place|theme|trail|guide):([a-z0-9-]+)$/);
        if (m) {
          const [, kind, id] = m;
          const dir = KINDS[kind];
          if (!fs.existsSync(path.join(process.cwd(), 'content', dir, `${id}.md`))) {
            throw new Error(`Broken link "${node.url}" in ${file.path ?? 'content'}: content/${dir}/${id}.md does not exist`);
          }
          node.url = `${prefix}/${dir}/${id}/`;
        }
      }
      (node.children || []).forEach(walk);
    };
    walk(tree);
  };
}
