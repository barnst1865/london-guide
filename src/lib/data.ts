import { getCollection, type CollectionEntry } from 'astro:content';
import fs from 'node:fs';
import path from 'node:path';
import { load as loadYaml } from 'js-yaml';
import { TYPES, BADGES } from './vocab.mjs';

export type Place = CollectionEntry<'places'>;
export type Theme = CollectionEntry<'themes'>;
export type Trail = CollectionEntry<'trails'>;

export interface SiteConfig {
  title: string;
  tagline: string;
  showWishlist: boolean;
}

export const site: SiteConfig = loadYaml(
  fs.readFileSync(path.join(process.cwd(), 'content', 'site.yaml'), 'utf8'),
) as SiteConfig;

/** Drafts are visible when running `npm run dev` (so you can review them) but never in a build. */
export const SHOW_DRAFTS = import.meta.env.DEV;

const visible = (v: string) => SHOW_DRAFTS || v === 'public';

let cache: Promise<{ places: Place[]; themes: Theme[]; trails: Trail[] }> | undefined;

/** All content that should appear on the site, after cross-reference validation. */
export function loadAll() {
  cache ??= (async () => {
    const allPlaces = await getCollection('places');
    const allThemes = await getCollection('themes');
    const allTrails = await getCollection('trails');
    validate(allPlaces, allThemes, allTrails);

    const places = allPlaces
      .filter((p) => visible(p.data.visibility))
      .filter((p) => site.showWishlist || p.data.badge !== 'wishlist')
      .filter((p) => p.data.status !== 'closed')
      .sort((a, b) => a.data.name.localeCompare(b.data.name));
    const themes = allThemes
      .filter((t) => visible(t.data.visibility))
      .sort((a, b) => a.data.order - b.data.order);
    const placeIds = new Set(places.map((p) => p.id));
    const trails = allTrails
      .filter((t) => visible(t.data.visibility))
      // a trail only shows if every stop is visible
      .filter((t) => t.data.stops.every((s) => placeIds.has(s.place)));
    return { places, themes, trails };
  })();
  return cache;
}

/** Fail the build loudly on broken references (§6.4). */
function validate(places: Place[], themes: Theme[], trails: Trail[]) {
  const errors: string[] = [];
  const themeIds = new Set(themes.map((t) => t.id));
  const placeIds = new Set(places.map((p) => p.id));
  for (const p of places) {
    for (const t of p.data.themes)
      if (!themeIds.has(t)) errors.push(`places/${p.id}.md: unknown theme "${t}"`);
    for (const s of p.data.pair_with)
      if (!placeIds.has(s)) errors.push(`places/${p.id}.md: pair_with "${s}" is not a place`);
  }
  for (const t of themes)
    for (const s of t.data.featured)
      if (!placeIds.has(s)) errors.push(`themes/${t.id}.md: featured "${s}" is not a place`);
  for (const tr of trails) {
    for (const s of tr.data.stops)
      if (!placeIds.has(s.place)) errors.push(`trails/${tr.id}.md: stop "${s.place}" is not a place`);
    for (const t of tr.data.themes)
      if (!themeIds.has(t)) errors.push(`trails/${tr.id}.md: unknown theme "${t}"`);
  }
  if (errors.length) throw new Error('Content validation failed:\n  ' + errors.join('\n  '));
}

/** Prefix a site path with the deploy base (e.g. /london-guide/). */
export function u(p = '') {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  return `${base}/${p.replace(/^\//, '')}`;
}

export const typeInfo = (t: string) => TYPES[t as keyof typeof TYPES];
export const badgeInfo = (b: string) => BADGES[b as keyof typeof BADGES];

/** Compact data for the map (no body text). Imprecise locations get no directions link. */
export function toMapPoint(p: Place, themes: Theme[]) {
  const d = p.data;
  return {
    id: p.id,
    name: d.name,
    type: d.type,
    typeLabel: typeInfo(d.type).single,
    color: typeInfo(d.type).color,
    themes: d.themes,
    themeTitles: d.themes.map((t) => themes.find((x) => x.id === t)?.data.short ?? t),
    badge: d.badge,
    badgeLabel: badgeInfo(d.badge).label,
    tags: d.tags,
    summary: d.summary,
    area: d.area,
    lat: d.coords[0],
    lng: d.coords[1],
    precise: d.location_precision === 'exact',
    draft: d.visibility === 'draft',
    url: u(`places/${p.id}/`),
  };
}

export function directionsUrl(p: Place) {
  if (p.data.location_precision !== 'exact') return undefined;
  if (p.data.google_maps_url) return p.data.google_maps_url;
  const [lat, lng] = p.data.coords;
  return `https://www.google.com/maps/dir/?api=1&destination=${lat},${lng}`;
}

export function priceLabel(price: number | string | undefined, type: string) {
  if (price === undefined) return undefined;
  if (typeof price === 'string') return price;
  if (price === 0) return 'Free';
  return '£'.repeat(price);
}
