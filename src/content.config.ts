import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';
import { TYPES, BADGES, TAGS, STATUSES, PRECISIONS } from './lib/vocab.mjs';

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
      badge: z.enum(keys(BADGES)),
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
const trails = defineCollection({
  loader: glob({ pattern: '*.md', base: './content/trails' }),
  schema: z.object({
    title: z.string(),
    summary: z.string().max(200),
    themes: z.array(slug).default([]),
    mode: z.enum(['walk', 'transit', 'mixed']),
    duration: z.string(),
    stops: z.array(z.object({ place: slug, note: z.string().optional() })).min(2),
    visibility: z.enum(['draft', 'public']),
  }),
});

export const collections = { places, themes, trails };
