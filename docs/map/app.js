/* ============================================================
   London Guide — Map Application
   ============================================================ */

(function () {
  "use strict";

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

  var DEFAULT_COLOR = "#6b6b6b";
  var MARKER_SIZE = 22;

  // ---- State ----
  var allFeatures = [];
  var markers = [];
  var hiddenCategories = new Set();
  var hiddenNeighborhoods = new Set();
  var hiddenVisited = new Set();

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
  function getCategoryColor(cat) {
    return CATEGORY_COLORS[cat] || DEFAULT_COLOR;
  }

  function getCategoryLabel(cat) {
    return CATEGORY_LABELS[cat] || cat;
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
    var color = getCategoryColor(props.category);

    var catBar = el("div", { className: "popup-cat-bar", "style.background": color });

    var nameEl = el("div", { className: "popup-name", textContent: props.name });
    var priceEl = props.price_range
      ? el("div", { className: "popup-price", textContent: props.price_range })
      : null;
    var header = el("div", { className: "popup-header" }, [nameEl, priceEl].filter(Boolean));

    var metaParts = [getCategoryLabel(props.category), props.subcategory, props.neighborhood]
      .filter(Boolean).join(" \u00B7 ");
    var meta = el("div", { className: "popup-meta", textContent: metaParts });

    // Rating stars
    var ratingEl = null;
    if (props.rating) {
      var starText = "\u2605".repeat(props.rating) + "\u2606".repeat(5 - props.rating);
      ratingEl = el("div", { className: "popup-rating", textContent: starText + " (family rating)" });
    }

    // Category badge
    var badges = el("div", { className: "popup-badges" });
    badges.appendChild(el("span", {
      className: "popup-badge",
      textContent: getCategoryLabel(props.category),
      "style.background": color,
    }));
    if (props.visited) {
      badges.appendChild(el("span", {
        className: "popup-badge",
        textContent: "Visited",
        "style.background": "#5B8C5A",
      }));
    }

    var summary = props.summary
      ? el("div", { className: "popup-summary", textContent: props.summary })
      : null;

    var notesEl = props.notes
      ? el("div", { className: "popup-notes", textContent: props.notes })
      : null;

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

    var items = [
      header, meta, ratingEl, badges, summary, notesEl, divider,
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
    var color = getCategoryColor(props.category);

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
  function applyFilters() {
    var visible = 0;
    markers.forEach(function (entry) {
      var props = entry.feature.properties;

      var catOk = !hiddenCategories.has(props.category);
      var neighOk = !hiddenNeighborhoods.has(props.neighborhood);
      var visitedLabel = props.visited ? "Yes" : "No";
      var visitedOk = !hiddenVisited.has(visitedLabel);

      if (catOk && neighOk && visitedOk) {
        entry.marker.addTo(map);
        visible++;
      } else {
        entry.marker.remove();
      }
    });
    document.getElementById("visibleCount").textContent = visible;
  }

  // ---- Build filter checkboxes ----
  function makeFilterItem(label, swatchColor, hiddenSet, filterValue) {
    var item = document.createElement("label");
    item.className = "filter-item";

    var cb = document.createElement("input");
    cb.type = "checkbox";
    cb.checked = true;
    cb.addEventListener("change", function () {
      if (cb.checked) {
        hiddenSet.delete(filterValue);
      } else {
        hiddenSet.add(filterValue);
      }
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
    // Categories
    var catContainer = document.getElementById("categoryFilters");
    var catSet = new Set();
    features.forEach(function (f) { if (f.properties.category) catSet.add(f.properties.category); });
    Array.from(catSet).sort().forEach(function (cat) {
      catContainer.appendChild(makeFilterItem(
        getCategoryLabel(cat), getCategoryColor(cat), hiddenCategories, cat
      ));
    });

    // Neighborhoods
    var neighContainer = document.getElementById("neighborhoodFilters");
    var neighSet = new Set();
    features.forEach(function (f) { if (f.properties.neighborhood) neighSet.add(f.properties.neighborhood); });
    Array.from(neighSet).sort().forEach(function (n) {
      neighContainer.appendChild(makeFilterItem(n, null, hiddenNeighborhoods, n));
    });

    // Visited
    var visitedContainer = document.getElementById("visitedFilters");
    visitedContainer.appendChild(makeFilterItem("Yes", null, hiddenVisited, "Yes"));
    visitedContainer.appendChild(makeFilterItem("No", null, hiddenVisited, "No"));
  }

  // ---- Legend ----
  function buildLegend(features) {
    var legend = document.getElementById("mapLegend");
    legend.appendChild(el("div", { className: "legend-title", textContent: "Categories" }));

    var catSet = new Set();
    features.forEach(function (f) { if (f.properties.category) catSet.add(f.properties.category); });

    Array.from(catSet).sort().forEach(function (cat) {
      var row = el("div", { className: "legend-row" });
      row.appendChild(el("span", { className: "legend-dot", "style.background": getCategoryColor(cat) }));
      row.appendChild(document.createTextNode(getCategoryLabel(cat)));
      legend.appendChild(row);
    });
  }

  // ---- Reset ----
  function setupReset() {
    document.getElementById("resetFilters").addEventListener("click", function () {
      hiddenCategories.clear();
      hiddenNeighborhoods.clear();
      hiddenVisited.clear();
      document.querySelectorAll(".filter-item input").forEach(function (cb) { cb.checked = true; });
      applyFilters();
    });
  }

  // ---- Mobile toggle ----
  function setupToggle() {
    var toggle = document.getElementById("controlsToggle");
    var panel = document.getElementById("controls");
    toggle.addEventListener("click", function () {
      panel.classList.toggle("open");
    });
    map.on("click", function () {
      panel.classList.remove("open");
    });
  }

  // ---- Init ----
  async function init() {
    try {
      var resp = await fetch("../data/sites.geojson");
      if (!resp.ok) throw new Error("HTTP " + resp.status);
      var data = await resp.json();
      allFeatures = data.features || [];
    } catch (err) {
      console.error("Failed to load sites.geojson:", err);
      return;
    }

    markers = allFeatures.map(createMarker);
    markers.forEach(function (entry) { entry.marker.addTo(map); });

    document.getElementById("totalCount").textContent = allFeatures.length;
    document.getElementById("visibleCount").textContent = allFeatures.length;

    buildFilters(allFeatures);
    buildLegend(allFeatures);
    setupReset();
    setupToggle();

    if (markers.length > 0) {
      var group = L.featureGroup(markers.map(function (m) { return m.marker; }));
      map.fitBounds(group.getBounds().pad(0.1));
    }
  }

  init();
})();
