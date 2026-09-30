import urllib.parse
import os
import json
import html as html_escape
from pathlib import Path

SITE_URL = os.environ.get("SITE_URL", "").strip().rstrip("/")
WA = "https://wa.me/233554520532?text=" + urllib.parse.quote("Hello Mystery Bakebite! I'd like to place an order 🍩")
IC = {
 'wa':'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4zM12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.3c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.3 8.3 0 1 1 12 20.3z"/></svg>',
 'ig':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>',
 'tt':'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.6 5.8A4.3 4.3 0 0 1 15.5 3h-3.1v12.4a2.6 2.6 0 1 1-2.6-2.6c.3 0 .5 0 .8.1V9.7a5.7 5.7 0 1 0 4.9 5.7V9.1a7.3 7.3 0 0 0 4.3 1.4V7.4a4.3 4.3 0 0 1-3.2-1.6z"/></svg>',
 'fb':'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 8V6c0-.9.6-1 1-1h2.5V1.2L14.1 1C10.4 1 9.5 3.8 9.5 5.6V8H7v4h2.5v11H14V12h3.1l.4-4z"/></svg>',
 'yt':'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12a31 31 0 0 0 .5 4.8 3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8zM9.7 15V9l5.8 3-5.8 3z"/></svg>',
 'heart':'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 21s-7.5-4.6-9.6-9.2C.9 8.4 3 4.5 6.7 4.5c2.1 0 3.6 1.2 5.3 3.1 1.7-1.9 3.2-3.1 5.3-3.1 3.7 0 5.8 3.9 4.3 7.3C19.5 16.4 12 21 12 21z"/></svg>',
 'arrow':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 'download':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12m0 0 4-4m-4 4-4-4M5 17v4h14v-4"/></svg>',
 'pin':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>',
 'phone':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
 'mail':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 6 10 7 10-7"/></svg>',
 'bulb':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2V16h5v-.1c0-.8.4-1.5 1-2A6 6 0 0 0 12 3z"/></svg>',
 'brush':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l2.4 5 5.6.8-4 3.9.9 5.6L12 15.6l-4.9 2.7.9-5.6-4-3.9 5.6-.8z"/></svg>',
 'heartline':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21s-7.5-4.6-9.6-9.2C.9 8.4 3 4.5 6.7 4.5c2.1 0 3.6 1.2 5.3 3.1 1.7-1.9 3.2-3.1 5.3-3.1 3.7 0 5.8 3.9 4.3 7.3C19.5 16.4 12 21 12 21z"/></svg>',
 'cap':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c0 1.5 3 3 6 3s6-1.5 6-3v-5M22 9v6"/></svg>',
 'whisk':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M14 10 21 3M4.5 19.5c-2-2-1.2-7.8 2.5-11.5s7-3 7-3 .7 3.3-3 7-9.5 4.5-6.5 7.5zM9 7c-1 2-1.3 5 0 8"/></svg>',
 'clock':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 'truck':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M1 5h13v11H1zM14 9h4l4 4v3h-8z"/><circle cx="5.5" cy="18.5" r="2"/><circle cx="18" cy="18.5" r="2"/></svg>',
 'bag':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M5 8h14l-1 13H6zM9 8V6a3 3 0 0 1 6 0v2"/></svg>',
 'card':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="6" y="2" width="12" height="20" rx="2"/><path d="M10 18h4"/></svg>',
 'cal':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M8 2v4M16 2v4"/></svg>',
 'cash':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2.5"/><path d="M6 9v.01M18 15v.01"/></svg>',
 'lock':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>',
 'gift':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="8" width="18" height="4"/><path d="M5 12v9h14v-9M12 8v13M12 8S10.5 3 8 4s0 4 4 4zm0 0s1.5-5 4-4-0 4-4 4z"/></svg>',
}
C='<span class="cedi">GH₵</span>'
def acc(v): return f'GH₵ {float(v):,.2f}'
def wa_item(cat, item, price):
    msg = f"Hello Mystery Bakebite! 🍩 I'd like to order:\n\n• {item} ({cat}): GH₵{price}{" (plain / with toppings. Please specify topping: Oreo, chocolate or raisin)" if "/" in price else ""}\n\nQuantity: \nDate needed: \nPickup or delivery (area in Tamale): \nName: "
    return "https://wa.me/233554520532?text=" + urllib.parse.quote(msg)
def wa_cat(cat):
    msg = f"Hello Mystery Bakebite! 🍩 I'm interested in your {cat}. Could you help me with an order?\n\nDate needed: \nPickup or delivery: "
    return "https://wa.me/233554520532?text=" + urllib.parse.quote(msg)
def header():
    def dd(label, key, items, foot=''):
        li=''.join(f'<a class="dd-link" href="{h}"><span class="dd-ic">{ic}</span><span><b>{t}</b><small>{d}</small></span></a>' for h,ic,t,d in items)
        return f"""<div class="nav-item has-dd" data-key="{key}"><button class="nav-link dd-btn" aria-expanded="false" aria-haspopup="true">{label}<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="m6 9 6 6 6-6"/></svg></button>
<div class="dd-panel"><div class="dd-inner">{li}</div>{foot}</div></div>"""
    def mega():
        cards=''.join(f'<a class="mg-card s-{c["slug"]}" href="class-{c["slug"]}.html"><span class="mg-num">{c["num"]}</span><span class="mg-lvl">{c["level"]}</span><b>{c["title"]}</b><span class="mg-meta">1 week · 6 recipes</span><span class="mg-fee">{acc(c["fee"])}</span></a>' for c in CLASSES)
        return f"""<div class="nav-item has-dd" data-key="classes"><button class="nav-link dd-btn" aria-expanded="false" aria-haspopup="true">Classes<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="m6 9 6 6 6-6"/></svg></button>
<div class="dd-panel dd-mega"><div class="mg-head"><div><p class="mg-kicker">Baking classes</p><p class="mg-script">Learn. Bake. Create.</p></div><a class="mg-all" href="classes.html">All classes →</a></div>
<div class="mg-grid">{cards}</div><a class="dd-foot" href="classes.html#{CLASSES[0]['slug']}">Bundle &amp; save: {BUNDLE[2]}% off 2 classes · {BUNDLE[3]}% off all 3 →</a></div></div>"""
    cls_items=[(f'class-{c["slug"]}.html', f'<b class="dd-n">{c["num"]}</b>', f'{c["level"]}', f'{c["title"]} · {acc(c["fee"])}') for c in CLASSES]
    cls_foot=f'<a class="dd-foot" href="classes.html">View all classes &amp; bundles (save up to {BUNDLE[3]}%) →</a>'
    ord_items=[('order.html',IC['whisk'],'How to Order','Three easy steps on WhatsApp'),('order.html#payment',IC['card'],'Payment','Cash, or full MoMo payment upfront'),('order.html#info',IC['clock'],'Ordering Info','Notice, delivery &amp; hours'),('index.html#custom',IC['gift'],'Custom Orders','Cakes and party packs')]
    about_items=[('index.html#story',IC['heartline'],'Our Story','Meet Emmanuella'),('index.html#gallery',IC['ig'],'Gallery','Fresh from the kitchen'),('index.html#reviews',IC['heart'],'Reviews','What customers say')]
    nav=(f'<a class="nav-link" href="menu.html" data-key="menu">Menu</a>'
         + mega()
         + dd('Order','order',ord_items)
         + dd('About','about',about_items))
    # mobile drawer
    def group(title, items): return f'<div class="dr-group"><p class="dr-h">{title}</p>'+''.join(f'<a href="{h}">{t}</a>' for h,_,t,_d in items)+'</div>'
    soc=''.join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n}">{IC[k]}</a>' for k,n,u in SOC)
    lv=''.join(f'<a class="dr-lv" href="class-{c["slug"]}.html"><b>{c["num"]}</b>{c["level"]}</a>' for c in CLASSES)
    drawer=f"""<div class="drawer" id="drawer" aria-hidden="true"><div class="dr-backdrop" data-close></div>
<aside class="dr-panel" role="dialog" aria-label="Menu"><div class="dr-top"><a class="brand" href="index.html"><img class="brand-logo" src="assets/logo.webp" alt=""><span class="brand-name"><span class="brand-mystery">Mystery</span><span class="brand-bakebite">Bakebite</span></span></a><button class="dr-close" data-close aria-label="Close menu">×</button></div>
<p class="dr-slogan">Unveiling The Uniqueness of A Recipe</p>
<nav class="dr-nav"><a class="dr-main" href="index.html">Home</a><a class="dr-main" href="index.html#story">Our Story</a><a class="dr-main" href="menu.html">Menu</a><a class="dr-main" href="classes.html">Classes</a>
<div class="dr-levels">{lv}</div>
<a class="dr-main" href="index.html#custom">Custom Orders</a><a class="dr-main" href="index.html#reviews">Reviews</a><a class="dr-main" href="index.html#gallery">Gallery</a><a class="dr-main" href="order.html">Order</a><a class="dr-main" href="index.html#contact">Contact</a></nav>
<div class="dr-bottom"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{IC['wa']} Order on WhatsApp</a><div class="dr-soc">{soc}</div><p>Open daily · 8am to 7pm · Tamale</p></div>
</aside></div>"""
    flat=[('index.html','Home','home'),('index.html#story','Our Story','story'),('menu.html','Menu','menu'),('classes.html','Classes','classes'),('index.html#custom','Custom Orders','custom'),('index.html#reviews','Reviews','reviews'),('index.html#gallery','Gallery','gallery'),('order.html','Order','order'),('index.html#contact','Contact','contact')]
    links=''.join(f'<a class="nav-link" href="{h}" data-key="{k}">{t}</a>' for h,t,k in flat)
    return f"""<header class="site-header nav5 nav6"><div class="wrap nav5-inner">
<a class="brand" href="index.html"><img class="brand-logo" src="assets/logo.webp" alt="Mystery Bakebite logo"><span class="brand-name"><span class="brand-mystery">Mystery</span><span class="brand-bakebite">Bakebite</span></span></a>
<nav class="main-nav" aria-label="Main">{links}</nav>
<a class="btn btn-wa header-wa" href="{WA}" target="_blank" rel="noopener">{IC['wa']}<span class="wa-label">Order on WhatsApp</span></a>
<button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="drawer"><span></span><span></span><span></span></button>
</div></header>{drawer}"""

SOC=[('tt','TikTok','https://www.tiktok.com/@mysterybakebite'),('ig','Instagram','https://www.instagram.com/mysterybakebite'),('fb','Facebook','https://www.facebook.com/mysterybakebite'),('yt','YouTube','https://www.youtube.com/@mysterybakebite')]
def footer():
    s=''.join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n}">{IC[k]}</a>' for k,n,u in SOC)
    cats=[('milky','Milky Doughnuts'),('slices','Cake Slices'),('cupcakes','Cupcakes'),('parfait','Cake Parfait'),('cookies','Cookies'),('loaves','Cake Loaves')]
    ml=''.join(f'<li><a href="menu.html#{a}">{b}</a></li>' for a,b in cats)
    return f'''<footer class="footer" id="contact">
<div class="f-cta"><div class="wrap f-cta-inner"><div><p class="f-cta-script">Craving something sweet?</p><p class="f-cta-sub">Send us a message and we'll bake it fresh for you.</p></div>
<a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{IC['wa']} Chat on WhatsApp</a></div></div>
<div class="wrap"><div class="footer-grid">
<div class="f-brand"><a class="brand" href="index.html"><img class="f-logo" src="assets/logo.webp" alt="Mystery Bakebite logo"><span class="brand-name"><span class="brand-mystery">Mystery</span><span class="brand-bakebite">Bakebite</span></span></a>
<p class="f-tag">Unveiling The Uniqueness of A Recipe</p>
<p>Every batch starts in Emmanuella's kitchen in Tamale: small, handmade and never rushed. Baking, training and creative custom orders.</p>
<div class="socials">{s}</div></div>
<div><h3 class="f-h">The Menu</h3><ul class="f-links">{ml}<li><a href="menu.html" class="f-more">Full price list →</a></li></ul></div>
<div><h3 class="f-h">Bakery</h3><ul class="f-links"><li><a href="order.html">How to Order</a></li><li><a href="order.html#info">Ordering Info</a></li><li><a href="order.html#payment">Payment Options</a></li><li><a href="index.html#gallery">Gallery</a></li><li><a href="index.html#reviews">Reviews</a></li><li><a href="classes.html">Baking Classes</a></li><li><a href="index.html#custom">Custom Orders</a></li><li><a href="index.html#story">Our Story</a></li><li><a href="assets/price-list-current.jpg" download="Mystery-Bakebite-Current-Menu.jpg">Download Menu</a></li></ul></div>
<div><h3 class="f-h">Visit &amp; Contact</h3><ul class="f-list">
<li>{IC['wa']}<a href="{WA}" target="_blank" rel="noopener">+233 55 452 0532</a></li>
<li>{IC['mail']}<a href="mailto:mysterybakebite@gmail.com">mysterybakebite@gmail.com</a></li>
<li>{IC['pin']}<span>Tamale, Northern Ghana</span></li>
<li>{IC['clock']}<span>Mon to Sun, 8am to 7pm</span></li></ul>
<div class="f-qr"><img src="assets/qr.jpg" alt="WhatsApp QR code"><span>Scan to<br>order</span></div></div>
</div></div>
<div class="f-bottom"><div class="wrap f-bottom-inner">
<p class="small">© 2026 Mystery Bakebite. All rights reserved.</p>
<p class="love">{IC['heart']} Baked with Love, Especially for You</p>
<a class="to-top" href="#top">Back to top ↑</a></div></div></footer>
<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{IC['wa']}</a>
<script src="js/main.js"></script></body></html>'''
def head(title, desc, lux=True, page='index.html', business=False, social_image='assets/lux-hero.jpg'):
    title = str(title)
    desc = ' '.join(str(desc).split())
    safe_title = html_escape.escape(title, quote=True)
    safe_desc = html_escape.escape(desc, quote=True)
    canonical = ''
    social_url = ''
    social_img = ''
    if SITE_URL:
        social_url = SITE_URL + ('/' if page.lstrip('/') == 'index.html' else '/' + page.lstrip('/'))
        social_img = SITE_URL + '/' + social_image.lstrip('/')
        canonical = f'<link rel="canonical" href="{html_escape.escape(social_url, quote=True)}">'
    og = (f'<meta property="og:type" content="website"><meta property="og:site_name" content="Mystery Bakebite">'
          f'<meta property="og:locale" content="en_GH"><meta property="og:title" content="{safe_title}">'
          f'<meta property="og:description" content="{safe_desc}">')
    twitter = (f'<meta name="twitter:card" content="{"summary_large_image" if social_img else "summary"}">'
               f'<meta name="twitter:title" content="{safe_title}"><meta name="twitter:description" content="{safe_desc}">')
    if social_url:
        og += f'<meta property="og:url" content="{html_escape.escape(social_url, quote=True)}"><meta property="og:image" content="{html_escape.escape(social_img, quote=True)}"><meta property="og:image:alt" content="Mystery Bakebite bakery in Tamale">'
        twitter += f'<meta name="twitter:image" content="{html_escape.escape(social_img, quote=True)}">'
    schema = ''
    if business:
        bakery = {
            '@context': 'https://schema.org', '@type': 'Bakery', 'name': 'Mystery Bakebite',
            'description': 'Home bakery in Tamale, Northern Ghana, offering handmade baked goods, classes and custom orders.',
            'telephone': '+233554520532', 'email': 'mysterybakebite@gmail.com',
            'address': {'@type': 'PostalAddress', 'addressLocality': 'Tamale', 'addressRegion': 'Northern Region', 'addressCountry': 'GH'},
            'areaServed': {'@type': 'City', 'name': 'Tamale'},
            'openingHoursSpecification': [{'@type': 'OpeningHoursSpecification',
                'dayOfWeek': ['https://schema.org/Monday', 'https://schema.org/Tuesday', 'https://schema.org/Wednesday', 'https://schema.org/Thursday', 'https://schema.org/Friday', 'https://schema.org/Saturday', 'https://schema.org/Sunday'],
                'opens': '08:00', 'closes': '19:00'}],
            'sameAs': [url for _key, _name, url in SOC]
        }
        if SITE_URL:
            bakery['url'] = SITE_URL + '/'
            bakery['image'] = SITE_URL + '/assets/logo.webp'
        schema = '<script type="application/ld+json">' + json.dumps(bakery, ensure_ascii=False) + '</script>'
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{safe_title}</title><meta name="description" content="{safe_desc}"><meta name="theme-color" content="#3A1F0F">{canonical}{og}{twitter}<link rel="icon" href="assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">{"<link rel=\"stylesheet\" href=\"css/lux.css\">" if lux else ""}{schema}</head><body id="top">'''
DIV=f'<div class="divider">{IC["heart"]}</div>'


INFO_ITEMS=[('clock','Order notice','Doughnuts, cookies &amp; chips: <b>order 24 hrs ahead</b>. Custom &amp; celebration cakes: <b>3 to 5 days</b>.'),
 ('truck','Delivery in Tamale','Delivery across Tamale. The fee depends on your area and is <b>confirmed on WhatsApp</b> with your order total.'),
 ('bag','Pickup','Free pickup in Tamale at an agreed time. The exact location is shared when your order is confirmed.'),
 ('card','Payment','<b>Cash on delivery or pickup</b>, or <b>full payment upfront via Mobile Money</b>. See payment options below.'),
 ('cal','Opening hours','Open <b>every day, Monday to Sunday, 8am to 7pm</b>. Messages sent after hours are answered the next morning.'),
 ('gift','Custom &amp; bulk','Parties, weddings, office treats and gift boxes. Tell us your theme, guest count and budget.')]
def info_block(extra_cls=''):
    cards=''.join(f'<div class="info-card reveal"><div class="info-ic">{IC[i]}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i,t,d in INFO_ITEMS)
    return f'''<section class="info {extra_cls}" id="info"><div class="wrap"><div class="sec-head reveal"><span class="kicker">Good to know</span><h2 class="sec-title">Ordering info</h2><p class="sec-sub">Everything you need before you message us.</p>{DIV}</div>
<div class="info-grid">{cards}</div></div></section>'''


def payment_block():
    return f"""<section class="payment" id="payment"><div class="wrap"><div class="sec-head reveal"><span class="kicker">Payment</span><h2 class="sec-title">Two simple ways to pay</h2><p class="sec-sub">Choose what suits you when you place your order on WhatsApp.</p>{DIV}</div>
<div class="pay-grid">
<article class="pay-card reveal"><span class="pay-num">Option 1</span><div class="pay-ic">{IC['cash']}</div><h3>Cash on Delivery or Pickup</h3>
<p>Pay in cash when your order arrives or when you collect it. No payment needed before we bake.</p>
<ul class="ticks"><li>Pay the rider on delivery, or pay at pickup</li><li>Please have the exact amount ready</li><li>Delivery fee confirmed on WhatsApp</li></ul></article>
<article class="pay-card featured reveal"><span class="pay-num">Option 2</span><div class="pay-ic">{IC['card']}</div><h3>Full Payment Upfront</h3>
<p>Pay the full amount in advance through <b>Mobile Money (MoMo)</b>. Your order is confirmed as soon as payment is received.</p>
<ol class="pay-steps"><li>Send your order on WhatsApp</li><li>We reply with your total and our MoMo details</li><li>Send the payment and share the screenshot or reference</li><li>We confirm and start baking</li></ol>
<div class="momo-row"><span class="momo">MTN MoMo</span><span class="momo">Telecel Cash</span><span class="momo">AT Money</span></div></article>
</div>
<p class="pay-note">{IC['lock']} For your safety, only send MoMo payments to the number and name we confirm in our WhatsApp chat.</p>
</div></section>"""

# NOTE: SAMPLE testimonials. Replace with real customer words (with permission) before launch.
TESTIMONIALS=[
 ("The milky donuts are unreal. Soft, fresh and so much cream inside. My whole office now asks me to order every Friday.","Abena","Tamale","milky"),
 ("Ordered a custom birthday cake for my daughter and it was exactly what I pictured. Emmanuella was patient with every detail.","Fuseini","Tamale","slices"),
 ("I joined a baking class as a complete beginner. Now I bake cupcakes for my family and even take small orders.","Rahinatu","Class student","cupcakes"),
 ("Ordering on WhatsApp was so easy. Paid with MoMo, got my parfaits on time and they were beautifully packed.","Kwame","Tamale","parfait"),
]

# NOTE: SAMPLE reviews below. Replace with real customer words (with permission) before launch.
TESTIMONIALS += [
 ("Best bofrot I've had outside my grandmother's kitchen. Soft, light and not oily at all.","Adwoa","Tamale","balls"),
 ("The red velvet slice was so moist. I came back the next day for the tasting box.","Yakubu","Tamale","slices"),
 ("Ordered 12 cupcakes for my son's party and every child wanted a second one.","Mariam","Tamale","cupcakes"),
 ("The banana loaf with chocolate topping is my weekend treat now. Always fresh.","Kofi","Tamale","loaves"),
 ("Cookies arrived warm and perfectly packed. The mixed box is great for sharing.","Esi","Tamale","cookies"),
 ("I took the Beginner class and finally understand how to knead dough properly.","Zainab","Class student","balls"),
 ("Her parfaits are beautiful and taste even better. Perfect for our church event.","Ama","Tamale","parfait"),
 ("Chips are crunchy and well seasoned. My kids finish the 500g pack in a day.","Iddrisu","Tamale","chips"),
 ("Delivery was right on time and the rider was very polite. Will order again.","Akosua","Tamale","milky"),
 ("The custom cake for our anniversary looked exactly like the picture I sent.","Sulemana","Tamale","slices"),
 ("Milky donuts with strawberry cream are my absolute favourite. So generous!","Efua","Tamale","milky"),
 ("Paid upfront with MoMo and got a confirmation straight away. Very professional.","Abdul-Rahman","Tamale","parfait"),
 ("The Intermediate class taught me butter bread. My family can't stop eating it.","Grace","Class student","loaves"),
 ("We ordered party packs of donut balls for our office. Gone in ten minutes.","Mohammed","Tamale","balls"),
 ("Emmanuella answers every question patiently. You can tell she loves what she does.","Linda","Tamale","cupcakes"),
 ("The chocolate chip cookies are chewy in the middle and crisp at the edges. Perfect.","Nana","Tamale","cookies"),
 ("I ordered a tasting box to try all the flavours. Lemon surprised me the most!","Awal","Tamale","slices"),
 ("Clean kitchen, small group and lots of hands-on time. Worth every cedi.","Salamatu","Class student","cupcakes"),
 ("The vanilla loaf is soft and not too sweet. Great with tea in the morning.","Yaw","Tamale","loaves"),
 ("My naming ceremony guests kept asking where the cupcakes came from.","Hawa","Tamale","cupcakes"),
 ("Fast replies on WhatsApp and the pickup was easy to arrange. Five stars.","Kwabena","Tamale","milky"),
 ("The Advanced class sourdough session changed how I bake. Loved it.","Patience","Class student","loaves"),
 ("The thank-you card in the box was such a sweet personal touch.","Rashida","Tamale","parfait"),
 ("Butter cookies taste homemade in the best way. My mum loves them.","Emmanuel","Tamale","cookies"),
 ("Consistent quality every single time I order. That is rare.","Fatima","Tamale","milky"),
 ("Our office Friday treats are now always from Mystery Bakebite.","Kojo","Tamale","balls"),
 ("I gifted a cupcake box to a friend and she ordered her own the next week.","Adjoa","Tamale","cupcakes"),
 ("Cake parfaits are the perfect size for a sweet craving after lunch.","Alhassan","Tamale","parfait"),
 ("Great value for the quality. The 12 piece milky donut box is a steal.","Selina","Tamale","milky"),
 ("From ordering to the last bite, everything felt personal and made with love.","Issah","Tamale","slices"),
]

def testimonials_block():
    cards=''.join(f"""<figure class="t-card"><span class="t-sample-chip">Sample quote</span><blockquote>“{q}”</blockquote><figcaption><img src="assets/{img}.webp" alt="" loading="lazy"><span><b>{n}</b><small>{w}</small></span></figcaption></figure>""" for q,n,w,img in TESTIMONIALS)
    cards_dup=cards.replace('<figure class="t-card">','<figure class="t-card" aria-hidden="true">')
    return f"""<section class="testimonials on-dark" id="reviews"><div class="wrap"><div class="sec-head reveal"><span class="kicker">Review preview</span><h2 class="sec-title">Customer review carousel preview</h2>{DIV}</div>
<p class="review-preview-note" role="note">Preview only. The quotes below are sample copy, not verified customer reviews. Replace them with customer-approved quotes before publication.</p>
<div class="review-motion-controls"><button class="review-motion-toggle" type="button" id="reviewsMotionToggle" aria-controls="reviewsTrack" aria-pressed="false">Pause reviews</button></div>
<div class="t-carousel" role="region" aria-label="Sample customer review carousel preview"><div class="t-track" id="reviewsTrack">{cards}{cards_dup}</div></div>
<p class="t-cta">Tried our bakes? <a href="{WA_REVIEW}" target="_blank" rel="noopener">Send us your review on WhatsApp</a></p></div></section>"""

GALLERY=[('milky','Milky doughnuts','wide'),('founder','Emmanuella at work','tall'),('parfait','Cake parfaits',''),('cupcakes','Cupcake box',''),
 ('slices','Signature cake slices','wide'),('thank-you','Our thank-you card','tall'),('balls','Doughnut balls',''),('cookies','Chocolate chip cookies',''),
 ('loaves','Banana &amp; vanilla loaves','wide'),('chips','Fried &amp; baked chips','wide')]
def gallery_block():
    items=''.join(f"""<button class="g-item {c} reveal" data-src="assets/{sl}.webp" data-cap="{cap}"><img src="assets/{sl}.webp" alt="{cap}" loading="lazy"><span class="g-cap">{cap}</span></button>""" for sl,cap,c in GALLERY)
    return f"""<section class="gallery" id="gallery"><div class="wrap"><div class="sec-head reveal"><span class="kicker">Gallery</span><h2 class="sec-title">Fresh from the kitchen</h2><p class="sec-sub">A peek at recent bakes. Tap any photo to view it larger. More every day on <a href="https://www.instagram.com/mysterybakebite" target="_blank" rel="noopener">@mysterybakebite</a>.</p>{DIV}</div>
<div class="g-grid">{items}</div></div></section>
<div class="lightbox" id="lightbox" hidden><button class="lb-close" aria-label="Close">×</button><button class="lb-prev" aria-label="Previous">‹</button><figure><img alt=""><figcaption></figcaption></figure><button class="lb-next" aria-label="Next">›</button></div>"""

# ---- menu data (current published menu prices)
MENU=[
 ('milky','Milky Doughnuts',None,30,True,[('Milky donuts, 2 pcs','30'),('Milky donuts, 3 pcs','42'),('Milky donuts, 6 pcs','75'),('Milky donuts, 12 pcs','140',1)]),
 ('balls','Doughnut Balls &amp; Mini Doughnuts',None,30,True,[('Mini donuts, pack of 10','35'),('Donut balls, pack of 12','30'),('Donut balls, party pack of 25','55',1)]),
 ('slices','Cake Slices',None,35,False,[('Classic slice (vanilla or banana)','35'),('Signature slice (chocolate, red velvet, carrot or lemon)','40'),('Tasting box, 4 half-slices, all flavours','70'),('Full flavour box, 4 full slices, one of each','130')]),
 ('loaves','Cake Loaves','Plain / with toppings: Oreo, chocolate or raisin',35,False,[('Banana loaf, big','70 / GH₵85'),('Vanilla loaf, big','65 / GH₵80'),('Banana loaf, small','35 / GH₵45'),('Vanilla loaf, small','35 / GH₵45')]),
 ('chips','Fried &amp; Baked Chips',None,30,False,[('Fried and baked chips','30'),('Large (500g)','70')]),
 ('parfait','Cake Parfait',None,35,False,[('Cake parfait (cup)','35')]),
 ('cookies','Cookies',None,30,True,[('Chocolate chip, pack of 6','40'),('Butter cookies, pack of 6','30'),('Mixed cookie box, 12 pcs','65',1)]),
 ('cupcakes','Cupcakes',None,75,False,[('6 pieces (box)','75'),('12 pieces (box)','140')]),
]
cards=''
for slug,name,note,frm,new,items in MENU:
    b='<span class="badge-new">NEW</span>' if new else ''
    cards+=f'''<div class="mcard reveal">{b}<a href="menu.html#{slug}" class="mcard-link" aria-label="{name} prices"></a><figure><img src="assets/{slug}.webp" alt="{name}" loading="lazy"></figure>
<div class="mcard-body"><h3>{name}</h3><span class="from">from <span class="price">{C}{frm}</span></span><div class="mcard-actions"><span class="more">See prices {IC['arrow']}</span><a class="order-btn" href="order.html#cat-{slug}">{IC['wa']}<span>Order</span></a></div></div></div>'''

VAL=[('bulb','Quality'),('brush','Creativity'),('heartline','Passion'),('cap','Education')]
vals=''.join(f'<span class="vbadge">{IC[i]}{t}</span>' for i,t in VAL)
TILES=[('milky','Cream-filled milky donuts'),('parfait','Layered cake parfaits'),('cupcakes','Swirled cupcakes'),('slices','Signature cake slices')]
tiles=''.join(f'<a class="tile reveal" href="https://www.instagram.com/mysterybakebite" target="_blank" rel="noopener"><img src="assets/{s}.webp" alt="{a}" loading="lazy"><div class="ov">{IC["ig"]}<b>{a}</b></div></a>' for s,a in TILES)
def wa_msg(m): return "https://wa.me/233554520532?text=" + urllib.parse.quote(m)
WA_CLASS = wa_msg("Hello Mystery Bakebite! 👩🏾‍🍳 I'd like to book a baking class.\n\nName: \nClass I'm interested in: \nExperience level (beginner / some experience): \nPreferred dates: ")
WA_CUSTOM = wa_msg("Hello Mystery Bakebite! 🎂 I'd like to request a custom order.\n\nOccasion: \nDate needed: \nNumber of guests / servings: \nTheme or colours: \nBudget (GH₵): \nPickup or delivery: ")
WA_REVIEW = wa_msg("Hello Mystery Bakebite! 💬 I'd like to share a review.\n\nWhat I ordered: \nMy review: \nName (as you'd like it shown): ")
info_cards=''.join(f'<div class="info-card reveal"><div class="info-ic">{IC[i]}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i,t,d in INFO_ITEMS)


# ============================================================
# CLASSES  (fees, durations, spaces are PLACEHOLDERS: edit here)
# ============================================================
CLASSES=[
 dict(slug='beginner', num='01', level='Beginner', cat='Basic', title='Local Ghanaian Bread-Making', img='balls',
  short='Master the Ghanaian classics and the fundamentals of dough.',
  purpose='Introduce beginners to fundamental Ghanaian bread-making techniques, basic dough preparation, shaping, frying, baking, and ingredient handling.',
  recipes=['Ghanaian Sugar Bread','Ghanaian Tea Bread','Bofrot (Togbei / Ghanaian Puff Puff)','Ghanaian Coconut Bread','Ghanaian Rock Buns','Atwemo (Twisted Fried Dough)'],
  learn=['Measuring and handling flour, yeast, sugar and fats','Mixing and kneading by hand','Proofing: how to tell when dough is ready','Shaping loaves, buns and twists','Deep-frying safely for bofrot and atwemo','Baking temperatures and checking doneness'],
  skill='No experience needed. Perfect if you have never baked bread before.',
  duration='1 week · Mon to Fri', time='9:00am to 1:00pm', hours='4 hours a day', fee='750', spaces='Small group, up to 8 students'),
 dict(slug='intermediate', num='02', level='Intermediate', cat='Intermediate', title='Butter Bread &amp; Wheat Bread', img='loaves',
  short='Richer doughs, wheat flours and neater shaping.',
  purpose='Build on basic baking skills by introducing richer doughs, wheat-based breads, enriched breads, shaping techniques, and more advanced preparation methods.',
  recipes=['Rich Butter Bread','Whole Meal Wheat Bread','Soft Buttermilk Rolls','Wheat Sandwich Baguettes','Cinnamon Swirl Butter Loaf','Wholewheat Burger Buns'],
  learn=['Working with enriched doughs (butter, milk, eggs)','Baking with whole meal and wholewheat flour','Windowpane test and dough strength','Rolling, filling and swirling loaves','Uniform rolls, buns and baguette shaping','Getting soft crumbs and golden crusts'],
  skill='Completed our Beginner class, or comfortable making a basic yeast dough.',
  duration='1 week · Mon to Fri', time='9:00am to 2:00pm', hours='5 hours a day', fee='950', spaces='Small group, up to 6 students'),
 dict(slug='advanced', num='03', level='Advanced', cat='Advanced', title='International Bread Varieties', img='slices',
  short='Artisan fermentation and breads from around the world.',
  purpose='Introduce advanced bread-making techniques and internationally recognized bread varieties, including fermentation, artisan shaping, specialty dough preparation, and different baking methods.',
  recipes=['Artisan Sourdough Boule','Classic French Baguette','Rosemary Focaccia','Braided Challah','Skillet Naan','New York-Style Bagels'],
  learn=['Building and feeding a sourdough starter','Long and cold fermentation','High-hydration dough handling','Artisan scoring, braiding and shaping','Boiling, skillet and steam baking methods','Planning a bakery-style production schedule'],
  skill='Completed our Intermediate class, or confident with enriched and wheat doughs.',
  duration='1 week · Mon to Fri', time='9:00am to 3:00pm', hours='6 hours a day', fee='1150', spaces='Small group, up to 6 students'),
]
BUNDLE={2:15,3:25}  # number of classes : discount %
CLASS_INCLUDED=['All ingredients and equipment','Printed recipe booklet for all 6 recipes','Apron to use during class','Take home everything you bake','Light refreshments','Certificate of completion']
CLASS_BRING=['A notebook and pen','Containers or a bag to carry your bakes home','Hair tie or cap, and closed shoes','An appetite to learn!']
CLASS_SCHEDULES=['Weekday mornings (8am to 1pm)','Weekday afternoons (1pm to 7pm)','Weekends (Saturday and Sunday)']

def stage_path(active=None):
    out=''
    for i,c in enumerate(CLASSES):
        cls='on' if active==c['slug'] else ''
        out+=f'<a class="path-step {cls}" href="class-{c["slug"]}.html"><span class="ps-num">{c["num"]}</span><span class="ps-lvl">{c["level"]}</span></a>'
        if i<2: out+='<span class="path-arrow" aria-hidden="true">→</span>'
    return f'<nav class="pathway" aria-label="Learning pathway">{out}</nav>'

def classes_teaser():
    tiles=''.join(f"""<a class="stage-tile s-{c['slug']} reveal" href="classes.html#{c['slug']}"><span class="st-num">{c['num']}</span><span class="st-lvl">{c['level']}</span><h3>{c['title']}</h3><p>{c['short']}</p><span class="st-meta">1 week · {c['time']}<br>6 recipes · {acc(c['fee'])}</span><span class="more">View class {IC['arrow']}</span></a>""" for c in CLASSES)
    return f"""<section class="classes-teaser on-dark" id="classes"><div class="wrap"><div class="sec-head reveal"><span class="kicker">Baking classes</span><h2 class="sec-title">Learn. Bake. Create.</h2><p class="sec-script">Unveiling The Uniqueness of A Recipe</p><p class="sec-sub">Hands-on, in-person bread-making classes in Tamale. Three stages, one pathway from your first dough to artisan loaves.</p>{DIV}</div>
{stage_path(TRACKS['bread'])}
<div class="stage-grid">{tiles}</div>
<div class="menu-ctas"><a class="btn btn-wa" href="classes.html">{IC['cap']} Explore all classes</a></div></div></section>"""

FOR_WHOM={
 'beginner':['You have never baked bread, or only a little','You want to master Ghanaian favourites at home','You are thinking about selling bread or snacks'],
 'intermediate':['You have done our Beginner class or bake basic doughs','You want softer, richer and healthier wheat breads','You want neater shaping for home or small business'],
 'advanced':['You have done our Intermediate class or bake confidently','You want to learn artisan and international breads','You are ready for sourdough and long fermentation'],
}
# ============================================================
# CLASS TRACKS: shared dark-luxe templates (bread + pastry)
# ============================================================
PASTRY_NOTICE = 'Our pastry recipe list and fees are being finalised. Listed fees and bundle totals are indicative only. We confirm the final fees, recipes and dates with you on WhatsApp before you book.'
PASTRY = [
 dict(slug='p-beginner', num='01', level='Beginner', cat='Pastry Basics', title='Pastry Foundations', img='cupcakes',
  short='Rubs, folds and the doughs that every good pastry starts with.',
  purpose='Introduce beginners to the core pastry doughs: how to rub, cream, fold, chill and bake shortcrust, sweet pastry and simple fillings.',
  recipes=[],
  learn=['Rubbing in, creaming and melting methods','Chilling, resting and handling dough','Lining tins and blind baking','Sweet shortcrust for tarts and pies','Mixing and piping simple fillings','Baking to colour without over-browning'],
  skill='No experience needed. Perfect if you have never made pastry before.',
  duration='1 week · Mon to Fri', time='9:00am to 1:00pm', hours='4 hours a day', fee='700', spaces='Small group, up to 8 students'),
 dict(slug='p-intermediate', num='02', level='Intermediate', cat='Laminated &amp; Choux', title='Puff, Choux &amp; Tarts', img='cookies',
  short='Lamination, choux piping and tarts that hold their shape.',
  purpose='Build on the foundations with laminated dough, choux pastry and filled tarts, plus the timing and temperature control they need.',
  recipes=[],
  learn=['Laminating dough for rough puff and flaky pastry','Turns, rests and keeping butter in layers','Cooking choux paste on the stove','Piping éclairs, puffs and swirls','Tart shells, frangipane and custard fillings','Baking schedules and oven management'],
  skill='Completed our Pastry Foundations class, or comfortable making a basic shortcrust.',
  duration='1 week · Mon to Fri', time='9:00am to 2:00pm', hours='5 hours a day', fee='900', spaces='Small group, up to 6 students'),
 dict(slug='p-advanced', num='03', level='Advanced', cat='Fine Patisserie', title='Fine Patisserie &amp; Finishing', img='parfait',
  short='Refined textures, glazes and plated patisserie.',
  purpose='Introduce advanced patisserie work: layered entremets, meringues, glazes and the finishing touches that make patisserie look professional.',
  recipes=[],
  learn=['Building layered entremets and mousses','Italian and Swiss meringue work','Mirror glazes and chocolate tempering','Pâte sucrée and fine tart finishing','Piping, plating and presentation','Planning a patisserie production schedule'],
  skill='Completed our Puff, Choux &amp; Tarts class, or confident with laminated and choux pastry.',
  duration='1 week · Mon to Fri', time='9:00am to 3:00pm', hours='6 hours a day', fee='1100', spaces='Small group, up to 6 students'),
]
PASTRY_FOR_WHOM = {
 'p-beginner':['You have never made pastry before','You want to understand dough, not just follow a recipe','You want bakes you can recreate at home'],
 'p-intermediate':['You have done our Pastry Foundations class','You want to tackle puff, choux and filled tarts','You want more confidence with timings and temperatures'],
 'p-advanced':['You have done our Intermediate pastry class','You want refined, professional-looking patisserie','You are ready for glazes, meringues and plating'],
}
def pfile(c): return 'class-pastry-' + c['slug'][2:] + '.html'
def bfile(c): return 'class-' + c['slug'] + '.html'

TRACKS = {
 'bread': dict(key='bread', cls='tr-bread', label='Bread Classes', noun='bread', subj='bread-making',
   lst=CLASSES, file=bfile, home='classes.html', whom=FOR_WHOM, notice=None, track_no='01',
   h1='Classes', crumb='<a href="index.html">Home</a> / Classes',
   lede='A hands-on bread pathway in Tamale. Three stages, from your first dough to artisan loaves baked with your own hands.',
   detail_crumb=lambda c: f'<a href="index.html">Home</a> / <a href="classes.html">Classes</a> / {c["level"]}',
   sub='Each stage builds on the one before. Start where you are comfortable and progress from Ghanaian classics to international artisan breads.',
   page_title='Baking Classes | Mystery Bakebite | {SL}',
   page_desc='Hands-on bread-making classes in Tamale for beginner, intermediate and advanced bakers. One-week courses, with dates arranged on WhatsApp.',
   other_label='See pastry classes', other_href='pastries.html'),
 'pastry': dict(key='pastry', cls='tr-pastry', label='Pastry Classes', noun='pastry', subj='pastry',
   lst=PASTRY, file=pfile, home='pastries.html', whom=PASTRY_FOR_WHOM, notice=PASTRY_NOTICE, track_no='02',
   h1='Pastries', crumb='<a href="index.html">Home</a> / <a href="classes.html">Classes</a> / Pastries',
   lede='A second pathway, built for pastry. Three stages from your first shortcrust to plated patisserie, taught hands-on in Tamale.',
   detail_crumb=lambda c: f'<a href="index.html">Home</a> / <a href="pastries.html">Pastries</a> / {c["level"]}',
   sub='Each stage builds on the one before, from your first shortcrust to plated patisserie, taught hands-on in Tamale.',
   page_title='Pastry Classes | Mystery Bakebite | {SL}',
   page_desc='Explore hands-on pastry classes in Tamale. Recipe lists and indicative fees are being finalised; message us on WhatsApp for details.',
   other_label='See bread classes', other_href='classes.html'),
}

# ============================================================
# CLASS TRACKS: cream templates (bread + pastry), one code path
# ============================================================
def track_switch(active='bread'):
    a = ' on' if active == 'bread' else ''
    b = ' on' if active == 'pastry' else ''
    return f'''<nav class="px-switch dark" aria-label="Class tracks"><span class="pxs-l">Track</span><a class="pxs{a}" href="classes.html">{IC['whisk']}<span>Bread Classes</span></a><a class="pxs{b}" href="pastries.html">{IC['gift']}<span>Pastry Classes</span></a></nav>'''

def stage_path(tr, active=None):
    L = tr['lst']; out = ''
    for i, c in enumerate(L):
        cls = 'on' if active == c['slug'] else ''
        out += f'<a class="path-step {cls}" href="{tr["file"](c)}"><span class="ps-num">{c["num"]}</span><span class="ps-lvl">{c["level"]}</span></a>'
        if i < len(L) - 1: out += '<span class="path-arrow" aria-hidden="true">→</span>'
    return f'<nav class="pathway" aria-label="{tr["label"]} pathway">{out}</nav>'

def class_card(c, tr):
    if c['recipes']:
        rec = ''.join(f'<li>{r}</li>' for r in c['recipes'])
    else:
        rec = ''.join('<li class="tba">To be announced</li>' for _ in range(6))
    f = tr['file'](c)
    provisional = tr['key'] == 'pastry'
    fee_text = ('Indicative fee · ' if provisional else '') + acc(c['fee'])
    action_text = 'Request details' if provisional else f'Book {c["level"]} Class'
    return f'''<article class="level-card s-{c['slug']} reveal" id="{c['slug']}">
<div class="lc-side"><span class="lc-num">{c['num']}</span><span class="lc-lvl">{c['level']}</span><figure><img src="assets/{c['img']}.webp" alt="" loading="lazy"></figure></div>
<div class="lc-body"><span class="lc-cat">{c['cat']} · {c['title']}</span><h2>{c['title']}</h2><p class="lc-short">{c['purpose']}</p>
<div class="lc-meta"><span>{IC['whisk']} <b>6 Recipes</b></span><span>{IC['cal']} {c['duration']}</span><span>{IC['clock']} {c['time']}</span><span class="lc-fee">{fee_text}</span></div>
<ol class="recipes">{rec}</ol>
<div class="lc-ctas"><a class="btn btn-brown" href="{f}">View Class {IC['arrow']}</a><a class="btn btn-wa" href="{f}#book">{action_text}</a></div></div></article>'''

def bundle_block(tr):
    L = tr['lst']; fees = [float(c['fee']) for c in L]
    provisional = tr['key'] == 'pastry'
    sale2 = f'Indicative {BUNDLE[2]}% off' if provisional else f'Save {BUNDLE[2]}%'
    sale3 = f'Indicative {BUNDLE[3]}% off' if provisional else f'Save {BUNDLE[3]}%'
    action2 = 'Request this bundle' if provisional else 'Book this bundle'
    action3 = 'Request full pathway details' if provisional else 'Book the full pathway'
    kicker = 'Indicative bundles' if provisional else 'Bundle &amp; save'
    intro = ('Pastry fees and bundle totals shown are indicative while the recipe list is being finalised. We confirm final pricing, recipes and dates on WhatsApp before you book.' if provisional else f'Book any <b>2 {tr["noun"]} classes</b> and get <b>{BUNDLE[2]}% off</b>, or all <b>3</b> for <b>{BUNDLE[3]}% off</b>. Any combination works; you can pick your classes in the booking form.')
    rows = ''
    for a, b in [(L[0], L[1]), (L[1], L[2])]:
        full = float(a['fee']) + float(b['fee'])
        rows += f'''<div class="bundle reveal"><span class="b-off">{sale2}</span><h3>{a['level']} + {b['level']}</h3><p class="b-was">{acc(full)}</p><p class="b-now">{acc(full*(1-BUNDLE[2]/100))}</p><a class="btn btn-brown" href="{tr['file'](a)}?add={b['slug']}#book">{action2}</a></div>'''
    full = sum(fees)
    rows += f'''<div class="bundle best reveal"><span class="b-off">{sale3}</span><h3>Full Pathway<small>Beginner + Intermediate + Advanced</small></h3><p class="b-was">{acc(full)}</p><p class="b-now">{acc(full*(1-BUNDLE[3]/100))}</p><a class="btn btn-wa" href="{tr['file'](L[0])}?add=all#book">{IC['cap']} {action3}</a></div>'''
    return f'''<div class="bundles"><div class="sec-head reveal"><span class="kicker">{kicker}</span><h2 class="sec-title">Take more than one class</h2><p class="sec-sub">{intro}</p>{DIV}</div>
<div class="bundle-grid">{rows}</div></div>'''

def classes_page(tr):
    L = tr['lst']; SL = 'Unveiling The Uniqueness of A Recipe'
    cards = ''.join(class_card(c, tr) + ('<div class="lc-connector" aria-hidden="true"><span>then</span></div>' if i < len(L)-1 else '') for i, c in enumerate(L))
    guide = ''.join(f'<div class="guide reveal"><span class="g-num">{c["num"]}</span><div><b>{c["level"]}</b><p>{c["skill"]}</p></div></div>' for c in L)
    notice = f'<p class="px-notice light">{IC["bulb"]}<span>{tr["notice"]}</span></p>' if tr['notice'] else ''
    fee_note = 'Indicative fees include all ingredients. Final fees and dates are confirmed with you on WhatsApp.' if tr['key'] == 'pastry' else 'Fees include all ingredients. Dates are arranged with you on WhatsApp.'
    return head(tr['page_title'].format(SL=SL), tr['page_desc'].format(SL=SL), page=tr['home'], social_image='assets/lux-story-2.jpg' if tr['key']=='pastry' else 'assets/lux-story-1.jpg') + header() + f"""
<main><section class="page-hero lux-pagehero tr-{tr['key']}"><div class="wrap"><img class="ph-logo" src="assets/logo.webp" alt="Mystery Bakebite logo"><h1>{tr['h1']}</h1><p class="script">{SL}</p><p class="ph-sub">Learn. Bake. Create.</p>
<p class="ph-meta">In person<i>♥</i>Tamale<i>♥</i>Small groups</p>{track_switch(tr['key'])}{stage_path(tr)}</div></section>
<section class="levels tr-{tr['key']}"><div class="wrap"><div class="sec-head reveal"><span class="kicker">Choose your level</span><h2 class="sec-title">A pathway, one stage at a time</h2><p class="sec-sub">{tr['sub']}</p>{DIV}</div>
{notice}
<div class="guide-grid">{guide}</div>
<div class="level-list">{cards}</div>
{bundle_block(tr)}
<p class="menu-note">{fee_note}</p>
<div class="menu-ctas"><a class="btn btn-ghost" href="{tr['other_href']}">{tr['other_label']} {IC['arrow']}</a></div></div></section></main>"""+footer()

def class_detail(i, tr):
    L = tr['lst']; c = L[i]; SL = 'Unveiling The Uniqueness of A Recipe'
    ttl = c['title'].replace('&amp;', '&')
    provisional = tr['key'] == 'pastry'
    fee_heading = 'Indicative class fee' if provisional else 'Class fee'
    fee_display = ('Indicative · ' if provisional else '') + acc(c['fee'])
    hero_action = 'Request this class' if provisional else f'Book {c["level"]} Class'
    book_heading = 'Request a place' if provisional else 'Book your place'
    booking_title = 'Ask about your class' if provisional else 'Reserve your spot'
    booking_copy = ('Send your preferred options. We confirm the current recipes, final fee and dates on WhatsApp before any booking.' if provisional else 'Fill in the form and tap Book Now. WhatsApp opens with your booking details, and we confirm your date and space in the chat.')
    booking_button = 'Request details on WhatsApp' if provisional else 'Book Now'
    total_label = 'Indicative estimated total' if provisional else 'Estimated total'
    payment_faq = ('After we confirm the current class and fee, you can pay in cash or make full payment upfront through Mobile Money. We share MoMo details on WhatsApp.' if provisional else 'You can pay in cash when the class starts, or make full payment upfront through Mobile Money. We share the MoMo details in the WhatsApp chat when your booking is confirmed.')
    bundle_faq = ('The displayed pastry bundle savings are indicative. Ask us on WhatsApp for the current fees and recipes; we confirm the final total before booking.' if provisional else f'Yes. Book any 2 {tr["noun"]} classes and get {BUNDLE[2]}% off, or all 3 for {BUNDLE[3]}% off. Just tick the classes you want in the booking form.')
    if c['recipes']:
        rec = ''.join(f'<div class="rcard reveal"><span class="r-num">{j+1:02d}</span><h3>{r}</h3><span class="r-tag">{c["level"]}</span></div>' for j, r in enumerate(c['recipes']))
    else:
        rec = ''.join(f'<div class="rcard tba reveal"><span class="r-num">{j+1:02d}</span><h3>To be announced</h3><span class="r-tag">{c["level"]}</span></div>' for j in range(6))
    learn = ''.join(f'<div class="skill reveal"><span class="sk-ic">{IC["whisk"] if j%3==0 else IC["clock"] if j%3==1 else IC["brush"]}</span><p>{r}</p></div>' for j, r in enumerate(c['learn']))
    inc = ''.join(f'<li>{r}</li>' for r in CLASS_INCLUDED)
    bring = ''.join(f'<li>{r}</li>' for r in CLASS_BRING)
    who = ''.join(f'<li>{r}</li>' for r in tr['whom'][c['slug']])
    opts = ''.join(f'<label class="opt"><input type="radio" name="schedule" value="{o}" {"checked" if j==0 else ""}><span>{o}</span></label>' for j, o in enumerate(CLASS_SCHEDULES))
    picks = ''.join(f'''<label class="opt pk"><input type="checkbox" name="cls" value="{x["slug"]}" data-fee="{x["fee"]}" data-name="{x["num"]} {x["level"]}: {x["title"].replace("&amp;","&")}" {"checked" if x is c else ""}><span><b>{x["num"]} {x["level"]}</b><small>{x["title"]}</small></span><em>{("Indicative · " if provisional else "") + acc(x["fee"])}</em></label>''' for x in L)
    fit = ''
    for x in L:
        st = 'now' if x is c else ('done' if L.index(x) < i else 'next')
        lab = {'now': 'You are here', 'done': 'Before this', 'next': 'Up next'}[st]
        fit += f'<a class="fit {st}" href="{tr["file"](x)}"><span class="fit-n">{x["num"]}</span><b>{x["level"]}</b><small>{lab}</small></a>'
    faqs = [
     ('How do I pay?', payment_faq),
     ('Can I book more than one class?', bundle_faq),
     ('Is this the right level for me?', c['skill'].replace('&amp;', '&') + ' Not sure? Message us on WhatsApp and we will help you choose.'),
     ('When does the next class start?', 'Classes run for one week, Monday to Friday. Choose your preferred schedule and start date in the form and we will confirm the date with you on WhatsApp.'),
     ('Do I need to bring ingredients or equipment?', 'No. All ingredients and equipment are included. You only need the few items listed under What to bring.'),
    ]
    faq = ''.join(f'<details class="faq reveal"{" open" if j==0 else ""}><summary>{q}<span class="fq-ic" aria-hidden="true">+</span></summary><p>{a}</p></details>' for j, (q, a) in enumerate(faqs))
    if i < len(L) - 1:
        n = L[i+1]
        if provisional:
            nxt = f'<section class="next-band"><div class="wrap nb-inner reveal"><div><span class="kicker">Next stage</span><h2>Next stage: {n["num"]} {n["level"]}</h2><p>{n["title"]} · indicative fee {acc(n["fee"])}</p></div><div class="nb-ctas"><a class="btn btn-ghost" href="{tr["file"](n)}">View {n["level"]} {IC["arrow"]}</a><a class="btn btn-wa" href="{tr["file"](c)}?add={n["slug"]}#book">Request both details</a></div></div></section>'
        else:
            nxt = f'<section class="next-band"><div class="wrap nb-inner reveal"><div><span class="kicker">Keep progressing</span><h2>Next stage: {n["num"]} {n["level"]}</h2><p>{n["title"]} · 6 recipes · {acc(n["fee"])}</p></div><div class="nb-ctas"><a class="btn btn-ghost" href="{tr["file"](n)}">View {n["level"]} {IC["arrow"]}</a><a class="btn btn-wa" href="{tr["file"](c)}?add={n["slug"]}#book">Book both, save {BUNDLE[2]}%</a></div></div></section>'
    elif provisional:
        nxt = f'<section class="next-band"><div class="wrap nb-inner reveal"><div><span class="kicker">Indicative full pathway</span><h2>Beginner → Intermediate → Advanced</h2><p>Ask about the full pastry pathway. Listed fees and savings are indicative; we confirm the final total on WhatsApp.</p></div><div class="nb-ctas"><a class="btn btn-ghost" href="{tr["home"]}">All {tr["noun"]} classes {IC["arrow"]}</a><a class="btn btn-wa" href="{tr["file"](L[2])}?add=all#book">Request full pathway</a></div></div></section>'
    else:
        nxt = f'<section class="next-band"><div class="wrap nb-inner reveal"><div><span class="kicker">The full pathway</span><h2>Beginner → Intermediate → Advanced</h2><p>Book all three {tr["noun"]} classes together and save {BUNDLE[3]}%.</p></div><div class="nb-ctas"><a class="btn btn-ghost" href="{tr["home"]}">All {tr["noun"]} classes {IC["arrow"]}</a><a class="btn btn-wa" href="{tr["file"](L[2])}?add=all#book">Book full pathway</a></div></div></section>'
    notice = f'<p class="px-notice light small">{IC["bulb"]}<span>{tr["notice"]}</span></p>' if tr['notice'] else ''
    detail_desc = (f'{c["level"]} pastry class in Tamale. Indicative fees and recipes are being finalised; confirm details on WhatsApp.' if tr['key']=='pastry' else f'{c["level"]} bread class in Tamale. One-week hands-on training; recommended times and dates arranged on WhatsApp.')
    return head(f'{c["level"]} {tr["noun"].capitalize()} Class: {ttl} | Mystery Bakebite', detail_desc, page=tr['file'](c), social_image='assets/lux-story-2.jpg' if tr['key']=='pastry' else 'assets/lux-story-1.jpg') + header() + f"""
<main>
<section class="page-hero lux-pagehero cx-hero s-{c['slug']}"><div class="wrap">
<p class="crumbs">{tr['detail_crumb'](c)}</p>
{track_switch(tr['key'])}
<div class="cx-grid">
<div class="cx-intro"><span class="cx-chip">Stage {c['num']} · {c['level']}</span>
<h1><span class="cx-num">{c['num']}</span>{c['title']}</h1>
<p class="ph-lede">{c['purpose']}</p>
<p class="script cd-slogan">{SL}</p>
<div class="hero-ctas"><a class="btn btn-wa" href="#book">{IC['wa']} {hero_action}</a><a class="btn btn-ghost" href="#recipes">See the 6 recipes</a></div></div>
<aside class="glance"><h2>At a glance</h2><ul>
<li>{IC['cal']}<span><small>Duration</small>{c['duration']}</span></li>
<li>{IC['clock']}<span><small>Recommended time</small>{c['time']} · {c['hours']}</span></li>
<li>{IC['whisk']}<span><small>Recipes</small>6 recipes</span></li>
<li>{IC['pin']}<span><small>Location</small>In person, Tamale</span></li>
<li>{IC['heartline']}<span><small>Available spaces</small>{c['spaces']}</span></li></ul>
<div class="gl-fee"><small>{fee_heading}</small><b>{acc(c['fee'])}</b><span>per student · ingredients included</span></div></aside>
</div>{stage_path(tr, c['slug'])}</div></section>

<nav class="subnav" aria-label="Class sections"><div class="wrap sn-inner">
<a href="#overview">Overview</a><a href="#recipes">Recipes</a><a href="#skills">Skills</a><a href="#details">Details</a><a href="#faq">FAQ</a><a href="#book" class="sn-book">{"Request a place" if provisional else "Book now"}</a></div></nav>

<section class="cx-sec" id="overview"><div class="wrap ov-grid">
<div class="reveal"><span class="kicker">Overview</span><h2 class="sec-title left">About this class</h2><p class="ov-lead">{c['purpose']}</p><p class="ov-p">{c['short']} Over one week in a small group, you'll make every recipe with your own hands, guided step by step by Emmanuella.</p></div>
<div class="who reveal"><h3>Is this class for you?</h3><ul class="ticks">{who}</ul><p class="who-skill"><b>Required skill level:</b> {c['skill']}</p></div>
</div>
<div class="wrap"><div class="fit-row reveal">{fit}</div></div></section>

<section class="cx-sec alt" id="recipes"><div class="wrap"><div class="sec-head reveal"><span class="kicker">What you'll bake</span><h2 class="sec-title">The 6 recipes</h2><p class="sec-sub">{c['cat']} · {c['title']}</p>{DIV}</div>
<div class="rgrid">{rec}</div>{notice}</div></section>

<section class="cx-sec" id="skills"><div class="wrap"><div class="sec-head reveal"><span class="kicker">Skills</span><h2 class="sec-title">What you'll learn</h2>{DIV}</div>
<div class="sgrid">{learn}</div></div></section>

<section class="cx-sec alt" id="details"><div class="wrap"><div class="sec-head reveal"><span class="kicker">Class details</span><h2 class="sec-title">Everything you need to know</h2>{DIV}</div>
<div class="dgrid">
<div class="dcard reveal"><h3>{IC['cal']} Schedule &amp; place</h3><dl>
<dt>Duration</dt><dd>{c['duration']}</dd><dt>Recommended time</dt><dd>{c['time']} ({c['hours']})</dd>
<dt>Location</dt><dd>In person, Tamale</dd><dt>Spaces</dt><dd>{c['spaces']}</dd><dt>{fee_heading}</dt><dd class="dd-fee">{acc(c['fee'])}</dd></dl></div>
<div class="dcard reveal"><h3>{IC['gift']} What's included</h3><ul class="ticks">{inc}</ul></div>
<div class="dcard reveal"><h3>{IC['bag']} What to bring</h3><ul class="ticks">{bring}</ul></div>
</div></div></section>

<section class="book-band on-dark" id="book"><div class="wrap bb-grid">
<div class="bb-intro reveal"><span class="kicker">{book_heading}</span><h2 class="sec-title left">{booking_title}</h2><p class="bk-slogan">{SL}</p>
<p class="bb-p">{booking_copy}</p>
<div class="bb-price"><small>{fee_heading} · Stage {c['num']} · {c['level']}</small><b>{acc(c['fee'])}</b><span>per student · {c['duration']} · {c['time']}</span></div>
<ul class="bb-deals"><li><b>{("Indicative " if provisional else "") + str(BUNDLE[2]) + "% off"}</b> when you book any 2 classes</li><li><b>{("Indicative " if provisional else "") + str(BUNDLE[3]) + "% off"}</b> when you book all 3 classes</li><li>Pay cash, or full payment upfront via MoMo</li></ul></div>
<form class="book-form bb-form reveal" data-track="{tr['noun']}" data-d2="{BUNDLE[2]}" data-d3="{BUNDLE[3]}" data-level="{c['num']} {c['level']}" data-title="{ttl}" data-fee="{c['fee']}">
<fieldset class="pick"><legend>1 · Choose your class(es)</legend>{picks}<p class="pick-hint">Add a 2nd class for <b>{BUNDLE[2]}% off</b>, or all 3 for <b>{BUNDLE[3]}% off</b>.</p></fieldset>
<fieldset><legend>2 · Preferred schedule</legend>{opts}</fieldset>
<fieldset><legend>3 · Your details</legend><div class="fld-grid">
<label class="fld">Preferred start date<input type="date" name="date"></label>
<label class="fld">Number of students<select name="seats"><option>1</option><option>2</option><option>3</option><option>4</option></select></label>
<label class="fld">Your name<input type="text" name="name" placeholder="Full name" required></label>
<label class="fld">Phone number<input type="tel" name="phone" placeholder="e.g. 024 000 0000"></label></div></fieldset>
<div class="bk-sum">
<p><span>Classes subtotal</span><span>GH₵ <span class="sub">{float(c['fee']):,.2f}</span></span></p>
<p class="disc-row" hidden><span>Bundle discount (<span class="disc-pct">0</span>%)</span><span>− GH₵ <span class="disc">0.00</span></span></p>
<p><span>Students</span><span>× <span class="n">1</span></span></p>
<p class="bk-total"><span>{total_label}</span><b>GH₵ <span class="tot">{float(c['fee']):,.2f}</span></b></p></div>
<button class="btn btn-wa bk-btn" type="submit">{IC['wa']} {booking_button}</button>
<p class="bk-note">{"Indicative fees only. We confirm the final fee, recipes, date and space on WhatsApp before booking." if provisional else "Your date and space are confirmed in the WhatsApp chat."}</p>
</form></div></section>

<section class="cx-sec" id="faq"><div class="wrap faq-wrap"><div class="sec-head reveal"><span class="kicker">Questions</span><h2 class="sec-title">Frequently asked</h2>{DIV}</div>{faq}</div></section>
{nxt}
</main>"""+footer()

# ============================================================
# ORDER PAGE
# ============================================================
def _variants():
    out=[]
    for slug,name,note,frm,new,items in MENU:
        cat=[]
        for k,it in enumerate(items):
            label,price=it[0],it[1]
            if '/' in price:
                a,b=[x.replace('GH₵','').strip() for x in price.split('/')]
                cat.append((f'{slug}-{k}',label,float(a),'Plain',len(it)>2))
                cat.append((f'{slug}-{k}t',label,float(b),'With toppings',len(it)>2))
            else:
                cat.append((f'{slug}-{k}',label,float(price),'',len(it)>2))
        out.append((slug,name,note,cat))
    return out

def order_page():
    SL='Unveiling The Uniqueness of A Recipe'
    cats=''
    for slug,name,note,cat in _variants():
        rows=''
        for vid,label,price,var,new in cat:
            v=f'<span class="oi-var">{var}</span>' if var else ''
            n='<span class="mini-new">NEW</span>' if new else ''
            full=label+(f' ({var})' if var else '')
            cname=name.replace('&amp;','&')
            rows+=(f'<div class="oi" data-id="{vid}" data-name="{full}" data-cat="{cname}" data-price="{price}">'
                   f'<div class="oi-info"><b>{label}{n}</b>{v}</div><span class="oi-price">{acc(price)}</span>'
                   f'<div class="qty"><button type="button" class="q-minus" aria-label="Remove one">−</button>'
                   f'<input type="number" min="0" max="99" value="0" aria-label="Quantity for {full}">'
                   f'<button type="button" class="q-plus" aria-label="Add one">+</button></div></div>')
        topn='<label class="fld topping" hidden>Topping for loaves<select name="topping"><option>Oreo</option><option>Chocolate</option><option>Raisin</option></select></label>' if slug=='loaves' else ''
        nt=f'<p class="oc-note">{note}</p>' if note else ''
        cats+=(f'<details class="ocat reveal" id="cat-{slug}"><summary><img src="assets/{slug}.webp" alt="" loading="lazy">'
               f'<span><b>{name}</b><small>{len(cat)} options</small></span><span class="oc-count" hidden>0</span><span class="oc-ic">+</span></summary>'
               f'<div class="ocat-body">{nt}{rows}{topn}</div></details>')
    info=''.join(f'<div class="info-card reveal"><div class="info-ic">{IC[i]}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i,t,d in INFO_ITEMS)
    html = head('Order | Mystery Bakebite', 'Choose your treats, pickup or delivery, and payment, then send your Mystery Bakebite order to WhatsApp in Tamale.', page='order.html', social_image='assets/lux-menu-hero.jpg') + header()
    html += f"""
<main><section class="page-hero lux-pagehero order-hero"><div class="wrap"><img class="ph-logo" src="assets/logo.webp" alt="Mystery Bakebite logo"><h1>Place Your Order</h1><p class="script">{SL}</p>
<p class="ph-meta">Choose treats<i>♥</i>Pickup or delivery<i>♥</i>Select payment<i>♥</i>Confirm on WhatsApp</p></div></section>

<section class="order-page"><div class="wrap op-grid">
<form class="op-form" id="orderForm" novalidate>
<div class="op-step reveal"><div class="op-h"><span>1</span><div><h2>Choose your treats</h2><p>Tap a category and use + to add items.</p></div></div>
<div class="ocats">{cats}</div></div>

<div class="op-step reveal"><div class="op-h"><span>2</span><div><h2>Pickup or delivery</h2><p>Open every day, 8am to 7pm.</p></div></div>
<div class="seg"><label class="seg-opt"><input type="radio" name="fulfil" value="Pickup" checked><span>{IC['bag']}<b>Pickup</b><small>Free, in Tamale</small></span></label>
<label class="seg-opt"><input type="radio" name="fulfil" value="Delivery"><span>{IC['truck']}<b>Delivery</b><small>Fee confirmed on WhatsApp</small></span></label></div>
<div class="fld-grid"><label class="fld">Date needed<input type="date" name="date" required></label>
<label class="fld">Preferred time<select name="time"><option>Morning (8am to 12pm)</option><option>Afternoon (12pm to 4pm)</option><option>Evening (4pm to 7pm)</option></select></label>
<label class="fld deliv" hidden style="grid-column:1/-1">Delivery area / landmark in Tamale<input type="text" name="area" placeholder="e.g. Kalpohin, near the market"></label></div></div>

<div class="op-step reveal" id="payment"><div class="op-h"><span>3</span><div><h2>Payment method</h2><p>Select how you'd like to pay.</p></div></div>
<div class="pay-pick">
<label class="pp"><input type="radio" name="pay" value="Cash on delivery / pickup" checked><span class="pp-box"><span class="pp-ic">{IC['cash']}</span><span class="pp-t"><b>Cash on Delivery or Pickup</b><small>Pay in cash when you receive or collect your order.</small></span><span class="pp-check"></span></span></label>
<label class="pp"><input type="radio" name="pay" value="Full payment upfront (Mobile Money)"><span class="pp-box"><span class="pp-ic">{IC['card']}</span><span class="pp-t"><b>Full Payment Upfront via Mobile Money</b><small>Pay the full amount by MoMo. We send our MoMo details on WhatsApp.</small></span><span class="pp-check"></span></span></label></div>
<div class="momo-net" hidden><p class="fld">Your MoMo network</p><div class="chips-r">
<label><input type="radio" name="net" value="MTN MoMo" checked><span>MTN MoMo</span></label><label><input type="radio" name="net" value="Telecel Cash"><span>Telecel Cash</span></label><label><input type="radio" name="net" value="AT Money"><span>AT Money</span></label></div>
<p class="pay-note">{IC['lock']} Only send payment to the MoMo number and name we confirm in our WhatsApp chat.</p></div></div>

<div class="op-step reveal"><div class="op-h"><span>4</span><div><h2>Your details</h2><p>So we can confirm your order.</p></div></div>
<div class="fld-grid"><label class="fld">Full name<input type="text" name="name" placeholder="Your name" required></label>
<label class="fld">Phone number<input type="tel" name="phone" placeholder="e.g. 024 000 0000" required></label>
<label class="fld" style="grid-column:1/-1">Notes (optional)<textarea name="notes" rows="3" placeholder="Allergies, message on a cake, colours, anything else"></textarea></label></div></div>
</form>

<aside class="cart" id="cart"><div class="cart-head"><p class="bk-slogan">{SL}</p><h2>Your order</h2></div>
<div class="cart-body"><p class="cart-empty">No items yet. Add treats from step 1.</p><ul class="cart-list"></ul></div>
<div class="cart-sum"><p><span>Subtotal</span><b>GH₵ <span class="c-sub">0.00</span></b></p>
<p class="c-del" hidden><span>Delivery fee</span><span>Confirmed on WhatsApp</span></p>
<p class="c-pay"><span>Payment</span><span class="c-paym">Cash on delivery / pickup</span></p>
<p class="c-tot"><span>Estimated total</span><b>GH₵ <span class="c-total">0.00</span></b></p></div>
<p class="cart-err" role="alert" hidden></p>
<button class="btn btn-wa cart-btn" type="submit" form="orderForm">{IC['wa']} Confirm order on WhatsApp</button>
<p class="bk-note">Sends your order to +233 55 452 0532. We reply to confirm availability and your final total.</p></aside>
</div>
<div class="wrap"><div class="receipt-result" id="receiptResult" role="status" hidden>
<div class="receipt-result-copy"><span class="kicker">Order summary</span><h2>Your receipt is ready</h2><p>Download a copy of your order request, or open a print-ready version. We confirm your order on WhatsApp.</p></div>
<div class="receipt-result-actions"><button class="btn btn-brown" id="downloadReceipt" type="button">{IC['download']} Download receipt</button><button class="btn btn-ghost-dark" id="printReceipt" type="button">Print / Save as PDF</button></div>
</div></div></section>

<section class="info op-info" id="info"><div class="wrap"><div class="sec-head reveal"><span class="kicker">Good to know</span><h2 class="sec-title">Ordering info</h2>{DIV}</div><div class="info-grid">{info}</div></div></section>
</main>
<div class="cart-bar" hidden><span><b class="cb-n">0</b> items · GH₵ <span class="cb-t">0.00</span></span><a href="#cart" class="btn btn-wa">Review order</a></div>"""
    return html + footer()


index=head('Mystery Bakebite | Home Bakery in Tamale','Home bakery in Tamale, Ghana. Shop handmade doughnuts, cakes and treats, explore baking classes, and request custom orders via WhatsApp.', page='index.html', business=True, social_image='assets/lux-hero.jpg')+header()+f"""
<main>
<section class="lux-hero">
<div class="lux-hero-glow" aria-hidden="true"></div>
<div class="wrap lux-hero-layout">
<div class="lux-hero-in">
<img class="lux-hero-logo" src="assets/logo.webp" alt="Mystery Bakebite logo">
<p class="lux-kicker">Home bakery <i>♥</i> Tamale, Northern Ghana</p>
<h1 class="lux-h1">Hi, I'm Emmanuella.<span>Welcome to my kitchen.</span></h1>
<p class="lux-slogan">Unveiling The Uniqueness of A Recipe</p>
<p class="lux-lede">Mystery Bakebite began in my home kitchen in Tamale with one belief: every recipe hides something special. I bake soft milky doughnuts, dripping cakes and parfaits for your everyday moments, teach others to bake, and create custom treats for your celebrations.</p>
<div class="hero-ctas"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{IC['wa']} Order on WhatsApp</a><a class="btn btn-ghost" href="menu.html">Explore the menu</a></div>
<p class="lux-sign">With love, Emmanuella<i>Founder &amp; Head Baker</i></p>
</div>
<figure class="lux-hero-visual"><img src="assets/lux-hero.webp" alt="Freshly baked breads, doughnuts and cakes from Mystery Bakebite"><figcaption><span>From the home kitchen</span><strong>Handmade in Tamale, with a little mystery.</strong></figcaption></figure>
</div>
<a class="lux-cue" href="#story"><span></span>Our story</a>
</section>
<div class="marquee" aria-hidden="true"><div class="marquee-track">MQ</div></div>

<section class="lux-story" id="story"><div class="wrap">
<div class="sec-head reveal"><span class="kicker">Our story</span><h2 class="sec-title">A recipe is never just a recipe</h2><p class="sec-script">Unveiling The Uniqueness of A Recipe</p>{DIV}</div>
<div class="lux-chapters">
<article class="lux-chapter reveal"><figure><img src="assets/lux-story-1.webp" alt="Dough being shaped by hand in the Mystery Bakebite kitchen" loading="lazy"></figure>
<div class="ch-body"><span class="ch-n">01</span><h3>It started at home</h3><p>A small kitchen in Tamale, a few trusted recipes, and family and friends who kept asking for more. Every batch is still made by hand, in small batches, by Emmanuella herself.</p></div></article>
<article class="lux-chapter reveal"><figure><img src="assets/lux-story-2.webp" alt="Cream being piped into a milky doughnut" loading="lazy"></figure>
<div class="ch-body"><span class="ch-n">02</span><h3>The mystery twist</h3><p>The "mystery" is that little something extra: more cream in a milky donut, a flavour pairing you didn't expect. It's what turns a good bake into your favourite one.</p></div></article>
<article class="lux-chapter reveal"><figure><img src="assets/lux-story-3.webp" alt="Hands decorating cupcakes during a baking class" loading="lazy"></figure>
<div class="ch-body"><span class="ch-n">03</span><h3>Sharing the craft</h3><p>Today, Mystery Bakebite also teaches hands-on baking classes and designs custom pieces for Tamale's birthdays, weddings and naming ceremonies.</p></div></article>
</div>
<div class="lux-quote reveal"><p>“I want every box that leaves my kitchen to feel like it was made just for you, because it was.”</p><cite>Emmanuella N. Awini, Founder &amp; Head Baker</cite><div class="vbadges center">{vals}</div></div>
</div></section>
<section class="menu-sec" id="menu"><div class="wrap"><div class="sec-head reveal"><span class="kicker">From my kitchen to your table</span><h2 class="sec-title">Something sweet for every moment</h2><p class="sec-sub">Eight favourites, baked to order. Explore sizes and prices, or order straight from a card.</p>{DIV}</div>
<div class="menu-grid">{cards}</div>
<div class="menu-ctas"><a class="btn btn-brown" href="menu.html">Full price list {IC['arrow']}</a><a class="btn btn-ghost-dark" href="assets/price-list-current.jpg" download="Mystery-Bakebite-Current-Menu.jpg">{IC["download"]}Download menu card</a></div>
<p class="menu-note">Current menu · All prices in GH₵</p></div></section>

"""+classes_teaser()+f"""
<section class="services custom-sec" id="custom"><div class="wrap">
<article class="svc svc-wide reveal"><figure><img src="assets/lux-custom.webp" alt="Celebration cake with gold drip made to order" loading="lazy"><span class="svc-tag">{IC['gift']} Creative</span></figure>
<div class="svc-body"><span class="kicker">Custom orders</span><h3>Dream it up with us</h3><p>Birthdays, weddings, naming ceremonies, office treats and gift boxes. Tell us your theme and we'll design something that's truly yours.</p>
<ul class="ticks two"><li>Celebration and themed cakes</li><li>Dessert tables and party packs</li><li>Branded gift boxes and bulk orders</li><li>Order 3 to 5 days ahead</li></ul>
<a class="btn btn-wa" href="{WA_CUSTOM}" target="_blank" rel="noopener">{IC['wa']} Request a custom order</a></div></article>
</div></section>

"""+testimonials_block()+gallery_block()+f"""
<section class="order-teaser on-dark" id="order"><div class="wrap ot-grid">
<div class="reveal"><span class="kicker">Ready to order?</span><h2 class="sec-title left">Build your order in a minute</h2><p class="sec-script">Unveiling The Uniqueness of A Recipe</p>
<p class="ot-p">Pick your treats, choose pickup or delivery, select how you'd like to pay, and we'll receive your order straight on WhatsApp.</p>
<div class="hero-ctas"><a class="btn btn-wa" href="order.html">{IC['bag']} Start your order</a><a class="btn btn-ghost" href="menu.html">View the menu</a></div></div>
<ol class="ot-steps reveal"><li><span>01</span><div><b>Choose your treats</b><p>Add items and quantities from the full menu.</p></div></li>
<li><span>02</span><div><b>Pickup or delivery</b><p>Tell us when and where in Tamale.</p></div></li>
<li><span>03</span><div><b>Select payment</b><p>Cash on delivery or pickup, or full MoMo payment upfront.</p></div></li>
<li><span>04</span><div><b>Confirm on WhatsApp</b><p>Your order is sent to +233 55 452 0532.</p></div></li></ol>
</div></section>
<section class="closing on-dark"><div class="wrap cl-inner reveal"><img class="cl-logo" src="assets/logo.webp" alt="">
<p class="cl-script">Baked with Love, Especially for You</p><p class="cl-p">Thank you for supporting a small, home-grown Tamale business. Whatever you're craving, let's make it together.</p>
<div class="hero-ctas"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{IC['wa']} Order on WhatsApp</a><a class="btn btn-ghost" href="classes.html">Explore classes</a></div></div></section>
</main>"""+footer()

# ---- menu page
pl=''
for slug,name,note,frm,new,items in MENU:
    lis=''
    for it in items:
        n='<span class="mini-new">NEW</span>' if len(it)>2 else ''
        plain = name.replace('&amp;','&')
        lis+=f'<li><span class="item">{it[0]}{n}</span><span class="dots"></span><span class="price">{C}{it[1]}</span><a class="order-btn" href="order.html?add={slug}-{items.index(it)}" aria-label="Add {it[0]} to your order">{IC["wa"]}<span>Order</span></a></li>'
    nt=f'<p class="note">{note}</p>' if note else ''
    pl+=f'<article class="pl-card reveal" id="{slug}"><figure><img src="assets/{slug}.webp" alt="{name}" loading="lazy"></figure><div class="pl-body"><h2>{name}</h2>{nt}<ul class="pl">{lis}</ul></div></article>'
CHIP={'milky':'Milky Doughnuts','balls':'Donut Balls','slices':'Cake Slices','loaves':'Cake Loaves','chips':'Chips','parfait':'Parfait','cookies':'Cookies','cupcakes':'Cupcakes'}
chips=''.join(f'<a class="mchip" href="menu.html#{sl}" data-cat="{sl}">{CHIP[sl]}</a>' for sl,_n,_no,_f,_nw,_i in MENU)
menu=head('Menu & Prices | Mystery Bakebite','Browse Mystery Bakebite doughnuts, cakes, snacks and current prices in Tamale. Order for pickup or delivery via WhatsApp.', page='menu.html', social_image='assets/lux-menu-hero.jpg')+header()+f'''
<main><section class="page-hero lux-menu-hero"><div class="lux-pagehero-media" aria-hidden="true"><img src="assets/lux-menu-hero.webp" alt=""></div><div class="wrap"><img class="ph-logo" src="assets/logo.webp" alt="Mystery Bakebite logo"><h1>Menu &amp; Prices</h1><p class="script">Unveiling The Uniqueness of A Recipe</p>
<p class="ph-meta">Current menu<i>♥</i>Tamale<i>♥</i>All prices in GH₵</p>
<div class="hero-ctas"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{IC['wa']} Order on WhatsApp</a><a class="btn btn-ghost" href="assets/price-list-current.jpg" download="Mystery-Bakebite-Current-Menu.jpg">{IC["download"]}Download menu card</a></div></div></section>
<nav class="mchips" aria-label="Menu categories"><div class="wrap mchips-in">{chips}</div></nav>
<section class="pricelist"><div class="wrap"><div class="pl-grid">{pl}</div></div></section>
'''+f'''<section class="order-strip"><div class="wrap"><p class="script">Ready to order?</p><p>Add your picks to an order, choose pickup or delivery and your payment method, then confirm on WhatsApp.</p><a class="btn btn-wa" href="order.html">{IC['bag']} Start your order</a></div></section></main>'''+footer()
MQ=''.join(f'<span>{i} {IC["heart"]} <em>freshly baked</em> {IC["heart"]}</span>' for i in ['Milky Doughnuts', 'Cake Slices', 'Cupcakes', 'Cake Parfaits', 'Donut Balls', 'Cookies', 'Cake Loaves', 'Baking Classes', 'Custom Orders'])
index=index.replace('MQ',MQ*2)
open('index.html','w').write(index); open('menu.html','w').write(menu)
open('classes.html','w').write(classes_page(TRACKS['bread']))
for _i,_c in enumerate(CLASSES): open(f'class-{_c["slug"]}.html','w').write(class_detail(_i, TRACKS['bread']))
open('order.html','w').write(order_page())
for _i,_c in enumerate(PASTRY): open(pfile(_c),'w').write(class_detail(_i, TRACKS['pastry']))
open('pastries.html','w').write(classes_page(TRACKS['pastry']))

# Search-crawler basics. Absolute sitemap URLs are emitted only when the public domain is configured.
SEO_PAGES = ['index.html', 'menu.html', 'classes.html', 'pastries.html', 'order.html',
             'class-beginner.html', 'class-intermediate.html', 'class-advanced.html',
             'class-pastry-beginner.html', 'class-pastry-intermediate.html', 'class-pastry-advanced.html']
robots = 'User-agent: *\nAllow: /\n'
if SITE_URL:
    robots += f'Sitemap: {SITE_URL}/sitemap.xml\n'
Path('robots.txt').write_text(robots)
if SITE_URL:
    urls = ''.join(f'<url><loc>{html_escape.escape(SITE_URL + ("/" if page == "index.html" else "/" + page), quote=False)}</loc></url>' for page in SEO_PAGES)
    Path('sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + '</urlset>\n')
else:
    Path('sitemap.xml').unlink(missing_ok=True)
