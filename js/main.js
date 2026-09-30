// Mystery Bakebite: tiny progressive-enhancement script
document.documentElement.classList.add('js');

// Navigation v2: dropdowns, drawer, current page
(function () {
  var items = document.querySelectorAll('.has-dd');
  function closeAll(except) { items.forEach(function (i) { if (i !== except) { i.classList.remove('open'); i.querySelector('.dd-btn').setAttribute('aria-expanded', 'false'); } }); }
  items.forEach(function (it) {
    var b = it.querySelector('.dd-btn');
    b.addEventListener('click', function (e) {
      e.stopPropagation(); var o = !it.classList.contains('open'); closeAll(it);
      it.classList.toggle('open', o); b.setAttribute('aria-expanded', o ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function (e) { if (!e.target.closest('.has-dd')) closeAll(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { closeAll(); closeDrawer(); } });
  document.querySelectorAll('.dd-link, .dd-foot').forEach(function (a) { a.addEventListener('click', function () { closeAll(); }); });

  var toggle = document.querySelector('.nav-toggle');
  function openDrawer() { document.body.classList.add('drawer-open'); toggle.setAttribute('aria-expanded', 'true'); document.getElementById('drawer').setAttribute('aria-hidden', 'false'); }
  function closeDrawer() { document.body.classList.remove('drawer-open'); if (toggle) toggle.setAttribute('aria-expanded', 'false'); var d = document.getElementById('drawer'); if (d) d.setAttribute('aria-hidden', 'true'); }
  if (toggle) toggle.addEventListener('click', openDrawer);
  document.querySelectorAll('[data-close], .dr-panel a').forEach(function (el) { el.addEventListener('click', closeDrawer); });

  // current page highlight
  var page = location.pathname.split('/').pop() || 'index.html';
  var key = page === 'menu.html' ? 'menu' : page === 'order.html' ? 'order' : (/^class/.test(page) || page === 'pastries.html') ? 'classes' : page === 'index.html' ? 'home' : null;
  if (key) { var el = document.querySelector('.main-nav [data-key="' + key + '"]'); if (el) el.classList.add('current'); }
  document.querySelectorAll('.dr-main').forEach(function (a) { if (a.getAttribute('href') === page || (key === 'classes' && a.getAttribute('href') === 'classes.html')) a.classList.add('current'); });
  document.querySelectorAll('.dd-link').forEach(function (a) { if (a.getAttribute('href') === page) a.style.background = 'rgba(212,164,55,.14)'; });
})();

// Reveal-on-scroll
if ('IntersectionObserver' in window) {
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
} else {
  document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('visible'); });
}

var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

// Keep scroll work inside animation frames so rapid wheel/touch input never
// forces repeated style and layout work on the browser's scroll thread.
function rafThrottle(fn) {
  var ticking = false;
  return function () {
    if (ticking) return;
    ticking = true;
    var run = function () { ticking = false; fn(); };
    if ('requestAnimationFrame' in window) requestAnimationFrame(run);
    else setTimeout(run, 16);
  };
}

// Stagger reveals among siblings + directional variants
document.querySelectorAll('.menu-grid, .insta-grid, .steps, .pl-grid, .svc-grid, .info-grid, .pay-grid, .g-grid, .class-choice-grid, .guide-grid, .cd-facts, .bundle-grid, .level-list, .rgrid, .sgrid, .dgrid').forEach(function (g) {
  Array.prototype.forEach.call(g.querySelectorAll('.reveal'), function (el, i) {
    el.style.setProperty('--d', (i % 4) * 0.1 + 's');
  });
});
document.querySelectorAll('.insta-grid .reveal').forEach(function (el) { el.classList.add('zoom'); });
// Page-purpose motion: stagger menu cards and order-builder steps without adding markup.
document.querySelectorAll('.pricelist .pl-card, .menu-guide-grid .menu-guide-card, .op-form .op-step, .ocats .ocat').forEach(function (el, i) {
  el.style.setProperty('--d', (i % 5) * 0.08 + 's');
});
var sp = document.querySelector('.story-photo'); if (sp) sp.classList.add('from-left');
var sc = document.querySelector('.story-grid > div:last-child'); if (sc) sc.classList.add('from-right');

// Scroll progress + header state + hero parallax
var bar = document.createElement('div'); bar.className = 'progress'; document.body.appendChild(bar);
var header = document.querySelector('.site-header');
var frame = document.querySelector('.hero-frame');
var headerScrolled = false;
function onScroll() {
  var y = window.scrollY, h = document.documentElement.scrollHeight - innerHeight;
  bar.style.transform = 'scaleX(' + (h > 0 ? y / h : 0) + ')';
  var nextHeaderState = y > 30;
  if (header && nextHeaderState !== headerScrolled) {
    header.classList.toggle('scrolled', nextHeaderState);
    headerScrolled = nextHeaderState;
  }
  if (frame && !reduce && y < 900) frame.style.transform = 'rotate(-1.6deg) translateY(' + (y * -0.08) + 'px)';
}
var scheduleScrollChrome = rafThrottle(onScroll);
addEventListener('scroll', scheduleScrollChrome, { passive: true }); onScroll();

var desktop = window.matchMedia('(min-width: 769px)').matches;
if (!reduce && desktop) {
  // Cursor sheen on menu cards (no tilt)
  document.querySelectorAll('.mcard').forEach(function (c) {
    c.addEventListener('mousemove', function (e) {
      var r = c.getBoundingClientRect();
      c.style.setProperty('--mx', (e.clientX - r.left) / r.width * 100 + '%');
      c.style.setProperty('--my', (e.clientY - r.top) / r.height * 100 + '%');
    });
  });
  // A few sprinkles, homepage hero only
  var hero = document.querySelector('.hero');
  if (hero) {
    var box = document.createElement('div'); box.className = 'sprinkles';
    var cols = ['#F7B7C8', '#D4A437', '#F5E6D6'];
    for (var i = 0; i < 10; i++) {
      var s = document.createElement('i');
      s.style.left = Math.random() * 100 + '%';
      s.style.background = cols[i % cols.length];
      s.style.animationDuration = 14 + Math.random() * 10 + 's';
      s.style.animationDelay = -Math.random() * 20 + 's';
      box.appendChild(s);
    }
    hero.insertBefore(box, hero.firstChild);
  }
}

// Ambient glass blobs in each section
(function () {
  if (!window.matchMedia('(min-width: 769px)').matches) return;
  var sets = [['pink', 'gold'], ['gold', 'warm'], ['pink', 'warm']];
  document.querySelectorAll('section, .footer').forEach(function (sec, i) {
    sets[i % 3].concat(['pink']).forEach(function (c, j) {
      var b = document.createElement('span');
      b.className = 'blob ' + c;
      var size = 260 + Math.random() * 220;
      b.style.width = b.style.height = size + 'px';
      b.style.left = (j === 0 ? -8 : j === 1 ? 62 : 30) + Math.random() * 12 + '%';
      b.style.top = (j === 1 ? -10 : 45) + Math.random() * 25 + '%';
      b.style.animationDelay = -Math.random() * 18 + 's';
      b.style.animationDuration = 16 + Math.random() * 10 + 's';
      sec.insertBefore(b, sec.firstChild);
    });
  });
})();

// Gallery lightbox
(function () {
  var lb = document.getElementById('lightbox'); if (!lb) return;
  var items = Array.prototype.slice.call(document.querySelectorAll('.g-item'));
  var img = lb.querySelector('img'), cap = lb.querySelector('figcaption'), idx = 0;
  function show(i) { idx = (i + items.length) % items.length; img.src = items[idx].dataset.src; img.alt = items[idx].dataset.cap; cap.innerHTML = items[idx].dataset.cap; }
  function open(i) { show(i); lb.hidden = false; document.body.style.overflow = 'hidden'; }
  function close() { lb.hidden = true; document.body.style.overflow = ''; }
  items.forEach(function (it, i) { it.addEventListener('click', function () { open(i); }); });
  lb.querySelector('.lb-close').onclick = close;
  lb.querySelector('.lb-prev').onclick = function (e) { e.stopPropagation(); show(idx - 1); };
  lb.querySelector('.lb-next').onclick = function (e) { e.stopPropagation(); show(idx + 1); };
  lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
  document.addEventListener('keydown', function (e) {
    if (lb.hidden) return;
    if (e.key === 'Escape') close(); if (e.key === 'ArrowLeft') show(idx - 1); if (e.key === 'ArrowRight') show(idx + 1);
  });
})();

// Class booking form -> WhatsApp (multi-class bundles)
document.querySelectorAll('.book-form').forEach(function (f) {
  var fmt = function (n) { return n.toLocaleString('en-GH', { minimumFractionDigits: 2, maximumFractionDigits: 2 }); };
  var d2 = +f.dataset.d2, d3 = +f.dataset.d3;
  var track = f.dataset.track || 'baking';
  var boxes = Array.prototype.slice.call(f.querySelectorAll('[name=cls]'));
  var seats = f.querySelector('[name=seats]');
  var q = f.querySelector.bind(f);
  // preselect from ?add=slug or ?add=all
  var add = new URLSearchParams(location.search).get('add');
  if (add) boxes.forEach(function (b) { if (add === 'all' || add.split(',').indexOf(b.value) > -1) b.checked = true; });
  var state = {};
  function calc() {
    var chosen = boxes.filter(function (b) { return b.checked; });
    if (!chosen.length) { chosen = [boxes.filter(function (b) { return b.defaultChecked; })[0] || boxes[0]]; chosen[0].checked = true; }
    var sub = chosen.reduce(function (t, b) { return t + (+b.dataset.fee); }, 0);
    var pct = chosen.length >= 3 ? d3 : chosen.length === 2 ? d2 : 0;
    var n = +seats.value, disc = sub * pct / 100, tot = (sub - disc) * n;
    q('.sub').textContent = fmt(sub);
    var discEl = q('.disc'), discPctEl = q('.disc-pct');
    if (discEl) discEl.textContent = fmt(disc);
    if (discPctEl) discPctEl.textContent = pct;
    var discRow = q('.disc-row'); if (discRow) discRow.hidden = !pct;
    q('.n').textContent = n; q('.tot').textContent = fmt(tot);
    state = { chosen: chosen, sub: sub, pct: pct, disc: disc, n: n, tot: tot };
  }
  boxes.forEach(function (b) { b.addEventListener('change', calc); });
  seats.addEventListener('change', calc); calc();
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var g = function (n) { var el = f.querySelector('[name=' + n + ']'); return el ? el.value.trim() : ''; };
    var sch = f.querySelector('[name=schedule]:checked') || f.querySelector('[name=schedule]');
    var list = state.chosen.map(function (b) { return '   - ' + b.dataset.name + ' (GH₵ ' + fmt(+b.dataset.fee) + ')'; }).join('\n');
    var intent = track === 'pastry' ? "I'd like to book the pastry classes below" : "I'd like to book the bread classes below";
    var msg = "Hello Mystery Bakebite! 👩🏾‍🍳 " + intent + ".\n\n" +
      '• Class' + (state.chosen.length > 1 ? 'es' : '') + ' (1 week each):\n' + list + '\n' +
      (state.pct ? '• Bundle discount: ' + state.pct + '% (− GH₵ ' + fmt(state.disc) + ' per student)\n' : '') +
      '• Recommended daily time: ' + (sch ? sch.value : '') + '\n' +
      '• Preferred start date: ' + (g('date') || 'Flexible') + '\n' +
      '• Number of students: ' + state.n + '\n' +
      '• Estimated total: GH₵ ' + fmt(state.tot) + '\n\n' +
      'Name: ' + g('name') + '\nPhone: ' + g('phone');
    window.open('https://wa.me/233554520532?text=' + encodeURIComponent(msg), '_blank', 'noopener');
  });
});

// Soft fade-out when moving between pages
if (!reduce) {
  document.querySelectorAll('a[href]').forEach(function (a) {
    var h = a.getAttribute('href');
    if (!h || h.charAt(0) === '#' || a.target === '_blank' || a.hasAttribute('download') || /^(https?:|mailto:|tel:)/.test(h) || h.indexOf('#') > 0 && h.split('#')[0] === location.pathname.split('/').pop()) return;
    a.addEventListener('click', function (e) {
      if (e.metaKey || e.ctrlKey || e.shiftKey) return;
      e.preventDefault(); document.body.classList.add('leaving');
      setTimeout(function () { location.href = h; }, 220);
    });
  });
  window.addEventListener('pageshow', function () { document.body.classList.remove('leaving'); });
}
// Flash the total when it changes
document.querySelectorAll('.book-form').forEach(function (f) {
  var t = f.querySelector('.bk-total b');
  f.addEventListener('change', function () { t.classList.remove('bump'); void t.offsetWidth; t.classList.add('bump'); });
});

// Class page sub-nav: reliable anchor scrolling, active state, and horizontal reveal
(function () {
  var allLinks = document.querySelectorAll('.subnav a[href^="#"]');
  if (!allLinks.length) return;
  var links = document.querySelectorAll('.subnav a:not(.sn-book)');
  var navInner = document.querySelector('.subnav .sn-inner');
  var map = {};

  function revealLink(link) {
    if (!navInner || navInner.scrollWidth <= navInner.clientWidth) return;
    var lr = link.getBoundingClientRect(), nr = navInner.getBoundingClientRect();
    if (lr.left < nr.left + 10 || lr.right > nr.right - 10) {
      navInner.scrollTo({ left: navInner.scrollLeft + (lr.left - nr.left) - 24, behavior: reduce ? 'auto' : 'smooth' });
    }
  }
  function setActive(id) {
    links.forEach(function (link) { link.classList.toggle('active', link === map[id]); });
    if (map[id]) revealLink(map[id]);
  }

  // Do not rely on the browser's default anchor calculation under the sticky
  // header and sub-navigation. The target sections already define the correct
  // scroll margin, so this keeps every click aligned below both bars.
  allLinks.forEach(function (link) {
    link.addEventListener('click', function (event) {
      var id = (link.getAttribute('href') || '').slice(1), target = id && document.getElementById(id);
      if (!target) return;
      event.preventDefault();
      target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start', inline: 'nearest' });
      try { history.replaceState(null, '', '#' + id); } catch (ignore) {}
      if (map[id]) setActive(id);
    });
  });

  links.forEach(function (link) { map[link.getAttribute('href').slice(1)] = link; });
  if (!('IntersectionObserver' in window)) { setActive('overview'); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting && map[entry.target.id]) setActive(entry.target.id);
    });
  }, { rootMargin: '-25% 0px -60% 0px', threshold: 0 });
  Object.keys(map).forEach(function (id) {
    var section = document.getElementById(id);
    if (section) io.observe(section);
  });
})();

// Sliding glow pill behind hovered nav item
(function () {
  var nav = document.querySelector('.nav2 .main-nav'), glow = nav && nav.querySelector('.nav-glow'); if (!glow) return;
  var links = nav.querySelectorAll(':scope > .nav-link, :scope > .nav-item > .nav-link');
  function move(el) { var r = el.getBoundingClientRect(), n = nav.getBoundingClientRect(); glow.style.left = (r.left - n.left) + 'px'; glow.style.width = r.width + 'px'; glow.style.opacity = 1; }
  function rest() { var cur = nav.querySelector('.current > .nav-link, .nav-link.current'); if (cur) move(cur); else glow.style.opacity = 0; }
  links.forEach(function (l) { (l.closest('.nav-item') || l).addEventListener('mouseenter', function () { move(l); }); l.addEventListener('focus', function () { move(l); }); });
  nav.addEventListener('mouseleave', function () { if (!nav.querySelector('.has-dd.open')) rest(); });
  setTimeout(rest, 50); addEventListener('resize', rest);
})();

// Home navigation follows sections in page order and keeps the active link in sync.
(function () {
  var page = location.pathname.split('/').pop() || 'index.html';
  if (page !== 'index.html') return;
  var sequence = [
    ['story', 'story'], ['menu', 'menu'], ['classes', 'classes'], ['custom', 'custom'],
    ['reviews', 'reviews'], ['gallery', 'gallery'], ['contact', 'contact']
  ];
  var links = document.querySelectorAll('.nav6 .main-nav [data-key]');
  function sync() {
    var line = Math.min(window.innerHeight * .4, 380);
    var active = 'home';
    sequence.forEach(function (pair) {
      var el = document.getElementById(pair[0]);
      if (el && el.getBoundingClientRect().top <= line) active = pair[1];
    });
    links.forEach(function (a) { a.classList.toggle('current', a.dataset.key === active); });
  }
  var scheduleHomeNav = rafThrottle(sync);
  addEventListener('scroll', scheduleHomeNav, { passive: true });
  addEventListener('resize', scheduleHomeNav);
  sync();
})();

// Show floating WhatsApp button after the first screen
(function () {
  var f = document.querySelector('.wa-float'); if (!f) return;
  function t() { f.classList.toggle('show', window.scrollY > window.innerHeight * 0.6); }
  var scheduleWa = rafThrottle(t);
  addEventListener('scroll', scheduleWa, { passive: true }); t();
})();

// ============ ORDER PAGE ============
(function () {
  var form = document.getElementById('orderForm'); if (!form) return;
  document.documentElement.classList.add('page-order');
  var fmt = function (n) { return n.toLocaleString('en-GH', { minimumFractionDigits: 2, maximumFractionDigits: 2 }); };
  var rows = Array.prototype.slice.call(form.querySelectorAll('.oi'));
  var list = document.querySelector('.cart-list'), empty = document.querySelector('.cart-empty');
  var err = document.querySelector('.cart-err'), bar = document.querySelector('.cart-bar');
  var q = function (sel) { return document.querySelector(sel); };

  function qtyOf(r) { return Math.max(0, Math.min(99, parseInt(r.querySelector('input').value, 10) || 0)); }
  function set(r, v) { r.querySelector('input').value = Math.max(0, Math.min(99, v)); update(); }

  rows.forEach(function (r) {
    r.querySelector('.q-plus').addEventListener('click', function () { set(r, qtyOf(r) + 1); });
    r.querySelector('.q-minus').addEventListener('click', function () { set(r, qtyOf(r) - 1); });
    r.querySelector('input').addEventListener('input', update);
  });

  // preselect from ?add=id and open #cat-
  var add = new URLSearchParams(location.search).get('add');
  if (add) { var r0 = rows.filter(function (r) { return r.dataset.id === add; })[0]; if (r0) { r0.querySelector('input').value = 1; var d = r0.closest('details'); d.open = true; setTimeout(function () { d.scrollIntoView({ behavior: 'smooth', block: 'center' }); }, 300); } }
  if (location.hash.indexOf('#cat-') === 0) { var d2 = document.querySelector(location.hash); if (d2) d2.open = true; }

  // min date = today
  var dt = form.querySelector('[name=date]'); var t = new Date(); t.setMinutes(t.getMinutes() - t.getTimezoneOffset()); dt.min = t.toISOString().slice(0, 10);

  form.querySelectorAll('[name=fulfil]').forEach(function (x) { x.addEventListener('change', update); });
  form.querySelectorAll('[name=pay]').forEach(function (x) { x.addEventListener('change', update); });

  function chosen() { return rows.filter(function (r) { return qtyOf(r) > 0; }); }
  function update() {
    var items = chosen(), sub = 0, n = 0;
    list.innerHTML = '';
    items.forEach(function (r) {
      var qn = qtyOf(r), line = qn * parseFloat(r.dataset.price); sub += line; n += qn;
      var li = document.createElement('li');
      li.innerHTML = '<span class="oli-q">' + qn + '×</span><span class="oli-n">' + r.dataset.name + '<small>' + r.dataset.cat + '</small></span><span class="oli-p">GH₵ ' + fmt(line) + '</span><button type="button" class="oli-x" aria-label="Remove">×</button>';
      li.querySelector('.oli-x').addEventListener('click', function () { set(r, 0); });
      list.appendChild(li);
    });
    empty.hidden = items.length > 0;
    // category counters
    document.querySelectorAll('.ocat').forEach(function (d) {
      var c = 0; d.querySelectorAll('.oi').forEach(function (r) { c += qtyOf(r); r.classList.toggle('on', qtyOf(r) > 0); });
      var b = d.querySelector('.oc-count'); b.textContent = c; b.hidden = !c;
      var tp = d.querySelector('.topping');
      if (tp) tp.hidden = !Array.prototype.some.call(d.querySelectorAll('.oi[data-id$="t"]'), function (r) { return qtyOf(r) > 0; });
    });
    var deliv = form.querySelector('[name=fulfil]:checked').value === 'Delivery';
    form.querySelector('.deliv').hidden = !deliv; q('.c-del').hidden = !deliv;
    var pay = form.querySelector('[name=pay]:checked').value;
    form.querySelector('.momo-net').hidden = pay.indexOf('Mobile Money') < 0;
    q('.c-paym').textContent = pay.indexOf('Mobile Money') > -1 ? 'MoMo, full upfront' : 'Cash on delivery / pickup';
    q('.c-sub').textContent = fmt(sub); q('.c-total').textContent = fmt(sub) + (deliv ? ' + delivery' : '');
    q('.cb-n').textContent = n; q('.cb-t').textContent = fmt(sub); bar.hidden = n === 0;
    err.hidden = true;
    return { items: items, sub: sub, n: n, deliv: deliv, pay: pay };
  }
  update();

  function fail(msg, el) { err.textContent = msg; err.hidden = false; if (el) { el.focus(); el.scrollIntoView({ behavior: 'smooth', block: 'center' }); } }

  var receiptBox = document.getElementById('receiptResult');
  var receiptMarkup = '', receiptFileStamp = '';
  function escReceipt(value) {
    return String(value == null ? '' : value).replace(/[&<>"\']/g, function (ch) {
      var entities = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' };
      return entities[ch];
    });
  }
  function logoDataUrl() {
    // Embedded during the build so the standalone printable receipt always carries the logo.
    return form.dataset.receiptLogo || '';
  }
  function makeReceipt(data) {
    var logo = data.logo ? '<img class="receipt-logo" src="' + data.logo + '" alt="Mystery Bakebite logo">' : '';
    var rows = data.items.map(function (it) {
      return '<tr><td><b>' + escReceipt(it.name) + '</b><small>' + escReceipt(it.category) + '</small></td><td>' + it.qty + '</td><td>GH₵ ' + fmt(it.unit) + '</td><td>GH₵ ' + fmt(it.line) + '</td></tr>';
    }).join('');
    var delivery = data.delivery ? '<div class="sum-row"><span>Delivery fee</span><b>Confirmed on WhatsApp</b></div>' : '<div class="sum-row"><span>Pickup</span><b>Free</b></div>';
    var notes = data.notes ? '<section class="receipt-info"><h3>Order notes</h3><p>' + escReceipt(data.notes).replace(/\n/g, '<br>') + '</p></section>' : '';
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Mystery Bakebite order receipt</title><style>' +
      ' :root{--brown:#3A1F0F;--gold:#D4A437;--pink:#F7B7C8;--cream:#F5E6D6;--warm:#8B5E3C}*{box-sizing:border-box}body{width:80mm;max-width:100vw;margin:0 auto;padding:0;background:#fff;color:var(--brown);font:11px/1.45 Georgia,serif}.receipt{width:80mm;max-width:100%;margin:0 auto;padding:4mm;background:#fff;color:var(--brown);border:0;border-radius:0;box-shadow:none}.brand{display:flex;flex-direction:column;align-items:center;gap:2mm;padding-bottom:3mm;border-bottom:1px dashed rgba(139,94,60,.45);text-align:center}.receipt-logo{display:block;width:36mm;height:36mm;max-width:100%;object-fit:contain;border:0;border-radius:0;background:transparent}.eyebrow{color:var(--warm);font-size:8px;font-weight:bold;letter-spacing:.16em;text-transform:uppercase}.brand h1{margin:1mm 0 0;font-size:15px;line-height:1.15;color:var(--brown)}.slogan{margin:1mm 0 0;color:var(--warm);font-size:9px;font-style:italic}.title{display:flex;align-items:flex-start;flex-direction:column;gap:2mm;margin:4mm 0}.title h2{margin:0;font-size:16px;line-height:1.2}.title p{margin:1mm 0 0;color:var(--warm);font-size:9px}.status{display:inline-block;padding:1.5mm 2mm;border:1px solid var(--gold);border-radius:99px;color:var(--brown);background:rgba(212,164,55,.14);font-size:7px;font-weight:bold;letter-spacing:.08em;text-align:center}.table-wrap{width:100%;overflow:visible}table{width:100%;table-layout:fixed;border-collapse:collapse}th{padding:1.5mm .8mm;text-align:left;color:var(--warm);font-size:7px;letter-spacing:.06em;text-transform:uppercase;border-bottom:1px solid var(--gold)}td{padding:2mm .8mm;border-bottom:1px dashed rgba(139,94,60,.26);vertical-align:top;font-size:8px;overflow-wrap:anywhere}td small{display:block;color:var(--warm);font-size:7px}th:nth-child(1),td:nth-child(1){width:39%}th:nth-child(2),td:nth-child(2){width:9%}th:nth-child(3),td:nth-child(3){width:25%}th:nth-child(4),td:nth-child(4){width:27%}td:nth-child(n+2),th:nth-child(n+2){text-align:right;white-space:nowrap}.summary{width:100%;max-width:none;margin:4mm 0 0;padding:2mm;border:1px solid rgba(212,164,55,.5);border-radius:2mm;background:#fff}.sum-row{display:flex;justify-content:space-between;gap:2mm;padding:1mm 0;color:var(--warm);font-size:8px}.sum-total{display:flex;justify-content:space-between;gap:2mm;padding-top:2mm;margin-top:1mm;border-top:1px solid var(--gold);font-weight:bold;color:var(--brown);font-size:11px}.sum-total b{color:var(--brown)}.receipt-info{margin-top:3mm;padding-top:2mm;border-top:1px dashed rgba(139,94,60,.3)}.receipt-info h3{margin:0 0 1mm;font-size:9px}.receipt-info p{margin:0;color:var(--warm);font-size:8px}.notice{margin:3mm 0 0;padding:2mm;border-left:2px solid var(--gold);background:rgba(212,164,55,.08);color:var(--warm);font-size:8px}.contact{margin-top:3mm;color:var(--warm);font-size:7px;text-align:center;overflow-wrap:anywhere}.actions{margin-top:4mm;display:flex;justify-content:center;gap:2mm;flex-wrap:wrap}.actions button{border:0;border-radius:99px;padding:2mm 3mm;background:var(--brown);color:var(--cream);font:inherit;font-size:9px;font-weight:bold;cursor:pointer}.actions button:hover{background:var(--warm)}@media(max-width:340px){body,.receipt{width:100vw}}@page{size:80mm 250mm;margin:0}@media print{html,body{width:80mm;min-width:80mm;max-width:80mm;margin:0;padding:0;background:#fff}.receipt{width:80mm;max-width:80mm;margin:0;padding:4mm 4mm 6mm;border:0;border-radius:0;box-shadow:none}.actions{display:none}*{-webkit-print-color-adjust:exact;print-color-adjust:exact}}' +
      '</style></head><body><main class="receipt"><header class="brand">' + logo + '<div><span class="eyebrow">Tamale, Ghana</span><h1>Mystery Bakebite</h1><p class="slogan">Unveiling The Uniqueness of A Recipe</p></div></header>' +
      '<section class="title"><div><h2>Order request receipt</h2><p>Prepared ' + escReceipt(data.created) + '</p></div><span class="status">AWAITING WHATSAPP CONFIRMATION</span></section>' +
      '<section class="receipt-info"><h3>Customer</h3><p><b>' + escReceipt(data.name) + '</b><br>' + escReceipt(data.phone) + '</p></section>' +
      '<section class="receipt-info"><h3>Order details</h3><p>' + escReceipt(data.fulfilment) + ' on ' + escReceipt(data.date) + ' at ' + escReceipt(data.time) + (data.delivery && data.area ? '<br>Delivery area: ' + escReceipt(data.area) : '') + '</p></section>' +
      '<div class="table-wrap"><table><thead><tr><th>Item</th><th>Qty</th><th>Unit price</th><th>Line total</th></tr></thead><tbody>' + rows + '</tbody></table></div>' +
      '<section class="summary"><div class="sum-row"><span>Subtotal</span><b>GH₵ ' + fmt(data.subtotal) + '</b></div>' + delivery + '<div class="sum-row"><span>Payment</span><b>' + escReceipt(data.payment) + '</b></div><div class="sum-total"><span>Estimated total</span><b>GH₵ ' + fmt(data.subtotal) + (data.delivery ? ' + delivery' : '') + '</b></div></section>' +
      notes + '<p class="notice">This is an order request receipt, not proof of payment. We will confirm availability, any delivery fee and your final total in the WhatsApp chat.</p>' +
      '<p class="contact">+233 55 452 0532 · mysterybakebite@gmail.com · Tamale, Ghana</p><div class="actions"><button onclick="window.print()">Print or save as PDF</button></div></main></body></html>';
  }
  function saveReceipt() {
    if (!receiptMarkup) return;
    var url = URL.createObjectURL(new Blob([receiptMarkup], { type: 'text/html;charset=utf-8' }));
    var a = document.createElement('a'); a.href = url; a.download = 'Mystery-Bakebite-Order-Receipt-' + receiptFileStamp + '.html';
    document.body.appendChild(a); a.click(); a.remove(); setTimeout(function () { URL.revokeObjectURL(url); }, 60000);
  }
  function openReceiptForPrint() {
    if (!receiptMarkup) return;
    var url = URL.createObjectURL(new Blob([receiptMarkup], { type: 'text/html;charset=utf-8' }));
    window.open(url, '_blank', 'noopener'); setTimeout(function () { URL.revokeObjectURL(url); }, 120000);
  }
  // The receipt is downloaded automatically as soon as it is generated.
  // Printing remains available as a separate POS/PDF action.
  var printReceiptButton = document.getElementById('printReceipt');
  if (printReceiptButton) printReceiptButton.addEventListener('click', openReceiptForPrint);

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var s = update(), g = function (nm) { var el = form.querySelector('[name=' + nm + ']'); return el ? el.value.trim() : ''; };
    if (!s.items.length) return fail('Please add at least one item to your order.', document.querySelector('.ocat summary'));
    if (!g('date')) return fail('Please choose the date you need your order.', form.querySelector('[name=date]'));
    if (s.deliv && !g('area')) return fail('Please enter your delivery area or landmark.', form.querySelector('[name=area]'));
    if (!g('name')) return fail('Please enter your name.', form.querySelector('[name=name]'));
    if (!g('phone')) return fail('Please enter your phone number.', form.querySelector('[name=phone]'));
    var lines = s.items.map(function (r) { var qn = qtyOf(r); return '• ' + qn + ' × ' + r.dataset.name + ' (' + r.dataset.cat + ') = GH₵ ' + fmt(qn * parseFloat(r.dataset.price)); }).join('\n');
    var tp = form.querySelector('.topping:not([hidden]) select');
    var momo = s.pay.indexOf('Mobile Money') > -1;
    var net = form.querySelector('[name=net]:checked');
    var d = new Date(g('date') + 'T00:00:00').toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' });
    var msg = "Hello Mystery Bakebite! 🍩 I'd like to place an order.\n\n" +
      '*ORDER*\n' + lines + '\n' + (tp ? 'Loaf topping: ' + tp.value + '\n' : '') +
      '\nSubtotal: GH₵ ' + fmt(s.sub) + (s.deliv ? ' (+ delivery fee)' : '') + '\n\n' +
      '*' + (s.deliv ? 'DELIVERY' : 'PICKUP') + '*\n' +
      'Date: ' + d + '\nTime: ' + g('time') + '\n' + (s.deliv ? 'Area: ' + g('area') + '\n' : '') + '\n' +
      '*PAYMENT*\n' + (momo ? 'Full payment upfront via Mobile Money (' + (net ? net.value : '') + '). Please send your MoMo details.' : 'Cash on ' + (s.deliv ? 'delivery' : 'pickup')) + '\n\n' +
      '*CUSTOMER*\nName: ' + g('name') + '\nPhone: ' + g('phone') + (g('notes') ? '\nNotes: ' + g('notes') : '');
    var now = new Date();
    var orderItems = s.items.map(function (r) {
      var quantity = qtyOf(r), unit = parseFloat(r.dataset.price);
      var topping = tp && r.dataset.cat === 'Cake Loaves' ? ' (Topping: ' + tp.value + ')' : '';
      return { name: r.dataset.name + topping, category: r.dataset.cat, qty: quantity, unit: unit, line: quantity * unit };
    });
    receiptFileStamp = now.toISOString().slice(0, 16).replace(/[T:]/g, '-');
    receiptMarkup = makeReceipt({
      logo: logoDataUrl(), created: now.toLocaleString('en-GH', { dateStyle: 'medium', timeStyle: 'short' }),
      name: g('name'), phone: g('phone'), fulfilment: s.deliv ? 'Delivery' : 'Pickup', date: d,
      time: g('time'), delivery: s.deliv, area: g('area'), subtotal: s.sub,
      payment: momo ? 'Mobile Money, ' + (net ? net.value : '') + ', full payment upfront' : 'Cash on ' + (s.deliv ? 'delivery' : 'pickup'),
      notes: g('notes'), items: orderItems
    });
    saveReceipt();
    if (receiptBox) { receiptBox.hidden = false; }
    window.open('https://wa.me/233554520532?text=' + encodeURIComponent(msg), '_blank', 'noopener');
    if (receiptBox) setTimeout(function () { receiptBox.scrollIntoView({ behavior: 'smooth', block: 'center' }); }, 120);
  });
})();

// ============ CINEMATIC HOME: story crossfade + subtle parallax ============
(function () {
  var sec = document.querySelector('.cine');
  if (sec) {
    var imgs = Array.prototype.slice.call(sec.querySelectorAll('.cs-img'));
    var panels = Array.prototype.slice.call(sec.querySelectorAll('.cine-panel'));
    function setActive(i) {
      var img = Math.min(i, imgs.length - 1);
      imgs.forEach(function (im, k) { im.classList.toggle('on', k === img); });
      panels.forEach(function (p, k) { p.classList.toggle('active', k === i); });
    }
    if (panels.length && 'IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) setActive(panels.indexOf(e.target)); });
      }, { rootMargin: '-45% 0px -45% 0px' });
      panels.forEach(function (p) { io.observe(p); });
      setActive(0);
    } else {
      panels.forEach(function (p) { p.classList.add('active'); });
      setActive(0);
    }
  }
})();

// subtle scroll parallax for [data-para]
(function () {
  var els = Array.prototype.slice.call(document.querySelectorAll('[data-para]'));
  if (!els.length || reduce || !('requestAnimationFrame' in window)) return;
  var ticking = false;
  function frame() {
    var vh = window.innerHeight;
    els.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.bottom < -200 || r.top > vh + 200) return;
      var d = (r.top + r.height / 2 - vh / 2) / vh;
      el.style.transform = 'translate3d(0,' + (d * parseFloat(el.dataset.para) * 100).toFixed(2) + 'px,0)';
    });
    ticking = false;
  }
  function onScroll() { if (!ticking) { ticking = true; requestAnimationFrame(frame); } }
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll);
  frame();
})();

// ============ MENU PAGE: sticky category chips ============
(function () {
  var bar = document.querySelector('.mchips');
  if (!bar) return;
  var chips = Array.prototype.slice.call(bar.querySelectorAll('.mchip'));
  var targets = chips.map(function (c) { return document.getElementById(c.dataset.cat); });
  function mark(i) {
    chips.forEach(function (c, k) { c.classList.toggle('active', k === i); });
    var c = chips[i];
    if (c && bar.scrollWidth > bar.clientWidth) {
      var cr = c.getBoundingClientRect(), br = bar.getBoundingClientRect();
      if (cr.left < br.left + 12 || cr.right > br.right - 12) {
        bar.scrollTo({ left: bar.scrollLeft + (cr.left - br.left) - 24, behavior: reduce ? 'auto' : 'smooth' });
      }
    }
  }
  chips.forEach(function (c, i) {
    c.addEventListener('click', function (event) {
      var target = targets[i];
      if (!target) return;
      event.preventDefault();
      target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start', inline: 'nearest' });
      try { history.replaceState(null, '', '#' + c.dataset.cat); } catch (ignore) {}
      mark(i);
    });
  });
  var ticking = false;
  function update() {
    var line = bar.getBoundingClientRect().height + 120, best = 0, bestTop = -Infinity;
    targets.forEach(function (t, i) {
      if (!t) return;
      var tp = t.getBoundingClientRect().top;
      if (tp <= line && tp > bestTop + 2) { bestTop = tp; best = i; }
    });
    if (bestTop === -Infinity) {
      var first = Infinity;
      targets.forEach(function (t, i) { if (!t) return; var tp = t.getBoundingClientRect().top; if (tp < first) { first = tp; best = i; } });
    }
    mark(best);
  }
  function onScroll() { if (!ticking) { ticking = true; requestAnimationFrame(function () { ticking = false; update(); }); } }
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll);
  update();
})();
