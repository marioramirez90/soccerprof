import os

workspace_dir = r"c:\Users\mario\Desktop\newsoccerprof"

def get_head(title="SoccerProf Academy | Privater Fußballtrainer Hamburg", desc="Individuelles Fußballtraining für Kinder, Jugendliche und Erwachsene in Hamburg."):
    html = '''<!DOCTYPE html>
<html lang="de" class="scroll-smooth">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>__TITLE__</title>
  <meta name="description" content="__DESC__">
  <meta name="keywords" content="Fußballtraining Hamburg, individuelles Fußballtraining Hamburg, Fußballtrainer Hamburg, Sami Ghaouar, SoccerProf Academy">

  <!-- Open Graph -->
  <meta property="og:title" content="__TITLE__">
  <meta property="og:description" content="__DESC__">
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
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            display: ['"Outfit"', 'sans-serif'],
          },
          colors: {
            brand: {
              gold: '#D4AF37',
              goldLight: '#F3E5AB',
              goldGlow: 'rgba(212, 175, 55, 0.4)',
              red: '#E63946',
              redDark: '#C52233',
              dark: '#0F172A',
              darker: '#090D16',
              bgLight: '#F8FAFC',
            }
          },
          boxShadow: {
            'gold-glow': '0 0 30px rgba(212, 175, 55, 0.35)',
            'red-glow': '0 10px 30px -5px rgba(230, 57, 70, 0.45)',
            'glass': '0 8px 32px 0 rgba(15, 23, 42, 0.08)',
            'card-hover': '0 25px 50px -12px rgba(15, 23, 42, 0.15)',
          }
        }
      }
    }
  </script>

  <!-- AOS CSS -->
  <link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css" />

  <!-- FontAwesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <style>
    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: #F8FAFC;
      color: #0F172A;
      overflow-x: hidden;
    }

    h1, h2, h3, .font-heading {
      font-family: 'Outfit', sans-serif;
    }

    .bg-mesh {
      background-image:
        radial-gradient(at 10% 20%, rgba(212, 175, 55, 0.08) 0px, transparent 50%),
        radial-gradient(at 90% 10%, rgba(230, 57, 70, 0.08) 0px, transparent 50%),
        radial-gradient(at 50% 80%, rgba(15, 23, 42, 0.05) 0px, transparent 50%),
        radial-gradient(circle at 50% 50%, rgba(248, 250, 252, 0.85) 0%, #F8FAFC 100%);
    }

    .grid-pattern {
      background-size: 40px 40px;
      background-image:
        linear-gradient(to right, rgba(15, 23, 42, 0.03) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(15, 23, 42, 0.03) 1px, transparent 1px);
    }

    .glass-card {
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(226, 232, 240, 0.9);
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .glass-card:hover {
      border-color: #D4AF37;
      transform: translateY(-6px);
      box-shadow: 0 22px 45px -10px rgba(212, 175, 55, 0.22), 0 0 20px rgba(212, 175, 55, 0.15);
    }

    .glass-nav {
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid rgba(226, 232, 240, 0.85);
    }

    /* NAV LINK ANIMATION */
    .nav-link-anim {
      position: relative;
      padding-bottom: 4px;
      transition: color 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .nav-link-anim::after {
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
    }

    .nav-link-anim:hover::after, .nav-link-anim.active::after {
      transform: scaleX(1);
    }

    .nav-link-anim:hover {
      color: #E63946;
    }

    /* BUTTON LIQUID FILL ANIMATION */
    .btn-fill-red {
      position: relative;
      overflow: hidden;
      z-index: 1;
      transition: color 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease, box-shadow 0.4s ease;
    }

    .btn-fill-red::before {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(135deg, #C52233 0%, #900C1C 100%);
      z-index: -1;
      transform: translateY(100%);
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      border-radius: inherit;
    }

    .btn-fill-red:hover::before, .btn-fill-red:active::before {
      transform: translateY(0%);
    }

    .btn-fill-gold {
      position: relative;
      overflow: hidden;
      z-index: 1;
      transition: color 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease, box-shadow 0.4s ease;
    }

    .btn-fill-gold::before {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(135deg, #D4AF37 0%, #B38F24 100%);
      z-index: -1;
      transform: translateY(100%);
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      border-radius: inherit;
    }

    .btn-fill-gold:hover::before, .btn-fill-gold:active::before {
      transform: translateY(0%);
    }

    /* ============================================================
       TRUE 3D FLY-TOWARDS-VIEWER LOGO ANIMATION OVERLAY ("Das kommt zu mir!")
       ============================================================ */
    #logo-bg-overlay {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 2;
      overflow: hidden;
      perspective: 1000px;
      transform-style: preserve-3d;
    }

    .global-logo-particle {
      position: absolute;
      width: 52px;
      height: 52px;
      background-image: url('img/logo/F3-3.avif');
      background-size: contain;
      background-repeat: no-repeat;
      background-position: center;
      transform-origin: center center;
      will-change: transform, opacity;
      backface-visibility: hidden;
      filter: drop-shadow(0 6px 14px rgba(0,0,0,0.15));
    }

    @keyframes float-slow {
      0%, 100% { transform: translateY(0px) rotate(0deg); }
      50% { transform: translateY(-14px) rotate(2deg); }
    }
    .animate-float { animation: float-slow 7s ease-in-out infinite; }

    details summary::-webkit-details-marker { display: none; }
    details[open] summary .faq-icon { transform: rotate(180deg); }
  </style>
</head>'''
    return html.replace("__TITLE__", title).replace("__DESC__", desc)

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
        active_cls = "nav-link-anim text-[#E63946] font-black active" if is_active else "nav-link-anim text-slate-700 hover:text-[#E63946]"
        nav_links_html += f'<a href="{link}" class="{active_cls}">{label}</a>\n'

    return f'''<!-- HEADER -->
  <header id="main-header" class="fixed top-0 left-0 w-full z-50 glass-nav transition-all duration-300 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      <!-- Brand Logo -->
      <a href="index.html" class="flex items-center gap-3 group">
        <img src="img/logo/F3-3.avif" alt="SoccerProf Academy Logo"
          class="h-12 sm:h-14 w-auto object-contain group-hover:scale-105 transition-transform drop-shadow-sm">
      </a>

      <!-- Desktop Navigation Links -->
      <nav class="hidden lg:flex items-center gap-7 text-sm font-bold">
        {nav_links_html}
      </nav>

      <!-- Right Action Group: Shop & Primary CTA -->
      <div class="hidden sm:flex items-center gap-4">
        <a href="shop.html"
          class="btn-fill-gold flex items-center gap-2 px-4 py-2 rounded-full bg-slate-100 text-slate-800 font-bold text-xs border border-slate-200 hover:text-slate-950">
          <i class="fa-solid fa-bag-shopping text-[#D4AF37]"></i>
          <span>Shop</span>
        </a>
        <a href="kontakt.html"
          class="btn-fill-red px-5 py-2.5 rounded-full bg-[#E63946] text-white font-black text-xs uppercase tracking-wider shadow-red-glow hover:shadow-xl transform hover:-translate-y-0.5 flex items-center gap-2">
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
    return '''<!-- FOOTER -->
  <footer class="bg-black text-slate-400 py-16 border-t border-slate-800 relative z-10">
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
    return '''<!-- DYNAMIC LOGO OVERLAY CONTAINER -->
  <div id="logo-bg-overlay"></div>

  <!-- SCRIPTS -->
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
      // SPECTACULAR 3D FLY-TOWARDS-VIEWER LOGO ANIMATION ENGINE ("Das kommt zu mir!")
      // ============================================================
      const overlay = document.getElementById('logo-bg-overlay');
      if (overlay) {
        const isMobile = window.innerWidth < 768;
        const particleCount = isMobile ? 35 : 75;
        const particlesData = [];

        for (let i = 0; i < particleCount; i++) {
          const el = document.createElement('div');
          el.className = 'global-logo-particle';

          // Random initial positions distributed across viewport
          const posX = Math.random() * 92 + 4; // %
          const posY = Math.random() * 92 + 4; // %
          
          // Z Depth start (-700px to +300px)
          const baseZ = -700 + Math.random() * 1000;
          const zSpeed = 0.7 + Math.random() * 1.5; // Z fly speed on scroll
          
          // Independent float drift vectors ("jeder bewegt sich dahin, wo er möchte")
          const driftX = (Math.random() - 0.5) * 70;
          const driftY = (Math.random() - 0.5) * 70;
          const driftFreq = 0.001 + Math.random() * 0.002;
          const phase = Math.random() * Math.PI * 2;
          
          const maxOpacity = 0.18 + Math.random() * 0.22; // High contrast & clear visibility
          const rotSpeed = (Math.random() - 0.5) * 0.15;
          let currRot = (Math.random() - 0.5) * 30;

          el.style.left = posX + '%';
          el.style.top = posY + '%';
          
          overlay.appendChild(el);

          particlesData.push({
            el,
            posX,
            posY,
            baseZ,
            zSpeed,
            driftX,
            driftY,
            driftFreq,
            phase,
            maxOpacity,
            rotSpeed,
            currRot
          });
        }

        let startTime = performance.now();

        function update3DLogoFlythrough(now) {
          const scrolled = window.scrollY;
          const elapsed = now - startTime;

          particlesData.forEach((pd) => {
            pd.currRot += pd.rotSpeed;
            
            // Calculate continuous Z depth flying TOWARDS camera ("Das kommt zu mir!")
            // Loop Z depth smoothly from -700px to +450px (total range 1150px)
            const rawZ = (pd.baseZ + scrolled * pd.zSpeed) % 1150;
            const currentZ = rawZ > 450 ? rawZ - 1150 : rawZ;

            // Independent continuous floating oscillation ("Jeder bewegt sich dahin, wo er möchte")
            const floatX = Math.sin(elapsed * pd.driftFreq + pd.phase) * pd.driftX;
            const floatY = Math.cos(elapsed * pd.driftFreq * 0.8 + pd.phase) * pd.driftY;
            const scrollYOffset = scrolled * 0.08;

            // Smooth opacity fade in from distance (-700px) and fade out as it flies past screen (+400px)
            let normOpacity = 1.0;
            if (currentZ < -400) {
              normOpacity = (currentZ + 700) / 300;
            } else if (currentZ > 250) {
              normOpacity = (450 - currentZ) / 200;
            }
            const finalOpacity = Math.max(0, Math.min(pd.maxOpacity, normOpacity * pd.maxOpacity));

            pd.el.style.transform = `translate3d(${floatX.toFixed(1)}px, ${(floatY + scrollYOffset).toFixed(1)}px, ${currentZ.toFixed(1)}px) rotate(${pd.currRot.toFixed(1)}deg)`;
            pd.el.style.opacity = finalOpacity.toFixed(3);
          });

          requestAnimationFrame(update3DLogoFlythrough);
        }

        requestAnimationFrame(update3DLogoFlythrough);
      }
    });

    function handleFormSubmit(e) {
      e.preventDefault();
      window.location.href = "https://wa.me/4917684156542?text=" + encodeURIComponent("Hallo Sami, ich habe eine Anfrage gesendet!");
    }
  </script>
</body>
</html>'''

def generate_index_html():
    body_part = '''<body class="bg-mesh relative grid-pattern antialiased text-slate-900 pb-20 sm:pb-0">

  <!-- Ambient Glow Orbs -->
  <div class="fixed top-20 left-10 w-96 h-96 bg-[#D4AF37]/10 rounded-full blur-3xl pointer-events-none -z-10 animate-float"></div>
  <div class="fixed top-1/2 right-10 w-[30rem] h-[30rem] bg-[#E63946]/10 rounded-full blur-3xl pointer-events-none -z-10 animate-pulse-glow"></div>

  ''' + get_header(active_page="Home") + '''

  <!-- ============================================================
       1. HERO SECTION (Links-bündig, Schriftfarben original & knackig)
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

        <!-- Hauptüberschrift -->
        <h1 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight leading-[1.15]">
          PRIVATER FUßBALL-TRAINER <br>
          <span class="text-[#D4AF37]">FÜR INDIVIDUELLES TRAINING</span> <br>
          <span class="relative inline-block text-[#E63946]">
            FÜR ANFÄNGER &amp; PROS.
            <svg class="absolute -bottom-2 left-0 w-full h-3 text-[#D4AF37]" viewBox="0 0 200 9" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M2 7C50 2 150 2 198 7" stroke="currentColor" stroke-width="4" stroke-linecap="round" />
            </svg>
          </span>
        </h1>

        <!-- Subline -->
        <p class="text-base sm:text-lg text-slate-700 font-medium leading-relaxed max-w-2xl">
          Individuelles Fußballtraining für Kinder, Jugendliche und ambitionierte Spieler in Hamburg – abgestimmt auf die Stärken, Ziele und Entwicklung jedes Spielers.
          <span class="block mt-2 font-bold text-slate-900">
            Einzeltraining und Kleingruppentraining als professionelle Ergänzung zum Vereinstraining.
          </span>
        </p>

        <!-- CTAs mit Liquid-Fill Animation -->
        <div class="flex flex-col sm:flex-row items-center justify-start gap-4 pt-2">
          <a href="kontakt.html"
            class="btn-fill-red w-full sm:w-auto px-8 py-4 rounded-full bg-[#E63946] text-white font-black text-sm uppercase tracking-wider shadow-red-glow hover:shadow-2xl flex items-center justify-center gap-3 group">
            <span>JETZT PROBETRAINING ANFRAGEN</span>
            <i class="fa-solid fa-arrow-right group-hover:translate-x-1 transition-transform"></i>
          </a>
          <a href="preise.html"
            class="btn-fill-gold w-full sm:w-auto px-8 py-4 rounded-full bg-white/95 text-slate-900 border-2 border-slate-900 font-bold text-sm shadow-sm flex items-center justify-center gap-2">
            <span>TRAININGSPAKETE ENTDECKEN</span>
            <i class="fa-solid fa-tags text-xs text-[#D4AF37]"></i>
          </a>
        </div>

        <!-- Trust Signals / Fakten-Strip -->
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

  <!-- ============================================================
       2. ÜBER MICH SEKTION (Sami Ghaouar) - DIREKT NACH DEM HERO!
       Foto: img/sami/sami.jpg
       Background: TIEFSCHWARZ (#090D16 / bg-black)
       ============================================================ -->
  <section id="ueber-mich" class="py-24 bg-[#090D16] text-white relative z-10 border-t border-b border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <!-- Foto von Sami (Exakt img/sami/sami.jpg!) -->
        <div class="lg:col-span-5 relative" data-aos="fade-right">
          <div class="relative rounded-3xl overflow-hidden shadow-2xl border-2 border-[#D4AF37]/40 group">
            <img src="img/sami/sami.jpg" alt="Head Coach Sami Ghaouar" class="w-full h-[480px] object-cover group-hover:scale-105 transition-transform duration-700">
            <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent"></div>
            <div class="absolute bottom-6 left-6 right-6 p-4 rounded-2xl bg-black/85 backdrop-blur-md border border-slate-800">
              <div class="text-xl font-black text-white">Sami Ghaouar</div>
              <div class="text-xs font-bold text-[#D4AF37]">UEFA-B Lizenz-Trainer &amp; Gründer SoccerProf Academy</div>
            </div>
          </div>
        </div>

        <!-- Content Über Mich -->
        <div class="lg:col-span-7 space-y-6" data-aos="fade-left">
          <div class="inline-block px-3.5 py-1 rounded-full bg-[#D4AF37]/20 text-[#D4AF37] font-black text-xs uppercase tracking-widest border border-[#D4AF37]/30">
            Über Mich &amp; Meine Philosophie
          </div>
          <h2 class="text-3xl sm:text-5xl font-black tracking-tight leading-tight">
            DEINE FUßBALLERISCHE ENTWICKLUNG STEHT AN ERSTER STELLE.
          </h2>
          <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
            Moin! Ich bin Sami Ghaouar, lizensierter UEFA-B Trainer und Gründer der SoccerProf Academy in Hamburg. Nach vielen Jahren Erfahrung im Jugend- und Seniorenbereich habe ich ein Trainingssystem entwickelt, das individuelle Stärken perfektioniert und Schwächen gezielt eliminiert.
          </p>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
            <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800">
              <div class="text-[#D4AF37] font-black text-sm mb-1"><i class="fa-solid fa-graduation-cap mr-2"></i>UEFA-B Lizenz</div>
              <div class="text-xs text-slate-400">Offiziell DFB-zertifizierte Methodik für beste Resultate.</div>
            </div>
            <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800">
              <div class="text-[#E63946] font-black text-sm mb-1"><i class="fa-solid fa-video mr-2"></i>Video-Feedback</div>
              <div class="text-xs text-slate-400">Detaillierte Analyse für direkte Bewegungs-Korrektur.</div>
            </div>
          </div>
          <div class="pt-4">
            <a href="ueber-uns.html" class="btn-fill-gold inline-flex items-center gap-2 px-8 py-4 rounded-full bg-[#D4AF37] text-slate-950 font-black text-xs uppercase tracking-wider shadow-gold-glow">
              <span>MEHR ÜBER SAMI &amp; DAS CONCEPT ERFAHREN</span>
              <i class="fa-solid fa-chevron-right text-xs"></i>
            </a>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ============================================================
       3. DIE 8 SÄULEN DES SOCCERPROF TRAININGS (Methodik)
       ============================================================ -->
  <section id="methoden" class="py-20 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
      <div class="text-center max-w-3xl mx-auto space-y-4" data-aos="fade-up">
        <div class="inline-block px-3.5 py-1 rounded-full bg-[#D4AF37]/10 text-[#D4AF37] font-black text-xs uppercase tracking-widest border border-[#D4AF37]/20">
          Systematisches Coaching
        </div>
        <h2 class="text-3xl sm:text-4xl font-black text-slate-900 tracking-tight">
          DIE 8 SÄULEN DES SOCCERPROF TRAININGS
        </h2>
        <p class="text-slate-600 text-sm sm:text-base font-medium">
          Ein ganzheitliches Trainingssystem für maximale Weiterentwicklung auf dem Platz.
        </p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <div class="glass-card p-6 rounded-2xl space-y-3" data-aos="fade-up" data-aos-delay="100">
          <div class="w-12 h-12 rounded-xl bg-[#E63946]/10 text-[#E63946] flex items-center justify-center text-xl font-black">1</div>
          <h3 class="text-lg font-black text-slate-900">Technik &amp; Ballführung</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Präzise Ballannahme, Ballbeherrschung auf engstem Raum &amp; beidfüßiger Feinschliff.</p>
        </div>
        <div class="glass-card p-6 rounded-2xl space-y-3" data-aos="fade-up" data-aos-delay="150">
          <div class="w-12 h-12 rounded-xl bg-[#D4AF37]/10 text-[#D4AF37] flex items-center justify-center text-xl font-black">2</div>
          <h3 class="text-lg font-black text-slate-900">Kognition &amp; Übersicht</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Schnelle Vororientierung, Schulterblick &amp; Handlungsschnelligkeit unter Zeitdruck.</p>
        </div>
        <div class="glass-card p-6 rounded-2xl space-y-3" data-aos="fade-up" data-aos-delay="200">
          <div class="w-12 h-12 rounded-xl bg-slate-900 text-white flex items-center justify-center text-xl font-black">3</div>
          <h3 class="text-lg font-black text-slate-900">Koordination &amp; Agilität</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Optimale Laufschule, Richtungswechsel &amp; Beweglichkeit für maximale Dynamik.</p>
        </div>
        <div class="glass-card p-6 rounded-2xl space-y-3" data-aos="fade-up" data-aos-delay="250">
          <div class="w-12 h-12 rounded-xl bg-[#E63946]/10 text-[#E63946] flex items-center justify-center text-xl font-black">4</div>
          <h3 class="text-lg font-black text-slate-900">Fußball-Athletik</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Spezifischer Kraftaufbau, Antrittsschnelligkeit &amp; verletzungsvorbeugendes Training.</p>
        </div>

        <div class="glass-card p-6 rounded-2xl space-y-3" data-aos="fade-up" data-aos-delay="300">
          <div class="w-12 h-12 rounded-xl bg-[#D4AF37]/10 text-[#D4AF37] flex items-center justify-center text-xl font-black">5</div>
          <h3 class="text-lg font-black text-slate-900">Taktik &amp; Position</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Positionsbezogenes Verhalten, Raumverständnis &amp; kluges Zweikampfverhalten.</p>
        </div>
        <div class="glass-card p-6 rounded-2xl space-y-3" data-aos="fade-up" data-aos-delay="350">
          <div class="w-12 h-12 rounded-xl bg-slate-900 text-white flex items-center justify-center text-xl font-black">6</div>
          <h3 class="text-lg font-black text-slate-900">Mentale Stärke</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Selbstvertrauen, Fokus bei Drucksituationen &amp; Sieger-Mentalität auf dem Platz.</p>
        </div>
        <div class="glass-card p-6 rounded-2xl space-y-3" data-aos="fade-up" data-aos-delay="400">
          <div class="w-12 h-12 rounded-xl bg-[#E63946]/10 text-[#E63946] flex items-center justify-center text-xl font-black">7</div>
          <h3 class="text-lg font-black text-slate-900">Spielformen &amp; 1v1</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Hohe Intensität in Durchsetzungs- &amp; Finte-Situationen für echten Spielvorteil.</p>
        </div>
        <div class="glass-card p-6 rounded-2xl space-y-3" data-aos="fade-up" data-aos-delay="450">
          <div class="w-12 h-12 rounded-xl bg-[#D4AF37]/10 text-[#D4AF37] flex items-center justify-center text-xl font-black">8</div>
          <h3 class="text-lg font-black text-slate-900">Video-Analyse</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Visuelles Feedback zur Korrektur von Bewegungsabläufen &amp; Detail-Fehlern.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================
       4. STANDORTE IN HAMBURG (Billstedt, Reinbek, Eimsbüttel)
       ============================================================ -->
  <section id="standorte" class="py-20 bg-black text-white relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-10">
      <div class="text-center max-w-2xl mx-auto space-y-3" data-aos="fade-up">
        <div class="inline-block px-3.5 py-1 rounded-full bg-[#E63946]/20 text-[#E63946] font-black text-xs uppercase tracking-widest border border-[#E63946]/30">
          Dein Platz in Hamburg
        </div>
        <h2 class="text-3xl sm:text-4xl font-black tracking-tight">TRAININGSSTANDORTE IN HAMBURG</h2>
        <p class="text-slate-400 text-sm">Flexible &amp; moderne Trainingsstätten in deiner Nähe.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="p-6 rounded-2xl bg-slate-900 border border-slate-800 space-y-3" data-aos="fade-up" data-aos-delay="100">
          <div class="text-[#D4AF37] font-black text-sm uppercase tracking-wider flex items-center gap-2">
            <i class="fa-solid fa-location-dot"></i> Hamburg-Billstedt
          </div>
          <h3 class="text-xl font-black text-white">Haupt-Trainingszentrum</h3>
          <p class="text-xs text-slate-400">Moderne Kunstrasen- &amp; Rasenplätze für Ganzjahrestraining.</p>
        </div>
        <div class="p-6 rounded-2xl bg-slate-900 border border-slate-800 space-y-3" data-aos="fade-up" data-aos-delay="200">
          <div class="text-[#D4AF37] font-black text-sm uppercase tracking-wider flex items-center gap-2">
            <i class="fa-solid fa-location-dot"></i> Hamburg-Reinbek
          </div>
          <h3 class="text-xl font-black text-white">Sportanlage Ost</h3>
          <p class="text-xs text-slate-400">Optimale Anbindung für Spieler aus dem Osten Hamburgs.</p>
        </div>
        <div class="p-6 rounded-2xl bg-slate-900 border border-slate-800 space-y-3" data-aos="fade-up" data-aos-delay="300">
          <div class="text-[#D4AF37] font-black text-sm uppercase tracking-wider flex items-center gap-2">
            <i class="fa-solid fa-location-dot"></i> Hamburg-Eimsbüttel
          </div>
          <h3 class="text-xl font-black text-white">Standort West</h3>
          <p class="text-xs text-slate-400">Zentrale Anlage für Athleten aus Eimsbüttel &amp; Umgebung.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================
       5. TRAININGSPAKETE & TARIFE (Pakete-Sektion)
       ============================================================ -->
  <section id="pakete" class="py-24 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-12">
      
      <div class="max-w-3xl mx-auto space-y-4" data-aos="fade-up">
        <div class="inline-block px-3.5 py-1 rounded-full bg-[#E63946]/10 text-[#E63946] font-black text-xs uppercase tracking-widest border border-[#E63946]/20">
          Transparente Tarife
        </div>
        <h2 class="text-3xl sm:text-5xl font-black text-slate-900 tracking-tight">
          WÄHLE DEIN TRAININGSPAKET
        </h2>
        <p class="text-slate-600 font-medium text-sm sm:text-base">
          Ob 1:1 Einzeltraining für maximale Intensität oder Kleingruppentraining – finde die perfekte Option für deine Ziele.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-left">
        
        <!-- Paket 1: Einzeltraining -->
        <div class="glass-card p-8 rounded-3xl space-y-6 relative flex flex-col justify-between" data-aos="fade-up" data-aos-delay="100">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="text-xs font-black uppercase tracking-wider text-slate-500">Intensiv</span>
              <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-800 text-[10px] font-bold">1:1 Coaching</span>
            </div>
            <h3 class="text-2xl font-black text-slate-900">Einzeltraining</h3>
            <p class="text-xs text-slate-600 leading-relaxed">
              100% individuelle Betreuung. Perfekt zur gezielten Technikverbesserung, Erstkorrektur &amp; Positionsschulung.
            </p>
            <div class="text-3xl font-black text-slate-900 pt-2">
              Auf Anfrage
            </div>
            <ul class="space-y-2.5 text-xs font-semibold text-slate-700 border-t border-slate-200/80 pt-4">
              <li class="flex items-center gap-2"><i class="fa-solid fa-circle-check text-[#D4AF37]"></i> Exklusiver 1:1 Fokus</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-circle-check text-[#D4AF37]"></i> Individueller Entwicklungsplan</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-circle-check text-[#D4AF37]"></i> Flexible Termine &amp; Plätze</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-circle-check text-[#D4AF37]"></i> Video-Feedback Einheiten</li>
            </ul>
          </div>
          <div class="pt-6">
            <a href="kontakt.html" class="btn-fill-red block w-full text-center py-3.5 rounded-full bg-slate-900 text-white font-black text-xs uppercase tracking-wider hover:bg-[#E63946] transition-colors">
              Paket Anfragen
            </a>
          </div>
        </div>

        <!-- Paket 2: Kleingruppe (Bestseller) -->
        <div class="glass-card p-8 rounded-3xl space-y-6 relative border-2 border-[#D4AF37] shadow-xl flex flex-col justify-between scale-105" data-aos="fade-up" data-aos-delay="200">
          <div class="absolute -top-3.5 left-1/2 -translate-x-1/2 px-4 py-1 rounded-full bg-[#D4AF37] text-slate-950 font-black text-[10px] uppercase tracking-widest shadow-md">
            Beliebteste Wahl
          </div>
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="text-xs font-black uppercase tracking-wider text-[#D4AF37]">Team &amp; Performance</span>
              <span class="px-3 py-1 rounded-full bg-[#D4AF37]/20 text-[#D4AF37] text-[10px] font-bold">Max 5 Spieler</span>
            </div>
            <h3 class="text-2xl font-black text-slate-900">Kleingruppe</h3>
            <p class="text-xs text-slate-600 leading-relaxed">
              Hohe Intensität gepaart mit spielnahen Zweikämpfen, Zeitdruck &amp; hoher Wiederholungszahl.
            </p>
            <div class="text-3xl font-black text-slate-900 pt-2">
              Auf Anfrage
            </div>
            <ul class="space-y-2.5 text-xs font-semibold text-slate-700 border-t border-slate-200/80 pt-4">
              <li class="flex items-center gap-2"><i class="fa-solid fa-circle-check text-[#D4AF37]"></i> Feste 5er Leistungsgruppen</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-circle-check text-[#D4AF37]"></i> Hohe Dynamik &amp; Motivation</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-circle-check text-[#D4AF37]"></i> Spielnahe Situationen</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-circle-check text-[#D4AF37]"></i> Regelmäßige Einheiten</li>
            </ul>
          </div>
          <div class="pt-6">
            <a href="kontakt.html" class="btn-fill-gold block w-full text-center py-3.5 rounded-full bg-[#D4AF37] text-slate-950 font-black text-xs uppercase tracking-wider shadow-gold-glow">
              Jetzt Anfragen
            </a>
          </div>
        </div>

        <!-- Paket 3: Mannschaftstraining -->
        <div class="glass-card p-8 rounded-3xl space-y-6 relative flex flex-col justify-between" data-aos="fade-up" data-aos-delay="300">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="text-xs font-black uppercase tracking-wider text-slate-500">Verein</span>
              <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-800 text-[10px] font-bold">Vor Ort</span>
            </div>
            <h3 class="text-2xl font-black text-slate-900">Mannschaft</h3>
            <p class="text-xs text-slate-600 leading-relaxed">
              Spezifische Zusatztrainings für dein gesamtes Vereinsteam direkt auf eurem Platz in Hamburg.
            </p>
            <div class="text-3xl font-black text-slate-900 pt-2">
              Individuell
            </div>
            <ul class="space-y-2.5 text-xs font-semibold text-slate-700 border-t border-slate-200/80 pt-4">
              <li class="flex items-center gap-2"><i class="fa-solid fa-circle-check text-[#D4AF37]"></i> Taktik &amp; Gruppendynamik</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-circle-check text-[#D4AF37]"></i> Gast-Coaching Einheiten</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-circle-check text-[#D4AF37]"></i> Saison-Vorbereitung</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-circle-check text-[#D4AF37]"></i> Auf den Verein abgestimmt</li>
            </ul>
          </div>
          <div class="pt-6">
            <a href="kontakt.html" class="btn-fill-red block w-full text-center py-3.5 rounded-full bg-slate-900 text-white font-black text-xs uppercase tracking-wider hover:bg-[#E63946] transition-colors">
              Verein Anfragen
            </a>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ============================================================
       6. FAQ SEKTION (Accordion)
       ============================================================ -->
  <section id="faq" class="py-20 relative z-10 bg-slate-100/80">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8" data-aos="fade-up">
      <div class="text-center space-y-3">
        <div class="inline-block px-3 py-1 rounded-full bg-slate-200 text-slate-800 font-bold text-xs uppercase tracking-widest">
          Transparenz &amp; Antworten
        </div>
        <h2 class="text-3xl font-black text-slate-900 tracking-tight">HÄUFIG GESTELLTE FRAGEN (FAQ)</h2>
      </div>

      <div class="space-y-4">
        <details class="glass-card p-5 rounded-2xl group cursor-pointer">
          <summary class="flex items-center justify-between font-bold text-slate-900 text-sm">
            <span>Für welche Altersgruppen ist das Training geeignet?</span>
            <i class="fa-solid fa-chevron-down text-xs text-[#D4AF37] faq-icon transition-transform"></i>
          </summary>
          <p class="mt-3 text-xs text-slate-600 leading-relaxed">
            Wir trainieren Kinder (ab ca. 6 Jahren), Jugendliche sowie ambitionierte Herren- und Damen-Spieler. Das Training wird exakt an das Alter und Leistungsniveau angepasst.
          </p>
        </details>

        <details class="glass-card p-5 rounded-2xl group cursor-pointer">
          <summary class="flex items-center justify-between font-bold text-slate-900 text-sm">
            <span>Ist das Training eine Ergänzung zum Vereinstraining?</span>
            <i class="fa-solid fa-chevron-down text-xs text-[#D4AF37] faq-icon transition-transform"></i>
          </summary>
          <p class="mt-3 text-xs text-slate-600 leading-relaxed">
            Ja, absolut! Das SoccerProf Training ersetzt das Vereinstraining nicht, sondern ergänzt es gezielt in den Bereichen, die im Mannschaftstraining zu kurz kommen.
          </p>
        </details>

        <details class="glass-card p-5 rounded-2xl group cursor-pointer">
          <summary class="flex items-center justify-between font-bold text-slate-900 text-sm">
            <span>Wo finden die Trainingseinheiten statt?</span>
            <i class="fa-solid fa-chevron-down text-xs text-[#D4AF37] faq-icon transition-transform"></i>
          </summary>
          <p class="mt-3 text-xs text-slate-600 leading-relaxed">
            Unsere Haupt-Standorte befinden sich in Hamburg-Billstedt, Hamburg-Reinbek und Hamburg-Eimsbüttel. Zudem bieten wir Mannschaftstraining direkt auf eurem Vereinsgelände an.
          </p>
        </details>
      </div>
    </div>
  </section>

  <!-- ============================================================
       7. KONTAKT & PROBETRAINING CTA
       ============================================================ -->
  <section id="kontakt" class="py-20 bg-black text-white relative z-10">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-8" data-aos="zoom-in">
      <div class="inline-block px-4 py-1.5 rounded-full bg-[#D4AF37]/20 text-[#D4AF37] font-black text-xs uppercase tracking-widest border border-[#D4AF37]/30">
        Jetzt starten
      </div>
      <h2 class="text-3xl sm:text-5xl font-black tracking-tight">
        BEREIT FÜR DEIN NÄCHSTES LEVEL IN HAMBURG?
      </h2>
      <p class="text-slate-300 font-medium text-base sm:text-lg max-w-2xl mx-auto">
        Vereinbare noch heute dein kostenloses Erstgespräch mit Head Coach Sami Ghaouar.
      </p>
      <div class="flex flex-col sm:flex-row items-center justify-center gap-4 pt-4">
        <a href="kontakt.html" class="btn-fill-red px-8 py-4 rounded-full bg-[#E63946] text-white font-black text-sm uppercase tracking-wider shadow-red-glow">
          Kostenloses Erstgespräch Buchen
        </a>
        <a href="https://wa.me/4917684156542" target="_blank" class="btn-fill-gold px-8 py-4 rounded-full bg-slate-900 text-white border border-slate-700 font-bold text-sm flex items-center gap-2">
          <i class="fa-brands fa-whatsapp text-emerald-400 text-lg"></i>
          <span>WhatsApp Chat</span>
        </a>
      </div>
    </div>
  </section>

  ''' + get_footer() + '''
  ''' + get_scripts()

    index_content = get_head() + "\n" + body_part

    with open(os.path.join(workspace_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_content)

    print("Generated index.html successfully!")

if __name__ == "__main__":
    generate_index_html()