import { Component, OnInit, AfterViewInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `

    <!-- ══════════════════════════════════════════════
         HERO SECTION (CLEAN WHITE & EDITORIAL)
         ══════════════════════════════════════════════ -->
    <section class="relative bg-white pt-28 pb-16 md:pt-36 md:pb-24 border-b border-slate-100 overflow-hidden">

      <!-- Subtle background grid pattern -->
      <div class="absolute inset-0 opacity-[0.025] pointer-events-none"
        style="background-image: linear-gradient(#0F172A 1px, transparent 1px),
                                 linear-gradient(90deg, #0F172A 1px, transparent 1px);
               background-size: 48px 48px;">
      </div>

      <div class="sp-container relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center">

          <!-- LEFT: Text Content -->
          <div class="lg:col-span-7 xl:col-span-6">

            <!-- Badge -->
            <div class="sp-badge sp-badge-red mb-6 anim-fade-up">
              <span class="dot pulse"></span>
              HAMBURG · KINDER, JUGENDLICHE & AMBITIONIERTE SPIELER
            </div>

            <!-- Headline -->
            <h1 class="hero-title mb-6 anim-fade-up delay-100">
              PRIVATER FUßBALL-TRAINER FÜR INDIVIDUELLES TRAINING FÜR ANFÄNGER & PROS.
            </h1>

            <!-- Subtitle -->
            <p class="text-base sm:text-lg text-slate-600 leading-relaxed mb-8 max-w-xl anim-fade-up delay-200">
              Individuelles Fußballtraining für Kinder, Jugendliche und ambitionierte Spieler in Hamburg – abgestimmt auf die Stärken, Ziele und Entwicklung jedes Spielers. Einzeltraining und Kleingruppentraining als professionelle Ergänzung zum Vereinstraining.
            </p>

            <!-- CTAs -->
            <div class="flex flex-col sm:flex-row gap-4 anim-fade-up delay-300">
              <a routerLink="/kontakt" class="btn btn-primary btn-lg shadow-md">
                <i class="fa-solid fa-calendar-check text-sm"></i>
                Jetzt Probetraining anfragen
              </a>
              <a routerLink="/preise" class="btn btn-outline btn-lg">
                Trainingspakete entdecken
                <i class="fa-solid fa-arrow-right text-sm"></i>
              </a>
            </div>

            <!-- Trust / Stats Row -->
            <div class="grid grid-cols-3 gap-6 mt-12 pt-8 border-t border-slate-200 anim-fade-up delay-400 max-w-lg">
              <div>
                <p class="stat-num text-slate-900">100<span class="text-red-600">%</span></p>
                <p class="text-xs font-bold text-slate-500 uppercase tracking-wider mt-1">Individuell</p>
              </div>
              <div class="border-l border-slate-200 pl-6">
                <p class="stat-num text-slate-900">1:1</p>
                <p class="text-xs font-bold text-slate-500 uppercase tracking-wider mt-1">Intensiv-Fokus</p>
              </div>
              <div class="border-l border-slate-200 pl-6">
                <p class="stat-num text-red-600">Hamburg</p>
                <p class="text-xs font-bold text-slate-500 uppercase tracking-wider mt-1">Flexibler Ort</p>
              </div>
            </div>

          </div>

          <!-- RIGHT: Visual Column -->
          <div class="lg:col-span-5 xl:col-span-6 relative anim-fade-up delay-200">

            <div class="relative max-w-md mx-auto lg:max-w-none">
              <!-- Main action card -->
              <div class="img-card aspect-[4/5] rounded-3xl shadow-xl overflow-hidden border border-slate-200">
                <img src="img/bilderwebsite/Fußballtraining im Freien.avif"
                  alt="SoccerProf Academy Hamburg – Professionelles Fußballtraining"
                  class="w-full h-full object-cover">
                <div class="img-card-overlay"></div>

                <!-- Floating coach tag bottom -->
                <div class="absolute bottom-6 left-6 right-6">
                  <div class="glass-light rounded-2xl p-4 flex items-center justify-between shadow-lg">
                    <div>
                      <p class="text-slate-900 font-extrabold text-sm">Sami Ghaouar</p>
                      <p class="text-slate-600 text-xs">Head Coach · Lizenzierter Privattrainer</p>
                    </div>
                    <span class="sp-badge sp-badge-red text-[10px]">
                      Hamburg
                    </span>
                  </div>
                </div>
              </div>

              <!-- Top-right feature pill -->
              <div class="absolute -top-4 -right-4 bg-white border border-slate-200 rounded-2xl p-3.5 shadow-lg hidden sm:flex items-center gap-3">
                <div class="w-9 h-9 rounded-xl bg-red-50 text-red-600 flex items-center justify-center font-bold text-sm">
                  <i class="fa-solid fa-trophy"></i>
                </div>
                <div>
                  <p class="text-slate-900 font-bold text-xs">DFB-zertifiziert</p>
                  <p class="text-slate-500 text-[11px]">Gezielte Talentförderung</p>
                </div>
              </div>

            </div>

          </div>

        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════
         ÜBER MICH / DER TRAINER (SERIÖS & STRUKTURIERT)
         ══════════════════════════════════════════════ -->
    <section class="sp-section bg-slate-50 border-b border-slate-200">
      <div class="sp-container">

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center">

          <!-- Image column -->
          <div class="lg:col-span-5 order-2 lg:order-1">
            <div class="relative max-w-md mx-auto">
              <div class="img-card aspect-[3/4] rounded-3xl shadow-lg border border-slate-200">
                <img src="img/sami/sami.jpg"
                  alt="Sami Ghaouar – Privater Fußballtrainer Hamburg"
                  class="w-full h-full object-cover object-top">
                <div class="img-card-overlay"></div>

                <!-- Bottom tag -->
                <div class="absolute bottom-6 left-6 right-6">
                  <div class="glass-light rounded-2xl p-4 flex items-center justify-between">
                    <div>
                      <p class="text-slate-900 font-extrabold text-base">Sami Ghaouar</p>
                      <p class="text-slate-600 text-xs">Gründer & Cheftrainer SoccerProf</p>
                    </div>
                    <img src="img/logo/F3-3.avif" alt="SoccerProf" class="h-9 w-auto">
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Text column -->
          <div class="lg:col-span-7 order-1 lg:order-2">
            <div class="sp-section-label">Über Mich · Der Trainer</div>
            <h2 class="font-heading text-3xl sm:text-4xl text-slate-900 mb-6">
              Individuelle Förderung mit Leidenschaft & Fachkompetenz
            </h2>

            <p class="text-slate-700 text-base leading-relaxed mb-5">
              Mein Name ist <strong class="text-slate-900 font-bold">Sami Ghaouar</strong>. Als lizenzierter Privattrainer in Hamburg verfolge ich das Ziel, Nachwuchstalenten und ambitionierten Fußballern die optimalen Trainingsbedingungen zu bieten, um ihr volles Potenzial auf dem Platz abzurufen.
            </p>
            <p class="text-slate-600 text-base leading-relaxed mb-8">
              Im Vereinstraining bleibt für die individuellen Feinheiten oft keine Zeit. Genau hier setzen wir an: Gezieltes Einzel- und Kleingruppentraining für Technik, Passschärfe, Handlungsschnelligkeit und mentale Wettkampfstärke – mit messbaren Fortschritten nach jeder Einheit.
            </p>

            <!-- 4 Training Pillars (Clean & Serious) -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-8">
              <div *ngFor="let f of trainerFeatures"
                class="bg-white border border-slate-200 rounded-2xl p-4 flex items-start gap-3.5 shadow-sm">
                <div class="feature-icon flex-shrink-0">
                  <i [class]="f.icon"></i>
                </div>
                <div>
                  <p class="text-slate-900 font-bold text-sm">{{ f.title }}</p>
                  <p class="text-slate-600 text-xs mt-1 leading-relaxed">{{ f.desc }}</p>
                </div>
              </div>
            </div>

            <div class="flex flex-wrap items-center gap-4">
              <a routerLink="/ueber-uns" class="btn btn-dark">
                Mehr über Philosophie & Trainer
                <i class="fa-solid fa-arrow-right text-xs"></i>
              </a>
              <a routerLink="/kontakt" class="btn btn-outline">
                Direkt Kontakt aufnehmen
              </a>
            </div>

          </div>

        </div>

      </div>
    </section>

    <!-- ══════════════════════════════════════════════
         KEY STATS STRIP (CLEAN LIGHT ACCENT STRIP)
         ══════════════════════════════════════════════ -->
    <section class="bg-slate-50 py-12 border-y border-slate-200">
      <div class="sp-container">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
          <div *ngFor="let s of stats" class="text-center">
            <p class="font-heading font-black text-slate-900 text-3xl sm:text-4xl tracking-tight">
              {{ s.value }}
            </p>
            <p class="text-slate-500 text-xs uppercase font-bold tracking-widest mt-1.5">{{ s.label }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════
         TRAININGSANGEBOTE SECTION (WHITE & STRUCTURED)
         ══════════════════════════════════════════════ -->
    <section class="sp-section bg-white border-b border-slate-100">
      <div class="sp-container">

        <!-- Section header -->
        <div class="text-center max-w-2xl mx-auto mb-16">
          <div class="sp-section-label justify-center">Trainingsangebote Hamburg</div>
          <h2 class="font-heading text-3xl sm:text-4xl text-slate-900 mb-4">
            Das passende Trainingspaket für dein Ziel
          </h2>
          <p class="text-slate-600 text-base">
            Vom hochintensiven 1:1 Einzeltraining bis zum taktischen Mannschaftstraining.
          </p>
        </div>

        <!-- Cards grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">

          <!-- 1. Einzeltraining -->
          <div class="price-card group">
            <div class="flex items-center justify-between">
              <div class="feature-icon">
                <i class="fa-solid fa-user text-lg"></i>
              </div>
              <span class="sp-badge sp-badge-neutral text-[10px]">1:1 Exklusiv</span>
            </div>
            <div>
              <h3 class="font-heading text-xl text-slate-900 mb-2">Einzeltraining</h3>
              <p class="text-slate-600 text-sm leading-relaxed">
                Das effektivste Format. Technischer Feinschliff, Beidfüßigkeit, Handlungsschnelligkeit und Positionstraining.
              </p>
            </div>
            <div class="mt-auto pt-4 border-t border-slate-100">
              <p class="text-2xl font-black text-slate-900">ab 40€ <span class="text-xs font-normal text-slate-500">/ Einheit</span></p>
            </div>
            <a routerLink="/einzeltraining" class="btn btn-primary w-full">Details & Buchen</a>
          </div>

          <!-- 2. Kleingruppe (Featured) -->
          <div class="price-card price-card-featured group relative">
            <div class="flex items-center justify-between">
              <div class="feature-icon bg-red-600 text-white border-red-600">
                <i class="fa-solid fa-users text-lg"></i>
              </div>
              <span class="sp-badge sp-badge-red text-[10px]">Sehr Beliebt</span>
            </div>
            <div>
              <h3 class="font-heading text-xl text-slate-900 mb-2">Kleingruppe</h3>
              <p class="text-slate-600 text-sm leading-relaxed">
                2 bis 4 Spieler. Ideal für Passschärfe, 1-gegen-1 Duelle und spielnahe wettkampforientierte Übungen.
              </p>
            </div>
            <div class="mt-auto pt-4 border-t border-red-100">
              <p class="text-2xl font-black text-slate-900">20–25€ <span class="text-xs font-normal text-slate-500">/ Spieler</span></p>
            </div>
            <a routerLink="/kleingruppe" class="btn btn-primary w-full">Details & Buchen</a>
          </div>

          <!-- 3. Mannschaft -->
          <div class="price-card group">
            <div class="flex items-center justify-between">
              <div class="feature-icon">
                <i class="fa-solid fa-shield-halved text-lg"></i>
              </div>
              <span class="sp-badge sp-badge-neutral text-[10px]">Team-Paket</span>
            </div>
            <div>
              <h3 class="font-heading text-xl text-slate-900 mb-2">Mannschaft</h3>
              <p class="text-slate-600 text-sm leading-relaxed">
                Spezifische Zusatzpakete für Jugend- und Amateurvereine zur Optimierung von Taktik, Fitness und Struktur.
              </p>
            </div>
            <div class="mt-auto pt-4 border-t border-slate-100">
              <p class="text-2xl font-black text-slate-900">ab 90€ <span class="text-xs font-normal text-slate-500">/ Session</span></p>
            </div>
            <a routerLink="/mannschaft" class="btn btn-outline w-full">Details & Anfrage</a>
          </div>

          <!-- 4. Powercamp -->
          <div class="price-card group">
            <div class="flex items-center justify-between">
              <div class="feature-icon">
                <i class="fa-solid fa-futbol text-lg"></i>
              </div>
              <span class="sp-badge sp-badge-neutral text-[10px]">Ferien-Event</span>
            </div>
            <div>
              <h3 class="font-heading text-xl text-slate-900 mb-2">Powercamp</h3>
              <p class="text-slate-600 text-sm leading-relaxed">
                Ganzheitliches Ferientraining mit Turnieren, Videoanalyse, gesunder Verpflegung und SoccerProf Ausrüstung.
              </p>
            </div>
            <div class="mt-auto pt-4 border-t border-slate-100">
              <p class="text-2xl font-black text-slate-900">80€ <span class="text-xs font-normal text-slate-500">/ Tag</span></p>
            </div>
            <a routerLink="/veranstaltungen" class="btn btn-outline w-full">Camp Termine</a>
          </div>

        </div>

        <!-- All pricing link -->
        <div class="text-center mt-12">
          <a routerLink="/preise" class="btn btn-outline">
            Komplette Preisübersicht ansehen
            <i class="fa-solid fa-arrow-right text-xs"></i>
          </a>
        </div>

      </div>
    </section>

    <!-- ══════════════════════════════════════════════
         TRAININGSMETHODE (4-PHASEN STRUKTUR)
         ══════════════════════════════════════════════ -->
    <section class="sp-section bg-slate-50 border-b border-slate-200">
      <div class="sp-container">

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center">

          <!-- Left: 4-Step Methodology -->
          <div class="lg:col-span-6">
            <div class="sp-section-label">Trainingsmethodik</div>
            <h2 class="font-heading text-3xl sm:text-4xl text-slate-900 mb-6">
              Die SoccerProf 4-Phasen-Methode
            </h2>
            <p class="text-slate-600 text-base leading-relaxed mb-8">
              Unser systematischer Trainingsansatz stellt sicher, dass jeder Spieler nachhaltig gefördert wird – von der initialen Analyse bis zur sicheren Umsetzung im Ligaspiel.
            </p>

            <div class="flex flex-col gap-4">
              <div *ngFor="let ph of phases; let i = index"
                class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 flex items-start gap-4 shadow-sm hover:border-slate-300 transition-colors">
                <div class="w-10 h-10 rounded-xl bg-red-50 text-red-600 font-extrabold flex items-center justify-center text-sm flex-shrink-0 border border-red-100">
                  0{{ i + 1 }}
                </div>
                <div>
                  <p class="text-slate-900 font-bold text-sm sm:text-base mb-0.5">{{ ph.title }}</p>
                  <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">{{ ph.desc }}</p>
                </div>
              </div>
            </div>

            <div class="mt-8">
              <a routerLink="/trainingsmethoden" class="btn btn-dark">
                Ausführliche Methodik entdecken
                <i class="fa-solid fa-arrow-right text-xs"></i>
              </a>
            </div>
          </div>

          <!-- Right: Visual Action Collage -->
          <div class="lg:col-span-6">
            <div class="grid grid-cols-2 gap-4">
              <div class="img-card aspect-[3/4] rounded-2xl col-span-1 row-span-2 shadow-md">
                <img src="img/sami/Technik Fußstellung.avif" alt="Techniktraining" class="w-full h-full object-cover">
                <div class="img-card-overlay"></div>
                <div class="absolute bottom-4 left-4 right-4">
                  <span class="sp-badge bg-white text-slate-900 text-xs font-bold shadow-sm">1. Technik</span>
                </div>
              </div>
              <div class="img-card aspect-square rounded-2xl shadow-md">
                <img src="img/sami/Athletiktraining.avif" alt="Athletiktraining" class="w-full h-full object-cover">
                <div class="img-card-overlay"></div>
                <div class="absolute bottom-3 left-3 right-3">
                  <span class="sp-badge bg-white text-slate-900 text-xs font-bold shadow-sm">2. Athletik</span>
                </div>
              </div>
              <div class="img-card aspect-square rounded-2xl shadow-md">
                <img src="img/sami/Ich Taktiktafel.avif" alt="Taktiktraining" class="w-full h-full object-cover">
                <div class="img-card-overlay"></div>
                <div class="absolute bottom-3 left-3 right-3">
                  <span class="sp-badge bg-white text-slate-900 text-xs font-bold shadow-sm">3. Taktik</span>
                </div>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- ══════════════════════════════════════════════
         FEEDBACK & ERFAHRUNGEN (SERIÖSE TESTIMONIALS)
         ══════════════════════════════════════════════ -->
    <section class="sp-section bg-white border-b border-slate-100">
      <div class="sp-container">

        <div class="text-center max-w-2xl mx-auto mb-14">
          <div class="sp-section-label justify-center">Feedback & Erfahrungen</div>
          <h2 class="font-heading text-3xl sm:text-4xl text-slate-900 mb-3">
            Was Eltern und Spieler sagen
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

    <!-- ══════════════════════════════════════════════
         BOTTOM CTA (CLEAN WHITE / ACCENT BANNER)
         ══════════════════════════════════════════════ -->
    <section class="bg-slate-50 py-20 border-b border-slate-200 relative overflow-hidden">
      <div class="sp-container relative z-10">
        <div class="max-w-2xl">
          <span class="sp-badge sp-badge-red mb-5">Jetzt unverbindlich anfragen</span>
          <h2 class="font-heading text-3xl sm:text-4xl text-slate-900 mb-5 leading-tight">
            Bereit für den nächsten Schritt in deiner Entwicklung?
          </h2>
          <p class="text-slate-600 text-base leading-relaxed mb-8">
            Sende uns deine Anfrage für ein Probetraining in Hamburg. Wir melden uns innerhalb von 24 Stunden mit einem Terminvorschlag.
          </p>
          <div class="flex flex-col sm:flex-row gap-4">
            <a routerLink="/kontakt" class="btn btn-primary btn-lg">
              <i class="fa-solid fa-paper-plane text-xs"></i>
              Probetraining anfragen
            </a>
            <a routerLink="/preise" class="btn btn-outline btn-lg">
              Preise & Details
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Mobile Sticky CTA Bar -->
    <div class="mobile-cta-bar">
      <a routerLink="/kontakt" class="btn btn-primary flex-1" style="border-radius:100px; padding: 11px 16px; font-size:0.8rem;">
        <i class="fa-solid fa-calendar-check text-xs"></i>
        Probetraining
      </a>
      <a routerLink="/preise" class="btn btn-outline flex-1" style="border-radius:100px; padding: 11px 16px; font-size:0.8rem;">
        Pakete
      </a>
    </div>
  `,
})
export class HomeComponent implements OnInit, AfterViewInit {

  trainerFeatures = [
    {
      icon: 'fa-solid fa-crosshairs',
      title: 'Technische Präzision',
      desc: 'Detaillierter Fokus auf saubere Ballannahme, Beidfüßigkeit und präzise Schusstechnik.'
    },
    {
      icon: 'fa-solid fa-brain',
      title: 'Spielintelligenz',
      desc: 'Raumorientierung, Vororientierung (Scannen) und schnelle Entscheidungsfindung unter Druck.'
    },
    {
      icon: 'fa-solid fa-bolt',
      title: 'Athletik & Schnelligkeit',
      desc: 'Fußballspezifische Explosivität, Richtungswechsel, Koordination und Stabilität.'
    },
    {
      icon: 'fa-solid fa-shield',
      title: 'Mentale Stärke',
      desc: 'Selbstvertrauen auf dem Platz, Siegermentalität und Fokus im Wettkampf.'
    },
  ];

  stats = [
    { value: '100%', label: 'Individuelle Betreuung' },
    { value: '1:1–1:4', label: 'Trainingsformate' },
    { value: 'Hamburg', label: 'Flexibler Standort' },
    { value: 'U8–Herren', label: 'Alle Altersklassen' },
  ];

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

  ngAfterViewInit() {
    this.initScrollReveal();
  }

  private initScrollReveal() {
    if (typeof window === 'undefined') return;
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(e => {
          if (e.isIntersecting) {
            e.target.classList.add('revealed');
          }
        });
      },
      { threshold: 0.1, rootMargin: '0px 0px -60px 0px' }
    );
    document.querySelectorAll('[data-reveal]').forEach(el => observer.observe(el));
  }
}
