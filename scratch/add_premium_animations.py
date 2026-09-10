# -*- coding: utf-8 -*-
"""
Add premium animations and interactions to SoccerProf index.html:
1. Logo watermark parallax background in key sections
2. Hero stagger load animation 
3. Sticky header that transforms on scroll (transparent → glass)
4. Active navigation via IntersectionObserver
5. Smooth JS scrolling with easing
6. Enhanced CSS microinteractions
7. Updated navigation (add Shop, correct structure)
8. Hero: two-column layout restored (text left, photo right)
"""

import re

src = open(r'c:\Users\mario\Desktop\newsoccerprof\index.html', 'r', encoding='utf-8').read()

# ── 1. Replace <style> block with enhanced version ────────────────────────────
OLD_STYLE_START = '  <style>'
OLD_STYLE_END   = '  </style>'

NEW_STYLE = r"""  <style>
    /* =============================================
       BASE
    ============================================= */
    *, *::before, *::after { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: #F8FAFC;
      color: #0F172A;
      overflow-x: hidden;
    }
    .bg-light { background-color: #F8FAFC; }
    .subtle-grid {
      background-size: 60px 60px;
      background-image:
        linear-gradient(to right, rgba(15,23,42,0.025) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(15,23,42,0.025) 1px, transparent 1px);
    }

    /* =============================================
       CARDS
    ============================================= */
    .glass-card {
      background: #ffffff;
      border: 1px solid rgba(226,232,240,0.9);
      transition: transform 0.32s cubic-bezier(0.4,0,0.2,1),
                  box-shadow 0.32s cubic-bezier(0.4,0,0.2,1),
                  border-color 0.32s cubic-bezier(0.4,0,0.2,1);
    }
    .glass-card:hover {
      border-color: rgba(212,175,55,0.55);
      box-shadow: 0 16px 40px -10px rgba(15,23,42,0.12), 0 0 0 1px rgba(212,175,55,0.12);
      transform: translateY(-4px);
    }
    .glass-card:hover .card-img img { transform: scale(1.05); }
    .card-img img { transition: transform 0.6s cubic-bezier(0.4,0,0.2,1); }

    /* =============================================
       NAVIGATION – sticky, transforms on scroll
    ============================================= */
    #site-header {
      position: fixed; top: 0; left: 0; width: 100%; z-index: 50;
      transition: background 0.4s ease, box-shadow 0.4s ease,
                  height 0.4s ease, padding 0.4s ease;
      height: 80px;
      background: transparent;
    }
    /* scrolled state – added via JS */
    #site-header.header-scrolled {
      background: rgba(255,255,255,0.96);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      box-shadow: 0 1px 24px rgba(15,23,42,0.08);
      height: 64px;
    }
    #site-header .header-inner {
      height: 100%;
      display: flex; align-items: center; justify-content: space-between;
      max-width: 80rem; margin: 0 auto; padding: 0 1.5rem;
    }
    #nav-logo { transition: transform 0.4s ease, opacity 0.4s ease; }
    #site-header.header-scrolled #nav-logo { transform: scale(0.87); }

    /* nav link active state */
    .nav-link {
      position: relative;
      font-size: .875rem; font-weight: 700; color: rgba(255,255,255,0.85);
      transition: color 0.2s ease;
      padding-bottom: 2px;
    }
    #site-header.header-scrolled .nav-link { color: #475569; }
    .nav-link::after {
      content: ''; position: absolute; bottom: -4px; left: 0; right: 0;
      height: 2px; background: #D4AF37; border-radius: 2px;
      transform: scaleX(0); transform-origin: left;
      transition: transform 0.25s ease;
    }
    .nav-link:hover { color: #D4AF37 !important; }
    .nav-link.active { color: #D4AF37 !important; }
    .nav-link.active::after { transform: scaleX(1); }
    #site-header.header-scrolled .nav-link:hover { color: #E63946 !important; }
    #site-header.header-scrolled .nav-link.active { color: #E63946 !important; }
    #site-header.header-scrolled .nav-link.active::after { background: #E63946; transform: scaleX(1); }

    /* shop badge */
    .nav-shop {
      font-size: .75rem; font-weight: 800; letter-spacing: .05em;
      color: rgba(255,255,255,0.7);
      border: 1px solid rgba(255,255,255,0.2);
      padding: 4px 12px; border-radius: 999px;
      transition: all 0.25s ease;
    }
    #site-header.header-scrolled .nav-shop {
      color: #0F172A; border-color: rgba(15,23,42,0.2);
    }
    .nav-shop:hover { background: rgba(212,175,55,0.15); border-color: #D4AF37; color: #D4AF37 !important; }

    /* CTA pill */
    .nav-cta {
      display: inline-flex; align-items: center; gap: 6px;
      padding: 8px 18px; border-radius: 999px;
      background: #E63946; color: #fff;
      font-size: .75rem; font-weight: 800; letter-spacing: .06em; text-transform: uppercase;
      box-shadow: 0 6px 20px -4px rgba(230,57,70,0.45);
      transition: background 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease;
      white-space: nowrap;
    }
    .nav-cta:hover {
      background: #C52233; transform: translateY(-2px);
      box-shadow: 0 10px 28px -4px rgba(230,57,70,0.55);
    }
    .nav-cta .cta-arrow {
      display: inline-block;
      transition: transform 0.22s ease;
    }
    .nav-cta:hover .cta-arrow { transform: translateX(3px) translateY(-1px); }

    /* =============================================
       HERO
    ============================================= */
    .hero-section {
      position: relative;
      background: linear-gradient(135deg, #0a1020 0%, #1a2540 55%, #0e1827 100%);
      overflow: hidden;
    }
    /* Subtle image overlay */
    .hero-section::after {
      content: '';
      position: absolute; inset: 0;
      background: url('img/packete/soccerprof-hamburg-kinder-jugendliche-fussballtraining.avif')
                  center/cover no-repeat;
      opacity: 0.10; z-index: 0; pointer-events: none;
    }
    .hero-inner { position: relative; z-index: 1; }

    /* Hero stagger load */
    .hero-animate {
      opacity: 0;
      transform: translateY(28px);
      transition: opacity 0.75s cubic-bezier(0.16,1,0.3,1),
                  transform 0.75s cubic-bezier(0.16,1,0.3,1);
    }
    .hero-animate.visible { opacity: 1; transform: translateY(0); }

    /* Photo column */
    .hero-photo-wrap {
      position: relative;
      border-radius: 28px;
      overflow: hidden;
      box-shadow: 0 30px 80px -20px rgba(0,0,0,0.6);
      border: 1.5px solid rgba(212,175,55,0.35);
    }
    .hero-photo-wrap img {
      width: 100%; display: block; object-fit: cover;
      transition: transform 0.8s cubic-bezier(0.4,0,0.2,1);
    }
    .hero-photo-wrap:hover img { transform: scale(1.04); }

    /* Gold line separator */
    .gold-line {
      display: inline-block; width: 44px; height: 2px;
      background: #D4AF37; border-radius: 2px;
    }

    /* =============================================
       TEXT GRADIENT
    ============================================= */
    .text-gradient-gold {
      background: linear-gradient(135deg, #B38F24 0%, #D4AF37 50%, #E8C84A 100%);
      -webkit-background-clip: text; background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    /* =============================================
       BUTTONS (microinteractions)
    ============================================= */
    .btn-primary {
      display: inline-flex; align-items: center; gap: 10px;
      padding: 14px 32px; border-radius: 999px;
      background: #E63946; color: #fff;
      font-weight: 800; font-size: .875rem; letter-spacing: .06em; text-transform: uppercase;
      box-shadow: 0 8px 28px -5px rgba(230,57,70,0.5);
      transition: background 0.22s ease, transform 0.22s ease, box-shadow 0.22s ease;
    }
    .btn-primary:hover {
      background: #C52233; transform: translateY(-3px);
      box-shadow: 0 14px 36px -5px rgba(230,57,70,0.6);
    }
    .btn-primary .btn-arrow { transition: transform 0.22s ease; }
    .btn-primary:hover .btn-arrow { transform: translateX(4px) translateY(-2px); }

    .btn-ghost {
      display: inline-flex; align-items: center; gap: 8px;
      padding: 13px 30px; border-radius: 999px;
      background: rgba(255,255,255,0.08); color: #fff;
      font-weight: 700; font-size: .875rem;
      border: 1.5px solid rgba(255,255,255,0.25);
      backdrop-filter: blur(4px);
      transition: background 0.22s ease, border-color 0.22s ease, transform 0.22s ease;
    }
    .btn-ghost:hover {
      background: rgba(255,255,255,0.15);
      border-color: rgba(255,255,255,0.5);
      transform: translateY(-2px);
    }
    .btn-outline {
      display: inline-flex; align-items: center; gap: 8px;
      padding: 13px 28px; border-radius: 999px;
      background: #fff; color: #0F172A;
      font-weight: 700; font-size: .875rem;
      border: 2px solid #0F172A;
      transition: background 0.22s ease, color 0.22s ease, transform 0.22s ease;
    }
    .btn-outline:hover {
      background: #0F172A; color: #fff; transform: translateY(-2px);
    }
    .btn-outline .btn-icon { color: #D4AF37; transition: transform 0.22s ease; }
    .btn-outline:hover .btn-icon { transform: rotate(15deg); }

    /* =============================================
       LOGO WATERMARK
    ============================================= */
    .logo-wm-container {
      position: absolute; inset: 0;
      overflow: hidden; pointer-events: none;
      z-index: 0;
    }
    .logo-wm {
      position: absolute;
      user-select: none; pointer-events: none;
      will-change: transform, opacity;
      transition: opacity 0.1s linear;
    }
    .logo-wm img { display: block; }

    /* =============================================
       STECKBRIEF BADGE
    ============================================= */
    .steckbrief-badge {
      background: rgba(15,23,42,0.05);
      border: 1px solid rgba(212,175,55,0.28);
      border-radius: 12px; padding: 8px 14px;
    }

    /* =============================================
       FAQ
    ============================================= */
    details summary::-webkit-details-marker { display: none; }
    details[open] summary .faq-icon { transform: rotate(180deg); }

    /* =============================================
       TRUST BAR ITEMS
    ============================================= */
    .trust-item {
      transition: transform 0.22s ease;
    }
    .trust-item:hover { transform: translateY(-2px); }

    /* =============================================
       SECTION LABEL
    ============================================= */
    .section-label {
      display: inline-flex; align-items: center; gap: 8px;
      font-size: 11px; font-weight: 800;
      letter-spacing: .15em; text-transform: uppercase;
    }

    /* =============================================
       MOBILE MENU
    ============================================= */
    #mobileMenu { display: none; }
    #mobileMenu.open { display: block; }

    /* =============================================
       MOBILE: reduce animations
    ============================================= */
    @media (max-width: 768px) {
      .logo-wm { display: none; }
      .hero-animate { transition-duration: 0.5s; }
    }
  </style>"""

# Replace old style block
start_idx = src.index(OLD_STYLE_START)
end_idx   = src.index(OLD_STYLE_END) + len(OLD_STYLE_END)
src = src[:start_idx] + NEW_STYLE + src[end_idx:]
print("CSS replaced OK")

# ── 2. Replace <header> block ─────────────────────────────────────────────────
OLD_HEADER_START = '  <!-- ============================================================\n       NAVIGATION HEADER'
OLD_HEADER_END   = '  </header>'

# Find positions
h_start = src.index(OLD_HEADER_START)
h_end   = src.index(OLD_HEADER_END) + len(OLD_HEADER_END)

NEW_HEADER = '''  <!-- ============================================================
       NAVIGATION HEADER
       ============================================================ -->
  <header id="site-header">
    <div class="header-inner">

      <!-- Brand Logo -->
      <a href="#hero" id="nav-logo" class="flex items-center gap-2 shrink-0">
        <img src="img/logo/F3-3.avif" alt="SoccerProf Academy" class="h-11 sm:h-13 w-auto object-contain">
      </a>

      <!-- Desktop Nav -->
      <nav class="hidden lg:flex items-center gap-6" aria-label="Hauptnavigation">
        <a href="#angebote"  class="nav-link" data-section="angebote">Training</a>
        <a href="#methode"   class="nav-link" data-section="methode">Methode</a>
        <a href="#ueber-uns" class="nav-link" data-section="ueber-uns">Über uns</a>
        <a href="#preise"    class="nav-link" data-section="preise">Preise</a>
        <a href="#kontakt"   class="nav-link" data-section="kontakt">Kontakt</a>
      </nav>

      <!-- Right Side -->
      <div class="hidden lg:flex items-center gap-3">
        <a href="https://www.soccerprof.de/shop" target="_blank" rel="noopener" class="nav-shop flex items-center gap-1.5">
          <i class="fa-solid fa-bag-shopping text-xs"></i>
          <span>Shop</span>
        </a>
        <a href="#kontakt" class="nav-cta">
          <i class="fa-solid fa-calendar-check text-xs"></i>
          <span>Kostenloses Erstgespräch</span>
          <span class="cta-arrow text-xs">↗</span>
        </a>
      </div>

      <!-- Mobile Toggle -->
      <button id="mobileMenuBtn" class="lg:hidden text-white p-2 text-xl focus:outline-none" aria-label="Menü">
        <i class="fa-solid fa-bars"></i>
      </button>
    </div>

    <!-- Mobile Dropdown -->
    <div id="mobileMenu" class="lg:hidden bg-white border-b border-slate-200 px-6 py-5 space-y-3 shadow-xl">
      <a href="#angebote"  class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Training</a>
      <a href="#methode"   class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Trainingsmethode</a>
      <a href="#ueber-uns" class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Über uns</a>
      <a href="#preise"    class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Preise</a>
      <a href="#kontakt"   class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Kontakt</a>
      <a href="https://www.soccerprof.de/shop" target="_blank" class="block font-bold text-[#D4AF37] mobile-link">
        <i class="fa-solid fa-bag-shopping mr-1"></i>Shop
      </a>
      <a href="#kontakt" class="block w-full text-center py-3.5 rounded-full bg-[#E63946] text-white font-black uppercase text-xs tracking-wider shadow-md mobile-link">
        <i class="fa-solid fa-calendar-check mr-2"></i>Kostenloses Erstgespräch
      </a>
    </div>
  </header>'''

src = src[:h_start] + NEW_HEADER + src[h_end:]
print("Header replaced OK")

# ── 3. Replace Hero Section ───────────────────────────────────────────────────
OLD_HERO_START = '  <!-- ============================================================\n       1. HERO SECTION'
OLD_HERO_END   = '  </section>\n\n  <!-- ============================================================\n       TRUST-LEISTE'

h2_start = src.index(OLD_HERO_START)
h2_end   = src.index(OLD_HERO_END) + len('  </section>')

NEW_HERO = '''  <!-- ============================================================
       1. HERO SECTION – Split Layout, Premium
       ============================================================ -->
  <section id="hero" class="hero-section min-h-[96vh] flex items-center pt-24 pb-12 md:pt-28 md:pb-16">
    <!-- Logo Watermark in Hero (strategic, not distracting) -->
    <div class="logo-wm-container" id="heroWatermark"></div>

    <div class="hero-inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 xl:gap-16 items-center">

        <!-- LEFT: Text + CTAs -->
        <div class="lg:col-span-6 xl:col-span-7 space-y-7">

          <!-- Eyebrow -->
          <div class="hero-animate flex items-center gap-3" style="transition-delay:0ms">
            <span class="gold-line"></span>
            <span class="text-[#D4AF37] text-[11px] font-black tracking-[0.22em] uppercase">
              SoccerProf Academy Hamburg · UEFA-B-Lizenz
            </span>
            <span class="gold-line"></span>
          </div>

          <!-- H1 -->
          <h1 class="hero-animate text-4xl sm:text-5xl xl:text-6xl font-black text-white tracking-tight leading-[1.06]"
              style="transition-delay:120ms">
            Mehr Technik.<br>
            Mehr <span class="text-gradient-gold">Selbstvertrauen.</span><br>
            Mehr Spiel.
          </h1>

          <!-- Subheadline -->
          <p class="hero-animate text-slate-300 text-base sm:text-lg font-medium leading-relaxed max-w-xl"
             style="transition-delay:240ms">
            Individuelles Fußballtraining für Kinder und Jugendliche in Hamburg –
            abgestimmt auf die Stärken, Ziele und Entwicklung jedes Spielers.
            <strong class="text-white block mt-2">
              Die perfekte Ergänzung zum Vereinstraining.
            </strong>
          </p>

          <!-- CTAs -->
          <div class="hero-animate flex flex-col sm:flex-row items-start gap-4" style="transition-delay:360ms">
            <a href="#kontakt" class="btn-primary">
              <i class="fa-solid fa-calendar-check text-sm"></i>
              <span>Kostenloses Erstgespräch</span>
              <span class="btn-arrow">↗</span>
            </a>
            <a href="#angebote" class="btn-ghost">
              <span>Training entdecken</span>
              <i class="fa-solid fa-arrow-down text-xs text-[#D4AF37]"></i>
            </a>
          </div>

          <!-- Trust pills -->
          <div class="hero-animate flex flex-wrap gap-3 pt-2" style="transition-delay:480ms">
            <span class="trust-item text-[11px] font-bold text-white/70 border border-white/15 px-3 py-1.5 rounded-full backdrop-blur-sm">
              ★★★★★ Kundenbewertungen
            </span>
            <span class="trust-item text-[11px] font-bold text-white/70 border border-white/15 px-3 py-1.5 rounded-full backdrop-blur-sm">
              UEFA-B Lizenz
            </span>
            <span class="trust-item text-[11px] font-bold text-white/70 border border-white/15 px-3 py-1.5 rounded-full backdrop-blur-sm">
              Seit 2012
            </span>
            <span class="trust-item text-[11px] font-bold text-white/70 border border-white/15 px-3 py-1.5 rounded-full backdrop-blur-sm">
              3 Standorte Hamburg
            </span>
            <span class="trust-item text-[11px] font-bold text-white/70 border border-white/15 px-3 py-1.5 rounded-full backdrop-blur-sm">
              HSV-Ausbildung
            </span>
          </div>
        </div>

        <!-- RIGHT: Training Photo -->
        <div class="lg:col-span-6 xl:col-span-5 hero-animate" style="transition-delay:200ms">
          <div class="hero-photo-wrap">
            <div class="absolute top-4 left-4 z-10 px-3 py-1.5 rounded-full bg-slate-900/85 backdrop-blur-sm border border-[#D4AF37]/40 text-white text-[11px] font-black flex items-center gap-2">
              <i class="fa-solid fa-bullseye text-[#D4AF37] text-xs"></i>
              <span>100% Individueller Fokus</span>
            </div>
            <img src="img/packete/soccerprof-hamburg-kinder-jugendliche-fussballtraining.avif"
                 alt="Individuelles Fußballtraining Kinder Jugendliche Hamburg SoccerProf"
                 class="h-[440px] sm:h-[520px] xl:h-[580px] w-full object-cover">
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent"></div>
            <!-- Bottom info strip -->
            <div class="absolute bottom-0 left-0 right-0 p-5">
              <div class="flex items-center gap-3 bg-white/95 backdrop-blur-sm rounded-2xl p-3.5 shadow-xl border border-slate-100">
                <div class="w-10 h-10 rounded-xl bg-[#E63946] text-white flex items-center justify-center font-black shadow-md shrink-0">
                  <i class="fa-solid fa-futbol text-sm"></i>
                </div>
                <div>
                  <div class="text-xs font-black text-slate-900">SoccerProf Academy · Sami Ghaouar</div>
                  <div class="text-[10px] text-slate-500 font-semibold">Öjendorfer Weg 80 · 22119 Hamburg Billstedt</div>
                  <div class="text-[10px] text-[#D4AF37] font-black uppercase tracking-wider mt-0.5">Die perfekte Ergänzung zum Fußballverein ⚽</div>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>'''

src = src[:h2_start] + NEW_HERO + src[h2_end:]
print("Hero replaced OK")

# ── 4. Add logo watermark containers to key sections ─────────────────────────
# Add to: warum section, methode section, ueber-uns section, final CTA section
def add_wm_to_section(html, section_id, wm_id):
    """Inject a logo-wm-container div right after the opening section tag"""
    pattern = f'<section id="{section_id}"'
    idx = html.find(pattern)
    if idx == -1:
        print(f"  WARNING: section id={section_id} not found!")
        return html
    # Find end of opening tag
    tag_end = html.index('>', idx) + 1
    wm_div = f'\n    <div class="logo-wm-container" id="{wm_id}"></div>'
    html = html[:tag_end] + wm_div + html[tag_end:]
    print(f"  Added watermark container to #{section_id}")
    return html

src = add_wm_to_section(src, 'warum',     'warumWatermark')
src = add_wm_to_section(src, 'ueber-uns', 'ueberWatermark')
src = add_wm_to_section(src, 'angebote',  'angeboteWatermark')

# ── 5. Replace old script block with new comprehensive JS ────────────────────
OLD_SCRIPT_START = '  <!-- ============================================================\n       SCRIPTS: AOS & INTERACTION'
OLD_SCRIPT_END   = '</body>\n</html>'

s_start = src.index(OLD_SCRIPT_START)

NEW_SCRIPTS = '''  <!-- ============================================================
       SCRIPTS: AOS + PREMIUM INTERACTIONS
       ============================================================ -->
  <script src="https://unpkg.com/aos@next/dist/aos.js"></script>
  <script>
  (function() {
    'use strict';

    /* ──────────────────────────────────────────────────
       AOS INIT
    ────────────────────────────────────────────────── */
    document.addEventListener('DOMContentLoaded', function() {
      AOS.init({ duration: 720, easing: 'ease-out-cubic', once: false, mirror: true });
    });

    /* ──────────────────────────────────────────────────
       HERO STAGGER ANIMATION
    ────────────────────────────────────────────────── */
    window.addEventListener('load', function() {
      var elems = document.querySelectorAll('.hero-animate');
      elems.forEach(function(el) {
        var delay = parseInt(el.style.transitionDelay) || 0;
        setTimeout(function() { el.classList.add('visible'); }, delay + 120);
      });
    });

    /* ──────────────────────────────────────────────────
       HEADER: transforms on scroll
    ────────────────────────────────────────────────── */
    var header = document.getElementById('site-header');
    var lastScroll = 0;
    function updateHeader() {
      var y = window.scrollY;
      if (y > 60) {
        header.classList.add('header-scrolled');
      } else {
        header.classList.remove('header-scrolled');
      }
      lastScroll = y;
    }
    window.addEventListener('scroll', updateHeader, { passive: true });
    updateHeader();

    /* ──────────────────────────────────────────────────
       SMOOTH SCROLL – custom easing
    ────────────────────────────────────────────────── */
    function easeInOutCubic(t) {
      return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
    }
    function smoothScrollTo(target, duration) {
      var start = window.scrollY;
      var headerH = header ? header.getBoundingClientRect().height : 72;
      var targetY = target.getBoundingClientRect().top + start - headerH - 12;
      var startTime = null;
      function step(now) {
        if (!startTime) startTime = now;
        var elapsed = now - startTime;
        var progress = Math.min(elapsed / duration, 1);
        window.scrollTo(0, start + (targetY - start) * easeInOutCubic(progress));
        if (progress < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    }
    document.querySelectorAll('a[href^="#"]').forEach(function(link) {
      link.addEventListener('click', function(e) {
        var id = link.getAttribute('href').slice(1);
        var el = document.getElementById(id);
        if (!el) return;
        e.preventDefault();
        var dist = Math.abs(el.getBoundingClientRect().top);
        var dur  = Math.min(1200, Math.max(600, dist * 0.6));
        smoothScrollTo(el, dur);
        // close mobile menu
        var mm = document.getElementById('mobileMenu');
        if (mm) mm.classList.remove('open');
      });
    });

    /* ──────────────────────────────────────────────────
       MOBILE MENU TOGGLE
    ────────────────────────────────────────────────── */
    var mobileBtn  = document.getElementById('mobileMenuBtn');
    var mobileMenu = document.getElementById('mobileMenu');
    if (mobileBtn && mobileMenu) {
      mobileBtn.addEventListener('click', function() {
        mobileMenu.classList.toggle('open');
      });
    }

    /* ──────────────────────────────────────────────────
       ACTIVE NAV via IntersectionObserver
    ────────────────────────────────────────────────── */
    var navLinks = document.querySelectorAll('.nav-link[data-section]');
    var sections = [];
    navLinks.forEach(function(link) {
      var id = link.dataset.section;
      var el = document.getElementById(id);
      if (el) sections.push({ el: el, link: link });
    });
    if (sections.length && 'IntersectionObserver' in window) {
      var obs = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            sections.forEach(function(s) { s.link.classList.remove('active'); });
            var active = sections.find(function(s) { return s.el === entry.target; });
            if (active) active.link.classList.add('active');
          }
        });
      }, { rootMargin: '-30% 0px -60% 0px', threshold: 0 });
      sections.forEach(function(s) { obs.observe(s.el); });
    }

    /* ──────────────────────────────────────────────────
       FORM SUBMIT
    ────────────────────────────────────────────────── */
    window.handleFormSubmit = function(e) {
      e.preventDefault();
      var box = document.getElementById('formSuccess');
      if (box) box.classList.remove('hidden');
      setTimeout(function() {
        window.location.href = 'https://wa.me/4917684156542?text='
          + encodeURIComponent('Hallo Sami, ich habe gerade eine Anfrage für die SoccerProf Academy gesendet!');
      }, 1500);
    };

    /* ──────────────────────────────────────────────────
       LOGO WATERMARK GENERATOR + SCROLL PARALLAX
    ────────────────────────────────────────────────── */
    var isMobile = window.matchMedia('(max-width: 768px)').matches;
    var wmData   = []; // { el, baseY, speed, baseOpacity }

    function buildWatermarks(containerId, count, opacityRange, sizeRange) {
      var container = document.getElementById(containerId);
      if (!container || isMobile) return;
      // make parent relative if not already
      var parent = container.parentElement;
      if (getComputedStyle(parent).position === 'static') {
        parent.style.position = 'relative';
      }
      for (var i = 0; i < count; i++) {
        var el = document.createElement('div');
        el.className = 'logo-wm';
        var size = sizeRange[0] + Math.random() * (sizeRange[1] - sizeRange[0]);
        var left = 2 + Math.random() * 95;   // %
        var top  = 2 + Math.random() * 95;   // %
        var rot  = -20 + Math.random() * 40; // deg
        var op   = opacityRange[0] + Math.random() * (opacityRange[1] - opacityRange[0]);
        var speed = 0.04 + Math.random() * 0.12; // parallax multiplier

        el.style.cssText = [
          'width:' + size + 'px',
          'left:'  + left + '%',
          'top:'   + top  + '%',
          'transform: rotate(' + rot + 'deg)',
          'opacity:' + op
        ].join(';');

        var img = document.createElement('img');
        img.src = 'img/logo/F3-3.avif';
        img.alt = '';
        img.width  = size;
        img.height = size;
        img.style.cssText = 'display:block;width:100%;filter:grayscale(1)';
        img.loading = 'lazy';
        el.appendChild(img);
        container.appendChild(el);

        wmData.push({ el: el, baseTop: top, speed: speed, baseOp: op, rot: rot });
      }
    }

    // Build watermarks in specific containers
    buildWatermarks('heroWatermark',    28, [0.025, 0.055], [20, 55]);
    buildWatermarks('warumWatermark',   22, [0.03,  0.06],  [18, 48]);
    buildWatermarks('ueberWatermark',   18, [0.03,  0.065], [20, 50]);
    buildWatermarks('angeboteWatermark',16, [0.025, 0.05],  [18, 42]);

    /* Scroll-driven parallax for watermarks */
    var ticking = false;
    function updateWatermarks() {
      var scrollY = window.scrollY;
      var winH    = window.innerHeight;
      wmData.forEach(function(wm) {
        var rect = wm.el.closest('.logo-wm-container').getBoundingClientRect();
        // Position relative to viewport
        var relScroll = -rect.top; // positive when scrolling past
        var dy = relScroll * wm.speed;
        // Fade out logos that drift far
        var fadeFactor = Math.max(0, Math.min(1, 1 - Math.abs(dy) / 400));
        var op = wm.baseOp * fadeFactor;
        wm.el.style.transform = 'rotate(' + wm.rot + 'deg) translateY(' + dy + 'px)';
        wm.el.style.opacity   = op;
      });
      ticking = false;
    }
    window.addEventListener('scroll', function() {
      if (!ticking) { requestAnimationFrame(updateWatermarks); ticking = true; }
    }, { passive: true });

  })();
  </script>
</body>
</html>'''

src = src[:s_start] + NEW_SCRIPTS

# ── 6. Write output ───────────────────────────────────────────────────────────
with open(r'c:\Users\mario\Desktop\newsoccerprof\index.html', 'w', encoding='utf-8') as f:
    f.write(src)

lines = src.count('\n')
print(f"\nDone! {lines} lines, {len(src):,} bytes written.")
print("Watermark sections: hero, warum, ueber-uns, angebote")
print("JS features: hero stagger, header scroll, smooth scroll, active nav, logo parallax")
