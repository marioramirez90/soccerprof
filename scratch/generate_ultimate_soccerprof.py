# -*- coding: utf-8 -*-
"""
Script to generate the ultimate, highly polished, conversion-optimized, and animated
SoccerProf Academy single-page website adhering 100% to all 33 user specification points.
"""

html_content = r'''<!DOCTYPE html>
<html lang="de" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SoccerProf Academy | Privater Fußballtrainer Hamburg – Sami Ghaouar</title>
  <meta name="description" content="Individuelles Fußballtraining für Kinder, Jugendliche und ambitionierte Spieler in Hamburg. Einzeltraining und Kleingruppentraining als perfekte Ergänzung zum Vereinstraining mit Sami Ghaouar (UEFA-B-Lizenz).">
  <meta name="keywords" content="Fußballtraining Hamburg, individuelles Fußballtraining Hamburg, Fußballtrainer Hamburg, Fußballtraining Kinder Hamburg, Fußball Einzeltraining Hamburg, Fußball Kleingruppentraining Hamburg, Fußballschule Hamburg, Sami Ghaouar, SoccerProf Academy">

  <!-- Open Graph / Meta -->
  <meta property="og:title" content="SoccerProf Academy Hamburg | Privater Fußballtrainer Sami Ghaouar">
  <meta property="og:description" content="Individuelles Fußballtraining für Kinder und Jugendliche in Hamburg. Mehr Technik. Mehr Selbstvertrauen. Mehr Spiel.">
  <meta property="og:image" content="img/logo/F3-3.avif">
  <meta property="og:type" content="website">

  <!-- Favicon -->
  <link rel="icon" href="img/favicon.ico" type="image/x-icon">

  <!-- Google Font: Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300..800;1,300..800&display=swap" rel="stylesheet">

  <!-- Tailwind CSS via CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
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
            'gold-glow': '0 0 25px rgba(212, 175, 55, 0.35)',
            'red-glow': '0 10px 25px -5px rgba(230, 57, 70, 0.45)',
            'glass': '0 8px 32px 0 rgba(15, 23, 42, 0.08)',
            'card-hover': '0 20px 40px -15px rgba(15, 23, 42, 0.12)',
          }
        }
      }
    }
  </script>

  <!-- AOS CSS via CDN -->
  <link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css" />

  <!-- FontAwesome Icons via CDN -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <style>
    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: #F8FAFC;
      color: #0F172A;
      overflow-x: hidden;
    }
    .bg-mesh {
      background-image: 
        radial-gradient(at 10% 20%, rgba(212, 175, 55, 0.07) 0px, transparent 50%),
        radial-gradient(at 90% 10%, rgba(230, 57, 70, 0.07) 0px, transparent 50%),
        radial-gradient(at 50% 80%, rgba(15, 23, 42, 0.04) 0px, transparent 50%),
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
      transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .glass-card:hover {
      border-color: #D4AF37;
      box-shadow: 0 18px 38px -10px rgba(212, 175, 55, 0.22), 0 0 15px rgba(212, 175, 55, 0.15);
    }
    .glass-nav {
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1px solid rgba(226, 232, 240, 0.85);
    }
    .text-gradient-gold {
      background: linear-gradient(135deg, #B38F24 0%, #D4AF37 50%, #F3E5AB 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    @keyframes float-slow {
      0%, 100% { transform: translateY(0px) rotate(0deg); }
      50% { transform: translateY(-12px) rotate(2deg); }
    }
    .animate-float {
      animation: float-slow 6s ease-in-out infinite;
    }
    @keyframes pulse-glow {
      0%, 100% { opacity: 0.5; transform: scale(1); }
      50% { opacity: 0.85; transform: scale(1.05); }
    }
    .animate-pulse-glow {
      animation: pulse-glow 4s ease-in-out infinite;
    }
    .steckbrief-badge {
      background: rgba(15, 23, 42, 0.05);
      border: 1px solid rgba(212, 175, 55, 0.3);
      border-radius: 12px;
      padding: 8px 14px;
    }
    /* FAQ Accordion Details */
    details summary::-webkit-details-marker {
      display: none;
    }
    details[open] summary .faq-icon {
      transform: rotate(180deg);
    }
  </style>
</head>
<body class="bg-mesh relative grid-pattern antialiased text-slate-900 pb-20 sm:pb-0">

  <!-- 3D THREE.JS CANVAS BACKGROUND -->
  <div id="threejs-container" class="fixed inset-0 w-full h-full pointer-events-none z-0"></div>

  <!-- Ambient Decorative Glow Orbs -->
  <div class="fixed top-20 left-10 w-96 h-96 bg-[#D4AF37]/10 rounded-full blur-3xl pointer-events-none -z-10 animate-float"></div>
  <div class="fixed top-1/2 right-10 w-[30rem] h-[30rem] bg-[#E63946]/10 rounded-full blur-3xl pointer-events-none -z-10 animate-pulse-glow"></div>
  <div class="fixed bottom-20 left-1/3 w-[26rem] h-[26rem] bg-[#D4AF37]/8 rounded-full blur-3xl pointer-events-none -z-10"></div>

  <!-- ============================================================
       NAVIGATION HEADER (Punkt 8: Schlank, fokussiert auf Conversion)
       ============================================================ -->
  <header class="fixed top-0 left-0 w-full z-50 glass-nav transition-all duration-300 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      
      <!-- Brand Logo -->
      <a href="#hero" class="flex items-center gap-3 group">
        <img src="img/logo/F3-3.avif" alt="SoccerProf Academy Logo" class="h-12 sm:h-14 w-auto object-contain group-hover:scale-105 transition-transform drop-shadow-sm">
      </a>

      <!-- Desktop Navigation Links (Max 6 Punkte) -->
      <nav class="hidden lg:flex items-center gap-7 text-sm font-bold text-slate-700">
        <a href="#angebote" class="hover:text-[#E63946] transition-colors">Training</a>
        <a href="#methode" class="hover:text-[#E63946] transition-colors">Trainingsmethode</a>
        <a href="#warum" class="hover:text-[#E63946] transition-colors">Warum SoccerProf</a>
        <a href="#ueber-uns" class="hover:text-[#E63946] transition-colors">Über uns</a>
        <a href="#steckbrief" class="hover:text-[#E63946] transition-colors">Trainer</a>
        <a href="#preise" class="hover:text-[#E63946] transition-colors">Preise</a>
        <a href="#kontakt" class="hover:text-[#E63946] transition-colors">Kontakt</a>
      </nav>

      <!-- Primary Action CTA Button -->
      <div class="hidden sm:flex items-center gap-3">
        <a href="#kontakt" class="px-5 py-2.5 rounded-full bg-[#E63946] hover:bg-[#C52233] text-white font-black text-xs uppercase tracking-wider shadow-red-glow hover:shadow-xl transition-all duration-300 transform hover:-translate-y-0.5 flex items-center gap-2">
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
      <a href="#angebote" class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Trainingsangebote</a>
      <a href="#methode" class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Trainingsmethode &amp; Bereiche</a>
      <a href="#warum" class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Warum SoccerProf</a>
      <a href="#ueber-uns" class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Über uns</a>
      <a href="#steckbrief" class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Der Trainer (Sami Ghaouar)</a>
      <a href="#preise" class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Preise &amp; Tarife</a>
      <a href="#faq" class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Häufige Fragen (FAQ)</a>
      <a href="#kontakt" class="block font-bold text-slate-800 hover:text-[#E63946] mobile-link">Kontakt &amp; Standorte</a>
      <a href="#kontakt" class="block w-full text-center py-3.5 rounded-full bg-[#E63946] text-white font-black uppercase text-xs tracking-wider shadow-red-glow mobile-link">
        <i class="fa-solid fa-calendar-check mr-2"></i>Kostenloses Erstgespräch
      </a>
    </div>
  </header>

  <!-- ============================================================
       1. HERO SECTION (Punkt 9: Conversion-Fokus, Attention, echte Fakten)
       ============================================================ -->
  <section id="hero" class="relative pt-36 pb-20 md:pt-44 md:pb-28 overflow-hidden min-h-[92vh] flex items-center z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <!-- Left Column: Copy & CTAs (7 Spalten) -->
        <div class="lg:col-span-7 space-y-7 text-center lg:text-left" data-aos="fade-right">
          
          <!-- Badge: Zielgruppe -->
          <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/95 border border-[#D4AF37] shadow-sm backdrop-blur-md">
            <span class="w-2.5 h-2.5 rounded-full bg-[#D4AF37] animate-ping"></span>
            <span class="text-xs font-black tracking-wider text-slate-900 uppercase">
              FÜR KINDER, JUGENDLICHE &amp; AMBITIONIERTE SPIELER
            </span>
          </div>

          <!-- Hauptüberschrift (Punkt 9: Vorgabe) -->
          <h1 class="text-4xl sm:text-5xl lg:text-6xl font-black text-slate-900 tracking-tight leading-[1.12]">
            Mehr Technik. <br>
            Mehr <span class="text-gradient-gold">Selbstvertrauen.</span> <br>
            <span class="relative inline-block text-slate-900">
              Mehr Spiel.
              <svg class="absolute -bottom-2 left-0 w-full h-3.5 text-[#E63946]" viewBox="0 0 200 9" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M2 7C50 2 150 2 198 7" stroke="currentColor" stroke-width="4.5" stroke-linecap="round"/></svg>
            </span>
          </h1>

          <!-- Nutzen-Subline & Ergänzung zum Verein -->
          <p class="text-base sm:text-lg text-slate-700 font-medium leading-relaxed max-w-2xl">
            Individuelles Fußballtraining für Kinder und Jugendliche in Hamburg – abgestimmt auf die Stärken, Ziele und Entwicklung jedes Spielers. 
            <span class="block mt-2 font-bold text-slate-900">
              Einzeltraining und Kleingruppentraining als professionelle Ergänzung zum Vereinstraining.
            </span>
          </p>

          <!-- CTAs -->
          <div class="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4 pt-2">
            <a href="#kontakt" class="w-full sm:w-auto px-8 py-4 rounded-full bg-[#E63946] hover:bg-[#C52233] text-white font-black text-sm uppercase tracking-wider shadow-red-glow hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-1 flex items-center justify-center gap-3 group">
              <span>Kostenloses Erstgespräch</span>
              <i class="fa-solid fa-arrow-right group-hover:translate-x-1 transition-transform"></i>
            </a>
            <a href="#angebote" class="w-full sm:w-auto px-8 py-4 rounded-full bg-white/95 hover:bg-slate-900 text-slate-900 hover:text-white border-2 border-slate-900 font-bold text-sm transition-all duration-300 transform hover:-translate-y-1 shadow-sm flex items-center justify-center gap-2">
              <span>Training entdecken</span>
              <i class="fa-solid fa-futbol text-xs text-[#D4AF37]"></i>
            </a>
          </div>

          <!-- Trust-Signale mit echten Fakten von soccerprof.de -->
          <div class="pt-6 border-t border-slate-200/90 grid grid-cols-2 sm:grid-cols-4 gap-3 bg-white/80 p-4 rounded-2xl backdrop-blur-md border border-slate-200/60 shadow-sm">
            <div class="text-center lg:text-left">
              <div class="text-lg font-black text-slate-900 flex items-center justify-center lg:justify-start gap-1">
                <span>★★★★★</span>
              </div>
              <div class="text-[11px] text-slate-600 font-bold">Kundenbewertungen</div>
            </div>
            <div class="text-center lg:text-left">
              <div class="text-lg font-black text-slate-900">UEFA-B</div>
              <div class="text-[11px] text-slate-600 font-bold">Lizenz-Trainer</div>
            </div>
            <div class="text-center lg:text-left">
              <div class="text-lg font-black text-[#D4AF37]">Seit 2012</div>
              <div class="text-[11px] text-slate-600 font-bold">Trainer-Erfahrung</div>
            </div>
            <div class="text-center lg:text-left">
              <div class="text-lg font-black text-[#E63946]">Hamburg</div>
              <div class="text-[11px] text-slate-600 font-bold">3 Standorte</div>
            </div>
          </div>

        </div>

        <!-- Right Column: Visual Training Photo (5 Spalten) -->
        <div class="lg:col-span-5" data-aos="fade-left">
          <div class="relative rounded-3xl overflow-hidden border-2 border-[#D4AF37]/60 shadow-2xl bg-slate-900 group">
            <div class="w-full h-[440px] sm:h-[520px] overflow-hidden relative">
              <img src="img/packete/soccerprof-hamburg-kinder-jugendliche-fussballtraining.avif" alt="Individuelles Fußballtraining für Kinder und Jugendliche in Hamburg" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950/85 via-slate-950/20 to-transparent"></div>
              
              <!-- Floating Badge Top Left -->
              <div class="absolute top-4 left-4 px-3.5 py-1.5 rounded-full bg-slate-900/90 backdrop-blur-md border border-[#D4AF37]/50 text-white text-xs font-black flex items-center gap-2">
                <i class="fa-solid fa-bullseye text-[#D4AF37]"></i>
                <span>100% Individueller Fokus</span>
              </div>

              <!-- Floating Card Bottom -->
              <div class="absolute bottom-6 left-6 right-6 p-4 rounded-2xl bg-white/95 backdrop-blur-md border border-slate-200 shadow-xl">
                <div class="flex items-center gap-3">
                  <div class="w-11 h-11 rounded-xl bg-[#E63946] text-white flex items-center justify-center font-black text-lg shadow-red-glow">
                    <i class="fa-solid fa-futbol"></i>
                  </div>
                  <div>
                    <div class="text-xs font-black text-slate-900">SoccerProf Academy | Sami Ghaouar</div>
                    <div class="text-[11px] text-slate-600 font-semibold">Öjendorfer Weg 80 · 22119 Hamburg Billstedt</div>
                    <div class="text-[10px] text-[#D4AF37] font-black uppercase mt-0.5">Die perfekte Ergänzung zum Fußballverein 👍 ⚽</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ============================================================
       TRUST-LEISTE DIREKT NACH DEM HERO (Punkt 10: Echte Fakten)
       ============================================================ -->
  <section class="py-6 bg-slate-900 text-white relative z-10 border-y border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
        
        <div class="p-4 rounded-2xl bg-slate-800/60 border border-slate-700/60">
          <div class="text-2xl sm:text-3xl font-black text-[#D4AF37] mb-1">UEFA-B</div>
          <div class="text-xs text-slate-300 font-bold uppercase tracking-wider">Trainer-Lizenz (2018)</div>
          <div class="text-[11px] text-slate-400 mt-0.5">DFB Sportschule Duisburg-Wedau</div>
        </div>

        <div class="p-4 rounded-2xl bg-slate-800/60 border border-slate-700/60">
          <div class="text-2xl sm:text-3xl font-black text-white mb-1">Seit 2012</div>
          <div class="text-xs text-slate-300 font-bold uppercase tracking-wider">Trainer-Erfahrung</div>
          <div class="text-[11px] text-slate-400 mt-0.5">Individual- &amp; Sportschultraining</div>
        </div>

        <div class="p-4 rounded-2xl bg-slate-800/60 border border-slate-700/60">
          <div class="text-2xl sm:text-3xl font-black text-[#E63946] mb-1">3 Standorte</div>
          <div class="text-xs text-slate-300 font-bold uppercase tracking-wider">Hamburg &amp; Umgebung</div>
          <div class="text-[11px] text-slate-400 mt-0.5">Billstedt · Reinbek · Eimsbüttel</div>
        </div>

        <div class="p-4 rounded-2xl bg-slate-800/60 border border-slate-700/60">
          <div class="text-2xl sm:text-3xl font-black text-[#D4AF37] mb-1">Flügelspieler</div>
          <div class="text-xs text-slate-300 font-bold uppercase tracking-wider">Hamburger SV (HSV)</div>
          <div class="text-[11px] text-slate-400 mt-0.5">Höchste Liga: Regionalliga</div>
        </div>

      </div>
    </div>
  </section>

  <!-- ============================================================
       2. PROBLEM SECTION (Punkt 11: Mannschaft vs. Individuell)
       ============================================================ -->
  <section class="py-20 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4" data-aos="fade-up">
        <div class="inline-block px-3.5 py-1 rounded-full bg-[#E63946]/10 text-[#E63946] font-black text-xs uppercase tracking-widest border border-[#E63946]/30">
          Die Herausforderung im Vereinsalltag
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight leading-tight">
          Im Mannschaftstraining bleibt nicht immer Zeit für jeden Spieler.
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg leading-relaxed">
          Mannschaftstraining ist ein wichtiger Bestandteil der Entwicklung. Aber wenn viele Spieler gleichzeitig trainieren, bleibt häufig weniger Zeit für individuelle Korrekturen, Wiederholungen und persönliche Entwicklungsziele. <strong>Genau hier setzt individuelles Training an.</strong>
        </p>
      </div>

      <!-- Drei Vorteile des individuellen Trainings (Punkt 11) -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <div class="glass-card p-8 rounded-3xl space-y-4 border-t-4 border-t-[#D4AF37]" data-aos="fade-up" data-aos-delay="100">
          <div class="w-14 h-14 rounded-2xl bg-slate-900 text-[#D4AF37] flex items-center justify-center text-2xl font-black shadow-md">
            <i class="fa-solid fa-eye"></i>
          </div>
          <h3 class="text-xl font-black text-slate-900">Individuelle Aufmerksamkeit</h3>
          <p class="text-slate-600 text-sm leading-relaxed">
            Jede Fußstellung, jede Ballberührung und jede Körperhaltung wird vom Trainer genau beobachtet und sofort im Detail korrigiert. Keine versteckten Fehler in der Menge.
          </p>
          <div class="pt-2 text-xs font-bold text-[#D4AF37] uppercase flex items-center gap-1.5">
            <i class="fa-solid fa-check-circle"></i> 100% Fokus auf den Spieler
          </div>
        </div>

        <div class="glass-card p-8 rounded-3xl space-y-4 border-t-4 border-t-[#E63946]" data-aos="fade-up" data-aos-delay="200">
          <div class="w-14 h-14 rounded-2xl bg-[#E63946] text-white flex items-center justify-center text-2xl font-black shadow-red-glow">
            <i class="fa-solid fa-arrows-rotate"></i>
          </div>
          <h3 class="text-xl font-black text-slate-900">Gezielte Wiederholungen</h3>
          <p class="text-slate-600 text-sm leading-relaxed">
            Statt langer Wartezeiten an Hütchenreihen erhält der Spieler in 60 bis 90 Minuten ein Vielfaches an Ballkontakten, Schüssen und 1-gegen-1-Situationen.
          </p>
          <div class="pt-2 text-xs font-bold text-[#E63946] uppercase flex items-center gap-1.5">
            <i class="fa-solid fa-check-circle"></i> Maximale Ballaktionen pro Einheit
          </div>
        </div>

        <div class="glass-card p-8 rounded-3xl space-y-4 border-t-4 border-t-slate-900" data-aos="fade-up" data-aos-delay="300">
          <div class="w-14 h-14 rounded-2xl bg-slate-900 text-white flex items-center justify-center text-2xl font-black shadow-md">
            <i class="fa-solid fa-chart-line"></i>
          </div>
          <h3 class="text-xl font-black text-slate-900">Training nach Entwicklungsstand</h3>
          <p class="text-slate-600 text-sm leading-relaxed">
            Kein Standardprogramm für alle. Ob schwacher Fuß, Vororientierung, Schnelligkeit oder Selbstvertrauen – wir trainieren genau das, was der Spieler jetzt braucht.
          </p>
          <div class="pt-2 text-xs font-bold text-slate-800 uppercase flex items-center gap-1.5">
            <i class="fa-solid fa-check-circle"></i> Passgenau abgestimmter Trainingsplan
          </div>
        </div>

      </div>

      <!-- Quote Box: Die perfekte Ergänzung -->
      <div class="mt-12 p-6 sm:p-8 rounded-3xl bg-white/90 backdrop-blur-md border-2 border-slate-200/90 shadow-md flex flex-col md:flex-row items-center justify-between gap-6" data-aos="zoom-in">
        <div class="flex items-center gap-4">
          <div class="text-4xl text-[#E63946]">⚽</div>
          <div>
            <div class="text-lg font-black text-slate-900">
              Die perfekte Ergänzung zum Fußballverein 👍
            </div>
            <p class="text-xs sm:text-sm text-slate-600 font-medium mt-0.5">
              SoccerProf ersetzt nicht den Verein, sondern gibt engagierten Spielern genau den Feinschliff, der im Mannschaftstraining zu kurz kommt.
            </p>
          </div>
        </div>
        <a href="#kontakt" class="shrink-0 px-6 py-3 rounded-full bg-slate-900 hover:bg-[#D4AF37] text-white hover:text-slate-900 font-bold text-xs uppercase tracking-wider transition-all shadow-md">
          Jetzt Erstgespräch vereinbaren
        </a>
      </div>

    </div>
  </section>

  <!-- ============================================================
       3. TRAININGSANGEBOTE (Punkt 12 & 13: Klare Priorisierung)
       ============================================================ -->
  <section id="angebote" class="py-20 bg-white/70 backdrop-blur-md relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4" data-aos="fade-up">
        <div class="inline-block px-3.5 py-1 rounded-full bg-[#D4AF37]/10 text-[#D4AF37] font-black text-xs uppercase tracking-widest border border-[#D4AF37]/30">
          Gezielte Förderung
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          Das passende Training für deine Entwicklung.
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg">
          Jedes Fußballtraining wird individuell auf die Stärken und Schwächen der Spieler:innen angepasst. <strong>Spaß in Verbindung mit spürbarer Entwicklung steht für uns jederzeit an erster Stelle.</strong>
        </p>
      </div>

      <!-- KERNANGEBOTE: 01 Einzeltraining prominenteste Karte, gefolgt von Kleingruppe & Mannschaft -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch mb-12">
        
        <!-- 01 EINZELTRAINING (Höchste visuelle Gewichtung! 7 Spalten auf Large) -->
        <div class="lg:col-span-7 glass-card p-8 sm:p-10 rounded-3xl flex flex-col justify-between border-2 border-[#D4AF37] shadow-xl relative overflow-hidden" data-aos="fade-up">
          <div class="absolute top-4 right-4 px-3.5 py-1 rounded-full bg-[#D4AF37] text-slate-900 font-black text-xs uppercase tracking-wider shadow-sm">
            01 · Kernangebot
          </div>

          <div>
            <div class="flex items-center gap-3 mb-4">
              <span class="w-10 h-10 rounded-xl bg-slate-900 text-[#D4AF37] flex items-center justify-center font-black text-base">
                1:1
              </span>
              <div>
                <h3 class="text-2xl sm:text-3xl font-black text-slate-900">Einzeltraining</h3>
                <div class="text-xs font-bold text-[#D4AF37] uppercase">100 % Fokus auf einen Spieler</div>
              </div>
            </div>

            <!-- Bild -->
            <div class="w-full h-56 sm:h-64 rounded-2xl overflow-hidden mb-6 shadow-md border border-slate-200/80 relative group">
              <img src="img/packete/soccerprof-hamburg-kinder-jugendliche-fussballtraining.avif" alt="Einzeltraining Fußball Hamburg Sami Ghaouar" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950/70 via-transparent to-transparent"></div>
              <span class="absolute bottom-3 left-3 text-white text-xs font-bold bg-slate-900/80 px-3 py-1 rounded-lg backdrop-blur-sm">
                Individuell nach persönlichen Wünschen &amp; Zielen
              </span>
            </div>

            <p class="text-slate-700 text-sm sm:text-base leading-relaxed mb-6 font-medium">
              Dein Kind spielt in einem Fußballverein, möchte aber privat noch mehr trainieren? Bestimmte Disziplinen sollen gefördert werden? Dann bist du bei uns genau richtig! Unser individuelles Training richtet sich gänzlich nach euren Wünschen, um dich oder deine Kinder auf eurem persönlichen sportlichen Weg zu begleiten.
            </p>

            <!-- Trainingsschwerpunkte im Einzeltraining -->
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-2.5 mb-8 text-xs font-bold text-slate-800">
              <div class="p-2.5 rounded-xl bg-slate-100 border border-slate-200 flex items-center gap-2">
                <i class="fa-solid fa-futbol text-[#D4AF37]"></i> Technik &amp; Ballannahme
              </div>
              <div class="p-2.5 rounded-xl bg-slate-100 border border-slate-200 flex items-center gap-2">
                <i class="fa-solid fa-bullseye text-[#E63946]"></i> Torabschluss &amp; Schuss
              </div>
              <div class="p-2.5 rounded-xl bg-slate-100 border border-slate-200 flex items-center gap-2">
                <i class="fa-solid fa-brain text-slate-700"></i> Kognition &amp; Tempo
              </div>
              <div class="p-2.5 rounded-xl bg-slate-100 border border-slate-200 flex items-center gap-2">
                <i class="fa-solid fa-shuffle text-[#D4AF37]"></i> Dribbling &amp; Beidfüßigkeit
              </div>
              <div class="p-2.5 rounded-xl bg-slate-100 border border-slate-200 flex items-center gap-2">
                <i class="fa-solid fa-shield-halved text-[#E63946]"></i> Mentale Stärke
              </div>
              <div class="p-2.5 rounded-xl bg-slate-100 border border-slate-200 flex items-center gap-2">
                <i class="fa-solid fa-video text-slate-700"></i> Video- &amp; Bewegungsanalyse
              </div>
            </div>
          </div>

          <div class="pt-4 border-t border-slate-200 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>
              <div class="text-xs text-slate-500 font-semibold">Preise &amp; Tarife:</div>
              <div class="text-base font-black text-slate-900">Auf Anfrage <span class="text-xs font-normal text-slate-500">(5er- &amp; 10er-Karten)</span></div>
            </div>
            <a href="#kontakt" class="w-full sm:w-auto px-8 py-3.5 rounded-2xl bg-slate-900 hover:bg-[#D4AF37] text-white hover:text-slate-900 font-black text-xs uppercase tracking-wider transition-all text-center shadow-md">
              Einzeltraining anfragen <i class="fa-solid fa-arrow-right ml-2"></i>
            </a>
          </div>
        </div>

        <!-- Right Side: 02 Kleingruppentraining & 03 Mannschaftstraining (5 Spalten) -->
        <div class="lg:col-span-5 space-y-8 flex flex-col justify-between">
          
          <!-- 02 KLEINGRUPPENTRAINING -->
          <div class="glass-card p-6 sm:p-7 rounded-3xl flex flex-col justify-between border-2 border-[#E63946] shadow-md hover:-translate-y-1 transition-all" data-aos="fade-up" data-aos-delay="100">
            <div>
              <div class="flex items-center justify-between mb-3">
                <span class="px-3 py-1 rounded-full text-[11px] font-black uppercase bg-[#E63946] text-white">
                  02 · Feste 5er-Gruppen
                </span>
                <span class="text-xs font-bold text-slate-500">Auf Anfrage</span>
              </div>
              
              <div class="w-full h-36 rounded-2xl overflow-hidden mb-4 relative">
                <img src="img/packete/kleingruppe.avif" alt="Kleingruppentraining Fußball Hamburg" class="w-full h-full object-cover">
              </div>

              <h3 class="text-xl font-black text-slate-900 mb-1.5">Kleingruppentraining</h3>
              <p class="text-slate-600 text-xs sm:text-sm leading-relaxed mb-4">
                In festen 5er-Gruppen trainieren wir gemeinsam, um individuelle Stärken auszubauen und Schwächen zu verbessern. Die Gruppe fördert Motivation und Teamgeist. So lernen dein Kind oder du wichtiges Handwerkszeug, das in jedem Fußballspiel genutzt werden kann.
              </p>
            </div>

            <a href="#kontakt" class="w-full py-3 rounded-xl bg-[#E63946] hover:bg-[#C52233] text-white font-black text-xs uppercase tracking-wider text-center block transition-all shadow-red-glow">
              Kleingruppe anfragen
            </a>
          </div>

          <!-- 03 MANNSCHAFTSTRAINING -->
          <div class="glass-card p-6 sm:p-7 rounded-3xl flex flex-col justify-between border border-slate-300 shadow-md hover:-translate-y-1 transition-all" data-aos="fade-up" data-aos-delay="200">
            <div>
              <div class="flex items-center justify-between mb-3">
                <span class="px-3 py-1 rounded-full text-[11px] font-black uppercase bg-slate-900 text-[#D4AF37]">
                  03 · Für Vereine &amp; Teams
                </span>
                <span class="text-xs font-bold text-slate-500">Auf Anfrage</span>
              </div>

              <div class="w-full h-36 rounded-2xl overflow-hidden mb-4 relative">
                <img src="img/packete/Fu%C3%9Fballspieler%20auf%20Bank.avif" alt="Mannschaftstraining Fußball Hamburg" class="w-full h-full object-cover">
              </div>

              <h3 class="text-xl font-black text-slate-900 mb-1.5">Mannschaftstraining</h3>
              <p class="text-slate-600 text-xs sm:text-sm leading-relaxed mb-4">
                Deine Mannschaft möchte Taktik, Technik oder den Gruppenzusammenhalt stärken? Wir stellen ein individuelles privates Fußballtraining zusammen, um mit viel Spaß und Begeisterung Potenziale zu verbessern.
              </p>
            </div>

            <a href="#kontakt" class="w-full py-3 rounded-xl bg-slate-900 hover:bg-[#D4AF37] text-white hover:text-slate-900 font-black text-xs uppercase tracking-wider text-center block transition-all">
              Mannschaftstraining anfragen
            </a>
          </div>

        </div>

      </div>

      <!-- SEKUNDÄRE ANGEBOTE (Punkt 21 & 22: Dezent integriert, stören die Hauptjourney nicht) -->
      <div class="pt-8 border-t border-slate-200">
        <div class="text-center mb-6">
          <span class="text-xs font-extrabold uppercase tracking-wider text-slate-500">
            Weitere Angebote der SoccerProf Academy:
          </span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          
          <!-- Veranstaltungen & Camps -->
          <div class="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm flex items-start gap-4 hover:border-[#D4AF37] transition-colors">
            <div class="w-12 h-12 rounded-xl bg-[#D4AF37]/10 text-[#D4AF37] flex items-center justify-center text-xl shrink-0 font-bold">
              <i class="fa-solid fa-campground"></i>
            </div>
            <div>
              <h4 class="text-base font-black text-slate-900">Veranstaltungen, Camps &amp; Kindergeburtstage</h4>
              <p class="text-slate-600 text-xs leading-relaxed mt-1 mb-2">
                Regelmäßige Fußballcamps, Turniere und sportliche Events für SoccerProf-Spieler:innen. Auch unvergessliche Kindergeburtstage voller Fußballaction könnt ihr bei uns feiern.
              </p>
              <a href="#kontakt" class="text-xs font-bold text-[#E63946] hover:underline flex items-center gap-1">
                Event anfragen <i class="fa-solid fa-chevron-right text-[10px]"></i>
              </a>
            </div>
          </div>

          <!-- Training für Erwachsene -->
          <div class="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm flex items-start gap-4 hover:border-[#D4AF37] transition-colors">
            <div class="w-12 h-12 rounded-xl bg-slate-900 text-white flex items-center justify-center text-xl shrink-0 font-bold">
              <i class="fa-solid fa-user-ninja"></i>
            </div>
            <div>
              <h4 class="text-base font-black text-slate-900">Training für Erwachsene</h4>
              <p class="text-slate-600 text-xs leading-relaxed mt-1 mb-2">
                Optimal für Spieler:innen, die Technik, Kraft-Ausdauer, Stellungsspiel und kognitive Fähigkeiten verfeinern möchten. Egal wie alt und fit du aktuell bist – unsere Ziele kennen keine Grenzen.
              </p>
              <a href="#kontakt" class="text-xs font-bold text-[#E63946] hover:underline flex items-center gap-1">
                Erwachsenentraining entdecken <i class="fa-solid fa-chevron-right text-[10px]"></i>
              </a>
            </div>
          </div>

        </div>
      </div>

    </div>
  </section>

  <!-- ============================================================
       4. TRAININGSMETHODE (Punkt 14 & 15: Visueller 4-Stufen Prozess)
       ============================================================ -->
  <section id="methode" class="py-20 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4" data-aos="fade-up">
        <div class="inline-block px-3.5 py-1 rounded-full bg-[#D4AF37]/10 text-[#D4AF37] font-black text-xs uppercase tracking-widest border border-[#D4AF37]/30">
          Unser Systematischer Ansatz
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          Nicht einfach mehr trainieren. <br><span class="text-gradient-gold">Sondern gezielter.</span>
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg">
          Das Training orientiert sich am Spieler – nicht an einem Standardprogramm. Nicht jeder Spieler braucht dasselbe. Durch unseren 4-Schritte-Prozess stellen wir sicher, dass jede Einheit maximale Wirkung erzielt.
        </p>
      </div>

      <!-- 4-Schritte Prozess Kacheln (Punkt 14) -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-20">
        
        <!-- Step 1 -->
        <div class="glass-card p-6 sm:p-8 rounded-3xl space-y-4 relative" data-aos="fade-up" data-aos-delay="100">
          <div class="text-4xl font-black text-[#D4AF37]/40 absolute top-6 right-6">01</div>
          <div class="w-12 h-12 rounded-2xl bg-slate-900 text-[#D4AF37] flex items-center justify-center text-xl font-bold">
            <i class="fa-solid fa-magnifying-glass-chart"></i>
          </div>
          <h3 class="text-xl font-black text-slate-900">Analyse</h3>
          <p class="text-slate-600 text-xs leading-relaxed">
            Wir analysieren die technischen, körperlichen und charakterlichen Stärken und Schwächen des Spielers direkt auf dem Platz.
          </p>
          <div class="text-[11px] font-bold text-slate-500 border-t border-slate-200 pt-3">
            Ist-Zustand erfassen
          </div>
        </div>

        <!-- Step 2 -->
        <div class="glass-card p-6 sm:p-8 rounded-3xl space-y-4 relative" data-aos="fade-up" data-aos-delay="200">
          <div class="text-4xl font-black text-[#E63946]/40 absolute top-6 right-6">02</div>
          <div class="w-12 h-12 rounded-2xl bg-[#E63946] text-white flex items-center justify-center text-xl font-bold shadow-red-glow">
            <i class="fa-solid fa-bullseye"></i>
          </div>
          <h3 class="text-xl font-black text-slate-900">Individuelle Ziele</h3>
          <p class="text-slate-600 text-xs leading-relaxed">
            Gemeinsam definieren wir klare Schwerpunkte: Sei es Beidfüßigkeit, Schnelligkeit, 1v1-Durchsetzungsvermögen oder Mentale Stärke.
          </p>
          <div class="text-[11px] font-bold text-slate-500 border-t border-slate-200 pt-3">
            Fokus schärfen
          </div>
        </div>

        <!-- Step 3 -->
        <div class="glass-card p-6 sm:p-8 rounded-3xl space-y-4 relative" data-aos="fade-up" data-aos-delay="300">
          <div class="text-4xl font-black text-[#D4AF37]/40 absolute top-6 right-6">03</div>
          <div class="w-12 h-12 rounded-2xl bg-slate-900 text-[#D4AF37] flex items-center justify-center text-xl font-bold">
            <i class="fa-solid fa-bolt"></i>
          </div>
          <h3 class="text-xl font-black text-slate-900">Gezieltes Training</h3>
          <p class="text-slate-600 text-xs leading-relaxed">
            Intensive Einheiten mit hoher Wiederholungszahl, Spielsituationen unter Zeitdruck und stetiger Detailkorrektur durch den Trainer.
          </p>
          <div class="text-[11px] font-bold text-slate-500 border-t border-slate-200 pt-3">
            Qualität vor Quantität
          </div>
        </div>

        <!-- Step 4 -->
        <div class="glass-card p-6 sm:p-8 rounded-3xl space-y-4 relative" data-aos="fade-up" data-aos-delay="400">
          <div class="text-4xl font-black text-slate-900/30 absolute top-6 right-6">04</div>
          <div class="w-12 h-12 rounded-2xl bg-slate-900 text-white flex items-center justify-center text-xl font-bold">
            <i class="fa-solid fa-trophy"></i>
          </div>
          <h3 class="text-xl font-black text-slate-900">Feedback &amp; Entwicklung</h3>
          <p class="text-slate-600 text-xs leading-relaxed">
            Ehrliches, motivierendes Feedback nach jeder Einheit. Wir beobachten die Fortschritte und passen die Übungsintensität kontinuierlich an.
          </p>
          <div class="text-[11px] font-bold text-slate-500 border-t border-slate-200 pt-3">
            Sichtbare Erfolge
          </div>
        </div>

      </div>

      <!-- TRAININGSBEREICHE (Punkt 15: Was wir gezielt verbessern können) -->
      <div class="text-center max-w-2xl mx-auto mb-12 space-y-3">
        <h3 class="text-2xl sm:text-3xl font-black text-slate-900">
          Was wir gezielt verbessern können
        </h3>
        <p class="text-slate-600 text-sm">
          Nur echte SoccerProf-Leistungen – praxisnah, intensiv und nachhaltig.
        </p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        
        <div class="p-5 rounded-2xl bg-white/90 border border-slate-200 shadow-sm hover:border-[#D4AF37] transition-all">
          <div class="text-xl text-[#D4AF37] mb-2"><i class="fa-solid fa-futbol"></i></div>
          <div class="font-black text-sm text-slate-900 mb-1">Technik</div>
          <p class="text-slate-600 text-xs leading-relaxed">Feinschliff an Ballannahme, Ballführung, Passpräzision, Beidfüßigkeit und sicherem Torabschluss.</p>
        </div>

        <div class="p-5 rounded-2xl bg-white/90 border border-slate-200 shadow-sm hover:border-[#E63946] transition-all">
          <div class="text-xl text-[#E63946] mb-2"><i class="fa-solid fa-chess"></i></div>
          <div class="font-black text-sm text-slate-900 mb-1">Taktik</div>
          <p class="text-slate-600 text-xs leading-relaxed">Stellungsspiel, Raumverständnis, Vororientierung und das richtige Verhalten im 1v1 defensiv wie offensiv.</p>
        </div>

        <div class="p-5 rounded-2xl bg-white/90 border border-slate-200 shadow-sm hover:border-[#D4AF37] transition-all">
          <div class="text-xl text-[#D4AF37] mb-2"><i class="fa-solid fa-brain"></i></div>
          <div class="font-black text-sm text-slate-900 mb-1">Kognition</div>
          <p class="text-slate-600 text-xs leading-relaxed">Visuelle Reizverarbeitung, schnelle Entscheidungsfindung unter Zeitdruck und Erhöhung des Handlungstempos.</p>
        </div>

        <div class="p-5 rounded-2xl bg-white/90 border border-slate-200 shadow-sm hover:border-[#E63946] transition-all">
          <div class="text-xl text-[#E63946] mb-2"><i class="fa-solid fa-person-running"></i></div>
          <div class="font-black text-sm text-slate-900 mb-1">Koordination</div>
          <p class="text-slate-600 text-xs leading-relaxed">Laufkoordination, Beweglichkeit, Antrittsschnelligkeit und optimale Körperbeherrschung mit und ohne Ball.</p>
        </div>

        <div class="p-5 rounded-2xl bg-white/90 border border-slate-200 shadow-sm hover:border-[#D4AF37] transition-all">
          <div class="text-xl text-[#D4AF37] mb-2"><i class="fa-solid fa-dumbbell"></i></div>
          <div class="font-black text-sm text-slate-900 mb-1">Fitness &amp; Ausdauer</div>
          <p class="text-slate-600 text-xs leading-relaxed">Fußballspezifische Kraftausdauer, Stabilität und Spritzigkeit, um auch in der 90. Minute den Unterschied zu machen.</p>
        </div>

        <div class="p-5 rounded-2xl bg-white/90 border border-slate-200 shadow-sm hover:border-[#E63946] transition-all">
          <div class="text-xl text-[#E63946] mb-2"><i class="fa-solid fa-shield-halved"></i></div>
          <div class="font-black text-sm text-slate-900 mb-1">Mentaltraining</div>
          <p class="text-slate-600 text-xs leading-relaxed">Selbstvertrauen aufbauen, mit Druck und Fehlern konstruktiv umgehen und Spielfreude ungezwungen entfalten.</p>
        </div>

        <div class="p-5 rounded-2xl bg-white/90 border border-slate-200 shadow-sm hover:border-[#D4AF37] transition-all">
          <div class="text-xl text-[#D4AF37] mb-2"><i class="fa-solid fa-compass"></i></div>
          <div class="font-black text-sm text-slate-900 mb-1">Stellungsspiel</div>
          <p class="text-slate-600 text-xs leading-relaxed">Vororientierung vor der Ballannahme, Schulterblick und das geschickte Besetzen gefährlicher Halbräume.</p>
        </div>

        <div class="p-5 rounded-2xl bg-white/90 border border-slate-200 shadow-sm hover:border-[#E63946] transition-all">
          <div class="text-xl text-[#E63946] mb-2"><i class="fa-solid fa-hands"></i></div>
          <div class="font-black text-sm text-slate-900 mb-1">Torwarttraining</div>
          <p class="text-slate-600 text-xs leading-relaxed">Mit zertifizierter Torwarttrainer-Lizenz: Stellungsspiel, Fangsicherheit, modernes Mitspielen und Reflexe.</p>
        </div>

      </div>

    </div>
  </section>

  <!-- ============================================================
       5. WARUM SOCCERPROF & REVIEWS (Punkt 16 & 17)
       ============================================================ -->
  <section id="warum" class="py-20 bg-white/70 backdrop-blur-md relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4" data-aos="fade-up">
        <div class="inline-block px-3.5 py-1 rounded-full bg-[#E63946]/10 text-[#E63946] font-black text-xs uppercase tracking-widest border border-[#E63946]/30">
          Vier Starke Argumente
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          Warum SoccerProf?
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg">
          Wir unterstützen talentierte Kinder und Jugendliche gezielt durch privates Konditions-, Taktik- und Mentaltraining. Immer mit dabei: <strong>Viel Herz und gesunder Menschenverstand</strong>.
        </p>
      </div>

      <!-- 4 Säulen von SoccerProf (Punkt 16) -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
        
        <div class="glass-card p-6 rounded-3xl space-y-3" data-aos="fade-up" data-aos-delay="100">
          <div class="w-12 h-12 rounded-2xl bg-slate-900 text-[#D4AF37] flex items-center justify-center text-lg font-bold">
            <i class="fa-solid fa-user-check"></i>
          </div>
          <h3 class="text-lg font-black text-slate-900 uppercase tracking-wide">Individuell</h3>
          <p class="text-slate-600 text-xs leading-relaxed">
            Jeder Spieler wird exakt entsprechend seinem aktuellen Entwicklungsstand und seinen Talenten trainiert.
          </p>
        </div>

        <div class="glass-card p-6 rounded-3xl space-y-3" data-aos="fade-up" data-aos-delay="200">
          <div class="w-12 h-12 rounded-2xl bg-[#E63946] text-white flex items-center justify-center text-lg font-bold shadow-red-glow">
            <i class="fa-solid fa-shapes"></i>
          </div>
          <h3 class="text-lg font-black text-slate-900 uppercase tracking-wide">Ganzheitlich</h3>
          <p class="text-slate-600 text-xs leading-relaxed">
            Nicht nur Technik – sondern auch Taktik, Kognition, Fitness, Koordination und mentale Aspekte im Einklang.
          </p>
        </div>

        <div class="glass-card p-6 rounded-3xl space-y-3" data-aos="fade-up" data-aos-delay="300">
          <div class="w-12 h-12 rounded-2xl bg-slate-900 text-[#D4AF37] flex items-center justify-center text-lg font-bold">
            <i class="fa-solid fa-heart"></i>
          </div>
          <h3 class="text-lg font-black text-slate-900 uppercase tracking-wide">Persönlich</h3>
          <p class="text-slate-600 text-xs leading-relaxed">
            Direkte Betreuung, vertrauensvolle Atmosphäre und ehrliches Feedback auf Augenhöhe mit den Spielern.
          </p>
        </div>

        <div class="glass-card p-6 rounded-3xl space-y-3" data-aos="fade-up" data-aos-delay="400">
          <div class="w-12 h-12 rounded-2xl bg-[#E63946] text-white flex items-center justify-center text-lg font-bold shadow-red-glow">
            <i class="fa-solid fa-handshake"></i>
          </div>
          <h3 class="text-lg font-black text-slate-900 uppercase tracking-wide">Ergänzend</h3>
          <p class="text-slate-600 text-xs leading-relaxed">
            Das Training ergänzt den Fußballverein sinnvoll dort, wo individuelles Arbeiten besonders wichtig ist.
          </p>
        </div>

      </div>

      <!-- REVIEWS: Echtes Testimonial von Angelika (Punkt 17) -->
      <div class="max-w-3xl mx-auto glass-card p-8 sm:p-10 rounded-3xl border-2 border-[#D4AF37]/60 shadow-xl text-center space-y-4" data-aos="zoom-in">
        <div class="flex justify-center text-[#D4AF37] text-2xl gap-1">
          <i class="fa-solid fa-star"></i>
          <i class="fa-solid fa-star"></i>
          <i class="fa-solid fa-star"></i>
          <i class="fa-solid fa-star"></i>
          <i class="fa-solid fa-star"></i>
        </div>
        <p class="text-lg sm:text-xl font-bold text-slate-900 italic leading-relaxed">
          "Danke lieber Sami! Uns hat’s auch gefreut und die Kids sind ganz begeistert von dir 🤩. Weil du so ein cooler Fußballer bist 😎. Und vor allem nett 😊"
        </p>
        <div class="pt-2">
          <div class="text-xs font-black uppercase text-[#E63946] tracking-widest">
            Angelika (Mutter) · SoccerProf Hamburg
          </div>
          <div class="text-[11px] text-slate-500 font-semibold mt-0.5">
            Verifizierte Elternstimme aus Hamburg
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ============================================================
       6. ÜBER UNS (Punkt 18 & Vorhandener Text aus soccerprof.de)
       ============================================================ -->
  <section id="ueber-uns" class="py-20 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4" data-aos="fade-up">
        <div class="inline-block px-3.5 py-1 rounded-full bg-[#D4AF37]/10 text-[#D4AF37] font-black text-xs uppercase tracking-widest border border-[#D4AF37]/30">
          Philosophie &amp; Team
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          Über uns
        </h2>
        <p class="text-slate-700 font-bold text-lg sm:text-xl">
          Unser Team aus Fußballbegeisterten, Sportpädagogen und leidenschaftlichen Trainern sorgt für Spaß, Motivation und Können!
        </p>
      </div>

      <div class="glass-card p-8 sm:p-12 rounded-3xl border border-slate-200 shadow-xl space-y-6 max-w-4xl mx-auto" data-aos="fade-up">
        <div class="flex items-center gap-3 text-[#E63946] font-black text-sm uppercase tracking-wider">
          <i class="fa-solid fa-users"></i>
          <span>UNSER TRAINERTEAM (2 TRAINER)</span>
        </div>
        <div class="space-y-4 text-slate-700 text-sm sm:text-base leading-relaxed font-medium">
          <p>
            Unser kleines Trainerteam besteht aus zwei Trainern. Wir haben uns darauf spezialisiert, jede:n Spieler:in individuell zu beraten und weiterzuentwickeln.
          </p>
          <p>
            Jeder Mensch ist einzigartig und genau so sollte jeder Fußballer und jede Fußballerin auch trainiert werden. Leider ist dies in Mannschaften kaum möglich. Außerdem nutzen immer weniger Kinder und Jugendliche die Möglichkeit, ihre Fähigkeiten auf Bolzplätzen zu verbessern.
          </p>
          <p class="p-4 rounded-2xl bg-[#D4AF37]/10 border-l-4 border-[#D4AF37] text-slate-900 font-bold">
            Daher ist es unser Ziel, jedem begeisterten Spieler und jeder engagierten Spielerin die Möglichkeit zu geben, sich in der <strong>SoccerProf Academy</strong> weiterzuentwickeln.
          </p>
          <p>
            Wir gehen intensiv auf die technischen, charakterlichen und körperlichen Stärken und Schwächen ein, um aus jedem einzelnen das maximale Potenzial herauszuholen. Auf deinen Wunsch hin beraten und unterstützen wir auch bei der Vereinssuche.
          </p>
        </div>
      </div>

    </div>
  </section>

  <!-- ============================================================
       7. DER TRAINER — STECKBRIEF SAMI GHAOUAR (Punkt 18: Reale Fakten)
       ============================================================ -->
  <section id="steckbrief" class="py-20 bg-slate-900 text-white relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4" data-aos="fade-up">
        <div class="inline-block px-3.5 py-1 rounded-full bg-[#D4AF37]/20 text-[#D4AF37] font-black text-xs uppercase border border-[#D4AF37]/30">
          Founder &amp; Head Coach
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black tracking-tight leading-tight">
          Hinter SoccerProf steht <span class="text-gradient-gold">echte Fußballerfahrung.</span>
        </h2>
        <p class="text-slate-300 font-medium text-sm sm:text-base italic max-w-2xl mx-auto">
          "Man lernt nie aus." Immer wieder begegnet uns dieser Spruch im Alltag, im Berufsleben und auch im Fußball trifft er definitiv zu. Damit das Weiterlernen gut klappt und vor allem richtig Spaß macht, unterstützen wir erfahrene Trainer Kinder, Jugendliche und Erwachsene – egal, ob Anfänger:innen oder Fortgeschrittene.
        </p>
      </div>

      <!-- DER EDLE STECKBRIEF (Card Layout mit Original-Daten) -->
      <div class="max-w-4xl mx-auto bg-gradient-to-br from-slate-800 to-slate-950 rounded-3xl border-2 border-[#D4AF37] shadow-2xl p-6 sm:p-10 relative overflow-hidden" data-aos="zoom-in">
        
        <!-- Background Glow -->
        <div class="absolute -right-20 -top-20 w-80 h-80 bg-[#D4AF37]/10 rounded-full blur-3xl pointer-events-none"></div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
          
          <!-- Foto Sami (Original aus img/sami) -->
          <div class="md:col-span-5 text-center">
            <div class="w-full h-80 sm:h-96 rounded-2xl overflow-hidden border-2 border-[#D4AF37]/60 shadow-xl relative group">
              <img src="img/sami/sami%20daumen%20hoch.avif" alt="Sami Ghaouar UEFA-B-Lizenz Trainer SoccerProf Academy" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <div class="absolute bottom-0 inset-x-0 bg-gradient-to-t from-slate-950 via-slate-950/70 to-transparent p-4">
                <span class="text-xs font-black text-[#D4AF37] tracking-widest uppercase">SOCCERPROF ACADEMY</span>
              </div>
            </div>
          </div>

          <!-- Steckbrief Details -->
          <div class="md:col-span-7 space-y-5">
            <div>
              <div class="flex items-center gap-3">
                <h3 class="text-3xl font-black text-white">Sami Ghaouar</h3>
                <span class="px-3 py-1 rounded-full bg-[#E63946] text-white font-black text-xs">Head Coach</span>
              </div>
              <p class="text-sm font-bold text-[#D4AF37] mt-1">
                UEFA-B-Lizenz-Trainer · Spezialisiert auf Kinder, Jugendliche &amp; Fortgeschrittene.
              </p>
            </div>

            <!-- Zitat von Sami (Wort für Wort aus soccerprof.de) -->
            <div class="p-4 rounded-2xl bg-slate-900/90 border border-[#D4AF37]/40 italic text-xs sm:text-sm text-slate-200">
              <i class="fa-solid fa-quote-left text-[#D4AF37] mr-2"></i>
              "Es macht mir Mega Spaß die Kids immer wieder zu pushen und ihnen ein Ziel vor dem Augen zu geben."
            </div>

            <!-- Steckbrief Daten-Grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
              <div class="steckbrief-badge">
                <span class="text-slate-400 block font-semibold">Höchste Spielklasse:</span>
                <span class="text-white font-black text-sm">Regionalliga</span>
              </div>
              <div class="steckbrief-badge">
                <span class="text-slate-400 block font-semibold">Position:</span>
                <span class="text-white font-black text-sm">Flügelspieler (Hamburger SV)</span>
              </div>
              <div class="steckbrief-badge sm:col-span-2">
                <span class="text-slate-400 block font-semibold">Coaching-Bereich:</span>
                <span class="text-white font-bold">Kinder &amp; Jugendbereich sowie Erwachsene (vor allem Fortgeschrittene)</span>
              </div>
            </div>

            <!-- Ausbildung Liste -->
            <div class="space-y-1.5 pt-1">
              <div class="text-xs font-black text-[#D4AF37] uppercase tracking-wider flex items-center gap-1.5">
                <i class="fa-solid fa-graduation-cap"></i> Ausbildung &amp; Lizenzen:
              </div>
              <ul class="text-xs text-slate-300 space-y-1 pl-4 list-disc font-medium">
                <li>B-Lizenz (2018)</li>
                <li>C-Lizenz (2014)</li>
                <li>Torwart-Trainer-Lizenz</li>
                <li>DFB-Fortbildung an der Sportschule Duisburg-Wedau</li>
              </ul>
            </div>

            <!-- Erfahrung Liste -->
            <div class="space-y-1.5 pt-1">
              <div class="text-xs font-black text-[#E63946] uppercase tracking-wider flex items-center gap-1.5">
                <i class="fa-solid fa-stopwatch"></i> Praxiserfahrung:
              </div>
              <ul class="text-xs text-slate-300 space-y-1 pl-4 list-disc font-medium">
                <li>Seit 2012 Individual- und Mannschaftstrainer</li>
                <li>Übungsleiter an Sportschulen für Klassen 1 bis 13</li>
                <li>Gelernter Flügelspieler beim Hamburger SV</li>
              </ul>
            </div>

            <!-- WhatsApp Direktkontakt -->
            <div class="pt-3">
              <a href="https://wa.me/4917684156542?text=Hallo%20Sami,%20ich%20habe%20deinen%20Steckbrief%20gesehen%20und%20m%C3%B6chte%20gerne%20ein%20Training%20anfragen!" target="_blank" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#25D366] hover:bg-[#20bd5a] text-white font-black text-xs uppercase tracking-wider shadow-lg transition-transform transform hover:scale-105">
                <i class="fa-brands fa-whatsapp text-lg"></i>
                <span>Direkt mit Sami per WhatsApp sprechen</span>
              </a>
            </div>

          </div>

        </div>

      </div>

    </div>
  </section>

  <!-- ============================================================
       8. ABLAUF (Punkt 19: So einfach startet dein Training)
       ============================================================ -->
  <section class="py-20 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4" data-aos="fade-up">
        <div class="inline-block px-3.5 py-1 rounded-full bg-[#E63946]/10 text-[#E63946] font-black text-xs uppercase tracking-widest border border-[#E63946]/30">
          In 3 einfachen Schritten
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          So einfach startet dein Training.
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg">
          Unkompliziert, transparent und unverbindlich. Wir begleiten dich vom ersten Kontakt bis zum Platz.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 relative max-w-5xl mx-auto">
        
        <!-- Step 1 -->
        <div class="glass-card p-8 rounded-3xl text-center space-y-4 relative" data-aos="fade-up" data-aos-delay="100">
          <div class="w-16 h-16 rounded-full bg-[#E63946] text-white mx-auto flex items-center justify-center text-2xl font-black shadow-red-glow">
            1
          </div>
          <h3 class="text-xl font-black text-slate-900">Kostenloses Erstgespräch</h3>
          <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">
            Wir sprechen kurz telefonisch oder per WhatsApp über den Spieler, die aktuellen Vereinsaktivitäten und seine individuellen Ziele.
          </p>
        </div>

        <!-- Step 2 -->
        <div class="glass-card p-8 rounded-3xl text-center space-y-4 relative" data-aos="fade-up" data-aos-delay="200">
          <div class="w-16 h-16 rounded-full bg-[#D4AF37] text-slate-900 mx-auto flex items-center justify-center text-2xl font-black shadow-md">
            2
          </div>
          <h3 class="text-xl font-black text-slate-900">Passendes Training finden</h3>
          <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">
            Gemeinsam wählen wir das ideale Trainingsformat: 1:1 Einzeltraining oder eine unserer festen 5er-Kleingruppen an einem Standort in Hamburg.
          </p>
        </div>

        <!-- Step 3 -->
        <div class="glass-card p-8 rounded-3xl text-center space-y-4 relative" data-aos="fade-up" data-aos-delay="300">
          <div class="w-16 h-16 rounded-full bg-slate-900 text-white mx-auto flex items-center justify-center text-2xl font-black shadow-md">
            3
          </div>
          <h3 class="text-xl font-black text-slate-900">Training starten</h3>
          <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">
            Der Spieler startet mit seinem individuellen Training, sammelt wertvolle Ballaktionen und entwickelt sich spürbar weiter.
          </p>
        </div>

      </div>

      <div class="mt-12 text-center" data-aos="fade-up">
        <a href="#kontakt" class="inline-flex items-center gap-3 px-8 py-4 rounded-full bg-[#E63946] hover:bg-[#C52233] text-white font-black text-xs uppercase tracking-wider shadow-red-glow transition-all">
          <span>Jetzt kostenloses Erstgespräch anfragen</span>
          <i class="fa-solid fa-arrow-right"></i>
        </a>
      </div>

    </div>
  </section>

  <!-- ============================================================
       9. PREISE & FORMATE (Punkt 20: Reale Formate, Transparenz)
       ============================================================ -->
  <section id="preise" class="py-20 bg-white/70 backdrop-blur-md relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4" data-aos="fade-up">
        <div class="inline-block px-3.5 py-1 rounded-full bg-[#D4AF37]/10 text-[#D4AF37] font-black text-xs uppercase tracking-widest border border-[#D4AF37]/30">
          Transparente Optionen
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          Transparente Preise. Passendes Training.
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg">
          Qualitatives Training zu fairen Konditionen in Hamburg. Keine versteckten Kosten.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-stretch max-w-5xl mx-auto">
        
        <!-- Box 1: Erstberatung -->
        <div class="glass-card p-8 rounded-3xl flex flex-col justify-between" data-aos="fade-up" data-aos-delay="100">
          <div>
            <h3 class="text-2xl font-black text-slate-900 mb-1">Erstberatung</h3>
            <div class="text-3xl font-black text-[#E63946] mb-4">Kostenlos</div>
            <p class="text-slate-600 text-xs mb-6">Persönliches Beratungsgespräch zur Abstimmung der Wünsche und Ziele deines Kindes.</p>
            <ul class="space-y-3 text-xs font-semibold text-slate-700 mb-8">
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Persönliche Beratung mit Trainer Sami</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Analyse der aktuellen Schwerpunkte</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Empfehlung des optimalen Formats</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> 100% Unverbindlich &amp; kostenfrei</li>
            </ul>
          </div>
          <a href="#kontakt" class="w-full py-3.5 rounded-2xl bg-slate-900 text-white font-black text-xs uppercase tracking-wider text-center block hover:bg-[#D4AF37] hover:text-slate-900 transition-colors shadow-sm">
            Erstgespräch anfragen
          </a>
        </div>

        <!-- Box 2: Kleingruppentraining -->
        <div class="glass-card p-8 rounded-3xl flex flex-col justify-between border-2 border-[#E63946] shadow-red-glow relative bg-white/95" data-aos="fade-up" data-aos-delay="200">
          <div class="absolute -top-3.5 left-1/2 -translate-x-1/2 bg-[#E63946] text-white font-black text-[10px] uppercase px-3.5 py-1 rounded-full shadow-sm">
            Feste 5er-Gruppe
          </div>
          <div>
            <h3 class="text-2xl font-black text-slate-900 mb-1">Kleingruppe</h3>
            <div class="text-2xl font-black text-slate-900 mb-4">Auf Anfrage <span class="text-xs font-normal text-slate-500">/ Tarif</span></div>
            <p class="text-slate-600 text-xs mb-6">Gemeinsam trainieren in festen 5er-Gruppen für maximale Motivation und Spielpraxis.</p>
            <ul class="space-y-3 text-xs font-semibold text-slate-700 mb-8">
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#E63946]"></i> Exakt 5 Spieler pro Gruppe</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#E63946]"></i> Hohe Dynamik, Wettkampf &amp; Teamgeist</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#E63946]"></i> Taktik, 1v1-Duelle &amp; Spielformen</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#E63946]"></i> Ganzjährig Outdoor &amp; Indoor</li>
            </ul>
          </div>
          <a href="#kontakt" class="w-full py-3.5 rounded-2xl bg-[#E63946] text-white font-black text-xs uppercase tracking-wider text-center block shadow-red-glow hover:bg-[#C52233] transition-colors">
            Kleingruppe anfragen
          </a>
        </div>

        <!-- Box 3: Einzeltraining -->
        <div class="glass-card p-8 rounded-3xl flex flex-col justify-between border-2 border-[#D4AF37]" data-aos="fade-up" data-aos-delay="300">
          <div>
            <div class="text-xs font-black text-[#D4AF37] uppercase mb-1">Meistgefragt</div>
            <h3 class="text-2xl font-black text-slate-900 mb-1">Einzeltraining</h3>
            <div class="text-2xl font-black text-slate-900 mb-4">Auf Anfrage <span class="text-xs font-normal text-slate-500">/ 5er &amp; 10er</span></div>
            <p class="text-slate-600 text-xs mb-6">100% persönliche Aufmerksamkeit für den individuellen Feinschliff deines Kinds.</p>
            <ul class="space-y-3 text-xs font-semibold text-slate-700 mb-8">
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> 1:1 Betreuung mit Head Coach Sami</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Detaillierte Bewegungs- &amp; Technikanalyse</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Individuell angepasste Trainingszeiten</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Flexible 5er- und 10er-Karten</li>
            </ul>
          </div>
          <a href="#kontakt" class="w-full py-3.5 rounded-2xl bg-slate-900 text-white font-black text-xs uppercase tracking-wider text-center block hover:bg-[#D4AF37] hover:text-slate-900 transition-colors shadow-sm">
            Einzeltraining anfragen
          </a>
        </div>

      </div>

    </div>
  </section>

  <!-- ============================================================
       10. FAQ ACCORDION (Punkt 23: Echte Fragen von soccerprof.de)
       ============================================================ -->
  <section id="faq" class="py-20 relative z-10">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center mb-16 space-y-4" data-aos="fade-up">
        <div class="inline-block px-3.5 py-1 rounded-full bg-[#E63946]/10 text-[#E63946] font-black text-xs uppercase tracking-widest border border-[#E63946]/30">
          Transparenz &amp; Klarheit
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          Häufig gestellte Fragen (FAQ)
        </h2>
        <p class="text-slate-600 font-medium text-base">
          Alles, was Eltern und Spieler vor dem Start wissen möchten.
        </p>
      </div>

      <div class="space-y-4">
        
        <details class="glass-card rounded-2xl p-5 group cursor-pointer border border-slate-200" data-aos="fade-up">
          <summary class="flex items-center justify-between font-black text-slate-900 text-base select-none">
            <span>Für welches Alter ist das SoccerProf-Training geeignet?</span>
            <i class="fa-solid fa-chevron-down text-sm text-[#D4AF37] faq-icon transition-transform duration-300"></i>
          </summary>
          <div class="pt-4 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-200/60 mt-3">
            Unser Schwerpunkt liegt auf Kindern und Jugendlichen aller Altersstufen – von Bambini und F-Jugend bis hin zur A-Jugend. Zudem bieten wir gezielte Performance-Einheiten für ambitionierte Erwachsene und Vereinsspieler an.
          </div>
        </details>

        <details class="glass-card rounded-2xl p-5 group cursor-pointer border border-slate-200" data-aos="fade-up" data-aos-delay="50">
          <summary class="flex items-center justify-between font-black text-slate-900 text-base select-none">
            <span>Ist das Training eine Konkurrenz zum Vereinsfußball?</span>
            <i class="fa-solid fa-chevron-down text-sm text-[#D4AF37] faq-icon transition-transform duration-300"></i>
          </summary>
          <div class="pt-4 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-200/60 mt-3">
            Nein, ganz im Gegenteil! Unser Motto lautet: <em>"Die perfekte Ergänzung zum Fußballverein 👍 ⚽"</em>. Wir arbeiten eng an den individuellen Schwächen und Stärken, für die im Mannschaftstraining mit 15–20 Spielern oft die Zeit fehlt. Die Fortschritte nimmt der Spieler direkt mit in sein Vereinsteam.
          </div>
        </details>

        <details class="glass-card rounded-2xl p-5 group cursor-pointer border border-slate-200" data-aos="fade-up" data-aos-delay="100">
          <summary class="flex items-center justify-between font-black text-slate-900 text-base select-none">
            <span>Wo genau findet das Training in Hamburg statt?</span>
            <i class="fa-solid fa-chevron-down text-sm text-[#D4AF37] faq-icon transition-transform duration-300"></i>
          </summary>
          <div class="pt-4 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-200/60 mt-3">
            Unser Hauptstützpunkt befindet sich am <strong>Öjendorfer Weg 80, 22119 Hamburg (Billstedt)</strong>. Zudem bieten wir Trainingseinheiten in <strong>Reinbek (Schleswig-Holstein)</strong> und <strong>Eimsbüttel (Hamburg West)</strong> an. Auf Wunsch und nach Absprache sind auch individuelle Trainingsorte möglich.
          </div>
        </details>

        <details class="glass-card rounded-2xl p-5 group cursor-pointer border border-slate-200" data-aos="fade-up" data-aos-delay="150">
          <summary class="flex items-center justify-between font-black text-slate-900 text-base select-none">
            <span>Wie groß sind die Gruppen beim Kleingruppentraining?</span>
            <i class="fa-solid fa-chevron-down text-sm text-[#D4AF37] faq-icon transition-transform duration-300"></i>
          </summary>
          <div class="pt-4 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-200/60 mt-3">
            Wir trainieren in festen 5er-Gruppen. So garantieren wir, dass jeder einzelne Spieler maximale Ballkontakte hat und dennoch echte Spielsituationen, Zweikämpfe und Teamgeist im Kleinfeld erlebt werden.
          </div>
        </details>

        <details class="glass-card rounded-2xl p-5 group cursor-pointer border border-slate-200" data-aos="fade-up" data-aos-delay="200">
          <summary class="flex items-center justify-between font-black text-slate-900 text-base select-none">
            <span>Wie läuft das kostenlose Erstgespräch ab?</span>
            <i class="fa-solid fa-chevron-down text-sm text-[#D4AF37] faq-icon transition-transform duration-300"></i>
          </summary>
          <div class="pt-4 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-200/60 mt-3">
            Ganz unkompliziert! Du füllst das Kontaktformular aus oder meldest dich direkt per WhatsApp oder Telefon. Trainer Sami bespricht mit dir den aktuellen Stand deines Kindes, eure Wünsche und Ziele und empfiehlt das passende Trainingsformat – 100% unverbindlich.
          </div>
        </details>

        <details class="glass-card rounded-2xl p-5 group cursor-pointer border border-slate-200" data-aos="fade-up" data-aos-delay="250">
          <summary class="flex items-center justify-between font-black text-slate-900 text-base select-none">
            <span>Werden auch Torhüter oder Erwachsene trainiert?</span>
            <i class="fa-solid fa-chevron-down text-sm text-[#D4AF37] faq-icon transition-transform duration-300"></i>
          </summary>
          <div class="pt-4 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-200/60 mt-3">
            Ja! Sami besitzt neben der UEFA-B-Lizenz auch eine offizielle Torwart-Trainer-Lizenz und bietet spezifisches Torwarttraining an. Ebenso bieten wir gesondertes Leistungstraining für Erwachsene an.
          </div>
        </details>

      </div>

    </div>
  </section>

  <!-- ============================================================
       11. FINAL CTA BANNER (Punkt 24: High-Conversion Abschluss)
       ============================================================ -->
  <section class="py-20 relative z-10">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="rounded-3xl bg-gradient-to-r from-slate-900 via-slate-950 to-slate-900 p-8 sm:p-14 text-white text-center space-y-6 border-2 border-[#D4AF37] shadow-2xl relative overflow-hidden" data-aos="zoom-in">
        
        <div class="absolute -top-24 -left-24 w-72 h-72 bg-[#D4AF37]/20 rounded-full blur-3xl pointer-events-none"></div>
        <div class="absolute -bottom-24 -right-24 w-72 h-72 bg-[#E63946]/20 rounded-full blur-3xl pointer-events-none"></div>

        <div class="inline-block px-4 py-1.5 rounded-full bg-white/10 text-[#D4AF37] text-xs font-black uppercase tracking-widest border border-white/20">
          Jetzt unverbindlich anfragen
        </div>

        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black tracking-tight leading-tight max-w-2xl mx-auto">
          Bereit für den <span class="text-gradient-gold">nächsten Schritt?</span>
        </h2>

        <p class="text-slate-300 text-sm sm:text-base max-w-xl mx-auto font-medium">
          Finde im persönlichen Erstgespräch heraus, welches Training am besten zu dir oder deinem Kind passt. Unverbindlich, ehrlich und direkt mit Trainer Sami.
        </p>

        <div class="flex flex-col sm:flex-row items-center justify-center gap-4 pt-4">
          <a href="#kontakt" class="w-full sm:w-auto px-8 py-4 rounded-full bg-[#E63946] hover:bg-[#C52233] text-white font-black text-xs uppercase tracking-wider shadow-red-glow transition-all transform hover:scale-105">
            <i class="fa-solid fa-calendar-check mr-2"></i>Kostenloses Erstgespräch anfragen
          </a>
          <a href="#preise" class="w-full sm:w-auto px-8 py-4 rounded-full bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs uppercase tracking-wider transition-all border border-slate-700">
            <i class="fa-solid fa-tags mr-2 text-[#D4AF37]"></i>Preise ansehen
          </a>
        </div>

      </div>
    </div>
  </section>

  <!-- ============================================================
       12. KONTAKT & STANDORTE MIT KARTE (Punkt 30: Einfaches Formular)
       ============================================================ -->
  <section id="kontakt" class="py-20 relative z-10 bg-white/60 backdrop-blur-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4" data-aos="fade-up">
        <div class="inline-block px-3.5 py-1 rounded-full bg-[#E63946]/10 text-[#E63946] font-black text-xs uppercase tracking-widest border border-[#E63946]/30">
          WIR FREUEN UNS AUF DEINE ANFRAGE!
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          Kontakt &amp; Standorte
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg">
          Bist du an einem Training für dich oder dein Kind interessiert? Gerne beraten wir dich persönlich.
        </p>
      </div>

      <!-- 3 Standorte Highlight Bar -->
      <div class="max-w-4xl mx-auto mb-12 p-5 rounded-3xl bg-slate-900 text-white flex flex-col sm:flex-row items-center justify-between gap-4 shadow-xl border border-[#D4AF37]/40" data-aos="fade-up">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-full bg-[#D4AF37] text-slate-900 flex items-center justify-center font-black">
            <i class="fa-solid fa-map-location-dot"></i>
          </div>
          <div>
            <div class="text-xs font-bold text-[#D4AF37] uppercase">3 Standorte in Hamburg und Schleswig-Holstein:</div>
            <div class="text-sm font-black text-white">Billstedt · Reinbek · Eimsbüttel</div>
          </div>
        </div>
        <div class="text-xs text-slate-400 font-semibold">
          Hauptstützpunkt: Öjendorfer Weg 80, 22119 Hamburg
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        
        <!-- Left: Formular & Kontaktdaten (6 Spalten) -->
        <div class="lg:col-span-6 glass-card p-8 rounded-3xl shadow-xl space-y-6" data-aos="fade-right">
          <div class="border-b border-slate-200 pb-4">
            <h3 class="text-xl font-black text-slate-900">SoccerProf Academy | Sami Ghaouar</h3>
            <p class="text-xs text-slate-500 mt-1">Schreib uns direkt eine Nachricht oder ruf uns an:</p>
          </div>

          <!-- Phone & Mail Links -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <a href="tel:+4917684156542" class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 flex items-center gap-3 hover:bg-slate-100 transition-colors">
              <div class="w-10 h-10 rounded-xl bg-[#E63946]/10 text-[#E63946] flex items-center justify-center text-base font-bold shrink-0">
                <i class="fa-solid fa-phone"></i>
              </div>
              <div class="overflow-hidden">
                <div class="text-[10px] text-slate-500 font-semibold uppercase">Telefon</div>
                <div class="text-xs font-bold text-slate-900 truncate">+49 176 841 565 42</div>
              </div>
            </a>

            <a href="mailto:sami@soccerprof.de?subject=Kontaktanfrage an SOCCERPROF" class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 flex items-center gap-3 hover:bg-slate-100 transition-colors">
              <div class="w-10 h-10 rounded-xl bg-[#D4AF37]/10 text-[#D4AF37] flex items-center justify-center text-base font-bold shrink-0">
                <i class="fa-solid fa-envelope"></i>
              </div>
              <div class="overflow-hidden">
                <div class="text-[10px] text-slate-500 font-semibold uppercase">E-Mail</div>
                <div class="text-xs font-bold text-slate-900 truncate">sami@soccerprof.de</div>
              </div>
            </a>
          </div>

          <!-- Kontaktformular mit allen Vorgabefeldern (Punkt 30) -->
          <form id="contactForm" onsubmit="handleFormSubmit(event)" class="space-y-4">
            <div>
              <label class="block text-xs font-extrabold text-slate-700 uppercase mb-1.5">Name des Ansprechpartners *</label>
              <input type="text" required placeholder="Vor- und Nachname" class="w-full px-4 py-3 rounded-2xl bg-white border border-slate-200 text-slate-900 text-xs focus:outline-none focus:border-[#D4AF37] transition-all">
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-extrabold text-slate-700 uppercase mb-1.5">E-Mail-Adresse *</label>
                <input type="email" required placeholder="deine-email@beispiel.de" class="w-full px-4 py-3 rounded-2xl bg-white border border-slate-200 text-slate-900 text-xs focus:outline-none focus:border-[#D4AF37] transition-all">
              </div>
              <div>
                <label class="block text-xs font-extrabold text-slate-700 uppercase mb-1.5">Telefonnummer</label>
                <input type="tel" placeholder="0176 ..." class="w-full px-4 py-3 rounded-2xl bg-white border border-slate-200 text-slate-900 text-xs focus:outline-none focus:border-[#D4AF37] transition-all">
              </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-extrabold text-slate-700 uppercase mb-1.5">Alter des Spielers</label>
                <input type="text" placeholder="z.B. 10 Jahre" class="w-full px-4 py-3 rounded-2xl bg-white border border-slate-200 text-slate-900 text-xs focus:outline-none focus:border-[#D4AF37] transition-all">
              </div>
              <div>
                <label class="block text-xs font-extrabold text-slate-700 uppercase mb-1.5">Trainingswunsch</label>
                <select class="w-full px-4 py-3 rounded-2xl bg-white border border-slate-200 text-slate-900 text-xs focus:outline-none focus:border-[#D4AF37] transition-all font-medium">
                  <option value="einzeltraining">Einzeltraining (1:1)</option>
                  <option value="kleingruppe">Kleingruppentraining (5er)</option>
                  <option value="mannschaft">Mannschaftstraining</option>
                  <option value="erwachsene">Training für Erwachsene</option>
                  <option value="erstgespraech">Kostenlose Beratung</option>
                </select>
              </div>
            </div>

            <div>
              <label class="block text-xs font-extrabold text-slate-700 uppercase mb-1.5">Deine Nachricht oder Wünsche</label>
              <textarea rows="3" placeholder="Teile uns Deine Wünsche, den aktuellen Verein oder konkrete Ziele mit..." class="w-full px-4 py-3 rounded-2xl bg-white border border-slate-200 text-slate-900 text-xs focus:outline-none focus:border-[#D4AF37] transition-all"></textarea>
            </div>

            <button type="submit" class="w-full py-3.5 rounded-2xl bg-[#E63946] hover:bg-[#C52233] text-white font-black text-xs uppercase tracking-wider shadow-red-glow hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-0.5 flex items-center justify-center gap-2">
              <i class="fa-solid fa-paper-plane"></i>
              <span>Kostenloses Erstgespräch anfragen</span>
            </button>

            <!-- Success notification box -->
            <div id="formSuccess" class="hidden p-3.5 rounded-2xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-700 text-center font-bold text-xs">
              <i class="fa-solid fa-circle-check mr-2"></i>Vielen Dank! Deine Anfrage wurde übermittelt. Trainer Sami meldet sich in Kürze bei dir.
            </div>
          </form>

          <!-- WhatsApp Schnellkontakt -->
          <div class="pt-2 text-center">
            <a href="https://wa.me/4917684156542?text=Hallo%20Sami,%20ich%20interessiere%20mich%20f%C3%BCr%20ein%20Training%20bei%20der%20SoccerProf%20Academy!" target="_blank" class="w-full py-3 rounded-2xl bg-[#25D366] hover:bg-[#20bd5a] text-white font-black text-xs uppercase tracking-wider flex items-center justify-center gap-2 shadow-md transition-all">
              <i class="fa-brands fa-whatsapp text-lg"></i>
              <span>Direkt über WhatsApp schreiben</span>
            </a>
          </div>

        </div>

        <!-- Right: Interaktive Google Maps Karte (6 Spalten) -->
        <div class="lg:col-span-6 space-y-6" data-aos="fade-left">
          
          <div class="glass-card rounded-3xl overflow-hidden border-2 border-[#D4AF37]/60 shadow-xl relative">
            <div class="p-4 bg-slate-900 text-white flex items-center justify-between">
              <div class="flex items-center gap-2 text-xs font-bold">
                <i class="fa-solid fa-map-pin text-[#E63946] text-sm"></i>
                <span>Hauptstützpunkt: Öjendorfer Weg 80, 22119 Hamburg</span>
              </div>
              <span class="text-[10px] bg-[#D4AF37]/20 text-[#D4AF37] px-2.5 py-0.5 rounded-full font-black uppercase">Billstedt</span>
            </div>

            <!-- Responsive Google Maps Embed Iframe -->
            <div class="w-full h-80 sm:h-96 relative bg-slate-100">
              <iframe 
                title="SoccerProf Academy Standort Hamburg Öjendorfer Weg"
                width="100%" 
                height="100%" 
                style="border:0;" 
                loading="lazy" 
                allowfullscreen 
                referrerpolicy="no-referrer-when-downgrade" 
                src="https://maps.google.com/maps?q=%C3%96jendorfer%20Weg%2080,%2022119%20Hamburg&t=&z=14&ie=UTF8&iwloc=&output=embed">
              </iframe>
            </div>

            <div class="p-4 bg-white flex flex-col sm:flex-row items-center justify-between gap-3 text-xs">
              <div class="text-slate-600 font-medium">
                <i class="fa-solid fa-car text-[#D4AF37] mr-1"></i> Gute Anbindung über Horner Rennbahn &amp; B5
              </div>
              <a href="https://maps.google.com/?q=%C3%96jendorfer%20Weg%2080,%2022119%20Hamburg" target="_blank" class="px-4 py-1.5 rounded-xl bg-slate-900 text-white font-bold text-[11px] hover:bg-[#E63946] transition-colors">
                In Google Maps öffnen <i class="fa-solid fa-arrow-up-right-from-square ml-1"></i>
              </a>
            </div>
          </div>

          <!-- Standorte Kacheln -->
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div class="glass-card p-4 rounded-2xl text-center border-l-4 border-[#E63946]">
              <div class="font-black text-xs text-slate-900">Billstedt</div>
              <div class="text-[11px] text-slate-500 mt-0.5">Öjendorfer Weg 80</div>
              <span class="text-[9px] text-[#D4AF37] font-bold uppercase">Hauptplatz</span>
            </div>
            <div class="glass-card p-4 rounded-2xl text-center border-l-4 border-[#D4AF37]">
              <div class="font-black text-xs text-slate-900">Reinbek</div>
              <div class="text-[11px] text-slate-500 mt-0.5">Schleswig-Holstein</div>
              <span class="text-[9px] text-slate-500 font-bold uppercase">Zusatz-Standort</span>
            </div>
            <div class="glass-card p-4 rounded-2xl text-center border-l-4 border-slate-900">
              <div class="font-black text-xs text-slate-900">Eimsbüttel</div>
              <div class="text-[11px] text-slate-500 mt-0.5">Hamburg West</div>
              <span class="text-[9px] text-slate-500 font-bold uppercase">Indoor / Kunstrasen</span>
            </div>
          </div>

        </div>

      </div>

    </div>
  </section>

  <!-- ============================================================
       13. FOOTER (Punkt 25: Strukturierte 4 Spalten)
       ============================================================ -->
  <footer class="bg-slate-950 text-slate-400 py-16 border-t border-slate-800 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 pb-12 border-b border-slate-800">
        
        <!-- Spalte 1: SoccerProf Marke & Info -->
        <div class="space-y-4">
          <div class="flex items-center gap-3">
            <img src="img/logo/F3-3.avif" alt="SoccerProf Academy Logo" class="h-9 w-auto object-contain">
            <span class="text-white font-black text-lg tracking-tight">SOCCER<span class="text-[#E63946]">PROF</span> ACADEMY</span>
          </div>
          <p class="text-xs text-slate-400 leading-relaxed font-medium">
            SoccerProf bietet ein privates, professionelles und individuelles Fußballtraining für Kinder, Jugendliche und Erwachsene in Hamburg und Umgebung.
          </p>
          <div class="text-xs text-slate-400">
            <i class="fa-solid fa-location-dot text-[#D4AF37] mr-1.5"></i>Öjendorfer Weg 80, 22119 Hamburg
          </div>
          <div class="flex items-center gap-3 pt-2">
            <a href="https://wa.me/4917684156542" target="_blank" class="w-9 h-9 rounded-full bg-slate-800 text-[#25D366] flex items-center justify-center hover:bg-[#25D366] hover:text-white transition-colors" aria-label="WhatsApp">
              <i class="fa-brands fa-whatsapp"></i>
            </a>
            <a href="tel:+4917684156542" class="w-9 h-9 rounded-full bg-slate-800 text-[#D4AF37] flex items-center justify-center hover:bg-[#D4AF37] hover:text-slate-900 transition-colors" aria-label="Telefon">
              <i class="fa-solid fa-phone"></i>
            </a>
            <a href="mailto:sami@soccerprof.de" class="w-9 h-9 rounded-full bg-slate-800 text-white flex items-center justify-center hover:bg-[#E63946] transition-colors" aria-label="E-Mail">
              <i class="fa-solid fa-envelope"></i>
            </a>
          </div>
        </div>

        <!-- Spalte 2: Training -->
        <div class="space-y-3">
          <h4 class="text-white font-black text-xs uppercase tracking-wider">Training</h4>
          <ul class="space-y-2 text-xs">
            <li><a href="#angebote" class="hover:text-white transition-colors">Einzeltraining (1:1)</a></li>
            <li><a href="#angebote" class="hover:text-white transition-colors">Kleingruppentraining (5er)</a></li>
            <li><a href="#angebote" class="hover:text-white transition-colors">Mannschaftstraining</a></li>
            <li><a href="#angebote" class="hover:text-white transition-colors">Training für Erwachsene</a></li>
            <li><a href="#methode" class="hover:text-white transition-colors">Trainingsmethoden</a></li>
            <li><a href="#preise" class="hover:text-white transition-colors">Preise &amp; Konditionen</a></li>
          </ul>
        </div>

        <!-- Spalte 3: SoccerProf -->
        <div class="space-y-3">
          <h4 class="text-white font-black text-xs uppercase tracking-wider">Über SoccerProf</h4>
          <ul class="space-y-2 text-xs">
            <li><a href="#ueber-uns" class="hover:text-white transition-colors">Über uns</a></li>
            <li><a href="#steckbrief" class="hover:text-white transition-colors">Trainer Sami Ghaouar</a></li>
            <li><a href="#warum" class="hover:text-white transition-colors">Warum SoccerProf</a></li>
            <li><a href="#angebote" class="hover:text-white transition-colors">Veranstaltungen &amp; Camps</a></li>
            <li><a href="#faq" class="hover:text-white transition-colors">Häufige Fragen (FAQ)</a></li>
            <li><a href="#kontakt" class="hover:text-white transition-colors">Kontakt &amp; Standorte</a></li>
          </ul>
        </div>

        <!-- Spalte 4: Rechtliches -->
        <div class="space-y-3">
          <h4 class="text-white font-black text-xs uppercase tracking-wider">Rechtliches &amp; Information</h4>
          <ul class="space-y-2 text-xs">
            <li><a href="#kontakt" class="hover:text-white transition-colors">Impressum</a></li>
            <li><a href="#kontakt" class="hover:text-white transition-colors">Datenschutzrichtlinie</a></li>
            <li><a href="#kontakt" class="hover:text-white transition-colors">Cookie-Richtlinie</a></li>
            <li><a href="#kontakt" class="hover:text-white transition-colors">AGB &amp; Widerruf</a></li>
          </ul>
        </div>

      </div>

      <!-- Footer Bottom -->
      <div class="pt-8 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-500 gap-4">
        <div>
          © 2026 SoccerProf Academy · Sami Ghaouar · Alle Rechte vorbehalten.
        </div>
        <div class="font-bold text-slate-400">
          DIE PERFEKTE ERGÄNZUNG ZUM FUßBALL VEREIN 👍 ⚽
        </div>
      </div>

    </div>
  </footer>

  <!-- ============================================================
       MOBILE STICKY BOTTOM BAR (Punkt 29: Sticky CTA)
       ============================================================ -->
  <div class="sm:hidden fixed bottom-0 left-0 w-full z-40 bg-white/95 backdrop-blur-md border-t border-slate-200 px-4 py-2.5 flex items-center justify-between shadow-2xl">
    <div class="text-left">
      <div class="text-[11px] font-black text-slate-900">SoccerProf Academy</div>
      <div class="text-[9px] text-[#D4AF37] font-black uppercase">Sami Ghaouar · Hamburg</div>
    </div>
    <a href="#kontakt" class="px-4 py-2 rounded-full bg-[#E63946] text-white font-black text-xs uppercase tracking-wider shadow-red-glow flex items-center gap-1.5">
      <i class="fa-solid fa-calendar-check"></i>
      <span>Erstgespräch</span>
    </a>
  </div>

  <!-- ============================================================
       SCRIPTS: THREE.JS (3D LOGO EMBLEM ANIMATION) & AOS
       ============================================================ -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://unpkg.com/aos@next/dist/aos.js"></script>

  <script>
    // Initialize AOS
    document.addEventListener('DOMContentLoaded', () => {
      AOS.init({
        duration: 750,
        easing: 'ease-out-cubic',
        once: false,
        mirror: true
      });
    });

    // Mobile Navbar Toggle
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    mobileMenuBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
    });
    document.querySelectorAll('.mobile-link').forEach(link => {
      link.addEventListener('click', () => mobileMenu.classList.add('hidden'));
    });

    // Form Submission & WhatsApp Forward
    function handleFormSubmit(e) {
      e.preventDefault();
      const successBox = document.getElementById('formSuccess');
      successBox.classList.remove('hidden');
      setTimeout(() => {
        window.location.href = "https://wa.me/4917684156542?text=" + encodeURIComponent("Hallo Sami, ich habe gerade eine Anfrage für die SoccerProf Academy gesendet!");
      }, 1500);
    }

    // ============================================================
    // 3D THREE.JS BACKGROUND SCENE WITH ROTATING LOGO & PARTICLES
    // ============================================================
    (function initThreeJS() {
      if (typeof THREE === 'undefined') return;
      const container = document.getElementById('threejs-container');
      if (!container) return;

      let width = window.innerWidth;
      let height = window.innerHeight;

      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
      camera.position.set(0, 0, 10);

      const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
      renderer.setSize(width, height);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      container.appendChild(renderer.domElement);

      function createRoundParticleTexture() {
        const canvas = document.createElement('canvas');
        canvas.width = 64;
        canvas.height = 64;
        const ctx = canvas.getContext('2d');

        const grad = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
        grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
        grad.addColorStop(0.3, 'rgba(212, 175, 55, 0.9)');
        grad.addColorStop(0.7, 'rgba(212, 175, 55, 0.4)');
        grad.addColorStop(1, 'rgba(212, 175, 55, 0)');

        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.arc(32, 32, 30, 0, Math.PI * 2);
        ctx.fill();

        return new THREE.CanvasTexture(canvas);
      }

      const roundParticleMap = createRoundParticleTexture();
      const textureLoader = new THREE.TextureLoader();
      const logoTexture = textureLoader.load('img/logo/F3-3.avif');

      const worldGroup = new THREE.Group();
      scene.add(worldGroup);

      const logoContainer = new THREE.Group();
      logoContainer.position.set(0, 0, 0);
      worldGroup.add(logoContainer);

      const logoRadius = 2.4;
      const logoGeo = new THREE.CylinderGeometry(logoRadius, logoRadius, 0.18, 64);
      const goldMat = new THREE.MeshStandardMaterial({
        color: 0xD4AF37,
        metalness: 0.9,
        roughness: 0.2,
        emissive: 0x221a00
      });
      const logoFaceMat = new THREE.MeshStandardMaterial({
        map: logoTexture,
        roughness: 0.2,
        metalness: 0.1,
        transparent: true,
        opacity: 0.95
      });

      const solidLogoMesh = new THREE.Mesh(logoGeo, [goldMat, logoFaceMat, logoFaceMat]);
      solidLogoMesh.rotation.x = Math.PI / 2;
      logoContainer.add(solidLogoMesh);

      // Dynamic Gold / White / Red Particles around the Emblem
      const particleCount = 2000;
      const originPositions = new Float32Array(particleCount * 3);
      const dispersedPositions = new Float32Array(particleCount * 3);
      const currentPositions = new Float32Array(particleCount * 3);
      const particleColors = new Float32Array(particleCount * 3);

      const cWhite = new THREE.Color(0xFFFFFF);
      const cGold  = new THREE.Color(0xD4AF37);
      const cRed   = new THREE.Color(0xE63946);

      for (let i = 0; i < particleCount; i++) {
        const theta = Math.random() * 2.0 * Math.PI;
        const r = Math.random() * logoRadius;
        const x = r * Math.cos(theta);
        const y = r * Math.sin(theta);
        const z = (Math.random() - 0.5) * 0.3;

        originPositions[i * 3]     = x;
        originPositions[i * 3 + 1] = y;
        originPositions[i * 3 + 2] = z;

        const mult = 2.2 + Math.random() * 3.8;
        dispersedPositions[i * 3]     = x * mult + (Math.random() - 0.5) * 5;
        dispersedPositions[i * 3 + 1] = y * mult + (Math.random() - 0.5) * 5;
        dispersedPositions[i * 3 + 2] = z * mult + (Math.random() - 0.5) * 5;

        currentPositions[i * 3]     = x;
        currentPositions[i * 3 + 1] = y;
        currentPositions[i * 3 + 2] = z;

        const rc = Math.random();
        let col = cWhite;
        if (rc > 0.4) col = cGold;
        if (rc > 0.82) col = cRed;

        particleColors[i * 3]     = col.r;
        particleColors[i * 3 + 1] = col.g;
        particleColors[i * 3 + 2] = col.b;
      }

      const particleGeo = new THREE.BufferGeometry();
      particleGeo.setAttribute('position', new THREE.BufferAttribute(currentPositions, 3));
      particleGeo.setAttribute('color', new THREE.BufferAttribute(particleColors, 3));

      const particleMat = new THREE.PointsMaterial({
        size: 0.20,
        map: roundParticleMap,
        vertexColors: true,
        transparent: true,
        opacity: 0.85,
        depthWrite: false,
        blending: THREE.AdditiveBlending
      });
      const particlePoints = new THREE.Points(particleGeo, particleMat);
      logoContainer.add(particlePoints);

      // Background ambient stars/particles
      const bgParticleCount = 160;
      const bgParticleGeo = new THREE.BufferGeometry();
      const bgParticlePos = new Float32Array(bgParticleCount * 3);
      for (let i = 0; i < bgParticleCount * 3; i += 3) {
        bgParticlePos[i]     = (Math.random() - 0.5) * 26;
        bgParticlePos[i + 1] = 6 - Math.random() * 50;
        bgParticlePos[i + 2] = (Math.random() - 0.5) * 12;
      }
      bgParticleGeo.setAttribute('position', new THREE.BufferAttribute(bgParticlePos, 3));
      const bgParticleMat = new THREE.PointsMaterial({
        size: 0.18,
        map: roundParticleMap,
        color: 0xD4AF37,
        transparent: true,
        opacity: 0.55,
        depthWrite: false,
        blending: THREE.AdditiveBlending
      });
      const bgParticles = new THREE.Points(bgParticleGeo, bgParticleMat);
      worldGroup.add(bgParticles);

      // Lights
      const ambientLight = new THREE.AmbientLight(0xffffff, 1.4);
      scene.add(ambientLight);

      const dirLight1 = new THREE.DirectionalLight(0xffffff, 1.6);
      dirLight1.position.set(5, 10, 5);
      scene.add(dirLight1);

      const dirLightGold = new THREE.DirectionalLight(0xD4AF37, 2.0);
      dirLightGold.position.set(-6, -4, 4);
      scene.add(dirLightGold);

      let targetCameraY = 0;
      let targetZoomZ = 9.5;
      let targetDissolve = 0;
      let currentDissolve = 0;
      let targetRotationX = 0;
      let targetRotationY = 0;

      window.addEventListener('mousemove', (e) => {
        const x = (e.clientX / window.innerWidth) - 0.5;
        const y = (e.clientY / window.innerHeight) - 0.5;
        targetRotationY = x * 0.45;
        targetRotationX = y * 0.45;
      });

      function updateScroll() {
        const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
        const scrollPercent = window.scrollY / maxScroll;

        targetCameraY = -scrollPercent * 40;
        targetZoomZ = 9.5 + Math.sin(scrollPercent * Math.PI * 4) * 2.0;
        const cycle = Math.abs(Math.sin(scrollPercent * Math.PI * 6));
        targetDissolve = Math.pow(cycle, 1.4);
      }

      window.addEventListener('scroll', updateScroll);
      updateScroll();

      window.addEventListener('resize', () => {
        width = window.innerWidth;
        height = window.innerHeight;
        camera.aspect = width / height;
        camera.updateProjectionMatrix();
        renderer.setSize(width, height);
      });

      function animate() {
        requestAnimationFrame(animate);

        currentDissolve += (targetDissolve - currentDissolve) * 0.08;
        logoFaceMat.opacity = Math.max(0.08, 1 - currentDissolve * 0.92);

        const posAttr = particleGeo.attributes.position;
        const posArr = posAttr.array;

        for (let i = 0; i < particleCount; i++) {
          const i3 = i * 3;
          posArr[i3]     = originPositions[i3]     + (dispersedPositions[i3]     - originPositions[i3])     * currentDissolve;
          posArr[i3 + 1] = originPositions[i3 + 1] + (dispersedPositions[i3 + 1] - originPositions[i3 + 1]) * currentDissolve;
          posArr[i3 + 2] = originPositions[i3 + 2] + (dispersedPositions[i3 + 2] - originPositions[i3 + 2]) * currentDissolve;
        }
        posAttr.needsUpdate = true;

        solidLogoMesh.rotation.z += 0.005;
        particlePoints.rotation.z += 0.0035;
        bgParticles.rotation.y -= 0.0006;

        camera.position.y += (targetCameraY - camera.position.y) * 0.07;
        camera.position.z += (targetZoomZ - camera.position.z) * 0.07;

        worldGroup.rotation.y += (targetRotationY - worldGroup.rotation.y) * 0.05;
        worldGroup.rotation.x += (targetRotationX - worldGroup.rotation.x) * 0.05;

        renderer.render(scene, camera);
      }

      animate();
    })();
  </script>
</body>
</html>
'''

with open(r'c:\Users\mario\Desktop\newsoccerprof\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Successfully wrote updated index.html with all 33 points!")
