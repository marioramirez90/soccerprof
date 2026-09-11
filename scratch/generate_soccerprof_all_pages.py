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

    .logo-particle-bg {{
      position: absolute;
      inset: 0;
      pointer-events: none;
      overflow: hidden;
      z-index: 1;
    }}

    .logo-particle {{
      position: absolute;
      width: 22px;
      height: 22px;
      opacity: 0.05;
      background-image: url('img/logo/F3-3.avif');
      background-size: contain;
      background-repeat: no-repeat;
      transition: transform 0.8s ease-out, opacity 0.8s ease;
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
        active_cls = "text-[#E63946] font-black" if is_active else "hover:text-[#E63946] transition-colors"
        nav_links_html += f'<a href="{link}" class="{active_cls}">{label}</a>\n'

    return f'''<!-- HEADER -->
  <header id="main-header" class="fixed top-0 left-0 w-full z-50 glass-nav transition-all duration-300 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      <!-- Brand Logo -->
      <a href="index.html" class="flex items-center gap-3 group">
        <img src="img/logo/F3-3.avif" alt="SoccerProf Academy Logo"
          class="h-12 sm:h-14 w-auto object-contain group-hover:scale-105 transition-transform drop-shadow-sm">
      </a>

      <!-- Desktop Navigation Links (Punkt 4: Minimalistischer Header) -->
      <nav class="hidden lg:flex items-center gap-7 text-sm font-bold text-slate-700">
        {nav_links_html}
      </nav>

      <!-- Right Action Group: Shop & Primary CTA -->
      <div class="hidden sm:flex items-center gap-4">
        <a href="shop.html"
          class="flex items-center gap-2 px-4 py-2 rounded-full bg-slate-100 hover:bg-[#D4AF37] hover:text-slate-900 text-slate-800 font-bold text-xs transition-all duration-300 border border-slate-200">
          <i class="fa-solid fa-bag-shopping text-[#D4AF37]"></i>
          <span>Shop</span>
        </a>
        <a href="kontakt.html"
          class="px-5 py-2.5 rounded-full bg-[#E63946] hover:bg-[#C52233] text-white font-black text-xs uppercase tracking-wider shadow-red-glow hover:shadow-xl transition-all duration-300 transform hover:-translate-y-0.5 flex items-center gap-2">
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
        class="block w-full text-center py-3.5 rounded-full bg-[#E63946] text-white font-black uppercase text-xs tracking-wider shadow-red-glow mobile-link">
        <i class="fa-solid fa-calendar-check mr-2"></i>Kostenloses Erstgespräch
      </a>
    </div>
  </header>'''

def get_footer():
    return '''<!-- FOOTER (Punkt 5: Zweite Navigationsebene) -->
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
    <a href="kontakt.html" class="px-4 py-2 rounded-full bg-[#E63946] text-white font-black text-xs uppercase tracking-wider shadow-red-glow flex items-center gap-1.5">
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

      // Dynamic Logo Background Particle Overlay (Punkt 9 & 10)
      const logoContainers = document.querySelectorAll('.logo-particle-bg');
      logoContainers.forEach(container => {
        const count = window.innerWidth < 768 ? 15 : 45;
        for (let i = 0; i < count; i++) {
          const particle = document.createElement('div');
          particle.className = 'logo-particle';
          particle.style.top = Math.random() * 100 + '%';
          particle.style.left = Math.random() * 100 + '%';
          const size = 16 + Math.random() * 20;
          particle.style.width = size + 'px';
          particle.style.height = size + 'px';
          particle.style.transform = `rotate(${Math.random() * 360}deg)`;
          container.appendChild(particle);
        }
      });

      // Parallax scroll effects for background logos & floating images
      window.addEventListener('scroll', () => {
        const scrolled = window.scrollY;
        const particles = document.querySelectorAll('.logo-particle');
        particles.forEach((p, idx) => {
          const speed = (idx % 4 + 1) * 0.02;
          p.style.transform = `translateY(${scrolled * speed}px) rotate(${scrolled * 0.04 + idx * 8}deg)`;
        });

        const floatingImgs = document.querySelectorAll('.floating-bg-image');
        floatingImgs.forEach((img, i) => {
          const speed = 0.04 + (i * 0.02);
          const rot = Math.sin(scrolled * 0.002 + i) * 3;
          const scale = 1 + Math.sin(scrolled * 0.001 + i) * 0.04;
          img.style.transform = `translateY(${scrolled * speed}px) rotate(${rot}deg) scale(${scale})`;
        });
      });
    });

    function handleFormSubmit(e) {
      e.preventDefault();
      window.location.href = "https://wa.me/4917684156542?text=" + encodeURIComponent("Hallo Sami, ich habe eine Anfrage gesendet!");
    }
  </script>
</body>
</html>'''

print("Core generator definitions loaded.")
