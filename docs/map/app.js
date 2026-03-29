/* ============================================================
   London Guide — Map Application
   Supports both all-sites mode and single-category mode via MAP_CONFIG
   ============================================================ */

(function () {
  "use strict";

  // ---- Configuration (set by category pages before this script loads) ----
  var config = window.MAP_CONFIG || null;
  var isCategoryMode = !!(config && config.category);

  // ---- Category colours ----
  var CATEGORY_COLORS = {
    "restaurants":    "#C8102E",
    "attractions":    "#2C3E6B",
    "neighborhoods":  "#5B8C5A",
    "day-trips":      "#8B6C42",
    "wmd-sites":      "#4A4A4A",
    "movie-sites":    "#7B2D8B",
    "kid-friendly":   "#E8873F",
    "historic-sites": "#6B4226",
  };

  var CATEGORY_LABELS = {
    "restaurants":    "Restaurants & Food",
    "attractions":    "Attractions & Museums",
    "neighborhoods":  "Neighborhoods",
    "day-trips":      "Day Trips",
    "wmd-sites":      "WMD Sites",
    "movie-sites":    "Movie Sites",
    "kid-friendly":   "Kid Friendly",
    "historic-sites": "Historic Sites",
  };

  // ---- Subcategory labels ----
  var SUBCATEGORY_LABELS = {
    "restaurant": "Restaurant", "pub": "Pub", "gastropub": "Gastropub",
    "cafe": "Cafe", "bakery": "Bakery", "wine-bar": "Wine Bar",
    "cocktail-bar": "Cocktail Bar", "market": "Market",
    "street-food": "Street Food", "afternoon-tea": "Afternoon Tea",
    "ice-cream": "Ice Cream",
    "museum": "Museum", "gallery": "Gallery", "landmark": "Landmark",
    "park": "Park", "garden": "Garden", "zoo": "Zoo",
    "theatre": "Theatre", "football": "Football", "sports": "Sports",
    "castle": "Castle", "countryside": "Countryside", "coast": "Coast",
    "historic-town": "Historic Town", "national-park": "National Park",
    "literary": "Literary", "family-adventure": "Family Adventure",
    "nuclear": "Nuclear", "radiological": "Radiological",
    "chemical": "Chemical", "biological": "Biological",
    "missile": "Missile", "activism": "Activism",
    "harry-potter": "Harry Potter", "james-bond": "James Bond",
    "sherlock": "Sherlock", "crown": "The Crown", "muppets": "Muppets",
    "other-film": "Other Film", "other-tv": "Other TV",
    "playground": "Playground", "outdoor-adventure": "Outdoor Adventure",
    "theme-park": "Theme Park", "farm": "Farm", "beach": "Beach",
    "battlefield": "Battlefield", "roman": "Roman", "medieval": "Medieval",
    "tudor": "Tudor", "civil-war": "Civil War", "industrial": "Industrial",
    "memorial": "Memorial",
  };

  // Generate subcategory colors — distinct hues within the category color family
  function getSubcategoryColor(subcat, category) {
    var base = CATEGORY_COLORS[category] || "#6b6b6b";
    var hash = 0;
    for (var i = 0; i < subcat.length; i++) hash = subcat.charCodeAt(i) + ((hash << 5) - hash);
    var shift = (hash % 60) - 30;
    var r = parseInt(base.slice(1, 3), 16);
    var g = parseInt(base.slice(3, 5), 16);
    var b = parseInt(base.slice(5, 7), 16);
    r = Math.max(0, Math.min(255, r + shift * 2));
    g = Math.max(0, Math.min(255, g + shift));
    b = Math.max(0, Math.min(255, b - shift));
    return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
  }

  var DEFAULT_COLOR = "#6b6b6b";
  var MARKER_SIZE = 22;

  // ---- State ----
  var allFeatures = [];
  var markers = [];
  var hiddenCategories = new Set();
  var hiddenSubcategories = new Set();
  var hiddenNeighborhoods = new Set();
  var hiddenVisited = new Set();
  var isListView = false;

  // ---- Map setup ----
  var map = L.map("map", {
    center: [51.509, -0.118],
    zoom: 12,
    zoomControl: true,
    attributionControl: true,
  });

  L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png", {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/">CARTO</a>',
    maxZoom: 19,
    subdomains: "abcd",
  }).addTo(map);

  // ---- Helpers ----
  function getMarkerColor(props) {
    if (isCategoryMode) {
      return getSubcategoryColor(props.subcategory || "other", config.category);
    }
    return CATEGORY_COLORS[props.category] || DEFAULT_COLOR;
  }

  function getCategoryLabel(cat) {
    return CATEGORY_LABELS[cat] || cat;
  }

  function getSubcategoryLabel(sub) {
    return SUBCATEGORY_LABELS[sub] || sub;
  }

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    if (attrs) {
      Object.entries(attrs).forEach(function (entry) {
        var k = entry[0], v = entry[1];
        if (k === "className") node.className = v;
        else if (k === "textContent") node.textContent = v;
        else if (k.startsWith("style.")) node.style[k.slice(6)] = v;
        else node.setAttribute(k, v);
      });
    }
    if (children) {
      children.forEach(function (child) {
        if (typeof child === "string") node.appendChild(document.createTextNode(child));
        else if (child) node.appendChild(child);
      });
    }
    return node;
  }

  // ---- Build popup ----
  function buildPopupContent(props) {
    var color = getMarkerColor(props);
    var catBar = el("div", { className: "popup-cat-bar", "style.background": color });
    var nameEl = el("div", { className: "popup-name", textContent: props.name });
    var priceEl = props.price_range ? el("div", { className: "popup-price", textContent: props.price_range }) : null;
    var header = el("div", { className: "popup-header" }, [nameEl, priceEl].filter(Boolean));

    var metaParts = [];
    if (!isCategoryMode) metaParts.push(getCategoryLabel(props.category));
    if (props.subcategory) metaParts.push(getSubcategoryLabel(props.subcategory));
    if (props.neighborhood) metaParts.push(props.neighborhood);
    var meta = el("div", { className: "popup-meta", textContent: metaParts.join(" \u00B7 ") });

    var ratingEl = null;
    if (props.rating) {
      var starText = "\u2605".repeat(props.rating) + "\u2606".repeat(5 - props.rating);
      ratingEl = el("div", { className: "popup-rating", textContent: starText + " (family rating)" });
    }

    var badges = el("div", { className: "popup-badges" });
    if (isCategoryMode && props.subcategory) {
      badges.appendChild(el("span", { className: "popup-badge", textContent: getSubcategoryLabel(props.subcategory), "style.background": color }));
    } else {
      badges.appendChild(el("span", { className: "popup-badge", textContent: getCategoryLabel(props.category), "style.background": CATEGORY_COLORS[props.category] || DEFAULT_COLOR }));
    }
    if (props.visited) {
      badges.appendChild(el("span", { className: "popup-badge", textContent: "Visited", "style.background": "#5B8C5A" }));
    }

    var summary = props.summary ? el("div", { className: "popup-summary", textContent: props.summary }) : null;
    var notesEl = props.notes ? el("div", { className: "popup-notes", textContent: props.notes }) : null;
    var divider = el("hr", { className: "popup-divider" });

    function detailRow(label, value) {
      if (!value) return null;
      var row = el("div", { className: "popup-detail" });
      row.appendChild(el("strong", { textContent: label + " " }));
      row.appendChild(document.createTextNode(value));
      return row;
    }
    function linkRow(label, url, text) {
      if (!url) return null;
      var row = el("div", { className: "popup-detail" });
      row.appendChild(el("strong", { textContent: label + " " }));
      row.appendChild(el("a", { href: url, target: "_blank", textContent: text || url }));
      return row;
    }

    var items = [header, meta, ratingEl, badges, summary, notesEl, divider,
      detailRow("Address:", props.address),
      linkRow("Website:", props.website, "Visit website"),
      linkRow("Google Maps:", props.google_maps_url, "View on Maps"),
    ].filter(Boolean);

    var inner = el("div", { className: "popup-inner" }, items);
    var container = document.createElement("div");
    container.appendChild(catBar);
    container.appendChild(inner);
    return container;
  }

  // ---- Create marker ----
  function createMarker(feature) {
    var props = feature.properties;
    var coords = feature.geometry.coordinates;
    var color = getMarkerColor(props);

    var markerDiv = document.createElement("div");
    markerDiv.className = "guide-marker";
    markerDiv.style.background = color;
    markerDiv.style.width = MARKER_SIZE + "px";
    markerDiv.style.height = MARKER_SIZE + "px";

    var icon = L.divIcon({
      className: "",
      html: markerDiv.outerHTML,
      iconSize: [MARKER_SIZE, MARKER_SIZE],
      iconAnchor: [MARKER_SIZE / 2, MARKER_SIZE / 2],
      popupAnchor: [0, -MARKER_SIZE / 2],
    });

    var marker = L.marker([coords[1], coords[0]], { icon: icon });
    marker.bindPopup(function () { return buildPopupContent(props); }, { maxWidth: 340 });
    return { marker: marker, feature: feature };
  }

  // ---- Filter logic ----
  function isVisible(props) {
    if (isCategoryMode) {
      if (hiddenSubcategories.has(props.subcategory || "")) return false;
    } else {
      if (hiddenCategories.has(props.category)) return false;
    }
    if (hiddenNeighborhoods.has(props.neighborhood)) return false;
    var visitedLabel = props.visited ? "Yes" : "No";
    if (hiddenVisited.has(visitedLabel)) return false;
    return true;
  }

  function applyFilters() {
    var visible = 0;
    markers.forEach(function (entry) {
      if (isVisible(entry.feature.properties)) {
        entry.marker.addTo(map);
        visible++;
      } else {
        entry.marker.remove();
      }
    });
    document.getElementById("visibleCount").textContent = visible;
    if (isListView) updateListView();
  }

  // ---- Build filter checkboxes ----
  function makeFilterItem(label, swatchColor, hiddenSet, filterValue) {
    var item = document.createElement("label");
    item.className = "filter-item";
    var cb = document.createElement("input");
    cb.type = "checkbox";
    cb.checked = true;
    cb.addEventListener("change", function () {
      if (cb.checked) hiddenSet.delete(filterValue);
      else hiddenSet.add(filterValue);
      applyFilters();
    });
    item.appendChild(cb);
    if (swatchColor) {
      var swatch = document.createElement("span");
      swatch.className = "filter-swatch";
      swatch.style.background = swatchColor;
      item.appendChild(swatch);
    }
    var lbl = document.createElement("span");
    lbl.className = "filter-label";
    lbl.textContent = label;
    item.appendChild(lbl);
    return item;
  }

  function buildFilters(features) {
    var catHeading = document.querySelector("#categoryFilters").previousElementSibling;
    var catContainer = document.getElementById("categoryFilters");

    if (isCategoryMode) {
      catHeading.textContent = "Subcategory";
      var subSet = new Set();
      features.forEach(function (f) { if (f.properties.subcategory) subSet.add(f.properties.subcategory); });
      Array.from(subSet).sort().forEach(function (sub) {
        catContainer.appendChild(makeFilterItem(getSubcategoryLabel(sub), getSubcategoryColor(sub, config.category), hiddenSubcategories, sub));
      });
    } else {
      var catSet = new Set();
      features.forEach(function (f) { if (f.properties.category) catSet.add(f.properties.category); });
      Array.from(catSet).sort().forEach(function (cat) {
        catContainer.appendChild(makeFilterItem(getCategoryLabel(cat), CATEGORY_COLORS[cat], hiddenCategories, cat));
      });
    }

    var neighContainer = document.getElementById("neighborhoodFilters");
    var neighSet = new Set();
    features.forEach(function (f) { if (f.properties.neighborhood) neighSet.add(f.properties.neighborhood); });
    Array.from(neighSet).sort().forEach(function (n) {
      neighContainer.appendChild(makeFilterItem(n, null, hiddenNeighborhoods, n));
    });

    var visitedContainer = document.getElementById("visitedFilters");
    visitedContainer.appendChild(makeFilterItem("Yes", null, hiddenVisited, "Yes"));
    visitedContainer.appendChild(makeFilterItem("No", null, hiddenVisited, "No"));
  }

  // ---- Legend ----
  function buildLegend(features) {
    var legend = document.getElementById("mapLegend");
    if (isCategoryMode) {
      legend.appendChild(el("div", { className: "legend-title", textContent: "Subcategories" }));
      var subSet = new Set();
      features.forEach(function (f) { if (f.properties.subcategory) subSet.add(f.properties.subcategory); });
      Array.from(subSet).sort().forEach(function (sub) {
        var row = el("div", { className: "legend-row" });
        row.appendChild(el("span", { className: "legend-dot", "style.background": getSubcategoryColor(sub, config.category) }));
        row.appendChild(document.createTextNode(getSubcategoryLabel(sub)));
        legend.appendChild(row);
      });
    } else {
      legend.appendChild(el("div", { className: "legend-title", textContent: "Categories" }));
      var catSet = new Set();
      features.forEach(function (f) { if (f.properties.category) catSet.add(f.properties.category); });
      Array.from(catSet).sort().forEach(function (cat) {
        var row = el("div", { className: "legend-row" });
        row.appendChild(el("span", { className: "legend-dot", "style.background": CATEGORY_COLORS[cat] }));
        row.appendChild(document.createTextNode(getCategoryLabel(cat)));
        legend.appendChild(row);
      });
    }
  }

  // ---- List View ----
  function buildListView(features) {
    var container = document.getElementById("listContainer");
    if (!container) return;
    // Clear existing content safely
    while (container.firstChild) container.removeChild(container.firstChild);

    var sorted = features.slice().sort(function (a, b) {
      return (a.properties.name || "").localeCompare(b.properties.name || "");
    });

    sorted.forEach(function (f) {
      var props = f.properties;
      var color = getMarkerColor(props);
      var metaParts = [];
      if (props.subcategory) metaParts.push(getSubcategoryLabel(props.subcategory));
      if (props.neighborhood) metaParts.push(props.neighborhood);

      var card = el("div", { className: "list-card" }, [
        el("div", { className: "list-card-bar", "style.background": color }),
        el("div", { className: "list-card-body" }, [
          el("div", { className: "list-card-header" }, [
            el("div", { className: "list-card-name", textContent: props.name }),
            props.price_range ? el("div", { className: "list-card-price", textContent: props.price_range }) : null,
          ].filter(Boolean)),
          el("div", { className: "list-card-meta", textContent: metaParts.join(" \u00B7 ") }),
          props.summary ? el("div", { className: "list-card-summary", textContent: props.summary }) : null,
        ].filter(Boolean)),
      ]);
      card.dataset.category = props.category || "";
      card.dataset.subcategory = props.subcategory || "";
      card.dataset.neighborhood = props.neighborhood || "";
      card.dataset.visited = props.visited ? "Yes" : "No";
      container.appendChild(card);
    });
  }

  function updateListView() {
    var container = document.getElementById("listContainer");
    if (!container) return;
    var cards = container.querySelectorAll(".list-card");
    cards.forEach(function (card) {
      var props = {
        category: card.dataset.category,
        subcategory: card.dataset.subcategory,
        neighborhood: card.dataset.neighborhood,
        visited: card.dataset.visited === "Yes",
      };
      card.style.display = isVisible(props) ? "" : "none";
    });
  }

  function setupViewToggle() {
    var btn = document.getElementById("viewToggle");
    if (!btn) return;
    var mapEl = document.getElementById("map");
    var listEl = document.getElementById("listView");
    if (!listEl) return;

    btn.addEventListener("click", function () {
      isListView = !isListView;
      mapEl.style.display = isListView ? "none" : "";
      listEl.classList.toggle("hidden", !isListView);
      btn.textContent = isListView ? "Map View" : "List View";
      if (isListView) updateListView();
      else map.invalidateSize();
    });
  }

  // ---- Reset ----
  function setupReset() {
    document.getElementById("resetFilters").addEventListener("click", function () {
      hiddenCategories.clear();
      hiddenSubcategories.clear();
      hiddenNeighborhoods.clear();
      hiddenVisited.clear();
      document.querySelectorAll(".filter-item input").forEach(function (cb) { cb.checked = true; });
      applyFilters();
    });
  }

  // ---- Mobile toggle ----
  function setupMobileToggle() {
    var toggle = document.getElementById("controlsToggle");
    var panel = document.getElementById("controls");
    toggle.addEventListener("click", function () { panel.classList.toggle("open"); });
    map.on("click", function () { panel.classList.remove("open"); });
  }

  // ---- Init ----
  async function init() {
    if (config) {
      var titleEl = document.querySelector(".header-title");
      if (titleEl && config.title) titleEl.textContent = config.title;
      var subEl = document.querySelector(".header-subtitle");
      if (subEl && config.subtitle) subEl.textContent = config.subtitle;
    }

    try {
      var resp = await fetch("../data/sites.geojson");
      if (!resp.ok) throw new Error("HTTP " + resp.status);
      var data = await resp.json();
      allFeatures = data.features || [];
    } catch (err) {
      console.error("Failed to load sites.geojson:", err);
      return;
    }

    if (isCategoryMode) {
      allFeatures = allFeatures.filter(function (f) {
        return f.properties.category === config.category;
      });
    }

    markers = allFeatures.map(createMarker);
    markers.forEach(function (entry) { entry.marker.addTo(map); });

    document.getElementById("totalCount").textContent = allFeatures.length;
    document.getElementById("visibleCount").textContent = allFeatures.length;

    buildFilters(allFeatures);
    buildLegend(allFeatures);
    buildListView(allFeatures);
    setupReset();
    setupMobileToggle();
    setupViewToggle();

    if (markers.length > 0) {
      var group = L.featureGroup(markers.map(function (m) { return m.marker; }));
      map.fitBounds(group.getBounds().pad(0.1));
    }
  }

  init();
})();
