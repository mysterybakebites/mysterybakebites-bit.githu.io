/*
 * Mystery Bakebite custom cake configuration.
 *
 * This is deliberately separate from the renderer so the bakery can change
 * active options, labels and prices without duplicating tier UI code. Prices
 * already present here are starting prices from the supplied cake menu; use
 * pricing_type: "custom_quote" for work that needs baker review.
 */
window.MB_CAKE_CONFIG = {
  structures: [
    { id: 'one-layer', name: '1 Layer Cake', description: 'One cake layer with your chosen shape and finish.' },
    { id: 'one-tier', name: '1 Tier Cake', description: 'One cake tier with selectable internal cake layers.' },
    { id: 'two-tier', name: '2 Tier Cake', description: 'Two separate cake tiers stacked together.' },
    { id: 'three-tier', name: '3 Tier Cake', description: 'Bottom, middle and top tiers for a statement cake.' },
    { id: 'four-tier', name: '4 Tier Cake', description: 'Bottom, lower-middle, upper-middle and top tiers.' },
    { id: 'custom', name: 'Custom Cake / Quote', description: 'For unusual designs that need a baker review and quote.' }
  ],
  shapes: [
    { id: 'round', name: 'Round', pricing_type: 'included', price: 0 },
    { id: 'square', name: 'Square', pricing_type: 'included', price: 0 },
    { id: 'rectangle', name: 'Rectangle', pricing_type: 'included', price: 0 },
    { id: 'heart', name: 'Heart', pricing_type: 'included', price: 0 },
    { id: 'number', name: 'Number', pricing_type: 'custom_quote', price: null },
    { id: 'letter', name: 'Letter', pricing_type: 'custom_quote', price: null }
  ],
  sizes: [
    { id: '4', name: '4"', description: 'Bento size', category: 'size', pricing_type: 'base_price', price: 120, active: true, sort_order: 1 },
    { id: '5', name: '5"', description: 'Serves 6–8', category: 'size', pricing_type: 'base_price', price: 150, active: true, sort_order: 2 },
    { id: '6', name: '6"', description: 'Serves 8–12', category: 'size', pricing_type: 'base_price', price: 220, active: true, sort_order: 3 },
    { id: '7', name: '7"', description: 'Serves 12–16', category: 'size', pricing_type: 'base_price', price: 280, active: true, sort_order: 4 },
    { id: '8', name: '8"', description: 'Serves 16–22', category: 'size', pricing_type: 'base_price', price: 350, active: true, sort_order: 5 },
    { id: '9', name: '9"', description: 'Baker confirms size quote', category: 'size', pricing_type: 'custom_quote', price: null, active: true, sort_order: 6 },
    { id: '10', name: '10"', description: 'Serves 25–32', category: 'size', pricing_type: 'base_price', price: 650, active: true, sort_order: 7 },
    { id: '12', name: '12"', description: 'Serves 35–45', category: 'size', pricing_type: 'base_price', price: 900, active: true, sort_order: 8 },
    { id: '14', name: '14"', description: 'Baker confirms size quote', category: 'size', pricing_type: 'custom_quote', price: null, active: true, sort_order: 9 },
    { id: '16', name: '16"', description: 'Baker confirms size quote', category: 'size', pricing_type: 'custom_quote', price: null, active: true, sort_order: 10 }
  ],
  shapeSizes: {
    round: ['4', '5', '6', '7', '8', '9', '10', '12', '14', '16'],
    square: ['5', '6', '7', '8', '9', '10', '12'],
    rectangle: ['8', '9', '10', '12', '14', '16'],
    heart: ['6', '7', '8', '9', '10'],
    number: ['8', '9', '10', '12', '14', '16'],
    letter: ['8', '9', '10', '12', '14', '16']
  },
  internalLayers: [
    { id: '1', name: '1 layer', category: 'internal_layers', pricing_type: 'included', price: 0 },
    { id: '2', name: '2 layers', category: 'internal_layers', pricing_type: 'add_on', price: 70 },
    { id: '3', name: '3 layers', category: 'internal_layers', pricing_type: 'custom_quote', price: null },
    { id: '4', name: '4 layers', category: 'internal_layers', pricing_type: 'custom_quote', price: null }
  ],
  flavours: [
    { id: 'vanilla', name: 'Vanilla', category: 'flavour', pricing_type: 'included', price: 0 },
    { id: 'banana', name: 'Banana', category: 'flavour', pricing_type: 'included', price: 0 },
    { id: 'chocolate', name: 'Chocolate', category: 'flavour', pricing_type: 'add_on', price: 20 },
    { id: 'marble', name: 'Marble', category: 'flavour', pricing_type: 'add_on', price: 30 },
    { id: 'red-velvet', name: 'Red Velvet', category: 'flavour', pricing_type: 'add_on', price: 40 },
    { id: 'lemon', name: 'Lemon', category: 'flavour', pricing_type: 'add_on', price: 20 },
    { id: 'orange', name: 'Orange', category: 'flavour', pricing_type: 'custom_quote', price: null },
    { id: 'coconut', name: 'Coconut', category: 'flavour', pricing_type: 'add_on', price: 30 },
    { id: 'carrot', name: 'Carrot', category: 'flavour', pricing_type: 'add_on', price: 30 },
    { id: 'chocolate-fudge', name: 'Chocolate Fudge', category: 'flavour', pricing_type: 'custom_quote', price: null },
    { id: 'black-forest', name: 'Black Forest', category: 'flavour', pricing_type: 'custom_quote', price: null },
    { id: 'cookies-cream', name: 'Cookies & Cream', category: 'flavour', pricing_type: 'custom_quote', price: null },
    { id: 'fruit-cake', name: 'Fruit Cake', category: 'flavour', pricing_type: 'add_on', price: 50, range: true }
  ],
  fillings: [
    { id: 'none', name: 'No Filling', category: 'filling', pricing_type: 'included', price: 0 },
    { id: 'vanilla-cream', name: 'Vanilla Cream', category: 'filling', pricing_type: 'add_on', price: 20 },
    { id: 'chocolate-cream', name: 'Chocolate Cream', category: 'filling', pricing_type: 'add_on', price: 20 },
    { id: 'strawberry', name: 'Strawberry', category: 'filling', pricing_type: 'add_on', price: 30 },
    { id: 'caramel', name: 'Caramel', category: 'filling', pricing_type: 'add_on', price: 30 },
    { id: 'cookies-filling', name: 'Cookies & Cream', category: 'filling', pricing_type: 'add_on', price: 30 },
    { id: 'cream-cheese', name: 'Cream Cheese', category: 'filling', pricing_type: 'add_on', price: 40 },
    { id: 'lemon-curd', name: 'Lemon Curd', category: 'filling', pricing_type: 'add_on', price: 30 },
    { id: 'fruit-filling', name: 'Fruit Filling', category: 'filling', pricing_type: 'add_on', price: 50 }
  ],
  icings: [
    { id: 'vanilla-buttercream', name: 'Vanilla Buttercream', category: 'icing', pricing_type: 'included', price: 0 },
    { id: 'butter-icing', name: 'Butter Icing', category: 'icing', pricing_type: 'included', price: 0 },
    { id: 'chocolate-buttercream', name: 'Chocolate Buttercream', category: 'icing', pricing_type: 'add_on', price: 20 },
    { id: 'cream-cheese-frosting', name: 'Cream Cheese Frosting', category: 'icing', pricing_type: 'add_on', price: 30 },
    { id: 'whipped-cream', name: 'Whipped Cream', category: 'icing', pricing_type: 'included', price: 0 },
    { id: 'swiss-meringue', name: 'Swiss Meringue Buttercream', category: 'icing', pricing_type: 'custom_quote', price: null },
    { id: 'italian-meringue', name: 'Italian Meringue Buttercream', category: 'icing', pricing_type: 'custom_quote', price: null },
    { id: 'ganache', name: 'Ganache', category: 'icing', pricing_type: 'add_on', price: 50 },
    { id: 'fondant', name: 'Fondant', category: 'icing', pricing_type: 'add_on', price: 150, range: true },
    { id: 'naked', name: 'Naked / Semi-Naked', category: 'icing', pricing_type: 'included', price: 0 }
  ],
  colours: ['White', 'Cream', 'Pink', 'Blue', 'Red', 'Yellow', 'Green', 'Purple', 'Black', 'Custom Colour'].map(function (name, i) { return { id: 'colour-' + i, name: name, category: 'icing_colour', pricing_type: 'included', price: 0 }; }),
  designs: [
    { id: 'simple', name: 'Simple', category: 'design', pricing_type: 'included', price: 0 },
    { id: 'minimalist', name: 'Minimalist', category: 'design', pricing_type: 'included', price: 0 },
    { id: 'floral', name: 'Floral', category: 'design', pricing_type: 'custom_quote', price: null },
    { id: 'vintage', name: 'Vintage', category: 'design', pricing_type: 'custom_quote', price: null },
    { id: 'chocolate-drip', name: 'Chocolate Drip', category: 'design', pricing_type: 'add_on', price: 40 },
    { id: 'luxury', name: 'Luxury', category: 'design', pricing_type: 'custom_quote', price: null },
    { id: 'cartoon', name: 'Cartoon', category: 'design', pricing_type: 'custom_quote', price: null },
    { id: 'geometric', name: 'Geometric', category: 'design', pricing_type: 'custom_quote', price: null },
    { id: 'custom', name: 'Custom', category: 'design', pricing_type: 'custom_quote', price: null }
  ],
  decorations: [
    { id: 'sprinkles', name: 'Sprinkles', category: 'decoration', pricing_type: 'custom_quote', price: null },
    { id: 'edible-pearls', name: 'Edible Pearls', category: 'decoration', pricing_type: 'custom_quote', price: null },
    { id: 'chocolate-pieces', name: 'Chocolate Pieces', category: 'decoration', pricing_type: 'add_on', price: 40 },
    { id: 'fresh-fruits', name: 'Fresh Fruits', category: 'decoration', pricing_type: 'add_on', price: 50 },
    { id: 'macarons', name: 'Macarons', category: 'decoration', pricing_type: 'custom_quote', price: null },
    { id: 'flowers', name: 'Flowers', category: 'decoration', pricing_type: 'custom_quote', price: null },
    { id: 'gold-decorations', name: 'Gold Decorations', category: 'decoration', pricing_type: 'custom_quote', price: null },
    { id: 'silver-decorations', name: 'Silver Decorations', category: 'decoration', pricing_type: 'custom_quote', price: null },
    { id: 'edible-image', name: 'Edible Image', category: 'decoration', pricing_type: 'add_on', price: 60 }
  ],
  toppings: [
    { id: 'oreo', name: 'Oreo / Biscuit Topping', category: 'topping', pricing_type: 'add_on', price: 30 },
    { id: 'chocolate-topping', name: 'Chocolate Toppings', category: 'topping', pricing_type: 'add_on', price: 40 },
    { id: 'fresh-fruit-topping', name: 'Fresh Fruit', category: 'topping', pricing_type: 'add_on', price: 50 },
    { id: 'cream-piping', name: 'Extra Cream Piping', category: 'topping', pricing_type: 'add_on', price: 30 }
  ],
  toppers: [
    { id: 'none', name: 'No Topper', category: 'topper', pricing_type: 'included', price: 0 },
    { id: 'standard', name: 'Cake Topper', category: 'topper', pricing_type: 'add_on', price: 30, range: true },
    { id: 'custom', name: 'Custom Topper', category: 'topper', pricing_type: 'custom_quote', price: null }
  ],
  assembly: {
    1: { id: 'assembly-1', name: 'Assembly', pricing_type: 'included', price: 0 },
    2: { id: 'assembly-2', name: 'Two-tier assembly', pricing_type: 'custom_quote', price: null },
    3: { id: 'assembly-3', name: 'Three-tier assembly', pricing_type: 'custom_quote', price: null },
    4: { id: 'assembly-4', name: 'Four-tier assembly', pricing_type: 'custom_quote', price: null }
  },
  limits: { inspirationImages: 3, maxFileSizeMb: 5, fillings: 2, decorations: 10, toppings: 10, extras: 4 },
  tierLabels: ['Bottom', 'Middle', 'Top', 'Top'],
  sizeOrder: ['4', '5', '6', '7', '8', '9', '10', '12', '14', '16']
};

/* Normalize metadata so every option remains configurable by a future baker dashboard. */
(function (config) {
  var groups = [
    ['shapes', 'single', 1, 1], ['sizes', 'single', 1, 1], ['internalLayers', 'single', 1, 1],
    ['flavours', 'single', 1, 1], ['fillings', 'multiple', 0, 2], ['icings', 'single', 1, 1],
    ['colours', 'single', 1, 1], ['designs', 'single', 1, 1], ['decorations', 'multiple', 0, 10],
    ['toppings', 'multiple', 0, 10], ['toppers', 'single', 1, 1]
  ];
  groups.forEach(function (entry) {
    (config[entry[0]] || []).forEach(function (item, index) {
      item.selection_type = entry[1];
      item.minimum_selection = entry[2];
      item.maximum_selection = entry[3];
      item.active = item.active !== false;
      item.sort_order = item.sort_order || index + 1;
    });
  });
  config.structures.forEach(function (item, index) {
    item.selection_type = 'single'; item.minimum_selection = 1; item.maximum_selection = 1; item.active = item.active !== false; item.sort_order = index + 1;
  });
})(window.MB_CAKE_CONFIG);

/* Simple customer-facing menu: advanced choices remain in the config for later activation. */
(function (config) {
  function showOnly(list, ids) {
    (list || []).forEach(function (item) { item.active = ids.indexOf(item.id) > -1; });
  }
  showOnly(config.sizes, ['4', '5', '6', '8', '10', '12']);
  showOnly(config.flavours, ['vanilla', 'banana', 'chocolate', 'lemon', 'marble', 'coconut', 'carrot', 'red-velvet', 'fruit-cake']);
  showOnly(config.fillings, ['none', 'vanilla-cream', 'chocolate-cream', 'strawberry', 'caramel', 'cookies-filling']);
  showOnly(config.icings, ['whipped-cream', 'butter-icing', 'fondant']);
  showOnly(config.colours, ['colour-0', 'colour-1', 'colour-2', 'colour-3', 'colour-9']);
  showOnly(config.designs, ['simple', 'minimalist', 'floral', 'chocolate-drip', 'custom']);
  showOnly(config.decorations, ['sprinkles', 'fresh-fruits', 'flowers', 'gold-decorations', 'edible-image']);
  showOnly(config.toppings, ['oreo', 'chocolate-topping', 'fresh-fruit-topping', 'cream-piping']);
})(window.MB_CAKE_CONFIG);
