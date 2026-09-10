import os

html_code = """<!DOCTYPE html>
<html lang="de" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SoccerProf Academy | Privater Fußballtrainer Hamburg – Sami Ghaouar</title>
  <meta name="description" content="SoccerProf bietet ein privates, professionelles und individuelles Fußballtraining für Kinder, Jugendliche und auch Erwachsene in Hamburg. Die perfekte Ergänzung zum Verein!">
  <meta name="keywords" content="Privater Fußballtrainer, individuelles Fußballtraining, Fußballtraining Hamburg, SoccerProf Academy, Sami Ghaouar, Einzeltraining Fußball, Kleingruppentraining">

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
      background: rgba(255, 255, 255, 0.90);
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
      background: rgba(255, 255, 255, 0.94);
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
    /* Steckbrief Styling */
    .steckbrief-badge {
      background: rgba(15, 23, 42, 0.05);
      border: 1px solid rgba(212, 175, 55, 0.3);
      border-radius: 12px;
      padding: 8px 14px;
    }
  </style>
</head>
<body class="bg-mesh relative grid-pattern antialiased text-slate-900 pb-16 sm:pb-0">

  <!-- 3D THREE.JS CANVAS BACKGROUND (CENTERED LOGO EMBLEM) -->
  <div id="threejs-container" class="fixed inset-0 w-full h-full pointer-events-none z-0"></div>

  <!-- Ambient Glow Orbs -->
  <div class="fixed top-20 left-10 w-96 h-96 bg-[#D4AF37]/10 rounded-full blur-3xl pointer-events-none -z-10 animate-float"></div>
  <div class="fixed bottom-20 right-10 w-[30rem] h-[30rem] bg-[#E63946]/10 rounded-full blur-3xl pointer-events-none -z-10"></div>

  <!-- NAVIGATION HEADER -->
  <header class="fixed top-0 left-0 w-full z-50 glass-nav transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      
      <!-- Logo -->
      <a href="#hero" class="flex items-center gap-3 group">
        <img src="img/logo/F3-3.avif" alt="SoccerProf Academy Logo" class="h-12 sm:h-14 w-auto object-contain group-hover:scale-105 transition-transform drop-shadow-sm">
      </a>

      <!-- Desktop Nav Links -->
      <nav class="hidden md:flex items-center gap-7 text-sm font-semibold text-slate-700">
        <a href="#warum" class="hover:text-[#E63946] transition-colors">Warum SoccerProf</a>
        <a href="#angebote" class="hover:text-[#E63946] transition-colors">Trainingsangebot</a>
        <a href="#ueber-uns" class="hover:text-[#E63946] transition-colors">Über uns</a>
        <a href="#steckbrief" class="hover:text-[#E63946] transition-colors">Der Trainer</a>
        <a href="#preise" class="hover:text-[#E63946] transition-colors">Preise</a>
        <a href="#kontakt" class="hover:text-[#E63946] transition-colors">Kontakt</a>
      </nav>

      <!-- Header Primary CTA -->
      <div class="hidden md:flex items-center gap-4">
        <a href="#kontakt" class="px-5 py-2.5 rounded-full bg-[#E63946] hover:bg-[#C52233] text-white font-bold text-sm shadow-red-glow hover:shadow-lg transition-all duration-300 transform hover:-translate-y-0.5">
          <i class="fa-solid fa-phone mr-2"></i>Kostenloses Beratungsgespräch
        </a>
      </div>

      <!-- Mobile Menu Toggle Button -->
      <button id="mobileMenuBtn" class="md:hidden text-slate-800 text-2xl focus:outline-none p-2" aria-label="Menu">
        <i class="fa-solid fa-bars"></i>
      </button>
    </div>

    <!-- Mobile Dropdown Navigation -->
    <div id="mobileMenu" class="hidden md:hidden bg-white/95 backdrop-blur-lg border-b border-slate-200 px-6 py-6 space-y-4 shadow-xl">
      <a href="#warum" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Warum SoccerProf</a>
      <a href="#angebote" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Trainingsangebot</a>
      <a href="#ueber-uns" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Über uns</a>
      <a href="#steckbrief" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Der Trainer</a>
      <a href="#preise" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Preise</a>
      <a href="#kontakt" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Kontakt</a>
      <a href="#kontakt" class="block w-full text-center py-3 rounded-full bg-[#E63946] text-white font-bold shadow-md mobile-link">
        Kostenloses Beratungsgespräch
      </a>
    </div>
  </header>

  <!-- 1. HERO SECTION (Exakt die Originaltexte von soccerprof.de) -->
  <section id="hero" class="relative pt-36 pb-20 md:pt-44 md:pb-28 overflow-hidden min-h-[90vh] flex items-center z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <!-- Left Hero Content -->
        <div class="lg:col-span-7 space-y-8 text-center lg:text-left">
          
          <!-- Tagline von soccerprof.de -->
          <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/95 border border-[#D4AF37] shadow-md backdrop-blur-md">
            <span class="w-2.5 h-2.5 rounded-full bg-[#D4AF37] animate-ping"></span>
            <span class="text-xs sm:text-sm font-extrabold tracking-wider text-slate-900 uppercase">
              FÜR KINDER, JUGENDLICHE UND ERWACHSENE
            </span>
          </div>

          <!-- Original Hauptüberschrift (Wort für Wort) -->
          <h1 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight leading-[1.15]">
            PRIVATER <span class="text-gradient-gold">FUßBALL-TRAINER</span> FÜR INDIVIDUELLES TRAINING FÜR <span class="relative inline-block text-slate-900">
              ANFÄNGER &amp; PROS.
              <svg class="absolute -bottom-2 left-0 w-full h-3 text-[#E63946]" viewBox="0 0 200 9" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M2 7C50 2 150 2 198 7" stroke="currentColor" stroke-width="4" stroke-linecap="round"/></svg>
            </span>
          </h1>

          <!-- Original Badge / Subtext von soccerprof.de -->
          <div class="inline-block p-4 rounded-2xl bg-white/90 backdrop-blur-md border border-slate-200/90 shadow-md">
            <div class="text-base sm:text-lg font-black text-slate-900 flex items-center justify-center lg:justify-start gap-2">
              <span>DIE PERFEKTE ERGÄNZUNG ZUM FUßBALL VEREIN</span>
              <span class="text-xl">👍 ⚽</span>
            </div>
            <p class="text-xs sm:text-sm text-slate-600 font-medium mt-1">
              SoccerProf Academy Hamburg und Umgebung · Individuelles Fußballtraining auf DFB- &amp; UEFA-B-Niveau.
            </p>
          </div>

          <!-- Buttons wie auf soccerprof.de -->
          <div class="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4 pt-2">
            <a href="#kontakt" class="w-full sm:w-auto px-8 py-4 rounded-full bg-[#E63946] hover:bg-[#C52233] text-white font-black text-base tracking-wide shadow-red-glow hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-1 flex items-center justify-center gap-3">
              <span>KONTAKT</span>
              <i class="fa-solid fa-arrow-right"></i>
            </a>
            <a href="#preise" class="w-full sm:w-auto px-8 py-4 rounded-full bg-white/90 hover:bg-slate-900 text-slate-900 hover:text-white border-2 border-slate-900 font-bold text-base transition-all duration-300 transform hover:-translate-y-1 shadow-sm flex items-center justify-center gap-2">
              <span>PREISE</span>
              <i class="fa-solid fa-tags text-xs"></i>
            </a>
          </div>

          <!-- Trust Leiste mit den realen Fakten -->
          <div class="pt-6 border-t border-slate-300/80 grid grid-cols-2 sm:grid-cols-4 gap-4 bg-white/70 p-4 rounded-2xl backdrop-blur-md border border-slate-200/60 shadow-sm">
            <div class="text-center lg:text-left">
              <div class="text-xl font-black text-slate-900">UEFA-B</div>
              <div class="text-[11px] text-slate-600 font-semibold uppercase">Trainer-Lizenz</div>
            </div>
            <div class="text-center lg:text-left">
              <div class="text-xl font-black text-[#D4AF37]">Seit 2012</div>
              <div class="text-[11px] text-slate-600 font-semibold uppercase">Trainererfahrung</div>
            </div>
            <div class="text-center lg:text-left">
              <div class="text-xl font-black text-[#E63946]">3 Standorte</div>
              <div class="text-[11px] text-slate-600 font-semibold uppercase">Hamburg &amp; Umgebung</div>
            </div>
            <div class="text-center lg:text-left">
              <div class="text-xl font-black text-slate-900">HSV</div>
              <div class="text-[11px] text-slate-600 font-semibold uppercase">Ausbildung</div>
            </div>
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
                    <div class="text-xs font-bold text-slate-900">SoccerProf Academy | Sami Ghaouar</div>
                    <div class="text-[11px] text-slate-500 font-medium">Öjendorfer Weg 80, 22119 Hamburg</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- 2. WARUM SOCCERPROF? (Originaltext von soccerprof.de) -->
  <section id="warum" class="py-20 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <div class="inline-block px-3 py-1 rounded-full bg-[#D4AF37]/10 text-[#D4AF37] font-extrabold text-xs uppercase tracking-widest border border-[#D4AF37]/30">
          Technik | Taktik | Kognitivtraining | Mentaltraining
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          WARUM SOCCERPROF?
        </h2>
        <p class="text-slate-700 font-medium text-base sm:text-lg leading-relaxed bg-white/80 p-6 rounded-3xl backdrop-blur-md border border-slate-200/80 shadow-sm text-left sm:text-center">
          Du suchst einen zuverlässigen und erfahrenen Fußballtrainer, der das individuelle Potenzial deines Kindes oder Teenagers erkennt und spielerisch fördert? Den hast du gefunden! Wir bei SoccerProf unterstützen talentierte Kinder und Jugendliche gezielt durch privates Konditions-, Taktik- und Mentaltraining. Immer mit dabei: <strong>Viel Herz und gesunder Menschenverstand</strong>. So stellen wir sicher, dass unsere Schützlinge ganz ungezwungen das Beste aus sich herausholen können. Als ideale Ergänzung zum Verein schaffen wir die Möglichkeit, dass Fußballtalente über sich hinauswachsen.
        </p>
      </div>

      <!-- 4 Säulen Kacheln -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <div class="glass-card p-6 rounded-3xl space-y-3" data-aos="fade-up" data-aos-delay="100">
          <div class="w-12 h-12 rounded-2xl bg-slate-900 text-[#D4AF37] flex items-center justify-center text-xl font-bold">
            <i class="fa-solid fa-futbol"></i>
          </div>
          <h3 class="text-lg font-black text-slate-900">Technik</h3>
          <p class="text-slate-600 text-xs leading-relaxed">
            Feinschliff an Ballannahme, Ballführung, Passpräzision, Beidfüßigkeit und sicherem Torabschluss.
          </p>
        </div>

        <div class="glass-card p-6 rounded-3xl space-y-3" data-aos="fade-up" data-aos-delay="200">
          <div class="w-12 h-12 rounded-2xl bg-[#E63946] text-white flex items-center justify-center text-xl font-bold shadow-red-glow">
            <i class="fa-solid fa-chess-board"></i>
          </div>
          <h3 class="text-lg font-black text-slate-900">Taktik</h3>
          <p class="text-slate-600 text-xs leading-relaxed">
            Stellungsspiel, Raumverständnis, Vororientierung und das richtige Verhalten im 1v1 defensiv wie offensiv.
          </p>
        </div>

        <div class="glass-card p-6 rounded-3xl space-y-3" data-aos="fade-up" data-aos-delay="300">
          <div class="w-12 h-12 rounded-2xl bg-slate-900 text-[#D4AF37] flex items-center justify-center text-xl font-bold">
            <i class="fa-solid fa-brain"></i>
          </div>
          <h3 class="text-lg font-black text-slate-900">Kognitivtraining</h3>
          <p class="text-slate-600 text-xs leading-relaxed">
            Visuelle Reizverarbeitung, schnelle Entscheidungsfindung unter Zeitdruck und Erhöhung des Handlungstempos.
          </p>
        </div>

        <div class="glass-card p-6 rounded-3xl space-y-3" data-aos="fade-up" data-aos-delay="400">
          <div class="w-12 h-12 rounded-2xl bg-[#E63946] text-white flex items-center justify-center text-xl font-bold shadow-red-glow">
            <i class="fa-solid fa-shield-halved"></i>
          </div>
          <h3 class="text-lg font-black text-slate-900">Mentaltraining</h3>
          <p class="text-slate-600 text-xs leading-relaxed">
            Selbstvertrauen aufbauen, Druck standhalten, Fokussierung und der Umgang mit sportlichen Rückschlägen.
          </p>
        </div>
      </div>

      <!-- Testimonial Quote von Angelika (Original soccerprof.de) -->
      <div class="mt-16 max-w-3xl mx-auto glass-card p-8 rounded-3xl border-2 border-[#D4AF37]/50 shadow-xl text-center space-y-4" data-aos="zoom-in">
        <div class="flex justify-center text-[#D4AF37] text-2xl gap-1">
          <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
        </div>
        <p class="text-base sm:text-xl font-bold text-slate-900 italic leading-relaxed">
          "Danke lieber Sami! Uns hat’s auch gefreut und die Kids sind ganz begeistert von dir 🤩. Weil du so ein cooler Fußballer bist 😎. Und vor allem nett 😊"
        </p>
        <div class="text-xs font-black uppercase text-[#E63946] tracking-widest">
          Angelika (Mutter) · SoccerProf Hamburg
        </div>
      </div>

      <!-- Banner: Kostenloses Beratungsgespräch -->
      <div class="mt-10 text-center">
        <div class="inline-flex flex-col sm:flex-row items-center gap-4 p-4 rounded-3xl bg-slate-900 text-white shadow-xl">
          <span class="text-sm font-bold pl-2"><i class="fa-solid fa-comments text-[#D4AF37] mr-2"></i>KOSTENLOSES BERATUNGSGESPRÄCH</span>
          <a href="tel:+4917684156542" class="px-6 py-2.5 rounded-full bg-[#E63946] hover:bg-[#C52233] text-white font-extrabold text-sm transition-all shadow-red-glow">
            <i class="fa-solid fa-phone mr-1.5"></i>+49 176 841 565 42
          </a>
        </div>
      </div>

    </div>
  </section>

  <!-- 3. UNSER TRAININGSANGEBOT (Originaltext & Formate von soccerprof.de) -->
  <section id="angebote" class="py-20 bg-white/70 backdrop-blur-md relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <div class="inline-block px-3 py-1 rounded-full bg-[#E63946]/10 text-[#E63946] font-extrabold text-xs uppercase tracking-widest border border-[#E63946]/30">
          Gezielte Förderung
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          UNSER TRAININGSANGEBOT
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg">
          Was möchten deine Kinder, Teenager oder auch du selbst lernen? Jedes Fußballtraining wird individuell auf die Stärken und Schwächen der Spieler:innen angepasst, um ihr maximales Potenzial abzurufen. <strong>Spaß in Verbindung mit Entwicklung steht für uns jederzeit an erster Stelle.</strong>
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 items-stretch">
        
        <!-- Angebot 1: Einzeltraining -->
        <div class="glass-card p-6 sm:p-8 rounded-3xl flex flex-col justify-between group hover:-translate-y-2 transition-all duration-300 border-2 border-[#D4AF37]" data-aos="fade-up" data-aos-delay="100">
          <div>
            <div class="w-full h-48 rounded-2xl overflow-hidden mb-6 shadow-md border border-slate-200/80 relative">
              <img src="img/packete/soccerprof-hamburg-kinder-jugendliche-fussballtraining.avif" alt="Einzeltraining SoccerProf Hamburg" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <span class="absolute top-3 right-3 px-3 py-1 rounded-full text-xs font-black uppercase bg-slate-900/90 text-[#D4AF37]">
                1:1 Training
              </span>
            </div>
            <h3 class="text-2xl font-black text-slate-900 mb-2">Einzeltraining</h3>
            <p class="text-slate-600 text-sm leading-relaxed mb-6">
              Dein Kind spielt in einem Fußballverein, möchte aber privat noch mehr trainieren? Bestimmte Disziplinen sollen gefördert werden? Dann bist du bei uns genau richtig! Unser individuelles Training richtet sich gänzlich nach euren Wünschen, um dich oder deine Kinder auf eurem persönlichen sportlichen Weg zu begleiten.
            </p>
          </div>
          <a href="#kontakt" class="w-full py-3.5 rounded-2xl bg-slate-900 hover:bg-[#D4AF37] text-white hover:text-slate-900 font-extrabold text-xs text-center block transition-all">
            MEHR ERFAHREN &amp; ANFRAGEN
          </a>
        </div>

        <!-- Angebot 2: Kleingruppentraining -->
        <div class="glass-card p-6 sm:p-8 rounded-3xl flex flex-col justify-between group hover:-translate-y-2 transition-all duration-300 border-2 border-[#E63946]" data-aos="fade-up" data-aos-delay="200">
          <div>
            <div class="w-full h-48 rounded-2xl overflow-hidden mb-6 shadow-md border border-slate-200/80 relative">
              <img src="img/packete/kleingruppe.avif" alt="Kleingruppentraining SoccerProf" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <span class="absolute top-3 right-3 px-3 py-1 rounded-full text-xs font-black uppercase bg-[#E63946] text-white">
                Feste 5er-Gruppen
              </span>
            </div>
            <h3 class="text-2xl font-black text-slate-900 mb-2">Kleingruppentraining</h3>
            <p class="text-slate-600 text-sm leading-relaxed mb-6">
              In festen 5er-Gruppen trainieren wir gemeinsam, um individuelle Stärken auszubauen und Schwächen zu verbessern. Die Gruppe fördert Motivation und Teamgeist. So lernen dein Kind oder du wichtiges Handwerkszeug, das in jedem Fußballspiel genutzt werden kann.
            </p>
          </div>
          <a href="#kontakt" class="w-full py-3.5 rounded-2xl bg-[#E63946] hover:bg-[#C52233] text-white font-extrabold text-xs text-center block transition-all shadow-red-glow">
            MEHR ERFAHREN &amp; ANFRAGEN
          </a>
        </div>

        <!-- Angebot 3: Mannschaftstraining -->
        <div class="glass-card p-6 sm:p-8 rounded-3xl flex flex-col justify-between group hover:-translate-y-2 transition-all duration-300" data-aos="fade-up" data-aos-delay="300">
          <div>
            <div class="w-full h-48 rounded-2xl overflow-hidden mb-6 shadow-md border border-slate-200/80 relative">
              <img src="img/packete/Fu%C3%9Fballspieler%20auf%20Bank.avif" alt="Mannschaftstraining SoccerProf" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <span class="absolute top-3 right-3 px-3 py-1 rounded-full text-xs font-black uppercase bg-slate-900/90 text-[#D4AF37]">
                Teams &amp; Klubs
              </span>
            </div>
            <h3 class="text-2xl font-black text-slate-900 mb-2">Mannschaftstraining</h3>
            <p class="text-slate-600 text-sm leading-relaxed mb-6">
              Deine Mannschaft möchte Taktik, Technik oder den Gruppenzusammenhalt stärken? Wir stellen ein individuelles privates Fußballtraining zusammen, um mit viel Spaß und Begeisterung Potenziale zu verbessern.
            </p>
          </div>
          <a href="#kontakt" class="w-full py-3.5 rounded-2xl bg-slate-900 hover:bg-[#D4AF37] text-white hover:text-slate-900 font-extrabold text-xs text-center block transition-all">
            MEHR ERFAHREN &amp; ANFRAGEN
          </a>
        </div>

        <!-- Angebot 4: Veranstaltungen & Camps -->
        <div class="glass-card p-6 sm:p-8 rounded-3xl flex flex-col justify-between group hover:-translate-y-2 transition-all duration-300" data-aos="fade-up" data-aos-delay="400">
          <div>
            <div class="w-full h-48 rounded-2xl overflow-hidden mb-6 shadow-md border border-slate-200/80 relative">
              <img src="img/bilderwebsite/ed34eb_bc3fa3f4a60144ee9c32042fd712a420~mv2.avif" alt="Veranstaltungen und Camps" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <span class="absolute top-3 right-3 px-3 py-1 rounded-full text-xs font-black uppercase bg-[#D4AF37] text-slate-900">
                Events &amp; Partys
              </span>
            </div>
            <h3 class="text-2xl font-black text-slate-900 mb-2">Veranstaltungen &amp; Camps</h3>
            <p class="text-slate-600 text-sm leading-relaxed mb-6">
              Wir veranstalten regelmäßig Fußballturniere, Events oder Camps für unsere SoccerProf-Spieler:innen. Auch unvergessliche Kindergeburtstage könnt ihr bei uns feiern.
            </p>
          </div>
          <a href="#kontakt" class="w-full py-3.5 rounded-2xl bg-slate-900 hover:bg-[#D4AF37] text-white hover:text-slate-900 font-extrabold text-xs text-center block transition-all">
            MEHR ERFAHREN &amp; ANFRAGEN
          </a>
        </div>

        <!-- Angebot 5: Training für Erwachsene -->
        <div class="glass-card p-6 sm:p-8 rounded-3xl flex flex-col justify-between group hover:-translate-y-2 transition-all duration-300 md:col-span-2" data-aos="fade-up" data-aos-delay="500">
          <div>
            <div class="w-full h-48 rounded-2xl overflow-hidden mb-6 shadow-md border border-slate-200/80 relative">
              <img src="img/bilderwebsite/ed34eb_62ddc206c2e5452697831563b63fb32e~mv2.avif" alt="Training für Erwachsene SoccerProf" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <span class="absolute top-3 right-3 px-3 py-1 rounded-full text-xs font-black uppercase bg-slate-900/90 text-[#D4AF37]">
                Adult Performance
              </span>
            </div>
            <h3 class="text-2xl font-black text-slate-900 mb-2">Training für Erwachsene</h3>
            <p class="text-slate-600 text-sm leading-relaxed mb-6">
              Unser individuelles Training für Erwachsene eignet sich optimal für Spieler:innen, die ihre Technik, Kraft-Ausdauer, ihr Stellungsspiel und ihre kognitiven Fähigkeiten verfeinern möchten. Ein professionelles Coachen unserer Trainer:innen motiviert noch weiter über die eigenen Grenzen zu wachsen. Unsere Ziele kennen keine Grenzen, egal wie alt und fit du aktuell bist.
            </p>
          </div>
          <a href="#kontakt" class="w-full py-3.5 rounded-2xl bg-slate-900 hover:bg-[#D4AF37] text-white hover:text-slate-900 font-extrabold text-xs text-center block transition-all">
            MEHR ERFAHREN &amp; ANFRAGEN
          </a>
        </div>

      </div>

    </div>
  </section>

  <!-- 4. ÜBER UNS (Exakt der Originaltext von soccerprof.de/aboutus) -->
  <section id="ueber-uns" class="py-20 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <div class="inline-block px-3 py-1 rounded-full bg-[#D4AF37]/10 text-[#D4AF37] font-extrabold text-xs uppercase tracking-widest border border-[#D4AF37]/30">
          Wer wir sind
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          ÜBER UNS
        </h2>
        <p class="text-slate-700 font-bold text-lg sm:text-xl">
          Unser Team aus Fußballbegeisterten, Sportpädagogen und leidenschaftlichen Trainern sorgt für Spaß, Motivation und Können!
        </p>
      </div>

      <!-- Unser Team Originaltext -->
      <div class="glass-card p-8 sm:p-12 rounded-3xl border border-slate-200/90 shadow-xl space-y-6 max-w-4xl mx-auto">
        <div class="flex items-center gap-3 text-[#E63946] font-black text-sm uppercase tracking-wider">
          <i class="fa-solid fa-users"></i>
          <span>UNSER TEAM</span>
        </div>
        <div class="space-y-4 text-slate-700 text-sm sm:text-base leading-relaxed">
          <p>
            Unser kleines Trainerteam besteht aus zwei Trainern. Wir haben uns darauf spezialisiert, jede:n Spieler:in individuell zu beraten und weiterzuentwickeln.
          </p>
          <p>
            Jeder Mensch ist einzigartig und genau so sollte jeder Fußballer und jede Fußballerin auch trainiert werden. Leider ist dies in Mannschaften kaum möglich. Außerdem nutzen immer weniger Kinder und Jugendliche die Möglichkeit, ihre Fähigkeiten auf Bolzplätzen zu verbessern.
          </p>
          <p class="p-4 rounded-2xl bg-amber-500/10 border-l-4 border-[#D4AF37] text-slate-900 font-medium">
            Daher ist es unser Ziel, jedem begeisterten Spieler und jeder engagierten Spielerin die Möglichkeit zu geben, sich in der <strong>SoccerProf Academy</strong> weiterzuentwickeln.
          </p>
          <p>
            Wir gehen intensiv auf die technischen, charakterlichen und körperlichen Stärken und Schwächen ein, um aus jedem einzelnen das maximale Potenzial herauszuholen. Auf deinen Wunsch hin beraten und unterstützen wir auch bei der Vereinssuche.
          </p>
        </div>
      </div>

    </div>
  </section>

  <!-- 5. DER TRAINER — STECKBRIEF SAMI GHAOUAR (Exakt wie im Audio gefordert!) -->
  <section id="steckbrief" class="py-20 bg-slate-900 text-white relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <div class="inline-block px-3 py-1 rounded-full bg-[#D4AF37]/20 text-[#D4AF37] font-extrabold text-xs uppercase border border-[#D4AF37]/30">
          Founder &amp; Head Coach
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black tracking-tight leading-tight">
          DER TRAINER — <span class="text-gradient-gold">STECKBRIEF</span>
        </h2>
        <p class="text-slate-300 font-medium text-sm sm:text-base italic">
          "Man lernt nie aus." Immer wieder begegnet uns dieser Spruch im Alltag, im Berufsleben und auch im Fußball trifft er definitiv zu. Damit das Weiterlernen gut klappt und vor allem richtig Spaß macht, unterstützen wir erfahrene Trainer Kinder, Jugendliche und Erwachsene – egal, ob Anfänger:innen oder Fortgeschrittene.
        </p>
      </div>

      <!-- DER RICHTIG GEILE STECKBRIEF (Card Layout) -->
      <div class="max-w-4xl mx-auto bg-gradient-to-br from-slate-800 to-slate-950 rounded-3xl border-2 border-[#D4AF37] shadow-2xl p-6 sm:p-10 relative overflow-hidden" data-aos="zoom-in">
        
        <!-- Background Glow -->
        <div class="absolute -right-20 -top-20 w-80 h-80 bg-[#D4AF37]/10 rounded-full blur-3xl pointer-events-none"></div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
          
          <!-- Foto Sami -->
          <div class="md:col-span-5 text-center">
            <div class="w-full h-80 sm:h-96 rounded-2xl overflow-hidden border-2 border-[#D4AF37]/60 shadow-xl relative group">
              <img src="img/sami/sami%20daumen%20hoch.avif" alt="Sami Ghaouar Founder UEFA-B-Lizenz" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
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
                <span class="px-3 py-1 rounded-full bg-[#E63946] text-white font-extrabold text-xs">Founder</span>
              </div>
              <p class="text-sm font-bold text-[#D4AF37] mt-1">
                UEFA-B-Lizenz-Trainer · Sami trainiert Kinder, Jugendliche und Erwachsene.
              </p>
            </div>

            <!-- Zitat von Sami -->
            <div class="p-4 rounded-2xl bg-slate-900/80 border border-[#D4AF37]/40 italic text-xs sm:text-sm text-slate-200">
              <i class="fa-solid fa-quote-left text-[#D4AF37] mr-2"></i>
              "Es macht mir Mega Spaß die Kids immer wieder zu pushen und ihnen ein Ziel vor dem Augen zu geben."
            </div>

            <!-- Steckbrief Daten-Grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
              <div class="steckbrief-badge">
                <span class="text-slate-400 block font-semibold">Höchste Spielklasse:</span>
                <span class="text-white font-black text-sm">Regional Liga</span>
              </div>
              <div class="steckbrief-badge">
                <span class="text-slate-400 block font-semibold">Position:</span>
                <span class="text-white font-black text-sm">Flügelspieler (Hamburger SV)</span>
              </div>
              <div class="steckbrief-badge sm:col-span-2">
                <span class="text-slate-400 block font-semibold">Coaching-Bereich:</span>
                <span class="text-white font-black">Kinder &amp; Jugendbereich und Erwachsene (vor allem Fortgeschrittene)</span>
              </div>
            </div>

            <!-- Ausbildung Liste -->
            <div class="space-y-1.5 pt-2">
              <div class="text-xs font-extrabold text-[#D4AF37] uppercase tracking-wider flex items-center gap-1.5">
                <i class="fa-solid fa-graduation-cap"></i> Ausbildung:
              </div>
              <ul class="text-xs text-slate-300 space-y-1 pl-4 list-disc">
                <li>B-Lizenz (2018)</li>
                <li>C-Lizenz (2014) und</li>
                <li>Torwart-Trainer-Lizenz</li>
                <li>DFB-Fortbildung an der Sportschule Duisburg-Wedau</li>
              </ul>
            </div>

            <!-- Erfahrung Liste -->
            <div class="space-y-1.5 pt-2">
              <div class="text-xs font-extrabold text-[#E63946] uppercase tracking-wider flex items-center gap-1.5">
                <i class="fa-solid fa-stopwatch"></i> Erfahrung:
              </div>
              <ul class="text-xs text-slate-300 space-y-1 pl-4 list-disc">
                <li>seit 2012 Individual- und Mannschaftstrainer</li>
                <li>Übungsleiter an Sportschulen für die Klassen 1 bis 13 Klasse</li>
                <li>gelernter Flügelspieler beim Hamburger SV</li>
              </ul>
            </div>

            <!-- CTA Button im Steckbrief -->
            <div class="pt-4">
              <a href="https://wa.me/4917684156542?text=Hallo%20Sami,%20ich%20habe%20deinen%20Steckbrief%20gesehen%20und%20m%C3%B6chte%20gerne%20trainieren!" target="_blank" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#25D366] hover:bg-[#20bd5a] text-white font-black text-xs shadow-lg transition-transform transform hover:scale-105">
                <i class="fa-brands fa-whatsapp text-lg"></i>
                <span>DIREKT MIT SAMI PER WHATSAPP SPRECHEN</span>
              </a>
            </div>

          </div>

        </div>

      </div>

    </div>
  </section>

  <!-- 6. PREISE (Kompakt & Transparent von soccerprof.de) -->
  <section id="preise" class="py-20 bg-white/70 backdrop-blur-md relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <div class="inline-block px-3 py-1 rounded-full bg-[#D4AF37]/10 text-[#D4AF37] font-extrabold text-xs uppercase tracking-widest border border-[#D4AF37]/30">
          Transparenz
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          PREISE &amp; FORMATE
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg">
          Qualitatives Training zu fairen Konditionen in Hamburg.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-stretch max-w-5xl mx-auto">
        
        <div class="glass-card p-8 rounded-3xl flex flex-col justify-between" data-aos="fade-up" data-aos-delay="100">
          <div>
            <h3 class="text-2xl font-black text-slate-900 mb-2">Erstberatung</h3>
            <div class="text-3xl font-black text-[#E63946] mb-4">Kostenlos</div>
            <p class="text-slate-600 text-xs mb-6">Persönliches Beratungsgespräch zur Abstimmung der Wünsche und Ziele.</p>
            <ul class="space-y-3 text-xs font-semibold text-slate-700 mb-8">
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Persönliche Beratung mit Sami</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Analyse der Fähigkeiten</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> 100% Unverbindlich</li>
            </ul>
          </div>
          <a href="#kontakt" class="w-full py-3.5 rounded-2xl bg-slate-900 text-white font-extrabold text-xs text-center block hover:bg-[#D4AF37] hover:text-slate-900 transition-colors">
            BERATUNG ANFRAGEN
          </a>
        </div>

        <div class="glass-card p-8 rounded-3xl flex flex-col justify-between border-2 border-[#D4AF37] shadow-gold-glow relative bg-white/95" data-aos="fade-up" data-aos-delay="200">
          <div class="absolute -top-3.5 left-1/2 -translate-x-1/2 bg-[#D4AF37] text-slate-900 font-black text-[10px] uppercase px-3 py-1 rounded-full">
            5er Gruppe
          </div>
          <div>
            <h3 class="text-2xl font-black text-slate-900 mb-2">Kleingruppe</h3>
            <div class="text-2xl font-black text-slate-900 mb-4">Auf Anfrage <span class="text-xs font-normal text-slate-500">/ Tarif</span></div>
            <p class="text-slate-600 text-xs mb-6">Gemeinsam trainieren in festen 5er-Gruppen für maximale Motivation.</p>
            <ul class="space-y-3 text-xs font-semibold text-slate-700 mb-8">
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#E63946]"></i> Max. 5 Spieler pro Gruppe</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#E63946]"></i> Hohe Dynamik &amp; Teamgeist</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#E63946]"></i> Ganzjährig Outdoor &amp; Indoor</li>
            </ul>
          </div>
          <a href="#kontakt" class="w-full py-3.5 rounded-2xl bg-[#E63946] text-white font-extrabold text-xs text-center block shadow-red-glow hover:bg-[#C52233] transition-colors">
            PREISE ANFRAGEN
          </a>
        </div>

        <div class="glass-card p-8 rounded-3xl flex flex-col justify-between" data-aos="fade-up" data-aos-delay="300">
          <div>
            <h3 class="text-2xl font-black text-slate-900 mb-2">Einzeltraining</h3>
            <div class="text-2xl font-black text-slate-900 mb-4">Auf Anfrage <span class="text-xs font-normal text-slate-500">/ 5er &amp; 10er</span></div>
            <p class="text-slate-600 text-xs mb-6">Volle Aufmerksamkeit für den persönlichen Feinschliff deines Kinds.</p>
            <ul class="space-y-3 text-xs font-semibold text-slate-700 mb-8">
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> 1:1 Betreuung mit Sami</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Video- &amp; Bewegungsanalyse</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-check text-[#D4AF37]"></i> Maßgeschneiderter Plan</li>
            </ul>
          </div>
          <a href="#kontakt" class="w-full py-3.5 rounded-2xl bg-slate-900 text-white font-extrabold text-xs text-center block hover:bg-[#D4AF37] hover:text-slate-900 transition-colors">
            PREISE ANFRAGEN
          </a>
        </div>

      </div>

    </div>
  </section>

  <!-- 7. KONTAKT & STANDORTE MIT KARTE (Vom Audio gefordert: viel besser + Karte!) -->
  <section id="kontakt" class="py-20 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <div class="inline-block px-3 py-1 rounded-full bg-[#E63946]/10 text-[#E63946] font-extrabold text-xs uppercase tracking-widest border border-[#E63946]/30">
          WIR FREUEN UNS AUF DEINE UNVERBINDLICHE ANFRAGE!
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          KONTAKT &amp; STANDORTE
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg">
          Bist du an einem Training für dich oder dein Kind interessiert? Gerne beraten wir dich persönlich.
        </p>
      </div>

      <!-- 3 Standorte Highlight Bar -->
      <div class="max-w-4xl mx-auto mb-12 p-5 rounded-3xl bg-slate-900 text-white flex flex-col sm:flex-row items-center justify-between gap-4 shadow-xl border border-[#D4AF37]/40">
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
        
        <!-- Left: Formular & Kontaktdaten -->
        <div class="lg:col-span-6 glass-card p-8 rounded-3xl shadow-xl space-y-6">
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

          <!-- Original Formular Felder von soccerprof.de/kontakt -->
          <form id="contactForm" onsubmit="handleFormSubmit(event)" class="space-y-4">
            <div>
              <label class="block text-xs font-extrabold text-slate-700 uppercase mb-1.5">Name *</label>
              <input type="text" required placeholder="Vor- und Nachname" class="w-full px-4 py-3 rounded-2xl bg-white border border-slate-200 text-slate-900 text-xs focus:outline-none focus:border-[#D4AF37] transition-all">
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-extrabold text-slate-700 uppercase mb-1.5">Email *</label>
                <input type="email" required placeholder="deine-email@beispiel.de" class="w-full px-4 py-3 rounded-2xl bg-white border border-slate-200 text-slate-900 text-xs focus:outline-none focus:border-[#D4AF37] transition-all">
              </div>
              <div>
                <label class="block text-xs font-extrabold text-slate-700 uppercase mb-1.5">Telefon</label>
                <input type="tel" placeholder="0176 ..." class="w-full px-4 py-3 rounded-2xl bg-white border border-slate-200 text-slate-900 text-xs focus:outline-none focus:border-[#D4AF37] transition-all">
              </div>
            </div>

            <div>
              <label class="block text-xs font-extrabold text-slate-700 uppercase mb-1.5">Betreff</label>
              <input type="text" placeholder="z.B. Einzeltraining für meinen Sohn" class="w-full px-4 py-3 rounded-2xl bg-white border border-slate-200 text-slate-900 text-xs focus:outline-none focus:border-[#D4AF37] transition-all">
            </div>

            <div>
              <label class="block text-xs font-extrabold text-slate-700 uppercase mb-1.5">Hier Nachricht eingeben...</label>
              <textarea rows="3" placeholder="Teile uns Deine Wünsche oder Fragen mit..." class="w-full px-4 py-3 rounded-2xl bg-white border border-slate-200 text-slate-900 text-xs focus:outline-none focus:border-[#D4AF37] transition-all"></textarea>
            </div>

            <button type="submit" class="w-full py-3.5 rounded-2xl bg-[#E63946] hover:bg-[#C52233] text-white font-black text-sm shadow-red-glow hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-0.5 flex items-center justify-center gap-2">
              <i class="fa-solid fa-paper-plane"></i>
              <span>absenden</span>
            </button>

            <!-- Success notification box -->
            <div id="formSuccess" class="hidden p-3.5 rounded-2xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-700 text-center font-bold text-xs">
              <i class="fa-solid fa-circle-check mr-2"></i>Vielen Dank für die Nachricht! Sami meldet sich in Kürze bei dir.
            </div>
          </form>

          <!-- WhatsApp Schnellbutton -->
          <div class="pt-2 text-center">
            <a href="https://wa.me/4917684156542?text=Hallo%20Sami,%20ich%20interessiere%20mich%20f%C3%BCr%20ein%20Training%20bei%20der%20SoccerProf%20Academy!" target="_blank" class="w-full py-3 rounded-2xl bg-[#25D366] hover:bg-[#20bd5a] text-white font-extrabold text-xs flex items-center justify-center gap-2 shadow-md transition-all">
              <i class="fa-brands fa-whatsapp text-lg"></i>
              <span>Direkt über WhatsApp kontaktieren</span>
            </a>
          </div>

        </div>

        <!-- Right: Interaktive Karte & Standort-Übersicht (Vom Audio gefordert!) -->
        <div class="lg:col-span-6 space-y-6">
          
          <!-- Google Maps Embed Karte für Öjendorfer Weg 80, Hamburg -->
          <div class="glass-card rounded-3xl overflow-hidden border-2 border-[#D4AF37]/60 shadow-xl relative">
            <div class="p-4 bg-slate-900 text-white flex items-center justify-between">
              <div class="flex items-center gap-2 text-xs font-bold">
                <i class="fa-solid fa-map-pin text-[#E63946] text-sm"></i>
                <span>Hauptstützpunkt: Öjendorfer Weg 80, 22119 Hamburg</span>
              </div>
              <span class="text-[10px] bg-[#D4AF37]/20 text-[#D4AF37] px-2.5 py-0.5 rounded-full font-extrabold">Billstedt</span>
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
                <i class="fa-solid fa-car text-[#D4AF37] mr-1"></i> Gut erreichbar über Horner Rennbahn &amp; B5
              </div>
              <a href="https://maps.google.com/?q=%C3%96jendorfer%20Weg%2080,%2022119%20Hamburg" target="_blank" class="px-4 py-1.5 rounded-xl bg-slate-900 text-white font-bold text-[11px] hover:bg-[#E63946] transition-colors">
                In Google Maps öffnen <i class="fa-solid fa-arrow-up-right-from-square ml-1"></i>
              </a>
            </div>
          </div>

          <!-- Standorte Kacheln -->
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div class="glass-card p-4 rounded-2xl text-center border-l-4 border-[#E63946]">
              <div class="font-extrabold text-xs text-slate-900">Billstedt</div>
              <div class="text-[11px] text-slate-500 mt-0.5">Öjendorfer Weg 80</div>
              <span class="text-[9px] text-[#D4AF37] font-bold">Hauptplatz</span>
            </div>
            <div class="glass-card p-4 rounded-2xl text-center border-l-4 border-[#D4AF37]">
              <div class="font-extrabold text-xs text-slate-900">Reinbek</div>
              <div class="text-[11px] text-slate-500 mt-0.5">Schleswig-Holstein</div>
              <span class="text-[9px] text-slate-500 font-bold">Zusatz-Standort</span>
            </div>
            <div class="glass-card p-4 rounded-2xl text-center border-l-4 border-slate-900">
              <div class="font-extrabold text-xs text-slate-900">Eimsbüttel</div>
              <div class="text-[11px] text-slate-500 mt-0.5">Hamburg West</div>
              <span class="text-[9px] text-slate-500 font-bold">Indoor / Kunstrasen</span>
            </div>
          </div>

        </div>

      </div>

    </div>
  </section>

  <!-- 8. FOOTER (Exakt wie im Original) -->
  <footer class="bg-slate-950 text-slate-400 py-16 border-t border-slate-800 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 pb-12 border-b border-slate-800">
        
        <!-- Spalte 1: SOCCERPROF -->
        <div class="space-y-4">
          <div class="flex items-center gap-3">
            <img src="img/logo/F3-3.avif" alt="SoccerProf Academy Logo" class="h-9 w-auto object-contain">
            <span class="text-white font-black text-lg tracking-tight">SOCCER<span class="text-[#E63946]">PROF</span> ACADEMY</span>
          </div>
          <p class="text-xs text-slate-400 leading-relaxed">
            SoccerProf bietet ein privates, professionelles und individuelles Fußballtraining für Kinder, Jugendliche und auch Erwachsene in Hamburg und Umgebung.
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
            <li><a href="#angebote" class="hover:text-white transition-colors">Einzeltraining</a></li>
            <li><a href="#angebote" class="hover:text-white transition-colors">Kleingruppentraining</a></li>
            <li><a href="#angebote" class="hover:text-white transition-colors">Mannschaftstraining</a></li>
            <li><a href="#angebote" class="hover:text-white transition-colors">Training für Erwachsene</a></li>
            <li><a href="#preise" class="hover:text-white transition-colors">Preise &amp; Tarife</a></li>
          </ul>
        </div>

        <!-- Spalte 3: UNTERNEHMEN -->
        <div class="space-y-3">
          <h4 class="text-white font-extrabold text-sm uppercase tracking-wider">Über SoccerProf</h4>
          <ul class="space-y-2 text-xs">
            <li><a href="#ueber-uns" class="hover:text-white transition-colors">Über uns</a></li>
            <li><a href="#steckbrief" class="hover:text-white transition-colors">Der Trainer (Sami Ghaouar)</a></li>
            <li><a href="#angebote" class="hover:text-white transition-colors">Veranstaltungen &amp; Camps</a></li>
            <li><a href="#kontakt" class="hover:text-white transition-colors">Jobs &amp; Karriere</a></li>
            <li><a href="#kontakt" class="hover:text-white transition-colors">Kontakt &amp; Standorte</a></li>
          </ul>
        </div>

        <!-- Spalte 4: RECHTLICHES -->
        <div class="space-y-3">
          <h4 class="text-white font-extrabold text-sm uppercase tracking-wider">Rechtliches</h4>
          <ul class="space-y-2 text-xs">
            <li><a href="#kontakt" class="hover:text-white transition-colors">Impressum</a></li>
            <li><a href="#kontakt" class="hover:text-white transition-colors">Datenschutzrichtlinie</a></li>
            <li><a href="#kontakt" class="hover:text-white transition-colors">Cookie-Richtlinie</a></li>
          </ul>
        </div>

      </div>

      <!-- Bottom Bar -->
      <div class="pt-8 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-500 gap-4">
        <div>
          © 2026 by SoccerProf Academy. | Sami Ghaouar
        </div>
        <div>
          DIE PERFEKTE ERGÄNZUNG ZUM FUßBALL VEREIN 👍 ⚽
        </div>
      </div>

    </div>
  </footer>

  <!-- MOBILE STICKY BOTTOM BAR -->
  <div class="sm:hidden fixed bottom-0 left-0 w-full z-40 bg-white/95 backdrop-blur-md border-t border-slate-200 px-4 py-2.5 flex items-center justify-between shadow-2xl">
    <div class="text-left">
      <div class="text-[11px] font-black text-slate-900">SoccerProf Academy</div>
      <div class="text-[9px] text-[#D4AF37] font-bold">Sami Ghaouar Hamburg</div>
    </div>
    <a href="tel:+4917684156542" class="px-4 py-2 rounded-full bg-[#E63946] text-white font-black text-xs shadow-red-glow flex items-center gap-1.5">
      <i class="fa-solid fa-phone"></i>
      <span>Jetzt anrufen</span>
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

    // Form submission handler
    function handleFormSubmit(e) {
      e.preventDefault();
      const successBox = document.getElementById('formSuccess');
      successBox.classList.remove('hidden');
      setTimeout(() => {
        window.location.href = "https://wa.me/4917684156542?text=" + encodeURIComponent("Hallo Sami, ich habe gerade eine Anfrage auf deiner SoccerProf-Website gesendet!");
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

print("Authentic SoccerProf website successfully built!")
