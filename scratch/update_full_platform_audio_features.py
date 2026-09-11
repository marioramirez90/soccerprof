import os

workspace_dir = r"c:\Users\mario\Desktop\newsoccerprof"

def get_head(title="SoccerProf Academy | Privater Fußballtrainer Hamburg", desc="Individuelles Fußballtraining für Kinder, Jugendliche und Erwachsene in Hamburg."):
    return f'''<!DOCTYPE html>
<html lang="de" class="scroll-smooth">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="Fußballtraining Hamburg, individuelles Fußballtraining Hamburg, Fußballtrainer Hamburg, Sami Ghaouar, SoccerProf Academy">

  <!-- Open Graph -->
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="img/logo/F3-3.avif">
  <meta property="og:type" content="website">

  <!-- Favicon -->
  <link rel="icon" href="img/favicon.ico" type="image/x-icon">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            display: ['"Outfit"', 'sans-serif'],
          }},
          colors: {{
            brand: {{
              gold: '#D4AF37',
              goldLight: '#F3E5AB',
              goldGlow: 'rgba(212, 175, 55, 0.4)',
              red: '#E63946',
              redDark: '#C52233',
              dark: '#0F172A',
              darker: '#090D16',
              bgLight: '#F8FAFC',
            }}
          }},
          boxShadow: {{
            'gold-glow': '0 0 30px rgba(212, 175, 55, 0.35)',
            'red-glow': '0 10px 30px -5px rgba(230, 57, 70, 0.45)',
            'glass': '0 8px 32px 0 rgba(15, 23, 42, 0.08)',
            'card-hover': '0 25px 50px -12px rgba(15, 23, 42, 0.15)',
          }}
        }}
      }}
    }}
  </script>

  <!-- AOS CSS -->
  <link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css" />

  <!-- FontAwesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <style>
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: #F8FAFC;
      color: #0F172A;
      overflow-x: hidden;
    }}

    h1, h2, h3, .font-heading {{
      font-family: 'Outfit', sans-serif;
    }}

    .bg-mesh {{
      background-image:
        radial-gradient(at 10% 20%, rgba(212, 175, 55, 0.08) 0px, transparent 50%),
        radial-gradient(at 90% 10%, rgba(230, 57, 70, 0.08) 0px, transparent 50%),
        radial-gradient(at 50% 80%, rgba(15, 23, 42, 0.05) 0px, transparent 50%),
        radial-gradient(circle at 50% 50%, rgba(248, 250, 252, 0.85) 0%, #F8FAFC 100%);
    }}

    .grid-pattern {{
      background-size: 40px 40px;
      background-image:
        linear-gradient(to right, rgba(15, 23, 42, 0.03) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(15, 23, 42, 0.03) 1px, transparent 1px);
    }}

    .glass-card {{
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(226, 232, 240, 0.9);
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .glass-card:hover {{
      border-color: #D4AF37;
      transform: translateY(-6px);
      box-shadow: 0 22px 45px -10px rgba(212, 175, 55, 0.22), 0 0 20px rgba(212, 175, 55, 0.15);
    }}

    .glass-nav {{
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid rgba(226, 232, 240, 0.85);
    }}

    .text-gradient-gold {{
      background: linear-gradient(135deg, #B38F24 0%, #D4AF37 50%, #F3E5AB 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .text-gradient-red {{
      background: linear-gradient(135deg, #E63946 0%, #C52233 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    /* ============================================================
       MODERN NAVIGATION LINK HOVER UNDERLINE ANIMATION (Audio Wunsch)
       ============================================================ */
    .nav-link-anim {{
      position: relative;
      padding-bottom: 4px;
      transition: color 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .nav-link-anim::after {{
      content: '';
      position: absolute;
      bottom: -2px;
      left: 0;
      width: 100%;
      height: 3px;
      background: linear-gradient(90deg, #E63946 0%, #D4AF37 100%);
      border-radius: 99px;
      transform: scaleX(0);
      transform-origin: left;
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .nav-link-anim:hover::after,
    .nav-link-anim.active::after {{
      transform: scaleX(1);
    }}

    .nav-link-anim:hover {{
      color: #E63946;
    }}

    /* ============================================================
       MODERN BUTTON COLOR FILL ANIMATION (Audio Wunsch)
       ============================================================ */
    .btn-fill-red {{
      position: relative;
      overflow: hidden;
      z-index: 1;
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .btn-fill-red::before {{
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(135deg, #C52233 0%, #0F172A 100%);
      z-index: -1;
      transform: translateY(100%);
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      border-radius: inherit;
    }}

    .btn-fill-red:hover::before,
    .btn-fill-red:active::before {{
      transform: translateY(0);
    }}

    .btn-fill-gold {{
      position: relative;
      overflow: hidden;
      z-index: 1;
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .btn-fill-gold::before {{
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(135deg, #D4AF37 0%, #B38F24 100%);
      z-index: -1;
      transform: translateY(100%);
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      border-radius: inherit;
    }}

    .btn-fill-gold:hover::before,
    .btn-fill-gold:active::before {{
      transform: translateY(0);
    }}

    .btn-fill-gold:hover {{
      color: #0F172A !important;
      border-color: #D4AF37 !important;
    }}

    /* ============================================================
       GLOBAL SCROLLING LOGO PARTICLES (Audio Wunsch: 40-50 Logos, scaling & moving)
       ============================================================ */
    .global-logo-particle {{
      position: absolute;
      width: 42px;
      height: 42px;
      background-image: url('img/logo/F3-3.avif');
      background-size: contain;
      background-repeat: no-repeat;
      pointer-events: none;
      will-change: transform;
      transition: transform 0.15s linear;
    }}

    .floating-bg-image {{
      position: absolute;
      pointer-events: none;
      z-index: 1;
      opacity: 0.12;
      border-radius: 24px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.15);
      transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.8s ease;
      filter: grayscale(20%) saturate(120%);
    }}

    @keyframes float-slow {{
      0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
      50% {{ transform: translateY(-14px) rotate(2deg); }}
    }}
    .animate-float {{ animation: float-slow 7s ease-in-out infinite; }}

    details summary::-webkit-details-marker {{ display: none; }}
    details[open] summary .faq-icon {{ transform: rotate(180deg); }}
  </style>
</head>'''

def get_header(active_page=""):
    nav_items = [
        ("Training", "training.html"),
        ("Trainingsmethoden", "trainingsmethoden.html"),
        ("Über uns", "ueber-uns.html"),
        ("Preise", "preise.html"),
        ("Kontakt", "kontakt.html"),
    ]
    
    nav_links_html = ""
    for label, link in nav_items:
        is_active = (active_page == label)
        active_cls = "nav-link-anim text-[#E63946] active font-black" if is_active else "nav-link-anim text-slate-700"
        nav_links_html += f'<a href="{link}" class="{active_cls}">{label}</a>\n'

    return f'''<!-- HEADER -->
  <header id="main-header" class="fixed top-0 left-0 w-full z-50 glass-nav transition-all duration-300 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      <!-- Brand Logo -->
      <a href="index.html" class="flex items-center gap-3 group">
        <img src="img/logo/F3-3.avif" alt="SoccerProf Academy Logo"
          class="h-12 sm:h-14 w-auto object-contain group-hover:scale-105 transition-transform drop-shadow-sm">
      </a>

      <!-- Desktop Navigation Links mit Unterstrich & Hover Fill Animation -->
      <nav class="hidden lg:flex items-center gap-7 text-sm font-bold text-slate-700">
        {nav_links_html}
      </nav>

      <!-- Right Action Group: Shop & Primary CTA Buttons -->
      <div class="hidden sm:flex items-center gap-4">
        <a href="shop.html"
          class="btn-fill-gold flex items-center gap-2 px-4 py-2 rounded-full bg-slate-100 text-slate-800 font-bold text-xs border border-slate-200 shadow-sm">
          <i class="fa-solid fa-bag-shopping text-[#D4AF37]"></i>
          <span>Shop</span>
        </a>
        <a href="kontakt.html"
          class="btn-fill-red px-5 py-2.5 rounded-full bg-[#E63946] text-white font-black text-xs uppercase tracking-wider shadow-red-glow hover:shadow-xl flex items-center gap-2">
          <i class="fa-solid fa-calendar-check"></i>
          <span>Kostenloses Erstgespräch</span>
        </a>
      </div>

      <!-- Mobile Menu Toggle Button -->
      <button id="mobileMenuBtn" class="lg:hidden text-slate-800 text-2xl focus:outline-none p-2" aria-label="Menü öffnen">
        <i class="fa-solid fa-bars"></i>
      </button>
    </div>

    <!-- Mobile Dropdown Navigation -->
    <div id="mobileMenu" class="hidden lg:hidden bg-white/98 backdrop-blur-xl border-b border-slate-200 px-6 py-6 space-y-4 shadow-2xl">
      <a href="training.html" class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Training & Angebot</a>
      <a href="trainingsmethoden.html" class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Trainingsmethoden</a>
      <a href="ueber-uns.html" class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Über uns & Trainer</a>
      <a href="preise.html" class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Preise & Tarife</a>
      <a href="veranstaltungen.html" class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Veranstaltungen & Camps</a>
      <a href="jobs.html" class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Jobs & Karriere</a>
      <a href="faq.html" class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Häufige Fragen (FAQ)</a>
      <a href="kontakt.html" class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Kontakt & Standorte</a>
      <a href="shop.html" class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link flex items-center justify-between">
        <span>SoccerProf Shop</span>
        <i class="fa-solid fa-bag-shopping text-[#D4AF37]"></i>
      </a>
      <a href="kontakt.html"
        class="btn-fill-red block w-full text-center py-3.5 rounded-full bg-[#E63946] text-white font-black uppercase text-xs tracking-wider shadow-red-glow mobile-link">
        <i class="fa-solid fa-calendar-check mr-2"></i>Kostenloses Erstgespräch
      </a>
    </div>
  </header>'''

def get_footer():
    return '''<!-- FOOTER (Zweite Navigationsebene) -->
  <footer class="bg-slate-950 text-slate-400 py-16 border-t border-slate-800 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 pb-12 border-b border-slate-800">
        
        <!-- Spalte 1: Training -->
        <div class="space-y-3">
          <h4 class="text-white font-black text-xs uppercase tracking-wider">Training</h4>
          <ul class="space-y-2 text-xs">
            <li><a href="einzeltraining.html" class="hover:text-white transition-colors">Einzeltraining (1:1)</a></li>
            <li><a href="kleingruppe.html" class="hover:text-white transition-colors">Kleingruppentraining (5er)</a></li>
            <li><a href="mannschaft.html" class="hover:text-white transition-colors">Mannschaftstraining</a></li>
            <li><a href="trainingsmethoden.html" class="hover:text-white transition-colors">Trainingsmethoden</a></li>
            <li><a href="preise.html" class="hover:text-white transition-colors">Preise &amp; Tarife</a></li>
          </ul>
        </div>

        <!-- Spalte 2: SoccerProf -->
        <div class="space-y-3">
          <h4 class="text-white font-black text-xs uppercase tracking-wider">SoccerProf</h4>
          <ul class="space-y-2 text-xs">
            <li><a href="ueber-uns.html" class="hover:text-white transition-colors">Über uns</a></li>
            <li><a href="veranstaltungen.html" class="hover:text-white transition-colors">Veranstaltungen &amp; Camps</a></li>
            <li><a href="jobs.html" class="hover:text-white transition-colors">Jobs &amp; Karriere</a></li>
            <li><a href="faq.html" class="hover:text-white transition-colors">Häufige Fragen (FAQ)</a></li>
            <li><a href="kontakt.html" class="hover:text-white transition-colors">Kontakt &amp; Standorte</a></li>
          </ul>
        </div>

        <!-- Spalte 3: Service & Shop -->
        <div class="space-y-3">
          <h4 class="text-white font-black text-xs uppercase tracking-wider">Service</h4>
          <ul class="space-y-2 text-xs">
            <li><a href="shop.html" class="hover:text-white transition-colors">SoccerProf Shop</a></li>
            <li><a href="kontakt.html" class="hover:text-white transition-colors">Kostenloses Erstgespräch</a></li>
            <li><a href="kontakt.html" class="hover:text-white transition-colors">Direkter Ansprechpartner</a></li>
          </ul>
        </div>

        <!-- Spalte 4: Rechtlich -->
        <div class="space-y-3">
          <h4 class="text-white font-black text-xs uppercase tracking-wider">Rechtlich</h4>
          <ul class="space-y-2 text-xs">
            <li><a href="impressum.html" class="hover:text-white transition-colors">Impressum</a></li>
            <li><a href="datenschutz.html" class="hover:text-white transition-colors">Datenschutzrichtlinie</a></li>
            <li><a href="cookie-richtlinie.html" class="hover:text-white transition-colors">Cookie-Richtlinie</a></li>
          </ul>
        </div>

      </div>

      <!-- Footer Bottom -->
      <div class="pt-8 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-500 gap-4">
        <div class="flex items-center gap-3">
          <img src="img/logo/F3-3.avif" alt="SoccerProf Logo" class="h-8 w-auto object-contain">
          <span>© 2026 SoccerProf Academy · Sami Ghaouar · Alle Rechte vorbehalten.</span>
        </div>
        <div class="font-bold text-slate-400">
          DIE PERFEKTE ERGÄNZUNG ZUM FUßBALLVEREIN 👍 ⚽
        </div>
      </div>
    </div>
  </footer>

  <!-- MOBILE STICKY BAR -->
  <div class="sm:hidden fixed bottom-0 left-0 w-full z-40 bg-white/95 backdrop-blur-md border-t border-slate-200 px-4 py-2.5 flex items-center justify-between shadow-2xl">
    <div>
      <div class="text-[11px] font-black text-slate-900">SoccerProf Academy</div>
      <div class="text-[9px] text-[#D4AF37] font-black uppercase">Sami Ghaouar · Hamburg</div>
    </div>
    <a href="kontakt.html" class="btn-fill-red px-4 py-2 rounded-full bg-[#E63946] text-white font-black text-xs uppercase tracking-wider shadow-red-glow flex items-center gap-1.5">
      <i class="fa-solid fa-calendar-check"></i>
      <span>Erstgespräch</span>
    </a>
  </div>'''

def get_scripts():
    return '''<!-- SCRIPTS -->
  <script src="https://unpkg.com/aos@next/dist/aos.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      AOS.init({
        duration: 750,
        easing: 'ease-out-cubic',
        once: false,
        mirror: true
      });

      // Mobile Menu Toggle
      const mobileMenuBtn = document.getElementById('mobileMenuBtn');
      const mobileMenu = document.getElementById('mobileMenu');
      if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => mobileMenu.classList.toggle('hidden'));
        document.querySelectorAll('.mobile-link').forEach(link => {
          link.addEventListener('click', () => mobileMenu.classList.add('hidden'));
        });
      }

      // ============================================================
      // DYNAMIC 40-50 LOGO BACKGROUND OVERLAY (Audio Wunsch)
      // sich vergrößern, verkleinern & überall bewegen beim Scrollen
      // ============================================================
      const bgOverlay = document.getElementById('logo-bg-overlay');
      if (bgOverlay) {
        const particleCount = window.innerWidth < 768 ? 20 : 45;
        const particlesData = [];

        for (let i = 0; i < particleCount; i++) {
          const p = document.createElement('div');
          p.className = 'global-logo-particle';
          const initialX = Math.random() * 95;
          const initialY = Math.random() * 95;
          const baseScale = 0.5 + Math.random() * 1.1;
          const opacity = 0.03 + Math.random() * 0.05; // leicht transparent

          p.style.top = initialY + '%';
          p.style.left = initialX + '%';
          p.style.opacity = opacity;
          p.style.transform = `scale(${baseScale}) rotate(${Math.random() * 360}deg)`;

          bgOverlay.appendChild(p);

          particlesData.push({
            element: p,
            baseScale: baseScale,
            speed: (i % 5 + 1) * 0.03,
            rotSpeed: (Math.random() - 0.5) * 0.2,
            initialY: initialY,
            initialX: initialX,
            phase: Math.random() * Math.PI * 2
          });
        }

        // Scroll listener: Logos move, rotate, scale up & down (vergrößern/verkleinern)
        window.addEventListener('scroll', () => {
          const scrolled = window.scrollY;
          particlesData.forEach((pd, idx) => {
            // Vergrößern / Verkleinern Welle
            const scaleWave = pd.baseScale + Math.sin(scrolled * 0.0025 + pd.phase) * 0.4;
            const moveY = scrolled * pd.speed * 0.15;
            const moveX = Math.sin(scrolled * 0.0012 + pd.phase) * 20;
            const rot = scrolled * pd.rotSpeed + idx * 10;

            pd.element.style.transform = `translate(${moveX}px, ${moveY}px) scale(${Math.max(0.2, scaleWave)}) rotate(${rot}deg)`;
          });
        });
      }
    });

    function handleFormSubmit(e) {
      e.preventDefault();
      window.location.href = "https://wa.me/4917684156542?text=" + encodeURIComponent("Hallo Sami, ich habe eine Anfrage gesendet!");
    }
  </script>
</body>
</html>'''

# ============================================================
# 1. BUILD INDEX.HTML (Startseite mit neuem Button Fill & Logo Animation)
# ============================================================
index_body = f'''<body class="bg-mesh relative grid-pattern antialiased text-slate-900 pb-20 sm:pb-0">

  <!-- 40-50 LOGO BACKGROUND ANIMATION OVERLAY (Audio Wunsch) -->
  <div id="logo-bg-overlay" class="fixed inset-0 pointer-events-none overflow-hidden z-0"></div>

  <!-- Ambient Glow Orbs -->
  <div class="fixed top-20 left-10 w-96 h-96 bg-[#D4AF37]/10 rounded-full blur-3xl pointer-events-none -z-10 animate-float"></div>
  <div class="fixed top-1/2 right-10 w-[30rem] h-[30rem] bg-[#E63946]/10 rounded-full blur-3xl pointer-events-none -z-10 animate-pulse-glow"></div>

  {get_header(active_page="Home")}

  <!-- ============================================================
       1. HERO SECTION (Links-bündig)
       ============================================================ -->
  <section id="hero" class="relative pt-36 pb-20 md:pt-44 md:pb-28 overflow-hidden min-h-[85vh] flex items-center z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full relative">
      <div class="max-w-3xl text-left space-y-7" data-aos="fade-right">

        <!-- Badge: Hamburg & Zielgruppe -->
        <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/95 border border-[#D4AF37] shadow-sm backdrop-blur-md">
          <span class="w-2.5 h-2.5 rounded-full bg-[#D4AF37] animate-ping"></span>
          <span class="text-xs font-black tracking-wider text-slate-900 uppercase">
            HAMBURG · KINDER, JUGENDLICHE &amp; AMBITIONIERTE SPIELER
          </span>
        </div>

        <!-- Hauptüberschrift (Kompakte Schriftgröße) -->
        <h1 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight leading-[1.18]">
          PRIVATER FUßBALL-TRAINER <br>
          <span class="text-gradient-gold">FÜR INDIVIDUELLES TRAINING</span> <br>
          <span class="relative inline-block text-slate-900">
            FÜR ANFÄNGER &amp; PROS.
            <svg class="absolute -bottom-2 left-0 w-full h-3 text-[#E63946]" viewBox="0 0 200 9" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M2 7C50 2 150 2 198 7" stroke="currentColor" stroke-width="4.5" stroke-linecap="round" />
            </svg>
          </span>
        </h1>

        <!-- Nutzen-Subline & Ergänzung zum Verein -->
        <p class="text-sm sm:text-base text-slate-700 font-medium leading-relaxed max-w-2xl">
          Individuelles Fußballtraining für Kinder, Jugendliche und Erwachsene – abgestimmt auf die Stärken, Ziele und Entwicklung jedes Spielers.
          <span class="block mt-1.5 font-bold text-slate-900">
            Professionelle Ergänzung zum Vereinstraining.
          </span>
        </p>

        <!-- CTAs mit Modern Button Color Fill Animation (Audio Wunsch) -->
        <div class="flex flex-col sm:flex-row items-center justify-start gap-4 pt-2">
          <a href="kontakt.html"
            class="btn-fill-red w-full sm:w-auto px-8 py-4 rounded-full bg-[#E63946] text-white font-black text-sm uppercase tracking-wider shadow-red-glow hover:shadow-2xl flex items-center justify-center gap-3 group">
            <span>KOSTENLOSES ERSTGESPRÄCH</span>
            <i class="fa-solid fa-arrow-right group-hover:translate-x-1 transition-transform"></i>
          </a>
          <a href="training.html"
            class="btn-fill-gold w-full sm:w-auto px-8 py-4 rounded-full bg-white/95 text-slate-900 border-2 border-slate-900 font-bold text-sm shadow-sm flex items-center justify-center gap-2">
            <span>TRAINING ENTDECKEN</span>
            <i class="fa-solid fa-futbol text-xs text-[#D4AF37]"></i>
          </a>
        </div>

        <!-- Trust-Signale -->
        <div class="pt-6 border-t border-slate-200/90 grid grid-cols-2 sm:grid-cols-4 gap-3 bg-white/80 p-4 rounded-2xl backdrop-blur-md border border-slate-200/60 shadow-sm max-w-2xl">
          <div class="text-left">
            <div class="text-lg font-black text-slate-900 flex items-center gap-1"><span>★★★★★</span></div>
            <div class="text-[11px] text-slate-600 font-bold">Kundenbewertungen</div>
          </div>
          <div class="text-left">
            <div class="text-lg font-black text-slate-900">UEFA-B</div>
            <div class="text-[11px] text-slate-600 font-bold">Lizenz-Trainer</div>
          </div>
          <div class="text-left">
            <div class="text-lg font-black text-[#D4AF37]">Seit 2012</div>
            <div class="text-[11px] text-slate-600 font-bold">Trainer-Erfahrung</div>
          </div>
          <div class="text-left">
            <div class="text-lg font-black text-[#E63946]">Hamburg</div>
            <div class="text-[11px] text-slate-600 font-bold">3 Standorte</div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- DYNAMIC FLOATING BACKGROUND IMAGES -->
  <div class="relative w-full pointer-events-none overflow-hidden h-0">
    <img src="img/sami/Athletiktraining.avif" alt="Athletik" class="floating-bg-image float-img-1 w-64 h-64 object-cover top-[600px] left-[-40px]">
    <img src="img/bilderwebsite/Fußballtraining auf Kunstrasen.avif" alt="Kunstrasen" class="floating-bg-image float-img-2 w-72 h-72 object-cover top-[1400px] right-[-50px]">
    <img src="img/sami/Technik Fußstellung.avif" alt="Technik" class="floating-bg-image float-img-3 w-60 h-60 object-cover top-[2400px] left-[-30px]">
    <img src="img/packete/kleingruppe.avif" alt="Kleingruppe" class="floating-bg-image float-img-4 w-80 h-80 object-cover top-[3400px] right-[-60px]">
  </div>

  <!-- ============================================================
       2. WARUM INDIVIDUELLES TRAINING?
       ============================================================ -->
  <section class="py-20 relative z-10 bg-white/80 backdrop-blur-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">

      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4" data-aos="fade-up">
        <div class="inline-block px-3.5 py-1 rounded-full bg-[#E63946]/10 text-[#E63946] font-black text-xs uppercase tracking-widest border border-[#E63946]/30">
          Die Herausforderung im Vereinsalltag
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight leading-tight">
          Warum individuelles Fußballtraining?
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg leading-relaxed">
          Mannschaftstraining ist extrem wichtig. Doch wenn 15–20 Spieler gleichzeitig trainieren, bleibt im Vereinsalltag häufig zu wenig Zeit für individuelle Korrekturen, Vororientierung und persönliche Entwicklungsziele. <strong>Genau hier setzt SoccerProf an.</strong>
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="glass-card p-8 rounded-3xl space-y-4 border-t-4 border-t-[#D4AF37]" data-aos="fade-up" data-aos-delay="100">
          <div class="w-14 h-14 rounded-2xl bg-slate-900 text-[#D4AF37] flex items-center justify-center text-2xl font-black shadow-md">
            <i class="fa-solid fa-eye"></i>
          </div>
          <h3 class="text-xl font-black text-slate-900">100% Aufmerksamkeit</h3>
          <p class="text-slate-600 text-sm leading-relaxed">
            Jede Fußstellung, jede Ballberührung und jede Körperhaltung wird im Detail korrigiert. Keine unentdeckten Fehler in der Menge.
          </p>
        </div>

        <div class="glass-card p-8 rounded-3xl space-y-4 border-t-4 border-t-[#E63946]" data-aos="fade-up" data-aos-delay="200">
          <div class="w-14 h-14 rounded-2xl bg-[#E63946] text-white flex items-center justify-center text-2xl font-black shadow-red-glow">
            <i class="fa-solid fa-arrows-rotate"></i>
          </div>
          <h3 class="text-xl font-black text-slate-900">Maximale Ballaktionen</h3>
          <p class="text-slate-600 text-sm leading-relaxed">
            Statt langanstehender Wartezeiten an Hütchenreihen erhält der Spieler in 60 bis 90 Minuten ein Vielfaches an Kontakten und Schüssen.
          </p>
        </div>

        <div class="glass-card p-8 rounded-3xl space-y-4 border-t-4 border-t-slate-900" data-aos="fade-up" data-aos-delay="300">
          <div class="w-14 h-14 rounded-2xl bg-slate-900 text-white flex items-center justify-center text-2xl font-black shadow-md">
            <i class="fa-solid fa-chart-line"></i>
          </div>
          <h3 class="text-xl font-black text-slate-900">Maßgeschneiderter Fortschritt</h3>
          <p class="text-slate-600 text-sm leading-relaxed">
            Ob schwacher Fuß, Vororientierung, Schnelligkeit oder Selbstvertrauen – wir trainieren genau das, was den Spieler weiterbringt.
          </p>
        </div>
      </div>

    </div>
  </section>

  <!-- ============================================================
       3. WÄHLE DAS PASSENDE TRAINING
       ============================================================ -->
  <section id="pakete" class="py-20 bg-slate-900 text-white relative z-10 overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4" data-aos="fade-up">
        <div class="inline-block px-4 py-1 rounded-full bg-[#D4AF37]/20 text-[#D4AF37] font-black text-xs uppercase tracking-widest border border-[#D4AF37]/30">
          Deine Optionen im Überblick
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black tracking-tight leading-tight">
          WÄHLE DAS PASSENDE TRAINING FÜR DICH
        </h2>
        <p class="text-slate-300 font-medium text-base sm:text-lg">
          Finde das Training, das zu dir und deinen Zielen passt.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-stretch max-w-6xl mx-auto">
        
        <!-- Einzeltraining -->
        <div class="bg-slate-800/80 border border-slate-700/80 rounded-3xl p-8 flex flex-col justify-between hover:border-[#D4AF37] transition-all duration-300 shadow-xl group" data-aos="fade-up" data-aos-delay="100">
          <div>
            <div class="w-full h-48 rounded-2xl overflow-hidden mb-6 relative">
              <img src="img/packete/soccerprof-hamburg-kinder-jugendliche-fussballtraining.avif" alt="Einzeltraining" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <div class="absolute top-3 left-3 px-3 py-1 rounded-full bg-slate-900/90 text-[#D4AF37] text-xs font-black uppercase border border-[#D4AF37]/50">
                1:1 Betreuung
              </div>
            </div>
            <h3 class="text-2xl font-black text-white mb-2">Einzeltraining</h3>
            <p class="text-slate-300 text-xs sm:text-sm font-semibold mb-4 text-[#D4AF37]">
              100% individuelle Fußball-Einheiten
            </p>
            <p class="text-slate-400 text-xs leading-relaxed mb-6">
              Individuelle Fußball-Einheiten für Spieler, die gezielt an ihren Stärken und Schwächen arbeiten möchten.
            </p>
            <ul class="space-y-2.5 text-xs text-slate-300 mb-8 border-t border-slate-700/60 pt-4">
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> 1:1 Betreuung</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Individuell abgestimmte Inhalte</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Technik &amp; Taktik</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Kognitive Fähigkeiten</li>
            </ul>
          </div>
          <a href="einzeltraining.html" class="btn-fill-gold w-full py-4 rounded-2xl bg-white/10 text-white font-black text-xs uppercase tracking-wider text-center block transition-all flex items-center justify-center gap-2 border border-white/20">
            <span>Einzeltraining entdecken</span>
            <i class="fa-solid fa-arrow-right"></i>
          </a>
        </div>

        <!-- Kleingruppentraining -->
        <div class="bg-gradient-to-b from-slate-800 to-slate-900 border-2 border-[#E63946] rounded-3xl p-8 flex flex-col justify-between relative shadow-red-glow group transform md:-translate-y-4" data-aos="fade-up" data-aos-delay="200">
          <div class="absolute -top-3.5 left-1/2 -translate-x-1/2 bg-[#E63946] text-white font-black text-[10px] uppercase px-4 py-1.5 rounded-full shadow-md tracking-wider">
            Feste 5er-Gruppe
          </div>
          <div>
            <div class="w-full h-48 rounded-2xl overflow-hidden mb-6 relative mt-2">
              <img src="img/packete/kleingruppe.avif" alt="Kleingruppe" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <div class="absolute top-3 left-3 px-3 py-1 rounded-full bg-[#E63946] text-white text-xs font-black uppercase">
                Für 2–6 Spieler
              </div>
            </div>
            <h3 class="text-2xl font-black text-white mb-2">Kleingruppentraining</h3>
            <p class="text-slate-300 text-xs sm:text-sm font-semibold mb-4 text-[#E63946]">
              Gemeinsam trainieren &amp; individuell gefördert werden
            </p>
            <p class="text-slate-400 text-xs leading-relaxed mb-6">
              Gemeinsam trainieren und trotzdem individuell gefördert werden. Für selbst organisierte Gruppen &amp; Teams.
            </p>
            <ul class="space-y-2.5 text-xs text-slate-300 mb-8 border-t border-slate-700/60 pt-4">
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#E63946]"></i> Feste 5er-Gruppen</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#E63946]"></i> Spielnahe Wettkampfformen</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#E63946]"></i> Teamgeist &amp; Motivation</li>
            </ul>
          </div>
          <a href="kleingruppe.html" class="btn-fill-red w-full py-4 rounded-2xl bg-[#E63946] text-white font-black text-xs uppercase tracking-wider text-center block transition-all shadow-red-glow flex items-center justify-center gap-2">
            <span>Kleingruppe entdecken</span>
            <i class="fa-solid fa-arrow-right"></i>
          </a>
        </div>

        <!-- Mannschaftstraining -->
        <div class="bg-slate-800/80 border border-slate-700/80 rounded-3xl p-8 flex flex-col justify-between hover:border-[#D4AF37] transition-all duration-300 shadow-xl group" data-aos="fade-up" data-aos-delay="300">
          <div>
            <div class="w-full h-48 rounded-2xl overflow-hidden mb-6 relative">
              <img src="img/packete/Fußballspieler auf Bank.avif" alt="Mannschaftstraining" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <div class="absolute top-3 left-3 px-3 py-1 rounded-full bg-slate-900/90 text-[#D4AF37] text-xs font-black uppercase border border-[#D4AF37]/50">
                Für Vereine &amp; Teams
              </div>
            </div>
            <h3 class="text-2xl font-black text-white mb-2">Mannschaftstraining</h3>
            <p class="text-slate-300 text-xs sm:text-sm font-semibold mb-4 text-[#D4AF37]">
              Gezielte Teamförderung vor Ort
            </p>
            <p class="text-slate-400 text-xs leading-relaxed mb-6">
              Professionelles Training für Mannschaften, Vereine und Teams direkt auf eurem Vereinsgelände.
            </p>
            <ul class="space-y-2.5 text-xs text-slate-300 mb-8 border-t border-slate-700/60 pt-4">
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Taktische Feinabstimmung</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Positionsspezifischer Fokus</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Vor Ort im Verein</li>
            </ul>
          </div>
          <a href="mannschaft.html" class="btn-fill-gold w-full py-4 rounded-2xl bg-white/10 text-white font-black text-xs uppercase tracking-wider text-center block transition-all flex items-center justify-center gap-2 border border-white/20">
            <span>Mannschaftstraining entdecken</span>
            <i class="fa-solid fa-arrow-right"></i>
          </a>
        </div>

      </div>

    </div>
  </section>

  <!-- ============================================================
       4. DYNAMISCHE BILD-STORYTELLING-SECTION
       ============================================================ -->
  <section class="py-20 bg-white/80 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">

      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4" data-aos="fade-up">
        <div class="inline-block px-3.5 py-1 rounded-full bg-[#E63946]/10 text-[#E63946] font-black text-xs uppercase tracking-widest border border-[#E63946]/30">
          Unsere Philosophie
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          ANALYSIEREN. TRAINIEREN. <span class="text-gradient-red">VERBESSERN.</span>
        </h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="glass-card p-6 rounded-3xl space-y-4" data-aos="fade-up" data-aos-delay="100">
          <div class="w-full h-56 rounded-2xl overflow-hidden shadow-md">
            <img src="img/sami/Ich Taktiktafel.avif" alt="Analysieren" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500">
          </div>
          <h3 class="text-xl font-black text-slate-900">01 · ANALYSIEREN</h3>
          <p class="text-slate-600 text-xs leading-relaxed">
            Wir analysieren die Bewegungsabläufe, Passpräzision und das Stellungsspiel des Spielers im Detail.
          </p>
        </div>

        <div class="glass-card p-6 rounded-3xl space-y-4" data-aos="fade-up" data-aos-delay="200">
          <div class="w-full h-56 rounded-2xl overflow-hidden shadow-md">
            <img src="img/sami/Technik Fußstellung.avif" alt="Trainieren" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500">
          </div>
          <h3 class="text-xl font-black text-slate-900">02 · TRAINIEREN</h3>
          <p class="text-slate-600 text-xs leading-relaxed">
            Gezieltes Training mit hoher Frequenz, um neue Automatismen fest im Muskelgedächtnis zu verankern.
          </p>
        </div>

        <div class="glass-card p-6 rounded-3xl space-y-4" data-aos="fade-up" data-aos-delay="300">
          <div class="w-full h-56 rounded-2xl overflow-hidden shadow-md">
            <img src="img/sami/Athletiktraining.avif" alt="Verbessern" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500">
          </div>
          <h3 class="text-xl font-black text-slate-900">03 · VERBESSERN</h3>
          <p class="text-slate-600 text-xs leading-relaxed">
            Spürbarer Leistungssprung auf dem Platz – für mehr Durchsetzungskraft und Selbstvertrauen im Spiel.
          </p>
        </div>
      </div>

    </div>
  </section>

  <!-- ============================================================
       5. TRAININGSMETHODEN
       ============================================================ -->
  <section class="py-20 bg-slate-50 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row items-end justify-between mb-12 gap-4">
        <div>
          <div class="text-xs font-black text-[#D4AF37] uppercase tracking-widest mb-2">Schwerpunkte</div>
          <h2 class="text-3xl sm:text-4xl font-black text-slate-900">Gezielte Trainingsmethoden</h2>
        </div>
        <a href="trainingsmethoden.html" class="btn-fill-gold px-6 py-3 rounded-full bg-slate-900 text-white font-bold text-xs uppercase transition-colors">
          Alle Trainingsmethoden entdecken →
        </a>
      </div>

      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div class="p-5 rounded-2xl bg-white border border-slate-200 shadow-sm hover:border-[#D4AF37] transition-all">
          <i class="fa-solid fa-futbol text-xl text-[#D4AF37] mb-2"></i>
          <div class="font-black text-sm text-slate-900">Technik</div>
          <div class="text-xs text-slate-500 mt-1">Ballannahme, Dribbling, Passspiel</div>
        </div>
        <div class="p-5 rounded-2xl bg-white border border-slate-200 shadow-sm hover:border-[#E63946] transition-all">
          <i class="fa-solid fa-brain text-xl text-[#E63946] mb-2"></i>
          <div class="font-black text-sm text-slate-900">Kognition</div>
          <div class="text-xs text-slate-500 mt-1">Handlungstempo &amp; Entscheidungen</div>
        </div>
        <div class="p-5 rounded-2xl bg-white border border-slate-200 shadow-sm hover:border-[#D4AF37] transition-all">
          <i class="fa-solid fa-person-running text-xl text-[#D4AF37] mb-2"></i>
          <div class="font-black text-sm text-slate-900">Koordination</div>
          <div class="text-xs text-slate-500 mt-1">Laufschule &amp; Beweglichkeit</div>
        </div>
        <div class="p-5 rounded-2xl bg-white border border-slate-200 shadow-sm hover:border-[#E63946] transition-all">
          <i class="fa-solid fa-dumbbell text-xl text-[#E63946] mb-2"></i>
          <div class="font-black text-sm text-slate-900">Kraft &amp; Ausdauer</div>
          <div class="text-xs text-slate-500 mt-1">Fußballspezifische Fitness</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================
       6. TRAINER SAMI GHAOUAR
       ============================================================ -->
  <section class="py-20 bg-slate-900 text-white relative z-10">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
        <div class="md:col-span-5 text-center">
          <img src="img/sami/sami daumen hoch.avif" alt="Sami Ghaouar" class="w-full h-80 object-cover rounded-3xl border-2 border-[#D4AF37] shadow-2xl">
        </div>
        <div class="md:col-span-7 space-y-4">
          <div class="text-xs font-black text-[#D4AF37] uppercase tracking-widest">Gründer &amp; Head Coach</div>
          <h2 class="text-3xl sm:text-4xl font-black">Sami Ghaouar</h2>
          <p class="text-slate-300 text-sm leading-relaxed font-medium">
            Sami besitzt die offizielle UEFA-B-Lizenz und verfügt über jahrelange Erfahrung als Trainer und Spieler (unter anderem im Nachwuchs des Hamburger SV).
          </p>
          <div class="pt-2">
            <a href="ueber-uns.html" class="btn-fill-red inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#E63946] text-white font-black text-xs uppercase tracking-wider">
              <span>Mehr über SoccerProf erfahren</span>
              <i class="fa-solid fa-arrow-right"></i>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================
       7. VERANSTALTUNGEN & CAMPS
       ============================================================ -->
  <section class="py-16 bg-white relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="p-8 sm:p-12 rounded-3xl bg-slate-900 text-white flex flex-col md:flex-row items-center justify-between gap-8 border-2 border-[#D4AF37]">
        <div class="space-y-3 max-w-xl">
          <div class="text-xs font-black text-[#D4AF37] uppercase tracking-widest">Camps · Turniere · Events</div>
          <h3 class="text-2xl sm:text-3xl font-black">Fußballcamps &amp; Kindergeburtstage</h3>
          <p class="text-slate-300 text-xs sm:text-sm">
            Regelmäßige Feriencamps, spannende Turniere und unvergessliche Kindergeburtstage voller Fußballaction.
          </p>
        </div>
        <a href="veranstaltungen.html" class="btn-fill-red shrink-0 px-8 py-4 rounded-full bg-[#E63946] text-white font-black text-xs uppercase tracking-wider">
          Alle Veranstaltungen ansehen →
        </a>
      </div>
    </div>
  </section>

  <!-- ============================================================
       8. FAQ ACCORDION
       ============================================================ -->
  <section class="py-20 bg-slate-50 relative z-10">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-12 space-y-3">
        <h2 class="text-3xl font-black text-slate-900">Häufig gestellte Fragen (FAQ)</h2>
        <p class="text-slate-600 text-sm">Wichtige Antworten vor dem ersten Training</p>
      </div>

      <div class="space-y-4">
        <details class="glass-card rounded-2xl p-5 cursor-pointer border border-slate-200">
          <summary class="flex items-center justify-between font-black text-slate-900 text-sm select-none">
            <span>Für welches Alter ist das SoccerProf-Training geeignet?</span>
            <i class="fa-solid fa-chevron-down text-xs text-[#D4AF37] faq-icon"></i>
          </summary>
          <div class="pt-3 text-xs text-slate-600 leading-relaxed border-t border-slate-200/60 mt-3">
            Unser Schwerpunkt liegt auf Kindern und Jugendlichen aller Altersstufen sowie ambitionierten Erwachsenen.
          </div>
        </details>

        <details class="glass-card rounded-2xl p-5 cursor-pointer border border-slate-200">
          <summary class="flex items-center justify-between font-black text-slate-900 text-sm select-none">
            <span>Ist das Training eine Konkurrenz zum Vereinsfußball?</span>
            <i class="fa-solid fa-chevron-down text-xs text-[#D4AF37] faq-icon"></i>
          </summary>
          <div class="pt-3 text-xs text-slate-600 leading-relaxed border-t border-slate-200/60 mt-3">
            Nein! Es ist die perfekte Ergänzung zum Fußballverein 👍 ⚽.
          </div>
        </details>
      </div>

      <div class="mt-8 text-center">
        <a href="faq.html" class="text-xs font-black text-[#E63946] uppercase hover:underline">
          Alle Fragen &amp; Antworten anzeigen →
        </a>
      </div>
    </div>
  </section>

  {get_footer()}
  {get_scripts()}'''

with open(os.path.join(workspace_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(get_head("SoccerProf Academy | Privater Fußballtrainer Hamburg", "Individuelles Fußballtraining in Hamburg.") + index_body)

print("Updated index.html with new button fill effects and logo scroll animation overlay!")
