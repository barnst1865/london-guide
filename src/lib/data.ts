import { getCollection, type CollectionEntry } from 'astro:content';
import fs from 'node:fs';
import path from 'node:path';
import { load as loadYaml } from 'js-yaml';
import { TYPES, BADGES } from './vocab.mjs';

export type Place = CollectionEntry<'places'>;
export type Theme = CollectionEntry<'themes'>;
export type Trail = CollectionEntry<'trails'>;
export type Guide = CollectionEntry<'guides'>;
export type TrailStop = Trail['data']['stops'][number];

export interface SiteConfig {
  title: string;
  tagline: string;
  /** Theme ids shown as the large "Start here" row on the home page. */
  startHere?: string[];
  /** Minimum public places before a theme shows on the home page. */
  minThemePlaces?: number;
  /** Hand-picked "Family favourites" for the home page, each with a one-line reason. */
  homeFavourites?: { place: string; why?: string }[];
}

export const site: SiteConfig = loadYaml(
  fs.readFileSync(path.join(process.cwd(), 'content', 'site.yaml'), 'utf8'),
) as SiteConfig;

/** Drafts are visible when running `npm run dev` (so you can review them) but never in a build. */
export const SHOW_DRAFTS = import.meta.env.DEV;

const visible = (v: string) => SHOW_DRAFTS || v === 'public';

interface AllContent {
  places: Place[];
  themes: Theme[];
  trails: Trail[];
  guides: Guide[];
}
let cache: Promise<AllContent> | undefined;

/** All content that should appear on the site, after cross-reference validation. */
export function loadAll() {
  cache ??= (async () => {
    const allPlaces = await getCollection('places');
    const allThemes = await getCollection('themes');
    const allTrails = await getCollection('trails');
    const allGuides = await getCollection('guides');
    validate(allPlaces, allThemes, allTrails, allGuides);

    const places = allPlaces
      .filter((p) => visible(p.data.visibility))
      .filter((p) => p.data.status !== 'closed')
      .sort((a, b) => a.data.name.localeCompare(b.data.name));
    const placeIds = new Set(places.map((p) => p.id));
    const themes = allThemes
      .filter((t) => visible(t.data.visibility))
      .sort((a, b) => a.data.order - b.data.order);
    const trails = allTrails
      .filter((t) => visible(t.data.visibility))
      // a trail shows only if every required stop is visible; hidden optional stops are dropped
      .filter((t) => t.data.stops.every((s) => !s.place || s.optional || placeIds.has(s.place)))
      .map((t) => ({ ...t, data: { ...t.data, stops: t.data.stops.filter((s) => !s.place || placeIds.has(s.place)) } }));
    const guides = allGuides
      .filter((g) => visible(g.data.visibility))
      .sort((a, b) => a.data.order - b.data.order || a.data.title.localeCompare(b.data.title));
    return { places, themes, trails, guides };
  })();
  return cache;
}

/** Fail the build loudly on broken references (§6.8). */
function validate(places: Place[], themes: Theme[], trails: Trail[], guides: Guide[]) {
  const errors: string[] = [];
  const themeIds = new Set(themes.map((t) => t.id));
  const placeIds = new Set(places.map((p) => p.id));
  const badTheme = (file: string, ids: string[]) =>
    ids.forEach((t) => !themeIds.has(t) && errors.push(`${file}: unknown theme "${t}"`));
  const badPlace = (file: string, field: string, ids: string[]) =>
    ids.forEach((s) => !placeIds.has(s) && errors.push(`${file}: ${field} "${s}" is not a place`));

  for (const p of places) {
    badTheme(`places/${p.id}.md`, p.data.themes);
    badPlace(`places/${p.id}.md`, 'pair_with', p.data.pair_with);
  }
  for (const t of themes) badPlace(`themes/${t.id}.md`, 'featured', t.data.featured);
  for (const tr of trails) {
    const f = `trails/${tr.id}.md`;
    badTheme(f, tr.data.themes);
    badPlace(f, 'stop', tr.data.stops.flatMap((s) => (s.place ? [s.place] : [])));
    const stopIds = new Set(tr.data.stops.map((s) => s.place));
    const stopNames = new Set(tr.data.stops.flatMap((s) => [s.place, s.waypoint].filter(Boolean)));
    for (const v of tr.data.variants) {
      if (v.ends_at && !stopIds.has(v.ends_at)) errors.push(`${f}: variant "${v.name}" ends_at "${v.ends_at}" is not a stop on this trail`);
      if (v.branches_at && !stopNames.has(v.branches_at)) errors.push(`${f}: variant "${v.name}" branches_at "${v.branches_at}" is not a stop or waypoint on this trail`);
    }
  }
  for (const g of guides) {
    badTheme(`guides/${g.id}.md`, g.data.themes);
    badPlace(`guides/${g.id}.md`, 'places', g.data.places);
  }
  for (const id of site.startHere ?? [])
    if (!themeIds.has(id)) errors.push(`site.yaml: startHere "${id}" is not a theme`);
  for (const f of site.homeFavourites ?? [])
    if (!placeIds.has(f.place)) errors.push(`site.yaml: homeFavourites "${f.place}" is not a place`);
  if (errors.length) throw new Error('Content validation failed:\n  ' + errors.join('\n  '));
}

/** Prefix a site path with the deploy base (e.g. /london-guide/). */
export function u(p = '') {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  return `${base}/${p.replace(/^\//, '')}`;
}

export const typeInfo = (t: string) => TYPES[t as keyof typeof TYPES];
/** Badge display info, or undefined for places without a badge. */
export const badgeInfo = (b?: string) => (b ? BADGES[b as keyof typeof BADGES] : undefined);

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
    badge: d.badge ?? '',
    badgeLabel: badgeInfo(d.badge)?.label ?? '',
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

/** Map point for a trail waypoint (a named spot that isn't a place file). */
export function waypointPoint(s: TrailStop) {
  return {
    id: `wp-${s.waypoint}`,
    name: s.waypoint!,
    type: 'waypoint',
    typeLabel: 'Waypoint',
    color: '#8a8f98',
    themes: [],
    themeTitles: [],
    badge: '',
    badgeLabel: '',
    tags: [],
    summary: s.note ?? '',
    area: '',
    lat: s.coords![0],
    lng: s.coords![1],
    precise: true,
    draft: false,
    waypoint: true,
    url: '',
  };
}

/**
 * Directions link. Searches by name and street address rather than our pin, so Google Maps
 * takes people to the real entrance even where our coordinates are a postcode centroid.
 * Falls back to the coordinates only when there's no address and the pin is exact.
 * Places pinned only to an area get no directions link.
 */
export function directionsUrl(p: Place) {
  const prec = p.data.location_precision;
  if (prec === 'area') return undefined;
  if (p.data.google_maps_url) return p.data.google_maps_url;
  const base = 'https://www.google.com/maps/dir/?api=1&destination=';
  if (p.data.address) return base + encodeURIComponent(`${p.data.name}, ${p.data.address}`);
  if (prec !== 'exact') return undefined;
  const [lat, lng] = p.data.coords;
  return `${base}${lat},${lng}`;
}

export function priceLabel(price: number | string | undefined, type: string) {
  if (price === undefined) return undefined;
  if (typeof price === 'string') return price;
  if (price === 0) return 'Free';
  return '£'.repeat(price);
}
