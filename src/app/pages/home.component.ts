import { Component, OnInit, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `

    <!-- ══════════════════════════════════════════════
         HERO SECTION (FULLSCREEN 100VH ON DESKTOP)
         ══════════════════════════════════════════════ -->
    <section class="relative bg-white min-h-[calc(100vh-80px)] lg:min-h-screen pt-24 pb-16 lg:pt-24 lg:pb-16 flex flex-col justify-center border-b border-slate-100 overflow-hidden">

      <!-- Subtle background grid -->
      <div class="absolute inset-0 opacity-[0.03] pointer-events-none"
        style="background-image: linear-gradient(#0F172A 1px, transparent 1px),
                                 linear-gradient(90deg, #0F172A 1px, transparent 1px);
               background-size: 44px 44px;">
      </div>

      <div class="sp-container relative z-10 w-full my-auto">
        <!-- TOP GRID: Left Text Content + Right Photo Card -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-stretch">

          <!-- LEFT: Text Content -->
          <div class="lg:col-span-7 xl:col-span-6 flex flex-col justify-between">
            <div>
              <div class="sub-title mb-3">
                HAMBURG · KINDER, JUGENDLICHE & AMBITIONIERTE SPIELER
              </div>

              <!-- Headline with "INDIVIDUELLES TRAINING" in Gold & DFB Underline -->
              <h1 class="hero-title mb-4">
                PRIVATER FUßBALL-TRAINER FÜR 
                <span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-500 via-yellow-500 to-amber-600 font-black">INDIVIDUELLES TRAINING</span> 
                FÜR 
                <span class="relative inline-block whitespace-nowrap">
                  <span class="relative z-10 text-slate-950">ANFÄNGER & PROS</span>
                  <!-- DFB-inspirierter Gold-Strich -->
                  <svg class="absolute -bottom-1.5 left-0 w-full h-3 -z-0 pointer-events-none" viewBox="0 0 240 12" fill="none" preserveAspectRatio="none">
                    <defs>
                      <linearGradient id="dfbGoldGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" stop-color="#F59E0B" />
                        <stop offset="50%" stop-color="#FCD34D" />
                        <stop offset="100%" stop-color="#D97706" />
                      </linearGradient>
                    </defs>
                    <path d="M 3 8.5 C 70 2.5, 160 2.5, 237 7 C 170 4.5, 80 5.5, 3 9.5" stroke="url(#dfbGoldGrad)" stroke-width="4.5" stroke-linecap="round" />
                  </svg>
                </span>.
              </h1>

              <p class="text-base text-slate-600 leading-relaxed mb-6 max-w-xl">
                Individuelles Fußballtraining für Kinder, Jugendliche und ambitionierte Spieler in Hamburg – abgestimmt auf die Stärken, Ziele und Entwicklung jedes Spielers. Einzeltraining und Kleingruppentraining als professionelle Ergänzung zum Vereinstraining.
              </p>

              <!-- Coach Mesut Style Buttons in Rot -->
              <div class="flex flex-wrap gap-4 items-center">
                <a routerLink="/kontakt" class="btn">
                  <span>Jetzt Probetraining anfragen</span>
                  <i class="fa-solid fa-arrow-right text-xs"></i>
                </a>
                <a routerLink="/preise" class="btn btn-outline">
                  <span>Trainingspakete entdecken</span>
                </a>
              </div>
            </div>
          </div>

          <!-- RIGHT: Visual Column (Starts at subtitle, ends right at bottom of buttons) -->
          <div class="lg:col-span-5 xl:col-span-6 relative">
            <div class="relative max-w-md mx-auto lg:max-w-none h-full">
              
              <!-- Coach Action Visual (Sami mit Taktiktafel) -->
              <div class="rounded-3xl overflow-hidden shadow-xl border border-slate-200 relative bg-slate-100 w-full h-full min-h-[380px] lg:min-h-full">
                <img src="img/sami/Ich Taktiktafel.avif"
                  alt="Coach Sami Ghaouar – Taktik & Coaching Hamburg"
                  class="w-full h-full object-cover object-top">
                <div class="absolute inset-0 bg-gradient-to-t from-slate-950/60 via-transparent to-transparent"></div>
                
                <!-- Bottom Coach Bar -->
                <div class="absolute bottom-4 left-4 right-4">
                  <div class="bg-white/95 backdrop-blur-md rounded-2xl p-3.5 flex items-center justify-between shadow-lg border border-white/60">
                    <div class="flex items-center gap-3">
                      <img src="img/logo/F3-3.avif" alt="SoccerProf" class="h-8 w-auto flex-shrink-0">
                      <div>
                        <p class="text-slate-900 font-extrabold text-sm leading-tight">Sami Ghaouar</p>
                        <p class="text-slate-500 text-xs">Head Coach · Lizenzierter Privattrainer</p>
                      </div>
                    </div>
                    <span class="sp-badge-theme text-[10px]">
                      Hamburg
                    </span>
                  </div>
                </div>
              </div>

              <!-- Top floating DFB badge -->
              <div class="absolute -top-3 -right-3 bg-white border border-slate-200 rounded-2xl p-2.5 sm:p-3 shadow-xl hidden sm:flex items-center gap-2.5 z-10">
                <div class="w-9 h-9 rounded-xl bg-slate-50 border border-slate-100 flex items-center justify-center p-1.5 flex-shrink-0">
                  <img src="img/logo/DFB-Logo-4.svg" alt="DFB zertifiziert" class="w-full h-full object-contain">
                </div>
                <div>
                  <p class="text-slate-900 font-bold text-xs">DFB-zertifiziert</p>
                  <p class="text-slate-500 text-[10px]">Gezielte Talentförderung</p>
                </div>
              </div>

            </div>
          </div>

        </div>

        <!-- STATS ROW: Right below the grid, right where the image ends! -->
        <div class="mt-8 lg:mt-10 pt-6 border-t border-slate-200">
          <div class="grid grid-cols-3 gap-6 max-w-lg">
            <div>
              <p class="font-heading font-black text-2xl sm:text-3xl text-slate-900">100<span class="text-red-600">%</span></p>
              <p class="text-xs font-bold text-slate-500 uppercase tracking-wider mt-0.5">Individuell</p>
            </div>
            <div class="border-l border-slate-200 pl-6">
              <p class="font-heading font-black text-2xl sm:text-3xl text-slate-900">1:1</p>
              <p class="text-xs font-bold text-slate-500 uppercase tracking-wider mt-0.5">Intensiv-Fokus</p>
            </div>
            <div class="border-l border-slate-200 pl-6">
              <p class="font-heading font-black text-2xl sm:text-3xl text-red-600">Hamburg</p>
              <p class="text-xs font-bold text-slate-500 uppercase tracking-wider mt-0.5">Flexibler Ort</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Coach Mesut Torn Paper Divider Bottom -->
      <div class="sec-shape-bottom">
        <img src="img/sec-shape-bottom.png" alt="divider">
      </div>
    </section>

    <!-- ══════════════════════════════════════════════
         ÜBER MICH / MISSION TABS (COACH MESUT STYLE)
         ══════════════════════════════════════════════ -->
    <section class="sp-section bg-slate-50 border-b border-slate-200 relative pt-20">
      <div class="sp-container">

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center">

          <!-- Image column -->
          <div class="lg:col-span-5 order-2 lg:order-1">
            <div class="relative max-w-md mx-auto">
              <div class="rounded-3xl overflow-hidden shadow-xl border border-slate-200 aspect-[3/4] relative">
                <img src="img/sami/sami.jpg"
                  alt="Sami Ghaouar – Privater Fußballtrainer Hamburg"
                  class="w-full h-full object-cover object-top">
                <div class="absolute inset-0 bg-gradient-to-t from-slate-950/70 via-transparent to-transparent"></div>

                <div class="absolute bottom-6 left-6 right-6">
                  <div class="bg-white/95 backdrop-blur-md rounded-2xl p-4 flex items-center justify-between">
                    <div>
                      <p class="text-slate-900 font-extrabold text-base">Sami Ghaouar</p>
                      <p class="text-slate-600 text-xs">Gründer & Head Coach</p>
                    </div>
                    <img src="img/logo/F3-3.avif" alt="SoccerProf" class="h-9 w-auto">
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Text column with Interactive Tabs -->
          <div class="lg:col-span-7 order-1 lg:order-2">
            <div class="sub-title">MEHR ÜBER MICH!</div>
            <h2 class="font-heading text-3xl sm:text-4xl text-slate-900 mb-6">
              Entfalte dein volles Potenzial und erreiche deine Ziele.
            </h2>

            <p class="text-slate-600 text-base leading-relaxed mb-6">
              Willkommen bei SoccerProf Academy – deiner Anlaufstelle für individuelles Technik- und Athletiktraining in Hamburg. Ob junger Nachwuchsspieler, ambitionierter Amateur oder angehender Profi: Gemeinsam arbeiten wir gezielt an deiner Ballbeherrschung, Schnelligkeit und mentalen Wettkampfstärke.
            </p>

            <!-- Coach Mesut Style Tabs: Mission / Vision / Ziel -->
            <div class="flex flex-wrap gap-2 mb-6">
              <button (click)="activeTab.set('mission')"
                [class.active]="activeTab() === 'mission'"
                class="mesut-tab-btn">
                Meine Mission
              </button>
              <button (click)="activeTab.set('vision')"
                [class.active]="activeTab() === 'vision'"
                class="mesut-tab-btn">
                Meine Vision
              </button>
              <button (click)="activeTab.set('ziel')"
                [class.active]="activeTab() === 'ziel'"
                class="mesut-tab-btn">
                Mein Ziel
              </button>
            </div>

            <!-- Tab Content -->
            <div class="bg-white border border-slate-200 rounded-2xl p-6 mb-8 shadow-sm">
              <div *ngIf="activeTab() === 'mission'" class="flex items-start gap-4">
                <div class="w-12 h-12 rounded-xl bg-red-50 text-red-600 flex items-center justify-center text-xl flex-shrink-0">
                  <i class="fa-solid fa-bullseye"></i>
                </div>
                <div>
                  <h4 class="font-heading font-bold text-slate-900 mb-1">Gezielte Talentförderung</h4>
                  <p class="text-slate-600 text-sm leading-relaxed">
                    Meine Mission ist es, jedem Spieler durch maßgeschneiderte Einheiten genau die technische und taktische Sicherheit zu geben, die im normalen Vereinstraining oft zu kurz kommt.
                  </p>
                </div>
              </div>

              <div *ngIf="activeTab() === 'vision'" class="flex items-start gap-4">
                <div class="w-12 h-12 rounded-xl bg-red-50 text-red-600 flex items-center justify-center text-xl flex-shrink-0">
                  <i class="fa-solid fa-eye"></i>
                </div>
                <div>
                  <h4 class="font-heading font-bold text-slate-900 mb-1">Ganzheitliche Entwicklung</h4>
                  <p class="text-slate-600 text-sm leading-relaxed">
                    Meine Vision ist eine Academy, die Athleten nicht nur technisch besser macht, sondern auch ihre Spielintelligenz, mentale Resilienz und Begeisterung für den Sport nachhaltig entfacht.
                  </p>
                </div>
              </div>

              <div *ngIf="activeTab() === 'ziel'" class="flex items-start gap-4">
                <div class="w-12 h-12 rounded-xl bg-red-50 text-red-600 flex items-center justify-center text-xl flex-shrink-0">
                  <i class="fa-solid fa-mountain"></i>
                </div>
                <div>
                  <h4 class="font-heading font-bold text-slate-900 mb-1">Messbare Fortschritte</h4>
                  <p class="text-slate-600 text-sm leading-relaxed">
                    Mein Ziel ist es, dich Schritt für Schritt auf dein nächstes Leistungslevel zu heben – mit sichtbaren Erfolgen bei Ballkontrolle, Zweikampfverhalten und Spielübersicht.
                  </p>
                </div>
              </div>
            </div>

            <!-- Bottom CTA Button & Email Info (Coach Mesut Style) -->
            <div class="flex flex-wrap items-center gap-6">
              <a routerLink="/kontakt" class="btn">
                <span>Vereinbare einen Termin!</span>
                <i class="fa-solid fa-arrow-right text-xs"></i>
              </a>

              <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center text-red-600">
                  <i class="fa-solid fa-envelope"></i>
                </div>
                <div>
                  <p class="text-xs text-slate-500 font-semibold">Noch Fragen? Schreib mir direkt:</p>
                  <a href="mailto:info@soccerprof.de" class="text-sm font-bold text-slate-900 hover:text-red-600 transition-colors">
                    info&#64;soccerprof.de
                  </a>
                </div>
              </div>
            </div>

          </div>

        </div>

      </div>
    </section>

    <!-- ══════════════════════════════════════════════
         TRAININGSPAKETE SECTION (COACH MESUT 4-KARTEN)
         ══════════════════════════════════════════════ -->
    <section class="sp-section bg-white border-b border-slate-100">
      <div class="sp-container">

        <!-- Section Header -->
        <div class="text-center max-w-2xl mx-auto mb-16">
          <div class="sub-title justify-center">UNSERE ANGEBOTE</div>
          <h2 class="font-heading text-3xl sm:text-4xl text-slate-900 mb-4">
            Wähle das passende Trainingspaket für dich
          </h2>
          <p class="text-slate-600 text-base">
            Professionelle Trainingsformate für maximale Entwicklung und messbare Leistungssteigerung.
          </p>
        </div>

        <!-- 4 Cards Grid (with Featured Dark Card like Coach Mesut) -->
        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">

          <!-- 1. Einzeltraining -->
          <div class="mesut-package-card">
            <div class="package-icon-box">
              <i class="fa-solid fa-user"></i>
            </div>
            <span class="sp-badge-theme text-[10px] w-fit mb-3">1:1 Exklusiv</span>
            <h3 class="font-heading text-2xl font-black text-slate-900 mb-2">Einzeltraining</h3>
            <p class="text-slate-600 text-sm leading-relaxed mb-6">
              Maximale Aufmerksamkeit. Detaillierter Fokus auf Beidfüßigkeit, Schusstechnik und Handlungsschnelligkeit.
            </p>
            <div class="mt-auto pt-6 border-t border-slate-100 mb-6">
              <p class="text-3xl font-black text-slate-900">ab 40€ <span class="text-xs font-normal text-slate-500">/ Einheit</span></p>
            </div>
            <a routerLink="/einzeltraining" class="btn btn-block">
              <span>Jetzt buchen</span>
            </a>
          </div>

          <!-- 2. Kleingruppe (FEATURED DARK CARD LIKE COACH MESUT) -->
          <div class="mesut-package-card featured relative">
            <div class="absolute -top-3 right-6">
              <span class="bg-red-600 text-white font-bold text-[10px] tracking-wider uppercase px-3 py-1 rounded-full shadow-md">
                SEHR BELIEBT
              </span>
            </div>
            <div class="package-icon-box">
              <i class="fa-solid fa-users"></i>
            </div>
            <span class="bg-slate-800 text-red-400 font-bold text-[10px] uppercase px-2.5 py-1 rounded w-fit mb-3">
              2 bis 4 Spieler
            </span>
            <h3 class="font-heading text-2xl font-black mb-2">Kleingruppe</h3>
            <p class="text-sm leading-relaxed mb-6">
              Spielnahe Dynamik, 1-gegen-1 Situationen, Passschärfe und wettkampforientierte Übungen unter hohem Tempo.
            </p>
            <div class="mt-auto pt-6 border-t border-slate-800 mb-6">
              <p class="text-3xl font-black text-white">20–25€ <span class="text-xs font-normal text-slate-400">/ Spieler</span></p>
            </div>
            <a routerLink="/kleingruppe" class="btn btn-block">
              <span>Jetzt buchen</span>
            </a>
          </div>

          <!-- 3. Mannschaftstraining -->
          <div class="mesut-package-card">
            <div class="package-icon-box">
              <i class="fa-solid fa-shield-halved"></i>
            </div>
            <span class="sp-badge-theme text-[10px] w-fit mb-3">Vereinspaket</span>
            <h3 class="font-heading text-2xl font-black text-slate-900 mb-2">Mannschaft</h3>
            <p class="text-slate-600 text-sm leading-relaxed mb-6">
              Spezifische Fördereinheiten für Jugend- und Herrenmannschaften zur Optimierung von Gruppentaktik & Athletik.
            </p>
            <div class="mt-auto pt-6 border-t border-slate-100 mb-6">
              <p class="text-3xl font-black text-slate-900">ab 90€ <span class="text-xs font-normal text-slate-500">/ Session</span></p>
            </div>
            <a routerLink="/mannschaft" class="btn btn-block">
              <span>Jetzt anfragen</span>
            </a>
          </div>

          <!-- 4. Powercamp -->
          <div class="mesut-package-card">
            <div class="package-icon-box">
              <i class="fa-solid fa-futbol"></i>
            </div>
            <span class="sp-badge-theme text-[10px] w-fit mb-3">Ferien-Event</span>
            <h3 class="font-heading text-2xl font-black text-slate-900 mb-2">Powercamp</h3>
            <p class="text-slate-600 text-sm leading-relaxed mb-6">
              Intensive Ferientage mit Turnieren, Videoanalyse, gesunder Verpflegung und SoccerProf Ausrüstung.
            </p>
            <div class="mt-auto pt-6 border-t border-slate-100 mb-6">
              <p class="text-3xl font-black text-slate-900">80€ <span class="text-xs font-normal text-slate-500">/ Tag</span></p>
            </div>
            <a routerLink="/veranstaltungen" class="btn btn-block">
              <span>Termine ansehen</span>
            </a>
          </div>

        </div>

        <!-- All pricing CTA link -->
        <div class="text-center mt-12">
          <a routerLink="/preise" class="btn btn-outline">
            <span>Alle Preise & Leistungsdetails</span>
            <i class="fa-solid fa-arrow-right text-xs"></i>
          </a>
        </div>

      </div>
    </section>

    <!-- ══════════════════════════════════════════════
         TRAININGSMETHODIK (4-PHASEN STRUKTUR)
         ══════════════════════════════════════════════ -->
    <section class="sp-section bg-slate-50 border-b border-slate-200">
      <div class="sp-container">

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center">

          <!-- Left: 4 Steps -->
          <div class="lg:col-span-6">
            <div class="sub-title">METHODIK & SYSTEM</div>
            <h2 class="font-heading text-3xl sm:text-4xl text-slate-900 mb-6">
              Die SoccerProf 4-Phasen-Methode
            </h2>
            <p class="text-slate-600 text-base leading-relaxed mb-8">
              Unser systematischer Trainingsansatz stellt sicher, dass jeder Spieler nachhaltig gefördert wird – von der initialen Analyse bis zur sicheren Umsetzung im Ligaspiel.
            </p>

            <div class="flex flex-col gap-4">
              <div *ngFor="let ph of phases; let i = index"
                class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 flex items-start gap-4 shadow-sm">
                <div class="w-10 h-10 rounded-xl bg-red-50 text-red-600 font-extrabold flex items-center justify-center text-sm flex-shrink-0 border border-red-100">
                  0{{ i + 1 }}
                </div>
                <div>
                  <p class="text-slate-900 font-bold text-base mb-0.5">{{ ph.title }}</p>
                  <p class="text-slate-600 text-sm leading-relaxed">{{ ph.desc }}</p>
                </div>
              </div>
            </div>

            <div class="mt-8">
              <a routerLink="/trainingsmethoden" class="btn">
                <span>Ausführliche Methodik entdecken</span>
                <i class="fa-solid fa-arrow-right text-xs"></i>
              </a>
            </div>
          </div>

          <!-- Right: Visual Collage -->
          <div class="lg:col-span-6">
            <div class="grid grid-cols-2 gap-4">
              <div class="rounded-2xl overflow-hidden shadow-md aspect-[3/4] col-span-1 row-span-2 relative">
                <img src="img/sami/Technik Fußstellung.avif" alt="Techniktraining" class="w-full h-full object-cover">
                <div class="absolute bottom-4 left-4 right-4">
                  <span class="bg-white/95 font-bold text-slate-900 text-xs px-3 py-1.5 rounded-lg shadow-sm">1. Technik</span>
                </div>
              </div>
              <div class="rounded-2xl overflow-hidden shadow-md aspect-square relative">
                <img src="img/sami/Athletiktraining.avif" alt="Athletiktraining" class="w-full h-full object-cover">
                <div class="absolute bottom-3 left-3 right-3">
                  <span class="bg-white/95 font-bold text-slate-900 text-xs px-3 py-1.5 rounded-lg shadow-sm">2. Athletik</span>
                </div>
              </div>
              <div class="rounded-2xl overflow-hidden shadow-md aspect-square relative">
                <img src="img/bilderwebsite/Fußballtraining im Freien.avif" alt="Taktik & Spielverständnis" class="w-full h-full object-cover">
                <div class="absolute bottom-3 left-3 right-3">
                  <span class="bg-white/95 font-bold text-slate-900 text-xs px-3 py-1.5 rounded-lg shadow-sm">3. Spielnähe</span>
                </div>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- ══════════════════════════════════════════════
         COACH MESUT STYLE BOOKING FORM SECTION IN ROT
         ══════════════════════════════════════════════ -->
    <section class="sp-section bg-white border-b border-slate-100">
      <div class="sp-container">

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch max-w-5xl mx-auto">

          <!-- Left: Red Highlights Card (Coach Mesut Style) -->
          <div class="lg:col-span-5 bg-red-600 text-white rounded-3xl p-8 sm:p-10 flex flex-col justify-between shadow-xl">
            <div>
              <span class="bg-white/20 text-white font-bold text-xs uppercase px-3 py-1 rounded-full mb-6 inline-block">
                Probetraining
              </span>
              <h3 class="font-heading text-2xl sm:text-3xl font-black mb-4 leading-tight">
                Vereinbare jetzt dein persönliches Probetraining
              </h3>
              <p class="text-red-100 text-sm leading-relaxed mb-8">
                Lerne Trainer Sami Ghaouar kennen und teste das SoccerProf Trainingskonzept unverbindlich auf dem Platz in Hamburg.
              </p>

              <div class="space-y-4">
                <div class="flex items-center gap-3">
                  <div class="w-7 h-7 rounded-full bg-white/20 flex items-center justify-center text-xs">✓</div>
                  <span class="text-sm font-semibold">Individuelle Potenzialanalyse</span>
                </div>
                <div class="flex items-center gap-3">
                  <div class="w-7 h-7 rounded-full bg-white/20 flex items-center justify-center text-xs">✓</div>
                  <span class="text-sm font-semibold">Maßgeschneiderte Übungsformen</span>
                </div>
                <div class="flex items-center gap-3">
                  <div class="w-7 h-7 rounded-full bg-white/20 flex items-center justify-center text-xs">✓</div>
                  <span class="text-sm font-semibold">Direktes Feedback & Förderplan</span>
                </div>
              </div>
            </div>

            <div class="mt-10 pt-6 border-t border-white/20 text-xs text-red-100">
              Antwortzeit garantiert innerhalb von 24 Stunden.
            </div>
          </div>

          <!-- Right: Booking Form -->
          <div class="lg:col-span-7 bg-slate-50 border border-slate-200 rounded-3xl p-8 sm:p-10 shadow-sm flex flex-col justify-center">
            <h4 class="font-heading font-black text-2xl text-slate-900 mb-2">Terminanfrage senden</h4>
            <p class="text-slate-600 text-sm mb-6">Fülle kurz die Angaben aus – wir melden uns schnellstmöglich.</p>

            <form class="space-y-4" (submit)="$event.preventDefault()">
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <input type="text" placeholder="Name des Spielers / Elternteil"
                  class="w-full px-4 py-3 bg-white border border-slate-200 rounded-xl text-sm focus:outline-none focus:border-red-600">
                <input type="tel" placeholder="Telefonnummer"
                  class="w-full px-4 py-3 bg-white border border-slate-200 rounded-xl text-sm focus:outline-none focus:border-red-600">
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <input type="email" placeholder="E-Mail-Adresse"
                  class="w-full px-4 py-3 bg-white border border-slate-200 rounded-xl text-sm focus:outline-none focus:border-red-600">
                <select class="w-full px-4 py-3 bg-white border border-slate-200 rounded-xl text-sm focus:outline-none focus:border-red-600 text-slate-700">
                  <option value="">Gewünschtes Format</option>
                  <option value="einzel">Einzeltraining (1:1)</option>
                  <option value="kleingruppe">Kleingruppe (2–4 Spieler)</option>
                  <option value="mannschaft">Mannschaftstraining</option>
                  <option value="powercamp">Powercamp</option>
                </select>
              </div>

              <textarea rows="3" placeholder="Altersklasse, Position oder bisherige Erfahrung..."
                class="w-full px-4 py-3 bg-white border border-slate-200 rounded-xl text-sm focus:outline-none focus:border-red-600"></textarea>

              <button type="submit" class="btn btn-block">
                <span>Anfrage jetzt absenden</span>
                <i class="fa-solid fa-paper-plane text-xs"></i>
              </button>
            </form>
          </div>

        </div>

      </div>
    </section>

    <!-- ══════════════════════════════════════════════
         FEEDBACK & ERFAHRUNGEN (TESTIMONIALS)
         ══════════════════════════════════════════════ -->
    <section class="sp-section bg-slate-50 border-b border-slate-200">
      <div class="sp-container">

        <div class="text-center max-w-2xl mx-auto mb-14">
          <div class="sub-title justify-center">ERFOLGREICHE ZUSAMMENARBEIT</div>
          <h2 class="font-heading text-3xl sm:text-4xl text-slate-900 mb-3">
            Was Eltern & Spieler sagen
          </h2>
          <p class="text-slate-600 text-base">
            Echte Bewertungen von Familien und Nachwuchsspielern aus Hamburg.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div *ngFor="let t of testimonials" class="testimonial-card">
            <div class="stars mb-4">
              <i class="fa-solid fa-star" *ngFor="let _ of [1,2,3,4,5]"></i>
            </div>
            <blockquote class="text-slate-700 text-sm leading-relaxed mb-6 flex-grow">
              "{{ t.text }}"
            </blockquote>
            <div class="flex items-center gap-3 pt-4 border-t border-slate-100">
              <div class="w-9 h-9 rounded-full bg-red-600 text-white flex items-center justify-center font-bold text-xs">
                {{ t.name.charAt(0) }}
              </div>
              <div>
                <p class="text-slate-900 font-bold text-xs">{{ t.name }}</p>
                <p class="text-slate-500 text-[11px]">{{ t.role }}</p>
              </div>
            </div>
          </div>
        </div>

      </div>
    </section>
  `,
})
export class HomeComponent implements OnInit {

  activeTab = signal<'mission' | 'vision' | 'ziel'>('mission');

  phases = [
    {
      title: 'Analyse & Zielsetzung',
      desc: 'Individuelle Stärken-Schwächen-Analyse und Definition messbarer Entwicklungsziele.'
    },
    {
      title: 'Technik & Grundlagen',
      desc: 'Systematischer Aufbau motorischer Grundlagen und präziser Ballbeherrschung.'
    },
    {
      title: 'Taktik & Spielverständnis',
      desc: 'Positionsbezogene Schulung, Spielsituationen und Entscheidungsqualität.'
    },
    {
      title: 'Wettkampf & Transfer',
      desc: 'Erfolgreiche Umsetzung der gelernten Fertigkeiten im offiziellen Ligaspiel.'
    },
  ];

  testimonials = [
    {
      text: 'Absolut professionelles Training! Mein Sohn hat in nur wenigen Monaten enorme Fortschritte bei Ballkontrolle und Selbstbewusstsein auf dem Platz gemacht.',
      name: 'Angelika M.',
      role: 'Mutter eines Nachwuchsspielers (12 J.)'
    },
    {
      text: 'Sami schafft es, jeden Spieler individuell zu fordern und zu fördern. Die Einheiten sind intensiv, strukturiert und extrem lehrreich. Uneingeschränkte Empfehlung!',
      name: 'Markus K.',
      role: 'Vater eines Jugendspielers (15 J.)'
    },
    {
      text: 'Durch das gezielte Kleingruppentraining hat sich meine Handlungsschnelligkeit und Schusstechnik deutlich verbessert. Das Niveau ist spitze!',
      name: 'Jonas T.',
      role: 'Ambitionierter Spieler, 17 Jahre'
    },
  ];

  ngOnInit() {}
}
