import os

html_code = """<!DOCTYPE html>
<html lang="de" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SoccerProf Academy | Individuelles Fußballtraining Hamburg – Sami Ghaouar</title>
  <meta name="description" content="SoccerProf Academy Hamburg: Individuelles Fußballtraining für Kinder, Jugendliche und ambitionierte Spieler auf DFB- & UEFA-B-Niveau. Ergänzung zum Vereinstraining. Kostenloses Erstgespräch anfragen!">
  <meta name="keywords" content="Fußballtraining Hamburg, individuelles Fußballtraining Hamburg, Fußballtrainer Hamburg, Einzeltraining Fußball Hamburg, Fußballtraining Kinder Hamburg, privater Fußballtrainer Hamburg, SoccerProf Academy, Sami Ghaouar">

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
              bgLight: '#F8FAFC',
            }
          },
          boxShadow: {
            'gold-glow': '0 0 25px rgba(212, 175, 55, 0.35)',
            'red-glow': '0 0 25px rgba(230, 57, 70, 0.45)',
            'glass': '0 8px 32px 0 rgba(15, 23, 42, 0.08)',
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
        radial-gradient(at 10% 20%, rgba(212, 175, 55, 0.06) 0px, transparent 50%),
        radial-gradient(at 90% 10%, rgba(230, 57, 70, 0.06) 0px, transparent 50%),
        radial-gradient(at 50% 80%, rgba(15, 23, 42, 0.03) 0px, transparent 50%),
        radial-gradient(circle at 50% 50%, rgba(248, 250, 252, 0.85) 0%, #F8FAFC 100%);
    }
    .grid-pattern {
      background-size: 40px 40px;
      background-image: 
        linear-gradient(to right, rgba(15, 23, 42, 0.03) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(15, 23, 42, 0.03) 1px, transparent 1px);
    }
    .glass-card {
      background: rgba(255, 255, 255, 0.88);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(226, 232, 240, 0.9);
      transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .glass-card:hover {
      border-color: #D4AF37;
      box-shadow: 0 15px 35px -5px rgba(212, 175, 55, 0.25), 0 0 15px rgba(212, 175, 55, 0.2);
    }
    .glass-nav {
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1px solid rgba(226, 232, 240, 0.8);
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
  </style>
</head>
<body class="bg-mesh relative grid-pattern antialiased text-slate-900 pb-16 sm:pb-0">

  <!-- 3D THREE.JS CANVAS BACKGROUND (CENTERED LOGO EMBLEM) -->
  <div id="threejs-container" class="fixed inset-0 w-full h-full pointer-events-none z-0"></div>

  <!-- Ambient Glow Orbs -->
  <div class="fixed top-20 left-10 w-96 h-96 bg-[#D4AF37]/10 rounded-full blur-3xl pointer-events-none -z-10 animate-float"></div>
  <div class="fixed bottom-20 right-10 w-[30rem] h-[30rem] bg-[#E63946]/10 rounded-full blur-3xl pointer-events-none -z-10"></div>

  <!-- NAVIGATION HEADER (Reduziert auf Kernpunkte) -->
  <header class="fixed top-0 left-0 w-full z-50 glass-nav transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      
      <!-- Logo führt zur Startseite -->
      <a href="#hero" class="flex items-center gap-3 group">
        <img src="img/logo/F3-3.avif" alt="SoccerProf Academy Logo" class="h-12 sm:h-14 w-auto object-contain group-hover:scale-105 transition-transform drop-shadow-sm">
      </a>

      <!-- Desktop Nav Links: Logo | Training | Trainingsmethode | Über uns | Preise | Kontakt -->
      <nav class="hidden md:flex items-center gap-8 text-sm font-semibold text-slate-700">
        <a href="#training" class="hover:text-[#E63946] transition-colors">Training</a>
        <a href="#methode" class="hover:text-[#E63946] transition-colors">Trainingsmethode</a>
        <a href="#ueber-uns" class="hover:text-[#E63946] transition-colors">Über uns</a>
        <a href="#preise" class="hover:text-[#E63946] transition-colors">Preise</a>
        <a href="#kontakt" class="hover:text-[#E63946] transition-colors">Kontakt</a>
      </nav>

      <!-- Header Primary CTA (Rechts auffälliger Button) -->
      <div class="hidden md:flex items-center gap-4">
        <a href="#erstgespraech" class="px-5 py-2.5 rounded-full bg-[#E63946] hover:bg-[#C52233] text-white font-bold text-sm shadow-red-glow hover:shadow-lg transition-all duration-300 transform hover:-translate-y-0.5">
          <i class="fa-solid fa-comments mr-2"></i>Kostenloses Erstgespräch
        </a>
      </div>

      <!-- Mobile Menu Toggle Button -->
      <button id="mobileMenuBtn" class="md:hidden text-slate-800 text-2xl focus:outline-none p-2" aria-label="Menu">
        <i class="fa-solid fa-bars"></i>
      </button>
    </div>

    <!-- Mobile Dropdown Navigation -->
    <div id="mobileMenu" class="hidden md:hidden bg-white/95 backdrop-blur-lg border-b border-slate-200 px-6 py-6 space-y-4 shadow-xl">
      <a href="#training" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Training</a>
      <a href="#methode" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Trainingsmethode</a>
      <a href="#ueber-uns" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Über uns</a>
      <a href="#preise" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Preise</a>
      <a href="#kontakt" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Kontakt</a>
      <a href="#erstgespraech" class="block w-full text-center py-3 rounded-full bg-[#E63946] text-white font-bold shadow-md mobile-link">
        Kostenloses Erstgespräch
      </a>
    </div>
  </header>

  <!-- 01 — HERO (Entscheidet innerhalb von 5 Sekunden) -->
  <section id="hero" class="relative pt-36 pb-20 md:pt-44 md:pb-28 overflow-hidden min-h-[90vh] flex items-center z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <!-- Left Hero Content -->
        <div class="lg:col-span-7 space-y-8 text-center lg:text-left">
          
          <!-- Badge: SEO & Location -->
          <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/90 border border-[#D4AF37] shadow-md backdrop-blur-md">
            <span class="w-2.5 h-2.5 rounded-full bg-[#D4AF37] animate-ping"></span>
            <span class="text-xs sm:text-sm font-extrabold tracking-wider text-slate-900 uppercase">
              INDIVIDUELLES FUßBALLTRAINING IN HAMBURG
            </span>
          </div>

          <!-- Headline (Favorit: Mehr Technik. Mehr Selbstvertrauen. Mehr Spiel.) -->
          <h1 class="text-4xl sm:text-5xl lg:text-6xl font-black text-slate-900 tracking-tight leading-[1.1]">
            Mehr Technik. <br class="hidden sm:inline" />
            <span class="text-gradient-gold">Mehr Selbstvertrauen.</span> <br />
            <span class="relative inline-block text-slate-900">
              Mehr Spiel.
              <svg class="absolute -bottom-2 left-0 w-full h-3 text-[#E63946]" viewBox="0 0 200 9" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M2 7C50 2 150 2 198 7" stroke="currentColor" stroke-width="4" stroke-linecap="round"/></svg>
            </span>
          </h1>

          <!-- Subheadline & Zusatz -->
          <div class="space-y-3">
            <p class="text-lg sm:text-xl text-slate-800 font-bold leading-relaxed bg-white/80 p-4 rounded-2xl backdrop-blur-md border border-slate-200/80 shadow-sm">
              Individuelles Fußballtraining für Kinder und Jugendliche – abgestimmt auf die Stärken, Ziele und Entwicklung jedes Spielers.
            </p>
            <p class="text-sm sm:text-base text-slate-600 font-medium">
              Einzeltraining &amp; Kleingruppen mit professioneller Betreuung – als perfekte Ergänzung zum Vereinstraining.
            </p>
          </div>

          <!-- Primary & Secondary CTAs -->
          <div class="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4 pt-2">
            <a href="#erstgespraech" class="w-full sm:w-auto px-8 py-4 rounded-full bg-[#E63946] hover:bg-[#C52233] text-white font-black text-base tracking-wide shadow-red-glow hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-1 flex items-center justify-center gap-3">
              <span>Kostenloses Erstgespräch</span>
              <i class="fa-solid fa-arrow-right"></i>
            </a>
            <a href="#training" class="w-full sm:w-auto px-8 py-4 rounded-full bg-white/90 hover:bg-slate-900 text-slate-900 hover:text-white border-2 border-slate-900 font-bold text-base transition-all duration-300 transform hover:-translate-y-1 shadow-sm flex items-center justify-center gap-2">
              <span>Training entdecken</span>
              <i class="fa-solid fa-chevron-down text-xs"></i>
            </a>
          </div>

          <!-- Checkmarks unter den Buttons -->
          <div class="flex flex-wrap items-center justify-center lg:justify-start gap-x-6 gap-y-2 text-xs font-bold text-slate-700 pt-2">
            <span class="flex items-center gap-1.5"><i class="fa-solid fa-circle-check text-[#D4AF37]"></i> Individuelles Training</span>
            <span class="flex items-center gap-1.5"><i class="fa-solid fa-circle-check text-[#D4AF37]"></i> Anfänger bis ambitionierte Spieler</span>
            <span class="flex items-center gap-1.5"><i class="fa-solid fa-circle-check text-[#D4AF37]"></i> Kleine Gruppen</span>
            <span class="flex items-center gap-1.5"><i class="fa-solid fa-circle-check text-[#D4AF37]"></i> Persönliche Entwicklung</span>
          </div>

        </div>

        <!-- Right Hero Visual (Authentisches Trainingsfoto) -->
        <div class="lg:col-span-5" data-aos="fade-left">
          <div class="relative rounded-3xl overflow-hidden border-2 border-[#D4AF37]/50 shadow-2xl bg-slate-900 group">
            <div class="w-full h-[420px] sm:h-[500px] overflow-hidden relative">
              <img src="img/packete/soccerprof-hamburg-kinder-jugendliche-fussballtraining.avif" alt="Individuelles Fußballtraining Kinder Jugendliche Hamburg" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent"></div>
              <div class="absolute bottom-6 left-6 right-6 p-4 rounded-2xl bg-white/90 backdrop-blur-md border border-slate-200 shadow-lg">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-full bg-[#E63946] text-white flex items-center justify-center font-black">
                    <i class="fa-solid fa-futbol"></i>
                  </div>
                  <div>
                    <div class="text-xs font-bold text-slate-900">SoccerProf Academy Hamburg</div>
                    <div class="text-[11px] text-slate-500 font-medium">Head Coach Sami Ghaouar · UEFA-B-Lizenz</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- 02 — VERTRAUEN / TRUST-LEISTE (Nimmt Eltern sofort die Unsicherheit) -->
  <section class="py-10 bg-white/80 border-y border-slate-200/80 backdrop-blur-md relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-6">
        <p class="text-xs uppercase tracking-widest font-black text-slate-500">
          Bereits von zahlreichen Spielern und Eltern in Hamburg vertraut
        </p>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
        
        <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/60 shadow-sm">
          <div class="flex items-center justify-center gap-1 text-[#D4AF37] text-sm mb-1">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </div>
          <div class="text-lg font-black text-slate-900">5,0 / 5 Bewertung</div>
          <div class="text-xs text-slate-500 font-semibold">Eltern- &amp; Spielerstimmen</div>
        </div>

        <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/60 shadow-sm">
          <div class="text-2xl font-black text-[#D4AF37]">UEFA-B</div>
          <div class="text-xs text-slate-900 font-black uppercase">Trainer-Lizenz</div>
          <div class="text-xs text-slate-500 font-semibold">Sami Ghaouar (DFB Standard)</div>
        </div>

        <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/60 shadow-sm">
          <div class="text-2xl font-black text-[#E63946]">Seit 2012</div>
          <div class="text-xs text-slate-900 font-black uppercase">Trainererfahrung</div>
          <div class="text-xs text-slate-500 font-semibold">Individual- &amp; Teamcoaching</div>
        </div>

        <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/60 shadow-sm">
          <div class="text-2xl font-black text-slate-900">Hamburg</div>
          <div class="text-xs text-slate-900 font-black uppercase">Stützpunkt</div>
          <div class="text-xs text-slate-500 font-semibold">Öjendorfer Weg 80 &amp; Hallen</div>
        </div>

      </div>
    </div>
  </section>

  <!-- 03 — DAS PROBLEM DER ELTERN (Psychologisch fundiert) -->
  <section id="problem" class="py-24 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <div class="inline-block px-3 py-1 rounded-full bg-[#E63946]/10 text-[#E63946] font-extrabold text-xs uppercase tracking-widest border border-[#E63946]/30">
          Der Haken im Vereinsalltag
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          Im Mannschaftstraining ist nicht immer Zeit für jeden Spieler.
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg leading-relaxed">
          Ein Vereinstrainer muss gleichzeitig 15 bis 20 Spieler betreuen und das Kollektiv vorbereiten. Dadurch bleibt für individuelle Korrekturen, gezielte Wiederholungen und persönliche Entwicklung oft nur wenig Zeit. Genau hier setzt SoccerProf an.
        </p>
      </div>

      <!-- 3 Core Solution Points -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <div class="glass-card p-8 rounded-3xl space-y-4 hover:border-[#D4AF37]" data-aos="fade-right">
          <div class="w-12 h-12 rounded-2xl bg-slate-900 text-[#D4AF37] flex items-center justify-center text-xl font-bold">
            <i class="fa-solid fa-bullseye"></i>
          </div>
          <h3 class="text-xl font-extrabold text-slate-900">Technik gezielt verbessern</h3>
          <p class="text-slate-600 text-sm leading-relaxed">
            Dribbling, Ballkontrolle, Passspiel, erster Kontakt und gezielter Torabschluss. Wiederholungszahlen und Intensität, die im Mannschaftstraining schlicht nicht möglich sind.
          </p>
        </div>

        <div class="glass-card p-8 rounded-3xl space-y-4 hover:border-[#E63946]" data-aos="fade-up">
          <div class="w-12 h-12 rounded-2xl bg-[#E63946] text-white flex items-center justify-center text-xl font-bold shadow-red-glow">
            <i class="fa-solid fa-sliders"></i>
          </div>
          <h3 class="text-xl font-extrabold text-slate-900">Individuelle Schwächen bearbeiten</h3>
          <p class="text-slate-600 text-sm leading-relaxed">
            Das Training orientiert sich am aktuellen Leistungsstand und den persönlichen Zielen des Spielers. Schwächen am schwachen Fuß oder Stellungsspiel werden systematisch behoben.
          </p>
        </div>

        <div class="glass-card p-8 rounded-3xl space-y-4 hover:border-[#D4AF37]" data-aos="fade-left">
          <div class="w-12 h-12 rounded-2xl bg-slate-900 text-[#D4AF37] flex items-center justify-center text-xl font-bold">
            <i class="fa-solid fa-brain"></i>
          </div>
          <h3 class="text-xl font-extrabold text-slate-900">Selbstvertrauen entwickeln</h3>
          <p class="text-slate-600 text-sm leading-relaxed">
            Bessere Fähigkeiten führen nicht nur zu besseren Aktionen auf dem Platz – sondern vor allem zu spürbar mehr Mut, Entscheidungsfreude und Spaß am Fußballspiel.
          </p>
        </div>

      </div>

    </div>
  </section>

  <!-- 04 & 05 — TRAININGSANGEBOTE (Einzeltraining als Hauptfokus) -->
  <section id="training" class="py-24 bg-white/70 backdrop-blur-md relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <div class="inline-block px-3 py-1 rounded-full bg-[#D4AF37]/10 text-[#D4AF37] font-extrabold text-xs uppercase tracking-widest border border-[#D4AF37]/30">
          Unser Trainings-Setup
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          Das Training, das zu deinem Spieler passt.
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg">
          Vom intensiven 1-zu-1 Feinschliff bis zur dynamischen 5er-Gruppe in Hamburg.
        </p>
      </div>

      <!-- 3 Angebote-Karten mit Einzeltraining prominent im Fokus -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 items-stretch mb-16">
        
        <!-- Karte 1: Einzeltraining (Hauptangebot - 100% Fokus) -->
        <div class="glass-card p-6 sm:p-8 rounded-3xl flex flex-col justify-between group hover:-translate-y-2 transition-all duration-300 border-2 border-[#D4AF37] shadow-gold-glow bg-white/95 relative" data-aos="fade-right">
          <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-[#D4AF37] text-slate-900 font-black text-xs uppercase px-4 py-1.5 rounded-full shadow-md z-20">
            ★ Höchste Intensität
          </div>
          <div>
            <div class="w-full h-48 rounded-2xl overflow-hidden mb-6 shadow-md border border-slate-200/80 relative">
              <img src="img/packete/soccerprof-hamburg-kinder-jugendliche-fussballtraining.avif" alt="Einzeltraining Fußball Hamburg 1:1" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <span class="absolute top-3 right-3 px-3 py-1 rounded-full text-xs font-black uppercase bg-slate-900/90 text-[#D4AF37]">
                1 Spieler · 100 % Fokus
              </span>
            </div>

            <h3 class="text-2xl font-black text-slate-900 mb-2">Einzeltraining</h3>
            <p class="text-slate-500 text-xs uppercase font-extrabold tracking-wider mb-3 text-[#D4AF37]">1 Spieler · 100 % Fokus</p>
            <p class="text-slate-600 text-sm mb-6">
              Für Spieler, die gezielt und intensiv an ihrer individuellen Entwicklung arbeiten möchten. Jede Übung und Minute gehört voll und ganz einem Spieler.
            </p>

            <ul class="space-y-3 mb-8 text-sm text-slate-700">
              <li class="flex items-start gap-2.5"><i class="fa-solid fa-circle-check text-[#D4AF37] mt-1 shrink-0"></i> Exklusive 1:1 Trainer-Aufmerksamkeit</li>
              <li class="flex items-start gap-2.5"><i class="fa-solid fa-circle-check text-[#D4AF37] mt-1 shrink-0"></i> Hohe Wiederholungszahl bei Ballannahme &amp; Abschluss</li>
              <li class="flex items-start gap-2.5"><i class="fa-solid fa-circle-check text-[#D4AF37] mt-1 shrink-0"></i> Detaillierte Bewegungs- &amp; Videoanalyse</li>
            </ul>
          </div>

          <a href="#erstgespraech" class="w-full py-4 rounded-2xl bg-[#E63946] hover:bg-[#C52233] text-white font-extrabold text-sm block text-center transition-all duration-300 shadow-red-glow">
            Einzeltraining anfragen
          </a>
        </div>

        <!-- Karte 2: Kleingruppentraining (2-5 Spieler) -->
        <div class="glass-card p-6 sm:p-8 rounded-3xl flex flex-col justify-between group hover:-translate-y-2 transition-all duration-300" data-aos="zoom-in">
          <div>
            <div class="w-full h-48 rounded-2xl overflow-hidden mb-6 shadow-md border border-slate-200/80 relative">
              <img src="img/packete/kleingruppe.avif" alt="Kleingruppentraining Fußball Hamburg" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <span class="absolute top-3 right-3 px-3 py-1 rounded-full text-xs font-black uppercase bg-slate-900/90 text-[#D4AF37]">
                2–5 Spieler
              </span>
            </div>

            <h3 class="text-2xl font-black text-slate-900 mb-2">Kleingruppentraining</h3>
            <p class="text-slate-500 text-xs uppercase font-extrabold tracking-wider mb-3 text-slate-600">2–5 Spieler · Gemeinsam besser werden</p>
            <p class="text-slate-600 text-sm mb-6">
              Ideal für Freunde, Geschwister oder kleine leistungsgerechte Gruppen. Wettkampfdynamik bei gleichzeitig hoher individueller Betreuung.
            </p>

            <ul class="space-y-3 mb-8 text-sm text-slate-700">
              <li class="flex items-start gap-2.5"><i class="fa-solid fa-circle-check text-[#D4AF37] mt-1 shrink-0"></i> Reale 1v1 &amp; 2v2 Spielsituationen</li>
              <li class="flex items-start gap-2.5"><i class="fa-solid fa-circle-check text-[#D4AF37] mt-1 shrink-0"></i> Passschärfe &amp; Umschaltspiel</li>
              <li class="flex items-start gap-2.5"><i class="fa-solid fa-circle-check text-[#D4AF37] mt-1 shrink-0"></i> Maximal 5 Spieler pro Trainer</li>
            </ul>
          </div>

          <a href="#erstgespraech" class="w-full py-4 rounded-2xl bg-slate-900 hover:bg-[#D4AF37] text-white hover:text-slate-900 font-extrabold text-sm block text-center transition-all duration-300 shadow-md">
            Kleingruppe anfragen
          </a>
        </div>

        <!-- Karte 3: Spezial- & Mannschaftstraining -->
        <div class="glass-card p-6 sm:p-8 rounded-3xl flex flex-col justify-between group hover:-translate-y-2 transition-all duration-300" data-aos="fade-left">
          <div>
            <div class="w-full h-48 rounded-2xl overflow-hidden mb-6 shadow-md border border-slate-200/80 relative">
              <img src="img/packete/Fu%C3%9Fballspieler%20auf%20Bank.avif" alt="Spezialtraining und Mannschaftstraining" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <span class="absolute top-3 right-3 px-3 py-1 rounded-full text-xs font-black uppercase bg-slate-900/90 text-[#D4AF37]">
                Spezial &amp; Teams
              </span>
            </div>

            <h3 class="text-2xl font-black text-slate-900 mb-2">Spezial- &amp; Teamtraining</h3>
            <p class="text-slate-500 text-xs uppercase font-extrabold tracking-wider mb-3 text-slate-600">Gezielte Schwerpunkte &amp; Klubs</p>
            <p class="text-slate-600 text-sm mb-6">
              Spezifische Einheiten für Torabschluss, 1-gegen-1 Offensive/Defensive, Kognition, Sichtungsvorbereitung oder Vor-Ort-Vereinscoaching.
            </p>

            <ul class="space-y-3 mb-8 text-sm text-slate-700">
              <li class="flex items-start gap-2.5"><i class="fa-solid fa-circle-check text-[#D4AF37] mt-1 shrink-0"></i> Vorbereitung auf Sichtungen &amp; Probetrainings</li>
              <li class="flex items-start gap-2.5"><i class="fa-solid fa-circle-check text-[#D4AF37] mt-1 shrink-0"></i> Kognitives Handlungstempo &amp; Scanning</li>
              <li class="flex items-start gap-2.5"><i class="fa-solid fa-circle-check text-[#D4AF37] mt-1 shrink-0"></i> Auch für Erwachsene &amp; Vereinsteams</li>
            </ul>
          </div>

          <a href="#erstgespraech" class="w-full py-4 rounded-2xl bg-slate-900 hover:bg-[#D4AF37] text-white hover:text-slate-900 font-extrabold text-sm block text-center transition-all duration-300 shadow-md">
            Spezialtraining anfragen
          </a>
        </div>

      </div>

      <!-- Visuelle Trainingsbereiche (Kompakt und visuell verständlich) -->
      <div class="mt-12 pt-12 border-t border-slate-200">
        <div class="text-center max-w-2xl mx-auto mb-8">
          <h3 class="text-xl font-black text-slate-900">Was bei SoccerProf trainiert werden kann</h3>
          <p class="text-xs text-slate-500 font-medium">Ein großer Teil aller Einheiten findet gezielt mit dem Ball statt.</p>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4">
          <div class="p-4 rounded-2xl bg-white/90 border border-slate-200 text-center space-y-2">
            <i class="fa-solid fa-futbol text-xl text-[#D4AF37]"></i>
            <div class="font-extrabold text-xs text-slate-900">Technik &amp; Ball</div>
            <div class="text-[11px] text-slate-500">Dribbling, Finten, Erstkontakt</div>
          </div>
          <div class="p-4 rounded-2xl bg-white/90 border border-slate-200 text-center space-y-2">
            <i class="fa-solid fa-brain text-xl text-[#E63946]"></i>
            <div class="font-extrabold text-xs text-slate-900">Kognition</div>
            <div class="text-[11px] text-slate-500">Wahrnehmung &amp; Reize</div>
          </div>
          <div class="p-4 rounded-2xl bg-white/90 border border-slate-200 text-center space-y-2">
            <i class="fa-solid fa-bolt text-xl text-[#D4AF37]"></i>
            <div class="font-extrabold text-xs text-slate-900">Koordination</div>
            <div class="text-[11px] text-slate-500">Beinarbeit &amp; Wendigkeit</div>
          </div>
          <div class="p-4 rounded-2xl bg-white/90 border border-slate-200 text-center space-y-2">
            <i class="fa-solid fa-chess-board text-xl text-[#E63946]"></i>
            <div class="font-extrabold text-xs text-slate-900">Taktik</div>
            <div class="text-[11px] text-slate-500">Stellungsspiel &amp; 1v1</div>
          </div>
          <div class="p-4 rounded-2xl bg-white/90 border border-slate-200 text-center space-y-2">
            <i class="fa-solid fa-hands-holding-circle text-xl text-[#D4AF37]"></i>
            <div class="font-extrabold text-xs text-slate-900">Torwarttraining</div>
            <div class="text-[11px] text-slate-500">Reflexe &amp; Spieleröffnung</div>
          </div>
          <div class="p-4 rounded-2xl bg-white/90 border border-slate-200 text-center space-y-2">
            <i class="fa-solid fa-shield-halved text-xl text-[#E63946]"></i>
            <div class="font-extrabold text-xs text-slate-900">Mentale Stärke</div>
            <div class="text-[11px] text-slate-500">Fokus &amp; Resilienz</div>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- 06 — TRAININGSMETHODE (Nicht einfach mehr trainieren. Sondern gezielter.) -->
  <section id="methode" class="py-24 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <div class="inline-block px-3 py-1 rounded-full bg-[#E63946]/10 text-[#E63946] font-extrabold text-xs uppercase tracking-widest border border-[#E63946]/30">
          Unser Prinzip
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          Nicht einfach mehr trainieren. Sondern gezielter.
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg">
          Ein klar strukturierter Prozess, der den Spieler in den Mittelpunkt stellt:
        </p>
      </div>

      <!-- 4-Schritte-Prozess: 01 Analyse, 02 Ziele/Plan, 03 Training, 04 Feedback/Entwicklung -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <div class="glass-card p-6 rounded-3xl space-y-4 hover:border-[#D4AF37]" data-aos="fade-up" data-aos-delay="100">
          <div class="w-12 h-12 rounded-2xl bg-slate-900 text-[#D4AF37] font-black flex items-center justify-center text-lg">
            01
          </div>
          <h3 class="text-lg font-black text-slate-900">Analyse</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Wo steht der Spieler aktuell? Wir erfassen Stärken, Schwächen und Bewegungsmuster im Detail.
          </p>
        </div>

        <div class="glass-card p-6 rounded-3xl space-y-4 hover:border-[#E63946]" data-aos="fade-up" data-aos-delay="200">
          <div class="w-12 h-12 rounded-2xl bg-[#E63946] text-white font-black flex items-center justify-center text-lg shadow-red-glow">
            02
          </div>
          <h3 class="text-lg font-black text-slate-900">Ziele &amp; Plan</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Was soll konkret verbessert werden? Daraus entsteht ein Training, das passgenau auf den Spieler zugeschnitten ist.
          </p>
        </div>

        <div class="glass-card p-6 rounded-3xl space-y-4 hover:border-[#D4AF37]" data-aos="fade-up" data-aos-delay="300">
          <div class="w-12 h-12 rounded-2xl bg-slate-900 text-[#D4AF37] font-black flex items-center justify-center text-lg">
            03
          </div>
          <h3 class="text-lg font-black text-slate-900">Training</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Gezielte Übungen und hohe Wiederholungszahl. Intensive Einheiten überwiegend mit dem Ball.
          </p>
        </div>

        <div class="glass-card p-6 rounded-3xl space-y-4 hover:border-[#E63946]" data-aos="fade-up" data-aos-delay="400">
          <div class="w-12 h-12 rounded-2xl bg-[#E63946] text-white font-black flex items-center justify-center text-lg shadow-red-glow">
            04
          </div>
          <h3 class="text-lg font-black text-slate-900">Feedback &amp; Entwicklung</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Fortschritte analysieren, Selbstvertrauen stärken und das Trainingsprogramm kontinuierlich anpassen.
          </p>
        </div>

      </div>

    </div>
  </section>

  <!-- 07 — WARUM SOCCERPROF? (4 klare Argumente ohne Blabla) -->
  <section id="warum" class="py-24 bg-white/80 backdrop-blur-md relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <div class="inline-block px-3 py-1 rounded-full bg-[#D4AF37]/10 text-[#D4AF37] font-extrabold text-xs uppercase tracking-widest border border-[#D4AF37]/30">
          Gezielter Mehrwert
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          Warum SoccerProf?
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg">
          Vier nachvollziehbare Gründe, die den Unterschied im Spiel deines Kindes ausmachen.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        
        <div class="glass-card p-8 rounded-3xl space-y-3" data-aos="fade-right">
          <div class="flex items-center gap-3 text-[#D4AF37] font-extrabold text-lg">
            <i class="fa-solid fa-user-check text-xl"></i>
            <span>01 — Individuell statt Standardprogramm</span>
          </div>
          <p class="text-slate-600 text-sm leading-relaxed">
            Jeder Spieler bringt andere Stärken, Schwächen und Ziele mit. Wir passen das Training exakt an das Profil des Spielers an.
          </p>
        </div>

        <div class="glass-card p-8 rounded-3xl space-y-3" data-aos="fade-left">
          <div class="flex items-center gap-3 text-[#E63946] font-extrabold text-lg">
            <i class="fa-solid fa-users-line text-xl"></i>
            <span>02 — Kleine Gruppen, große Aufmerksamkeit</span>
          </div>
          <p class="text-slate-600 text-sm leading-relaxed">
            Weniger Spieler bedeutet mehr Ballkontakte, sofortige Korrekturen bei Fehlern und deutlich höhere Wiederholungszahlen.
          </p>
        </div>

        <div class="glass-card p-8 rounded-3xl space-y-3" data-aos="fade-right">
          <div class="flex items-center gap-3 text-[#E63946] font-extrabold text-lg">
            <i class="fa-solid fa-handshake text-xl"></i>
            <span>03 — Ergänzung zum Vereinstraining</span>
          </div>
          <p class="text-slate-600 text-sm leading-relaxed">
            Das Training ersetzt den Verein nicht – es ergänzt ihn dort, wo individuelles Arbeiten besonders wertvoll ist und Früchte trägt.
          </p>
        </div>

        <div class="glass-card p-8 rounded-3xl space-y-3" data-aos="fade-left">
          <div class="flex items-center gap-3 text-[#D4AF37] font-extrabold text-lg">
            <i class="fa-solid fa-compass-drafting text-xl"></i>
            <span>04 — Entwicklung mit System</span>
          </div>
          <p class="text-slate-600 text-sm leading-relaxed">
            Das Training folgt einem klaren didaktischen Aufbau und orientiert sich kontinuierlich am Entwicklungsstand des Spielers.
          </p>
        </div>

      </div>

    </div>
  </section>

  <!-- 08 — ERGEBNISSE / TESTIMONIALS (Social Proof von echten Eltern) -->
  <section id="ergebnisse" class="py-24 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <div class="inline-block px-3 py-1 rounded-full bg-[#E63946]/10 text-[#E63946] font-extrabold text-xs uppercase tracking-widest border border-[#E63946]/30">
          Erfahrungsberichte
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          Das sagen unsere Spieler und Eltern.
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg">
          Nicht nur wir sagen das – echte Stimmen aus dem Hamburger Trainingsalltag.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <!-- Testimonial 1: Mutter Angelika (Original von soccerprof.de) -->
        <div class="glass-card p-8 rounded-3xl relative border-2 border-[#D4AF37]/50 shadow-xl flex flex-col justify-between" data-aos="fade-up" data-aos-delay="100">
          <div>
            <div class="flex items-center gap-1 text-[#D4AF37] mb-4 text-sm">
              <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
            </div>
            <p class="text-slate-800 font-medium text-sm leading-relaxed italic mb-6">
              "Danke lieber Sami! Uns hat's auch gefreut, dein Training tut unserem Sohn so gut und bringt ihn spielerisch und mental enorm weiter!"
            </p>
          </div>
          <div class="flex items-center gap-4 pt-4 border-t border-slate-200">
            <div class="w-12 h-12 rounded-full bg-slate-900 text-[#D4AF37] flex items-center justify-center font-black text-lg">
              A
            </div>
            <div>
              <div class="font-extrabold text-slate-900 text-sm">Mutter Angelika</div>
              <div class="text-xs text-slate-500 font-medium">Elterneinschätzung Hamburg</div>
            </div>
          </div>
        </div>

        <!-- Testimonial 2: Vater eines U14 Spielers -->
        <div class="glass-card p-8 rounded-3xl relative shadow-xl flex flex-col justify-between" data-aos="fade-up" data-aos-delay="200">
          <div>
            <div class="flex items-center gap-1 text-[#D4AF37] mb-4 text-sm">
              <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
            </div>
            <p class="text-slate-800 font-medium text-sm leading-relaxed italic mb-6">
              "Unser Sohn hat sich technisch unglaublich weiterentwickelt und geht mittlerweile viel selbstbewusster ins Spiel. Die kognitiven Übungen zeigen Wirkung."
            </p>
          </div>
          <div class="flex items-center gap-4 pt-4 border-t border-slate-200">
            <div class="w-12 h-12 rounded-full bg-[#E63946] text-white flex items-center justify-center font-black text-lg">
              T
            </div>
            <div>
              <div class="font-extrabold text-slate-900 text-sm">Thomas M.</div>
              <div class="text-xs text-slate-500 font-medium">Vater eines U14-Spielers</div>
            </div>
          </div>
        </div>

        <!-- Testimonial 3: Lukas K. (Amateurspieler) -->
        <div class="glass-card p-8 rounded-3xl relative shadow-xl flex flex-col justify-between" data-aos="fade-up" data-aos-delay="300">
          <div>
            <div class="flex items-center gap-1 text-[#D4AF37] mb-4 text-sm">
              <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
            </div>
            <p class="text-slate-800 font-medium text-sm leading-relaxed italic mb-6">
              "Sami fordert einen in jeder Minute. Die Technik- und Schnelligkeitseinheiten haben mir vor der Saison extrem geholfen, meine Position zu sichern."
            </p>
          </div>
          <div class="flex items-center gap-4 pt-4 border-t border-slate-200">
            <div class="w-12 h-12 rounded-full bg-slate-900 text-white flex items-center justify-center font-black text-lg">
              L
            </div>
            <div>
              <div class="font-extrabold text-slate-900 text-sm">Lukas K.</div>
              <div class="text-xs text-slate-500 font-medium">Herren-Amateurspieler</div>
            </div>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- 09 — TRAINER / SAMI GHAOUAR (Echte Qualifikationen & Werdegang) -->
  <section id="ueber-uns" class="py-24 bg-slate-900 text-white relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <!-- Foto von Trainer Sami Ghaouar -->
        <div class="lg:col-span-5" data-aos="zoom-in">
          <div class="relative rounded-3xl overflow-hidden border-2 border-[#D4AF37]/50 shadow-2xl p-2 bg-slate-950">
            <div class="w-full h-96 sm:h-[480px] rounded-2xl overflow-hidden relative">
              <img src="img/sami/sami%20daumen%20hoch.avif" alt="Sami Ghaouar Head Coach SoccerProf" class="w-full h-full object-cover">
              <div class="absolute bottom-0 inset-x-0 bg-gradient-to-t from-slate-950 via-slate-950/80 to-transparent p-6 text-center">
                <h3 class="text-2xl font-black text-white">Sami Ghaouar</h3>
                <p class="text-xs text-[#D4AF37] font-bold uppercase tracking-widest mt-1">Gründer &amp; Head Coach</p>
                <div class="mt-3 flex gap-2 justify-center">
                  <span class="text-[10px] bg-[#D4AF37]/20 text-[#D4AF37] px-3 py-1 rounded-full font-extrabold border border-[#D4AF37]/40">UEFA-B-LIZENZ</span>
                  <span class="text-[10px] bg-[#E63946]/20 text-[#E63946] px-3 py-1 rounded-full font-extrabold border border-[#E63946]/40">HAMBURG</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Fakten & Qualifikation zu Sami -->
        <div class="lg:col-span-7 space-y-6" data-aos="fade-left">
          <div class="inline-block px-3 py-1 rounded-full bg-[#D4AF37]/20 text-[#D4AF37] font-extrabold text-xs uppercase border border-[#D4AF37]/30">
            Erfahrung &amp; Kompetenz
          </div>
          <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black tracking-tight leading-tight">
            Hinter SoccerProf steht echte Fußballerfahrung.
          </h2>
          <p class="text-slate-300 font-medium text-base leading-relaxed">
            Als langjähriger Individual- und Mannschaftstrainer in Hamburg steht <strong class="text-white">Sami Ghaouar</strong> für akribisches, zielorientiertes und motivierendes Coaching. Früher selbst als Flügelspieler beim <strong class="text-[#D4AF37]">Hamburger SV (HSV)</strong> ausgebildet und mit Erfahrung aus der Regionalliga, gibt er sein Wissen heute an die nächste Generation weiter.
          </p>

          <!-- Echte Qualifikations-Kacheln -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
            <div class="p-4 rounded-2xl bg-slate-800/80 border border-slate-700">
              <div class="text-[#D4AF37] font-extrabold text-sm mb-1"><i class="fa-solid fa-graduation-cap mr-2"></i>UEFA-B-Lizenz Trainer</div>
              <p class="text-xs text-slate-400">B-Lizenz 2018, C-Lizenz 2014 &amp; DFB-Fortbildung Sportschule Duisburg-Wedau.</p>
            </div>
            <div class="p-4 rounded-2xl bg-slate-800/80 border border-slate-700">
              <div class="text-[#E63946] font-extrabold text-sm mb-1"><i class="fa-solid fa-futbol mr-2"></i>HSV &amp; Regionalliga</div>
              <p class="text-xs text-slate-400">Gelernter Flügelspieler beim Hamburger SV mit Regionalliga-Praxis.</p>
            </div>
            <div class="p-4 rounded-2xl bg-slate-800/80 border border-slate-700">
              <div class="text-[#D4AF37] font-extrabold text-sm mb-1"><i class="fa-solid fa-stopwatch mr-2"></i>Trainer seit 2012</div>
              <p class="text-xs text-slate-400">Über ein Jahrzehnt Erfahrung im Einzeltraining &amp; Vereinen.</p>
            </div>
            <div class="p-4 rounded-2xl bg-slate-800/80 border border-slate-700">
              <div class="text-[#E63946] font-extrabold text-sm mb-1"><i class="fa-solid fa-location-dot mr-2"></i>Standort Hamburg</div>
              <p class="text-xs text-slate-400">Öjendorfer Weg 80 (Sommer) &amp; beheizte Soccer-Hallen (Winter).</p>
            </div>
          </div>

          <div class="pt-4 flex flex-col sm:flex-row gap-4">
            <a href="#erstgespraech" class="inline-flex items-center justify-center gap-3 px-8 py-4 rounded-full bg-[#E63946] hover:bg-[#C52233] text-white font-black text-sm shadow-red-glow transition-all transform hover:-translate-y-1">
              <span>Kostenloses Erstgespräch mit Sami</span>
              <i class="fa-solid fa-arrow-right"></i>
            </a>
            <a href="https://wa.me/4917684156542?text=Hallo%20Sami,%20ich%20interessiere%20mich%20f%C3%BCr%20dein%20Training!" target="_blank" class="inline-flex items-center justify-center gap-2 px-6 py-4 rounded-full bg-[#25D366] hover:bg-[#20bd5a] text-white font-black text-sm transition-all transform hover:-translate-y-1">
              <i class="fa-brands fa-whatsapp text-lg"></i>
              <span>Direkt WhatsApp</span>
            </a>
          </div>

        </div>

      </div>
    </div>
  </section>

  <!-- 10 — ABLAUF (In 3 Schritten zum individuellen Training) -->
  <section id="ablauf" class="py-24 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <div class="inline-block px-3 py-1 rounded-full bg-[#D4AF37]/10 text-[#D4AF37] font-extrabold text-xs uppercase tracking-widest border border-[#D4AF37]/30">
          So einfach startet dein Training
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          In 3 Schritten zum individuellen Training.
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg">
          Was passiert, wenn du jetzt Kontakt aufnimmst? Glasklar und unkompliziert:
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <div class="glass-card p-8 rounded-3xl text-center space-y-4 relative border-2 border-slate-200" data-aos="fade-up" data-aos-delay="100">
          <div class="w-16 h-16 rounded-full bg-[#E63946] text-white flex items-center justify-center text-2xl font-black mx-auto shadow-red-glow">
            1
          </div>
          <h3 class="text-xl font-black text-slate-900">01 Kontakt aufnehmen</h3>
          <p class="text-slate-600 text-sm leading-relaxed">
            Kurzes kostenloses Erstgespräch. Wir sprechen unverbindlich über den Spieler, seine aktuellen Ziele und seine Situation im Verein.
          </p>
        </div>

        <div class="glass-card p-8 rounded-3xl text-center space-y-4 relative border-2 border-[#D4AF37]/50" data-aos="fade-up" data-aos-delay="200">
          <div class="w-16 h-16 rounded-full bg-slate-900 text-[#D4AF37] flex items-center justify-center text-2xl font-black mx-auto shadow-md">
            2
          </div>
          <h3 class="text-xl font-black text-slate-900">02 Ziele besprechen</h3>
          <p class="text-slate-600 text-sm leading-relaxed">
            Wir schauen gemeinsam, wo der Spieler steht, woran gearbeitet werden soll und welches Trainingsformat (1:1 oder 5er-Gruppe) ideal passt.
          </p>
        </div>

        <div class="glass-card p-8 rounded-3xl text-center space-y-4 relative border-2 border-slate-200" data-aos="fade-up" data-aos-delay="300">
          <div class="w-16 h-16 rounded-full bg-[#E63946] text-white flex items-center justify-center text-2xl font-black mx-auto shadow-red-glow">
            3
          </div>
          <h3 class="text-xl font-black text-slate-900">03 Training starten</h3>
          <p class="text-slate-600 text-sm leading-relaxed">
            Der Spieler startet mit einem Training auf dem Platz in Hamburg, das passgenau auf seine persönliche Entwicklung ausgerichtet ist.
          </p>
        </div>

      </div>

      <div class="mt-12 text-center">
        <a href="#erstgespraech" class="inline-flex items-center gap-3 px-8 py-4 rounded-full bg-[#E63946] hover:bg-[#C52233] text-white font-black text-base shadow-red-glow transition-all transform hover:-translate-y-1">
          <span>Kostenloses Erstgespräch vereinbaren</span>
          <i class="fa-solid fa-arrow-right"></i>
        </a>
      </div>

    </div>
  </section>

  <!-- 11 — PREISE (Transparent. Persönlich. Passend.) -->
  <section id="preise" class="py-24 bg-white/80 backdrop-blur-md relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <div class="inline-block px-3 py-1 rounded-full bg-[#D4AF37]/10 text-[#D4AF37] font-extrabold text-xs uppercase tracking-widest border border-[#D4AF37]/30">
          Transparenz
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          Transparent. Persönlich. Passend.
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg">
          Faire Trainingspakete abgestimmt auf deinen Rhythmus. Keine Knebelverträge.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-stretch">
        
        <!-- Paket 1: Erstgespräch & Beratung -->
        <div class="glass-card p-8 rounded-3xl flex flex-col justify-between" data-aos="fade-right">
          <div>
            <h3 class="text-2xl font-black text-slate-900 mb-2">Erstgespräch</h3>
            <div class="text-3xl font-black text-[#E63946] mb-4">0 €</div>
            <p class="text-slate-600 text-sm mb-6">Unverbindliches Vorgespräch zur Analyse des aktuellen Bedarfs.</p>
            <ul class="space-y-3 text-xs font-semibold text-slate-700 mb-8">
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Persönliche Beratung mit Sami</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Analyse der individuellen Ziele</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> 100% unverbindlich &amp; kostenfrei</li>
            </ul>
          </div>
          <a href="#erstgespraech" class="w-full py-3.5 rounded-2xl bg-slate-900 text-white font-extrabold text-xs text-center block hover:bg-[#D4AF37] hover:text-slate-900 transition-colors">
            JETZT ANFRAGEN
          </a>
        </div>

        <!-- Paket 2: Kleingruppentraining (Beliebt) -->
        <div class="glass-card p-8 rounded-3xl flex flex-col justify-between border-2 border-[#D4AF37] shadow-gold-glow relative bg-white/95" data-aos="zoom-in">
          <div class="absolute -top-3.5 left-1/2 -translate-x-1/2 bg-[#D4AF37] text-slate-900 font-black text-[10px] uppercase px-3 py-1 rounded-full">
            Empfohlen
          </div>
          <div>
            <h3 class="text-2xl font-black text-slate-900 mb-2">Kleingruppe (2–5)</h3>
            <div class="text-2xl font-black text-slate-900 mb-4">Auf Anfrage <span class="text-xs font-normal text-slate-500">/ Paket</span></div>
            <p class="text-slate-600 text-sm mb-6">Gemeinsam trainieren mit maximal 5 Spielern pro Trainer.</p>
            <ul class="space-y-3 text-xs font-semibold text-slate-700 mb-8">
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#E63946]"></i> Max. 5 Spieler für hohe Betreuungsdichte</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#E63946]"></i> Hohe Wiederholungszahlen &amp; Spielreize</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#E63946]"></i> Sommer Kunstrasen &amp; Winter Halle</li>
            </ul>
          </div>
          <a href="#erstgespraech" class="w-full py-3.5 rounded-2xl bg-[#E63946] text-white font-extrabold text-xs text-center block shadow-red-glow hover:bg-[#C52233] transition-colors">
            PREISE ANFRAGEN
          </a>
        </div>

        <!-- Paket 3: 1:1 Einzeltraining -->
        <div class="glass-card p-8 rounded-3xl flex flex-col justify-between" data-aos="fade-left">
          <div>
            <h3 class="text-2xl font-black text-slate-900 mb-2">1:1 Einzeltraining</h3>
            <div class="text-2xl font-black text-slate-900 mb-4">Auf Anfrage <span class="text-xs font-normal text-slate-500">/ 5er- &amp; 10er-Karten</span></div>
            <p class="text-slate-600 text-sm mb-6">Voller Fokus auf die persönliche Entwicklung eines Spielers.</p>
            <ul class="space-y-3 text-xs font-semibold text-slate-700 mb-8">
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> 100% Aufmerksamkeitsdichte</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Video- &amp; Bewegungsanalyse</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Positions- &amp; Rollen-Coaching</li>
            </ul>
          </div>
          <a href="#erstgespraech" class="w-full py-3.5 rounded-2xl bg-slate-900 text-white font-extrabold text-xs text-center block hover:bg-[#D4AF37] hover:text-slate-900 transition-colors">
            PREISE ANFRAGEN
          </a>
        </div>

      </div>

    </div>
  </section>

  <!-- 12 — EVENTS & CAMPS (Sekundärer Bereich) -->
  <section class="py-16 bg-white/60 backdrop-blur-md border-b border-slate-200 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row items-center justify-between gap-6">
        <div>
          <div class="inline-block px-3 py-1 rounded-full bg-[#E63946]/10 text-[#E63946] font-extrabold text-xs uppercase mb-2">
            Mehr als Training
          </div>
          <h3 class="text-2xl font-black text-slate-900">Power Camps &amp; Kindergeburtstage in Hamburg</h3>
          <p class="text-slate-600 text-xs sm:text-sm mt-1">
            Feriencamps in den Hamburger Schulferien, unvergessliche Fußball-Geburtstage und Erwachsenen-Workshops.
          </p>
        </div>
        <a href="#erstgespraech" class="shrink-0 px-6 py-3 rounded-full bg-slate-900 hover:bg-[#E63946] text-white font-extrabold text-xs transition-colors">
          Events &amp; Camps anfragen
        </a>
      </div>
    </div>
  </section>

  <!-- 13 — FAQ (Ganz unten mit Akkordeon) -->
  <section id="faq" class="py-24 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <div class="inline-block px-3 py-1 rounded-full bg-[#E63946]/10 text-[#E63946] font-extrabold text-xs uppercase tracking-widest border border-[#E63946]/30">
          Transparenz &amp; Information
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          Häufig gestellte Fragen
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg">
          Hier findest Du alle wichtigen Antworten rund um unser Training in Hamburg.
        </p>
      </div>

      <div class="max-w-4xl mx-auto space-y-4" data-aos="fade-up">
        
        <!-- FAQ 1 -->
        <div class="glass-card rounded-2xl overflow-hidden border border-slate-200/80">
          <button class="faq-button w-full px-6 py-5 text-left font-extrabold text-slate-900 text-base sm:text-lg flex justify-between items-center focus:outline-none hover:text-[#E63946] transition-colors">
            <span>Für welches Alter eignet sich das Training?</span>
            <i class="fa-solid fa-chevron-down faq-icon text-[#D4AF37] transition-transform duration-300"></i>
          </button>
          <div class="faq-content hidden px-6 pb-6 text-slate-600 text-sm leading-relaxed border-t border-slate-100 pt-4">
            Unser Hauptfokus liegt auf Nachwuchsspielern von <strong>6 bis 17 Jahren</strong> (Kinder &amp; Jugendliche). Zudem bieten wir spezialisierte Einheiten für ambitionierte Erwachsene, Herren- und Damenspieler an.
          </div>
        </div>

        <!-- FAQ 2 -->
        <div class="glass-card rounded-2xl overflow-hidden border border-slate-200/80">
          <button class="faq-button w-full px-6 py-5 text-left font-extrabold text-slate-900 text-base sm:text-lg flex justify-between items-center focus:outline-none hover:text-[#E63946] transition-colors">
            <span>Muss mein Kind bereits Fußball spielen können?</span>
            <i class="fa-solid fa-chevron-down faq-icon text-[#D4AF37] transition-transform duration-300"></i>
          </button>
          <div class="faq-content hidden px-6 pb-6 text-slate-600 text-sm leading-relaxed border-t border-slate-100 pt-4">
            Grundlegende Begeisterung für den Sport reicht völlig aus. Egal ob Einsteiger mit Grundkenntnissen oder ambitionierter Leistungsspieler: Das Training wird individuell an den aktuellen Entwicklungsstand angepasst.
          </div>
        </div>

        <!-- FAQ 3 -->
        <div class="glass-card rounded-2xl overflow-hidden border border-slate-200/80">
          <button class="faq-button w-full px-6 py-5 text-left font-extrabold text-slate-900 text-base sm:text-lg flex justify-between items-center focus:outline-none hover:text-[#E63946] transition-colors">
            <span>Ist das Training eine Ergänzung zum Verein?</span>
            <i class="fa-solid fa-chevron-down faq-icon text-[#D4AF37] transition-transform duration-300"></i>
          </button>
          <div class="faq-content hidden px-6 pb-6 text-slate-600 text-sm leading-relaxed border-t border-slate-100 pt-4">
            Ja, absolut! SoccerProf ist <strong>kein Ersatz</strong> für den Verein, sondern eine hochspezialisierte Ergänzung. Das Gelernte fließt direkt am Wochenende in die Mannschaftsleistung im Verein ein.
          </div>
        </div>

        <!-- FAQ 4 -->
        <div class="glass-card rounded-2xl overflow-hidden border border-slate-200/80">
          <button class="faq-button w-full px-6 py-5 text-left font-extrabold text-slate-900 text-base sm:text-lg flex justify-between items-center focus:outline-none hover:text-[#E63946] transition-colors">
            <span>Wie läuft das erste Training ab?</span>
            <i class="fa-solid fa-chevron-down faq-icon text-[#D4AF37] transition-transform duration-300"></i>
          </button>
          <div class="faq-content hidden px-6 pb-6 text-slate-600 text-sm leading-relaxed border-t border-slate-100 pt-4">
            Nach einem kurzen Erstgespräch starten wir mit einer ersten Bestandsaufnahme auf dem Platz. Trainer Sami analysiert Ballgefühl, Erstkontakt und Bewegungsabläufe, um den idealen Trainingsplan festzulegen.
          </div>
        </div>

        <!-- FAQ 5 -->
        <div class="glass-card rounded-2xl overflow-hidden border border-slate-200/80">
          <button class="faq-button w-full px-6 py-5 text-left font-extrabold text-slate-900 text-base sm:text-lg flex justify-between items-center focus:outline-none hover:text-[#E63946] transition-colors">
            <span>Wo findet das Training statt?</span>
            <i class="fa-solid fa-chevron-down faq-icon text-[#D4AF37] transition-transform duration-300"></i>
          </button>
          <div class="faq-content hidden px-6 pb-6 text-slate-600 text-sm leading-relaxed border-t border-slate-100 pt-4">
            Unser Hauptstützpunkt liegt am <strong>Öjendorfer Weg 80, 22119 Hamburg</strong> (Horner Rennbahn / Billstedt). Im Sommer trainieren wir auf modernstem Kunstrasen im Freien, im Winter in beheizten Indoor-Hallen in Hamburg.
          </div>
        </div>

        <!-- FAQ 6 -->
        <div class="glass-card rounded-2xl overflow-hidden border border-slate-200/80">
          <button class="faq-button w-full px-6 py-5 text-left font-extrabold text-slate-900 text-base sm:text-lg flex justify-between items-center focus:outline-none hover:text-[#E63946] transition-colors">
            <span>Wie lange dauert eine Trainingseinheit?</span>
            <i class="fa-solid fa-chevron-down faq-icon text-[#D4AF37] transition-transform duration-300"></i>
          </button>
          <div class="faq-content hidden px-6 pb-6 text-slate-600 text-sm leading-relaxed border-t border-slate-100 pt-4">
            Eine reguläre Trainingseinheit dauert <strong>60 bis 75 Minuten</strong>. Dadurch halten wir die geistige und körperliche Konzentration auf absolutem Höchstniveau.
          </div>
        </div>

        <!-- FAQ 7 -->
        <div class="glass-card rounded-2xl overflow-hidden border border-slate-200/80">
          <button class="faq-button w-full px-6 py-5 text-left font-extrabold text-slate-900 text-base sm:text-lg flex justify-between items-center focus:outline-none hover:text-[#E63946] transition-colors">
            <span>Kann mein Kind mit Freunden oder Geschwistern trainieren?</span>
            <i class="fa-solid fa-chevron-down faq-icon text-[#D4AF37] transition-transform duration-300"></i>
          </button>
          <div class="faq-content hidden px-6 pb-6 text-slate-600 text-sm leading-relaxed border-t border-slate-100 pt-4">
            Ja! Im Kleingruppentraining stellen wir leistungshomogene Gruppen mit 2 bis 5 befreundeten Spielern oder Geschwistern zusammen.
          </div>
        </div>

        <!-- FAQ 8 -->
        <div class="glass-card rounded-2xl overflow-hidden border border-slate-200/80">
          <button class="faq-button w-full px-6 py-5 text-left font-extrabold text-slate-900 text-base sm:text-lg flex justify-between items-center focus:outline-none hover:text-[#E63946] transition-colors">
            <span>Was muss mein Kind zum Training mitbringen?</span>
            <i class="fa-solid fa-chevron-down faq-icon text-[#D4AF37] transition-transform duration-300"></i>
          </button>
          <div class="faq-content hidden px-6 pb-6 text-slate-600 text-sm leading-relaxed border-t border-slate-100 pt-4">
            Normale Fußballbekleidung, passende Nockenschuhe (Hallen- oder Multinockenschuhe im Winter), Schienbeinschoner und ausreichend Wasser. Alle Übungsgeräte stellen wir.
          </div>
        </div>

        <!-- FAQ 9 -->
        <div class="glass-card rounded-2xl overflow-hidden border border-slate-200/80">
          <button class="faq-button w-full px-6 py-5 text-left font-extrabold text-slate-900 text-base sm:text-lg flex justify-between items-center focus:outline-none hover:text-[#E63946] transition-colors">
            <span>Wie kann ich ein Erstgespräch vereinbaren?</span>
            <i class="fa-solid fa-chevron-down faq-icon text-[#D4AF37] transition-transform duration-300"></i>
          </button>
          <div class="faq-content hidden px-6 pb-6 text-slate-600 text-sm leading-relaxed border-t border-slate-100 pt-4">
            Ganz unkompliziert über das untenstehende Formular oder per direktem WhatsApp-Klick an Sami Ghaouar (+49 176 841 565 42). Wir melden uns umgehend zurück!
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- 14 — FINAL CTA & FORMULAR (Bereit für den nächsten Schritt?) -->
  <section id="erstgespraech" class="py-24 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="glass-card rounded-3xl p-8 sm:p-12 border-2 border-[#D4AF37] shadow-2xl relative overflow-hidden bg-gradient-to-br from-white via-white to-amber-500/5">
        
        <div class="max-w-3xl mx-auto text-center space-y-6 mb-12">
          <div class="inline-block px-4 py-1.5 rounded-full bg-[#E63946] text-white font-black text-xs uppercase tracking-widest shadow-red-glow">
            Jetzt starten
          </div>
          <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
            Bereit für den nächsten Schritt?
          </h2>
          <p class="text-slate-700 font-medium text-base sm:text-lg">
            Finde heraus, welches Training zu dir oder deinem Kind passt. Unverbindlich, persönlich und ohne Verpflichtung.
          </p>
          <div class="flex items-center justify-center gap-4 text-xs font-bold text-slate-500 uppercase tracking-wider">
            <span>Unverbindlich</span> • <span>Persönlich</span> • <span>Ohne Verpflichtung</span>
          </div>
        </div>

        <!-- Formular -->
        <div class="max-w-2xl mx-auto">
          <form id="contactForm" onsubmit="handleFormSubmit(event)" class="space-y-6">
            
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
              <div>
                <label class="block text-xs font-extrabold text-slate-700 uppercase mb-2">Vor- &amp; Nachname *</label>
                <input type="text" required placeholder="z.B. Markus Weber" class="w-full px-4 py-3.5 rounded-2xl bg-white border border-slate-200 text-slate-900 text-sm focus:outline-none focus:border-[#D4AF37] focus:ring-2 focus:ring-[#D4AF37]/20 transition-all">
              </div>
              <div>
                <label class="block text-xs font-extrabold text-slate-700 uppercase mb-2">Telefonnummer *</label>
                <input type="tel" required placeholder="z.B. 0176 12345678" class="w-full px-4 py-3.5 rounded-2xl bg-white border border-slate-200 text-slate-900 text-sm focus:outline-none focus:border-[#D4AF37] focus:ring-2 focus:ring-[#D4AF37]/20 transition-all">
              </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
              <div>
                <label class="block text-xs font-extrabold text-slate-700 uppercase mb-2">E-Mail-Adresse *</label>
                <input type="email" required placeholder="z.B. eltern@beispiel.de" class="w-full px-4 py-3.5 rounded-2xl bg-white border border-slate-200 text-slate-900 text-sm focus:outline-none focus:border-[#D4AF37] focus:ring-2 focus:ring-[#D4AF37]/20 transition-all">
              </div>
              <div>
                <label class="block text-xs font-extrabold text-slate-700 uppercase mb-2">Alter / Jahrgang des Spielers</label>
                <select class="w-full px-4 py-3.5 rounded-2xl bg-white border border-slate-200 text-slate-900 text-sm focus:outline-none focus:border-[#D4AF37] focus:ring-2 focus:ring-[#D4AF37]/20 transition-all">
                  <option>Kinder (6 - 11 Jahre)</option>
                  <option>Jugendliche (12 - 17 Jahre)</option>
                  <option>Erwachsene / Amateure</option>
                  <option>Verein / Mannschaft</option>
                </select>
              </div>
            </div>

            <div>
              <label class="block text-xs font-extrabold text-slate-700 uppercase mb-2">Trainingswunsch</label>
              <select class="w-full px-4 py-3.5 rounded-2xl bg-white border border-slate-200 text-slate-900 text-sm focus:outline-none focus:border-[#D4AF37] focus:ring-2 focus:ring-[#D4AF37]/20 transition-all">
                <option>Kostenloses Erstgespräch</option>
                <option>1:1 Einzeltraining</option>
                <option>Kleingruppentraining (2–5 Spieler)</option>
                <option>Spezialtraining (Kognition / Torabschluss)</option>
              </select>
            </div>

            <div>
              <label class="block text-xs font-extrabold text-slate-700 uppercase mb-2">Nachricht / Anmerkung (optional)</label>
              <textarea rows="3" placeholder="Beschreibe kurz die Wünsche oder die Position des Spielers..." class="w-full px-4 py-3.5 rounded-2xl bg-white border border-slate-200 text-slate-900 text-sm focus:outline-none focus:border-[#D4AF37] focus:ring-2 focus:ring-[#D4AF37]/20 transition-all"></textarea>
            </div>

            <button type="submit" class="w-full py-4 rounded-2xl bg-[#E63946] hover:bg-[#C52233] text-white font-black text-base shadow-red-glow hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-0.5 flex items-center justify-center gap-3">
              <i class="fa-solid fa-paper-plane"></i>
              <span>Kostenloses Erstgespräch anfragen</span>
            </button>

            <!-- Success notification box -->
            <div id="formSuccess" class="hidden p-4 rounded-2xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-700 text-center font-bold text-sm">
              <i class="fa-solid fa-circle-check mr-2"></i>Vielen Dank! Deine Anfrage wurde erfolgreich weitergeleitet. Sami meldet sich in Kürze!
            </div>

          </form>

          <!-- WhatsApp Alternative -->
          <div class="mt-8 pt-6 border-t border-slate-200 text-center">
            <p class="text-xs text-slate-500 font-medium mb-3">Lieber direkt persönlich schreiben?</p>
            <a href="https://wa.me/4917684156542?text=Hallo%20Sami,%20ich%20m%C3%B6chte%20gerne%20ein%20kostenloses%20Erstgespr%C3%A4ch%20vereinbaren!" target="_blank" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#25D366] hover:bg-[#20bd5a] text-white font-extrabold text-xs shadow-md transition-transform transform hover:scale-105">
              <i class="fa-brands fa-whatsapp text-lg"></i>
              <span>Direkt auf WhatsApp schreiben</span>
            </a>
          </div>

        </div>

      </div>

    </div>
  </section>

  <!-- 15 — FOOTER (4 Spalten nach Vorgabe) -->
  <footer id="kontakt" class="bg-slate-950 text-slate-400 py-16 border-t border-slate-800 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 pb-12 border-b border-slate-800">
        
        <!-- Spalte 1: SOCCERPROF -->
        <div class="space-y-4">
          <div class="flex items-center gap-3">
            <img src="img/logo/F3-3.avif" alt="SoccerProf Academy Logo" class="h-9 w-auto object-contain">
            <span class="text-white font-black text-lg tracking-tight">SOCCER<span class="text-[#E63946]">PROF</span> ACADEMY</span>
          </div>
          <p class="text-xs text-slate-400 leading-relaxed">
            Individuelles Fußballtraining für Kinder, Jugendliche und ambitionierte Talente in Hamburg. DFB- &amp; UEFA-B-Lizenzstandard.
          </p>
          <div class="text-xs text-slate-400">
            <i class="fa-solid fa-location-dot text-[#D4AF37] mr-1.5"></i>Öjendorfer Weg 80, 22119 Hamburg
          </div>
          <div class="flex items-center gap-3 pt-2">
            <a href="https://wa.me/4917684156542" target="_blank" class="w-8 h-8 rounded-full bg-slate-800 text-[#25D366] flex items-center justify-center hover:bg-[#25D366] hover:text-white transition-colors" aria-label="WhatsApp">
              <i class="fa-brands fa-whatsapp"></i>
            </a>
            <a href="tel:+4917684156542" class="w-8 h-8 rounded-full bg-slate-800 text-[#D4AF37] flex items-center justify-center hover:bg-[#D4AF37] hover:text-slate-900 transition-colors" aria-label="Telefon">
              <i class="fa-solid fa-phone"></i>
            </a>
          </div>
        </div>

        <!-- Spalte 2: TRAINING -->
        <div class="space-y-3">
          <h4 class="text-white font-extrabold text-sm uppercase tracking-wider">Training</h4>
          <ul class="space-y-2 text-xs">
            <li><a href="#training" class="hover:text-white transition-colors">Einzeltraining (1:1)</a></li>
            <li><a href="#training" class="hover:text-white transition-colors">Kleingruppentraining (2–5)</a></li>
            <li><a href="#training" class="hover:text-white transition-colors">Mannschaftstraining</a></li>
            <li><a href="#methode" class="hover:text-white transition-colors">Trainingsmethode</a></li>
            <li><a href="#preise" class="hover:text-white transition-colors">Preise &amp; Pakete</a></li>
          </ul>
        </div>

        <!-- Spalte 3: UNTERNEHMEN -->
        <div class="space-y-3">
          <h4 class="text-white font-extrabold text-sm uppercase tracking-wider">Unternehmen</h4>
          <ul class="space-y-2 text-xs">
            <li><a href="#ueber-uns" class="hover:text-white transition-colors">Über uns</a></li>
            <li><a href="#ueber-uns" class="hover:text-white transition-colors">Trainer (Sami Ghaouar)</a></li>
            <li><a href="#training" class="hover:text-white transition-colors">Veranstaltungen &amp; Camps</a></li>
            <li><a href="#faq" class="hover:text-white transition-colors">Häufige Fragen (FAQ)</a></li>
            <li><a href="#kontakt" class="hover:text-white transition-colors">Jobs &amp; Karriere</a></li>
          </ul>
        </div>

        <!-- Spalte 4: RECHTLICHES -->
        <div class="space-y-3">
          <h4 class="text-white font-extrabold text-sm uppercase tracking-wider">Rechtliches</h4>
          <ul class="space-y-2 text-xs">
            <li><a href="#kontakt" class="hover:text-white transition-colors">Impressum</a></li>
            <li><a href="#kontakt" class="hover:text-white transition-colors">Datenschutz</a></li>
            <li><a href="#kontakt" class="hover:text-white transition-colors">AGB</a></li>
            <li><a href="#kontakt" class="hover:text-white transition-colors">Widerrufsbelehrung</a></li>
          </ul>
        </div>

      </div>

      <!-- Bottom Bar -->
      <div class="pt-8 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-500 gap-4">
        <div>
          © 2026 SoccerProf Academy Hamburg – Sami Ghaouar. Alle Rechte vorbehalten.
        </div>
        <div>
          Individuelles Fußballtraining auf DFB- &amp; UEFA-B-Niveau in Hamburg.
        </div>
      </div>

    </div>
  </footer>

  <!-- MOBILE STICKY BOTTOM CONVERSION BAR -->
  <div class="sm:hidden fixed bottom-0 left-0 w-full z-40 bg-white/95 backdrop-blur-md border-t border-slate-200 px-4 py-2.5 flex items-center justify-between shadow-2xl">
    <div class="text-left">
      <div class="text-[11px] font-black text-slate-900">SoccerProf Hamburg</div>
      <div class="text-[9px] text-[#D4AF37] font-bold">1:1 &amp; Kleingruppe</div>
    </div>
    <a href="#erstgespraech" class="px-5 py-2 rounded-full bg-[#E63946] text-white font-black text-xs shadow-red-glow">
      Erstgespräch buchen
    </a>
  </div>

  <!-- SCRIPTS: THREE.JS, AOS & INTERACTION -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://unpkg.com/aos@next/dist/aos.js"></script>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      AOS.init({
        duration: 800,
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

    // FAQ Accordion Toggle
    document.querySelectorAll('.faq-button').forEach(button => {
      button.addEventListener('click', () => {
        const content = button.nextElementSibling;
        const icon = button.querySelector('.faq-icon');
        const isOpen = !content.classList.contains('hidden');
        
        document.querySelectorAll('.faq-content').forEach(c => c.classList.add('hidden'));
        document.querySelectorAll('.faq-icon').forEach(i => i.style.transform = 'rotate(0deg)');
        
        if (!isOpen) {
          content.classList.remove('hidden');
          if (icon) icon.style.transform = 'rotate(180deg)';
        }
      });
    });

    // Form submission handler
    function handleFormSubmit(e) {
      e.preventDefault();
      const successBox = document.getElementById('formSuccess');
      successBox.classList.remove('hidden');
      setTimeout(() => {
        window.location.href = "https://wa.me/4917684156542?text=" + encodeURIComponent("Hallo Sami, ich habe gerade eine Anfrage für ein kostenloses Erstgespräch auf deiner Website gestellt!");
      }, 1500);
    }

    // 3D Three.js Centered Round Particle Emblem with Scroll Dynamics
    (function initThreeJS() {
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

      const logoRadius = 2.5;
      const logoGeo = new THREE.CylinderGeometry(logoRadius, logoRadius, 0.2, 64);
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
        opacity: 1.0
      });

      const solidLogoMesh = new THREE.Mesh(logoGeo, [goldMat, logoFaceMat, logoFaceMat]);
      solidLogoMesh.rotation.x = Math.PI / 2;
      logoContainer.add(solidLogoMesh);

      const particleCount = 2400;
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

        const mult = 2.5 + Math.random() * 4.0;
        dispersedPositions[i * 3]     = x * mult + (Math.random() - 0.5) * 6;
        dispersedPositions[i * 3 + 1] = y * mult + (Math.random() - 0.5) * 6;
        dispersedPositions[i * 3 + 2] = z * mult + (Math.random() - 0.5) * 6;

        currentPositions[i * 3]     = x;
        currentPositions[i * 3 + 1] = y;
        currentPositions[i * 3 + 2] = z;

        const rc = Math.random();
        let col = cWhite;
        if (rc > 0.4) col = cGold;
        if (rc > 0.8) col = cRed;

        particleColors[i * 3]     = col.r;
        particleColors[i * 3 + 1] = col.g;
        particleColors[i * 3 + 2] = col.b;
      }

      const particleGeo = new THREE.BufferGeometry();
      particleGeo.setAttribute('position', new THREE.BufferAttribute(currentPositions, 3));
      particleGeo.setAttribute('color', new THREE.BufferAttribute(particleColors, 3));

      const particleMat = new THREE.PointsMaterial({
        size: 0.22,
        map: roundParticleMap,
        vertexColors: true,
        transparent: true,
        opacity: 0.9,
        depthWrite: false,
        blending: THREE.AdditiveBlending
      });
      const particlePoints = new THREE.Points(particleGeo, particleMat);
      logoContainer.add(particlePoints);

      const bgParticleCount = 180;
      const bgParticleGeo = new THREE.BufferGeometry();
      const bgParticlePos = new Float32Array(bgParticleCount * 3);
      for (let i = 0; i < bgParticleCount * 3; i += 3) {
        bgParticlePos[i]     = (Math.random() - 0.5) * 24;
        bgParticlePos[i + 1] = 5 - Math.random() * 55;
        bgParticlePos[i + 2] = (Math.random() - 0.5) * 12;
      }
      bgParticleGeo.setAttribute('position', new THREE.BufferAttribute(bgParticlePos, 3));
      const bgParticleMat = new THREE.PointsMaterial({
        size: 0.2,
        map: roundParticleMap,
        color: 0xD4AF37,
        transparent: true,
        opacity: 0.6,
        depthWrite: false,
        blending: THREE.AdditiveBlending
      });
      const bgParticles = new THREE.Points(bgParticleGeo, bgParticleMat);
      worldGroup.add(bgParticles);

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
        targetRotationY = x * 0.5;
        targetRotationX = y * 0.5;
      });

      function updateScroll() {
        const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
        const scrollPercent = window.scrollY / maxScroll;

        targetCameraY = -scrollPercent * 45;
        targetZoomZ = 9.5 + Math.sin(scrollPercent * Math.PI * 5) * 2.5;
        const cycle = Math.abs(Math.sin(scrollPercent * Math.PI * 6));
        targetDissolve = Math.pow(cycle, 1.5);
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
        logoFaceMat.opacity = Math.max(0.05, 1 - currentDissolve * 0.95);

        const posAttr = particleGeo.attributes.position;
        const posArr = posAttr.array;

        for (let i = 0; i < particleCount; i++) {
          const i3 = i * 3;
          posArr[i3]     = originPositions[i3]     + (dispersedPositions[i3]     - originPositions[i3])     * currentDissolve;
          posArr[i3 + 1] = originPositions[i3 + 1] + (dispersedPositions[i3 + 1] - originPositions[i3 + 1]) * currentDissolve;
          posArr[i3 + 2] = originPositions[i3 + 2] + (dispersedPositions[i3 + 2] - originPositions[i3 + 2]) * currentDissolve;
        }
        posAttr.needsUpdate = true;

        solidLogoMesh.rotation.z += 0.006;
        particlePoints.rotation.z += 0.004;
        bgParticles.rotation.y -= 0.0008;

        camera.position.y += (targetCameraY - camera.position.y) * 0.08;
        camera.position.z += (targetZoomZ - camera.position.z) * 0.08;

        worldGroup.rotation.y += (targetRotationY - worldGroup.rotation.y) * 0.05;
        worldGroup.rotation.x += (targetRotationX - worldGroup.rotation.x) * 0.05;

        renderer.render(scene, camera);
      }

      animate();
    })();
  </script>
</body>
</html>
"""

with open(r"c:\Users\mario\Desktop\newsoccerprof\index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("Successfully written refined SoccerProf Academy index.html with all real credentials!")
