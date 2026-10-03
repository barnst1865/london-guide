// Controlled vocabularies. Changing these lists is a master-session job (see PROJECT_INSTRUCTIONS.md §5).
// Theme ids are NOT listed here: a theme exists when content/themes/<id>.md exists.

export const TYPES = {
  'historic-site': { label: 'Historic sites', single: 'Historic site', color: '#8a5a2b' },
  museum: { label: 'Museums', single: 'Museum', color: '#2f6f8f' },
  church: { label: 'Churches', single: 'Church', color: '#6b5b95' },
  pub: { label: 'Pubs', single: 'Pub', color: '#b5452f' },
  bar: { label: 'Bars', single: 'Bar', color: '#a13d6b' },
  restaurant: { label: 'Restaurants', single: 'Restaurant', color: '#c77d1a' },
  cafe: { label: 'Cafés', single: 'Café', color: '#9a7b4f' },
  'quick-bite': { label: 'Quick bites', single: 'Quick bite', color: '#d4699a' },
  'market-shop': { label: 'Markets & shops', single: 'Market / shop', color: '#4f8a3c' },
  'park-walk': { label: 'Parks & walks', single: 'Park / walk', color: '#2e7d5b' },
  entertainment: { label: 'Entertainment', single: 'Entertainment', color: '#d0532c' },
  'sport-venue': { label: 'Sport', single: 'Sport venue', color: '#1f7a8c' },
  viewpoint: { label: 'Viewpoints', single: 'Viewpoint', color: '#3d5a99' },
  tour: { label: 'Tours', single: 'Tour', color: '#7a6a2e' },
  'day-trip': { label: 'Day trips', single: 'Day trip', color: '#556270' },
};

export const BADGES = {
  favourite: { label: '★ Family favourite', short: 'Favourite' },
  like: { label: 'We like it', short: 'We like it' },
  tip: { label: 'Trusted tip', short: 'Trusted tip' },
  wishlist: { label: 'On our list', short: 'On our list' },
};

export const TAGS = {
  'kid-friendly': 'Kid-friendly',
  'teen-appeal': 'Teens will like it',
  'dog-friendly': 'Dog-friendly',
  free: 'Free',
  'booking-essential': 'Book ahead',
  'rainy-day': 'Rainy day',
  outdoors: 'Outdoors',
  'step-free': 'Step-free',
  'late-night': 'Late night',
  seasonal: 'Seasonal',
  'quick-visit': 'Under an hour',
  'half-day': 'Half a day',
  'group-friendly': 'Good for groups',
  sunday: 'Good on a Sunday',
};

export const STATUSES = ['open', 'seasonal', 'closed', 'temporarily-closed'];
export const PRECISIONS = ['exact', 'street', 'area'];

// Guide groups, in the order they appear on the Guides page (§5.6).
export const GUIDE_GROUPS = {
  practical: { label: 'Practical London', blurb: 'How to get around, eat out and fit in.' },
  area: { label: 'Around town', blurb: "What's actually good in the busiest parts of town." },
  essay: { label: 'Essays', blurb: 'Longer reads on the things we love about London.' },
  'living-here': { label: 'Living here', blurb: 'For people moving to London rather than visiting.' },
};
