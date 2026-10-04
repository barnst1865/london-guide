import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';
import { TYPES, TAGS, STATUSES, PRECISIONS, GUIDE_GROUPS } from './lib/vocab.mjs';

const keys = (o: Record<string, unknown>) => Object.keys(o) as [string, ...string[]];
const slug = z.string().regex(/^[a-z0-9]+(-[a-z0-9]+)*$/, 'must be lowercase-hyphenated');

// One file per place: content/places/<slug>.md  (schema: PROJECT_INSTRUCTIONS.md §6.1)
const places = defineCollection({
  loader: glob({ pattern: '*.md', base: './content/places' }),
  schema: z
    .object({
      name: z.string().min(1),
      type: z.enum(keys(TYPES)),
      themes: z.array(slug).min(1),
      // Only `favourite` (§5.4). Leftover like / tip / wishlist values fail the build so they get cleaned up.
      badge: z
        .string()
        .refine((b) => b === 'favourite', {
          message: "badge can only be 'favourite' (or leave it out). like / tip / wishlist were retired on 2026-10-04",
        })
        .optional(),
      tags: z.array(z.enum(keys(TAGS))).default([]),
      price: z.union([z.number().int().min(0).max(4), z.string()]).optional(),
      summary: z.string().min(1).max(160),
      area: z.string().min(1),
      address: z.string().optional(),
      coords: z.tuple([z.number().min(49).max(56), z.number().min(-6).max(2)]),
      location_precision: z.enum(PRECISIONS as [string, ...string[]]),
      stations: z.array(z.string()).default([]),
      website: z.string().url().optional(),
      google_maps_url: z.string().url().optional(),
      pair_with: z.array(slug).default([]),
      status: z.enum(STATUSES as [string, ...string[]]),
      visibility: z.enum(['draft', 'public']),
      last_verified: z.coerce.date().optional(),
      sources: z.array(z.string()).default([]),
      // Optional one-liner from our kids, shown as a quote. No names or ages (§3).
      kids_say: z.string().max(140).optional(),
    })
    .refine((d) => d.visibility === 'draft' || d.last_verified, {
      message: 'public places must have last_verified (facts checked before publishing)',
      path: ['last_verified'],
    }),
});

// content/themes/<id>.md  (§6.2)
const themes = defineCollection({
  loader: glob({ pattern: '*.md', base: './content/themes' }),
  schema: z.object({
    title: z.string(),
    short: z.string(),
    order: z.number(),
    icon: z.string().optional(),
    color: z.string().regex(/^#[0-9a-fA-F]{6}$/),
    featured: z.array(slug).default([]),
    blurb: z.string().max(140),
    visibility: z.enum(['draft', 'public']).default('public'),
  }),
});

// content/trails/<id>.md  (§6.3)
// A stop is either a place (by slug) or a waypoint (a named point with coords, e.g. a bridge crossing).
const coords = z.tuple([z.number().min(49).max(56), z.number().min(-6).max(2)]);
const stop = z
  .object({
    place: slug.optional(),
    waypoint: z.string().optional(),
    coords: coords.optional(),
    note: z.string().optional(),
    optional: z.boolean().default(false),   // shown as an optional detour
    segment: z.string().optional(),         // starts a new named section of the trail at this stop
  })
  .refine((s) => (s.place ? !s.waypoint && !s.coords : !!s.waypoint && !!s.coords), {
    message: 'each stop needs either `place`, or `waypoint` + `coords` (not both)',
  });

const trails = defineCollection({
  loader: glob({ pattern: '*.md', base: './content/trails' }),
  schema: z.object({
    title: z.string(),
    summary: z.string().max(200),
    themes: z.array(slug).default([]),
    mode: z.enum(['walk', 'transit', 'mixed']),
    duration: z.string(),
    stops: z.array(stop).min(2),
    // Ways to shorten or extend the trail, e.g. { name: "Short version", description: "...", ends_at: white-hart-barnes }
    variants: z
      .array(z.object({ name: z.string(), description: z.string(), ends_at: slug.optional() }))
      .default([]),
    featured: z.boolean().default(false),   // shown on the home page
    tags: z.array(z.enum(keys(TAGS))).default([]),
    visibility: z.enum(['draft', 'public']),
  }),
});

// content/guides/<id>.md  (§5.6, §6.5): standalone written guides and essays.
const guides = defineCollection({
  loader: glob({ pattern: '*.md', base: './content/guides' }),
  schema: z
    .object({
      title: z.string(),
      summary: z.string().max(200),
      group: z.enum(keys(GUIDE_GROUPS)),
      order: z.number().default(100),
      themes: z.array(slug).default([]),      // related themes (links)
      places: z.array(slug).default([]),      // places shown as cards and on a map at the end
      featured: z.boolean().default(false),   // shown on the home page
      visibility: z.enum(['draft', 'public']),
      last_verified: z.coerce.date().optional(),
      sources: z.array(z.string()).default([]),
    })
    .refine((d) => d.visibility === 'draft' || d.last_verified, {
      message: 'public guides must have last_verified (facts checked before publishing)',
      path: ['last_verified'],
    }),
});

export const collections = { places, themes, trails, guides };
