import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import 'leaflet.markercluster/dist/MarkerCluster.css';
import 'leaflet.markercluster/dist/MarkerCluster.Default.css';

interface Point {
  id: string; name: string; type: string; typeLabel: string; color: string;
  themes: string[]; themeTitles: string[]; badge: string; badgeLabel: string; tags: string[];
  summary: string; area: string; lat: number; lng: number; precise: boolean; draft: boolean; url: string;
}

const LONDON: L.LatLngTuple = [51.507, -0.1];
const dark = () => window.matchMedia('(prefers-color-scheme: dark)').matches;

function el(tag: string, cls?: string, text?: string) {
  const e = document.createElement(tag);
  if (cls) e.className = cls;
  if (text) e.textContent = text;
  return e;
}

function popup(p: Point) {
  const box = el('div');
  box.append(el('h4', '', p.name));
  box.append(el('div', 'pmeta', `${p.typeLabel} · ${p.area} · ${p.badgeLabel}${p.draft ? ' · DRAFT' : ''}`));
  box.append(el('p', '', p.summary));
  if (!p.precise) box.append(el('p', 'pmeta', 'Approximate location'));
  const a = el('a', '', 'Read more →') as HTMLAnchorElement;
  a.href = p.url;
  box.append(a);
  return box;
}

function marker(p: Point) {
  const cls = ['lg-pin', p.badge === 'favourite' ? 'fav' : '', p.precise ? '' : 'area'].join(' ');
  const icon = L.divIcon({
    className: '',
    html: `<div class="${cls}" style="--c:${p.color}"></div>`,
    iconSize: [20, 20],
    iconAnchor: [10, 10],
    popupAnchor: [0, -10],
  });
  return L.marker([p.lat, p.lng], { icon, title: p.name, alt: p.name }).bindPopup(() => popup(p));
}

export async function initMaps() {
  // markercluster expects a global L
  (window as any).L = L;
  await import('leaflet.markercluster');

  document.querySelectorAll<HTMLElement>('.lg-map').forEach((host) => {
    if (host.dataset.ready) return;
    host.dataset.ready = '1';
    const points: Point[] = JSON.parse(host.querySelector('script')?.textContent || '[]');

    const map = L.map(host, { scrollWheelZoom: host.classList.contains('full'), zoomControl: true });
    const style = dark() ? 'dark_all' : 'rastertiles/voyager';
    L.tileLayer(`https://{s}.basemaps.cartocdn.com/${style}/{z}/{x}/{y}{r}.png`, {
      maxZoom: 19,
      subdomains: 'abcd',
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    }).addTo(map);

    const useCluster = points.length > 25;
    const layer: L.LayerGroup = useCluster
      ? (L as any).markerClusterGroup({ showCoverageOnHover: false, maxClusterRadius: 40 })
      : L.layerGroup();
    layer.addTo(map);

    const render = (list: Point[]) => {
      layer.clearLayers();
      list.forEach((p) => layer.addLayer(marker(p)));
      if (list.length === 1) map.setView([list[0].lat, list[0].lng], 15);
      else if (list.length > 1) map.fitBounds(L.latLngBounds(list.map((p) => [p.lat, p.lng])), { padding: [30, 30], maxZoom: 15 });
      else map.setView(LONDON, 11);
    };

    if (host.dataset.route && points.length > 1) {
      L.polyline(points.map((p) => [p.lat, p.lng] as L.LatLngTuple), { color: '#b3261e', weight: 3, opacity: .7, dashArray: '6 6' }).addTo(map);
    }

    render(points);

    if (host.dataset.filters) {
      const form = document.getElementById('map-filters') as HTMLFormElement | null;
      const count = document.getElementById('map-count');
      if (!form) return;
      // Prefill from the URL, e.g. map/?theme=historic-pubs
      const params = new URLSearchParams(location.search);
      for (const [k, v] of params) {
        const f = form.elements.namedItem(k) as HTMLInputElement | HTMLSelectElement | null;
        if (!f) continue;
        if (f instanceof HTMLInputElement && f.type === 'checkbox') f.checked = v === '1';
        else f.value = v;
      }
      const apply = () => {
        const fd = new FormData(form);
        const theme = String(fd.get('theme') || '');
        const type = String(fd.get('type') || '');
        const fav = fd.get('fav') === '1';
        const tags = ['kid-friendly', 'free', 'rainy-day'].filter((t) => fd.get(t) === '1');
        const list = points.filter((p) =>
          (!theme || p.themes.includes(theme)) &&
          (!type || p.type === type) &&
          (!fav || p.badge === 'favourite') &&
          tags.every((t) => p.tags.includes(t)));
        render(list);
        if (count) count.textContent = `${list.length} place${list.length === 1 ? '' : 's'}`;
        const q = new URLSearchParams();
        if (theme) q.set('theme', theme);
        if (type) q.set('type', type);
        if (fav) q.set('fav', '1');
        tags.forEach((t) => q.set(t, '1'));
        history.replaceState(null, '', q.toString() ? `?${q}` : location.pathname);
      };
      form.addEventListener('change', apply);
      apply();
    }
  });
}
