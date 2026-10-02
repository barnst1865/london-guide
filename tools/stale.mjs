// Lists places whose facts haven't been checked in 12+ months (or never). Usage: npm run stale
import fs from 'node:fs';
import path from 'node:path';
import { load } from 'js-yaml';

const dir = path.join(process.cwd(), 'content', 'places');
const cutoff = new Date();
cutoff.setFullYear(cutoff.getFullYear() - 1);
const rows = [];
for (const f of fs.readdirSync(dir).filter((f) => f.endsWith('.md'))) {
  const m = fs.readFileSync(path.join(dir, f), 'utf8').match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!m) continue;
  const d = load(m[1]) || {};
  const lv = d.last_verified ? new Date(d.last_verified) : null;
  if (!lv || lv < cutoff) rows.push([lv ? lv.toISOString().slice(0, 10) : 'never     ', d.visibility, f.replace(/\.md$/, '')]);
}
rows.sort((a, b) => a[0].localeCompare(b[0]));
console.log(rows.length ? rows.map((r) => r.join('  ')).join('\n') : 'Everything has been verified in the last 12 months.');
console.log(`\n${rows.length} place(s) need checking.`);
