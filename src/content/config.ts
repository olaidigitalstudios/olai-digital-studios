import { defineCollection, z } from 'astro:content';

const gamesCollection = defineCollection({
  type: 'data',
  schema: ({ image }) =>
    z.object({
      title: z.string().min(1, 'Title is required'),
      tagline: z.string().max(120, 'Tagline must be under 120 characters'),
      genre: z.string(),
      status: z.enum(['Available Now', 'In Development', 'Early Access']),
      coverImage: image(),
      coverAlt: z.string(),
      featuredOrder: z.number().default(99),
      storeLinks: z
        .array(
          z.object({
            platform: z.enum([
              'google-play',
              'app-store',
              'steam',
              'itch',
              'microsoft-store',
              'web'
            ]),
            label: z.string(),
            url: z.string().optional(),
            primary: z.boolean().default(false)
          })
        )
        .default([])
    })
});

export const collections = {
  games: gamesCollection
};
