import { Component, OnInit, AfterViewInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `

    <!-- ══════════════════════════════════════════════
         HERO SECTION
         ══════════════════════════════════════════════ -->
    <section class="hero-gradient relative min-h-screen flex items-center overflow-hidden">

      <!-- Background grid lines -->
      <div class="absolute inset-0 opacity-[0.03]"
        style="background-image: linear-gradient(rgba(255,255,255,1) 1px, transparent 1px),
                                   linear-gradient(90deg, rgba(255,255,255,1) 1px, transparent 1px);
               background-size: 60px 60px;">
      </div>

      <!-- Red glow orb top-right -->
      <div class="absolute -top-20 -right-20 w-[500px] h-[500px] rounded-full opacity-10"
        style="background: radial-gradient(circle, #E63946 0%, transparent 70%);">
      </div>

      <!-- Gold glow orb bottom-left -->
      <div class="absolute bottom-0 -left-40 w-[600px] h-[400px] rounded-full opacity-[0.06]"
        style="background: radial-gradient(circle, #D4AF37 0%, transparent 70%);">
      </div>

      <div class="sp-container relative z-10 pt-32 pb-20">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-16 items-center">

          <!-- LEFT: Text Content -->
          <div class="lg:col-span-6 xl:col-span-5">

            <!-- Badge -->
            <div class="sp-badge sp-badge-red mb-8 anim-fade-up">
              <span class="dot pulse"></span>
              HAMBURG · PRIVATER FUSSBALLTRAINER
            </div>

            <!-- Headline -->
            <h1 class="hero-title mb-8 anim-fade-up delay-100">
              PRIVATER
              FUßBALL-<em>TRAINER</em>
              FÜR INDIVIDUELLES
              TRAINING.
            </h1>

            <p class="text-base md:text-lg text-slate-400 leading-relaxed mb-10 max-w-lg anim-fade-up delay-200">
              Individuelles Fußballtraining für Kinder, Jugendliche und ambitionierte Spieler in Hamburg – abgestimmt auf die Stärken, Ziele und Entwicklung jedes Spielers.
            </p>

            <!-- CTAs -->
            <div class="flex flex-col sm:flex-row gap-4 anim-fade-up delay-300">
              <a routerLink="/kontakt" class="btn btn-primary btn-lg">
                <i class="fa-solid fa-calendar-check"></i>
                Probetraining anfragen
              </a>
              <a routerLink="/preise" class="btn btn-outline btn-lg">
                Trainingspakete entdecken
                <i class="fa-solid fa-arrow-right"></i>
              </a>
            </div>

            <!-- Trust Row -->
            <div class="flex flex-wrap items-center gap-6 mt-12 pt-10 border-t border-white/10 anim-fade-up delay-400">
              <div>
                <p class="stat-num text-white">100<span class="text-gradient-red">%</span></p>
                <p class="text-xs text-slate-500 uppercase font-bold mt-1">Individuell</p>
              </div>
              <div class="w-px h-10 bg-white/10"></div>
              <div>
                <p class="stat-num text-white">1:1</p>
                <p class="text-xs text-slate-500 uppercase font-bold mt-1">Intensiv-Fokus</p>
              </div>
              <div class="w-px h-10 bg-white/10"></div>
              <div>
                <p class="stat-num text-gradient-gold">Hamburg</p>
                <p class="text-xs text-slate-500 uppercase font-bold mt-1">Flexibler Ort</p>
              </div>
            </div>

          </div>

          <!-- RIGHT: Big Visual -->
          <div class="lg:col-span-6 xl:col-span-7 relative anim-fade-up delay-200">

            <!-- Main hero image -->
            <div class="relative">
              <!-- Glow behind image -->
              <div class="absolute inset-4 rounded-3xl opacity-40 blur-3xl"
                style="background: linear-gradient(135deg, rgba(230,57,70,0.4) 0%, rgba(212,175,55,0.3) 100%);">
              </div>

              <div class="img-card aspect-[4/5] max-h-[680px] rounded-3xl shadow-2xl relative z-10">
                <img src="img/bilderwebsite/Fußballtraining im Freien.avif"
                  alt="SoccerProf Academy – Training in Hamburg"
                  class="w-full h-full object-cover">
                <div class="img-card-overlay"></div>

                <!-- Floating badge bottom-left -->
                <div class="absolute bottom-8 left-8 right-8 flex items-end justify-between">
                  <div class="glass rounded-2xl px-5 py-4">
                    <p class="text-white font-bold text-sm">Sami Ghaouar</p>
                    <p class="text-slate-400 text-xs mt-0.5">Head Coach · SoccerProf Academy</p>
                  </div>
                  <div class="sp-badge sp-badge-gold">
                    <i class="fa-solid fa-star text-xs"></i>
                    TOP TRAINER
                  </div>
                </div>
              </div>
            </div>

            <!-- Floating stat card top-right -->
            <div class="absolute -top-6 -right-6 glass rounded-2xl p-5 shadow-2xl hidden lg:block">
              <p class="text-slate-400 text-xs uppercase font-bold mb-1">Anfänger & Pros</p>
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl flex items-center justify-center text-lg"
                  style="background: rgba(230,57,70,0.2);">⚽</div>
                <div>
                  <p class="text-white font-black text-xl">1:1–1:4</p>
                  <p class="text-slate-500 text-xs">Trainingsformate</p>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>

      <!-- Scroll indicator -->
      <div class="absolute bottom-8 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2 opacity-30">
        <span class="text-xs text-white uppercase tracking-widest font-bold">Scroll</span>
        <div class="w-px h-10 bg-white/30 relative overflow-hidden rounded-full">
          <div class="absolute top-0 left-0 right-0 h-1/2 bg-white rounded-full animate-bounce"></div>
        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════
         ÜBER MICH / TRAINER SECTION
         ══════════════════════════════════════════════ -->
    <section class="sp-section" style="background: var(--sp-dark-2);">
      <div class="sp-divider"></div>
      <div class="sp-container py-0">

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 xl:gap-24 items-center">

          <!-- Image column -->
          <div class="relative order-2 lg:order-1">
            <div class="img-card aspect-[3/4] max-h-[650px] rounded-3xl shadow-2xl">
              <img src="img/sami/sami.jpg"
                alt="Sami Ghaouar – Privater Fußballtrainer Hamburg"
                class="w-full h-full object-cover object-top">
              <div class="img-card-overlay"></div>

              <!-- Coach info overlay -->
              <div class="absolute bottom-8 left-8 right-8">
                <div class="glass rounded-2xl px-6 py-5">
                  <div class="flex items-center justify-between">
                    <div>
                      <p class="text-white font-black text-xl">Sami Ghaouar</p>
                      <p class="text-slate-400 text-sm mt-0.5">Gründer & Head Coach</p>
                    </div>
                    <img src="img/logo/F3-3.avif" alt="SoccerProf" class="h-12 w-auto opacity-80">
                  </div>
                </div>
              </div>
            </div>

            <!-- Floating achievement -->
            <div class="absolute -top-4 -right-4 glass rounded-2xl p-4 shadow-2xl hidden lg:flex items-center gap-3">
              <div class="w-10 h-10 rounded-xl flex items-center justify-center text-base"
                style="background: rgba(212,175,55,0.2);">🏆</div>
              <div>
                <p class="text-white font-bold text-sm">Lizenzierter Trainer</p>
                <p class="text-slate-500 text-xs">DFB & DOSB zertifiziert</p>
              </div>
            </div>
          </div>

          <!-- Text column -->
          <div class="order-1 lg:order-2">
            <div class="sp-section-label">Über Mich / Der Trainer</div>
            <h2 class="font-heading text-3xl sm:text-4xl xl:text-5xl text-white mb-6">
              Individuelle Förderung<br>mit <span class="text-gradient-gold">Leidenschaft</span>
              <br>& Fachkompetenz
            </h2>

            <p class="text-slate-400 text-base leading-relaxed mb-5">
              Mein Name ist <strong class="text-white">Sami Ghaouar</strong>. Als erfahrener Privattrainer in Hamburg verfolge ich das Ziel, jungen Talenten und ambitionierten Spielern die optimalen Werkzeuge an die Hand zu geben, um ihr volles Potenzial auszuschöpfen.
            </p>
            <p class="text-slate-400 text-base leading-relaxed mb-8">
              Ob Technik, Ballbeherrschung, Spielverständnis oder mentale Stärke: Im gezielten Einzel- und Kleingruppentraining gehen wir detailliert auf Stärken und Schwächen ein. Jeder Spieler erhält einen <strong class="text-white">maßgeschneiderten Trainingsplan</strong>.
            </p>

            <!-- Feature list -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-10">
              <div *ngFor="let f of trainerFeatures"
                class="flex items-start gap-3 p-4 rounded-2xl"
                style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06);">
                <div class="feature-icon flex-shrink-0"
                  [style.background]="f.iconBg">
                  <i [class]="f.icon" [style.color]="f.iconColor"></i>
                </div>
                <div>
                  <p class="text-white font-bold text-sm">{{ f.title }}</p>
                  <p class="text-slate-500 text-xs mt-0.5 leading-relaxed">{{ f.desc }}</p>
                </div>
              </div>
            </div>

            <a routerLink="/ueber-uns" class="btn btn-outline">
              Mehr über die SoccerProf Philosophie
              <i class="fa-solid fa-arrow-right"></i>
            </a>
          </div>

        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════
         SOCIAL PROOF / STATS BAR
         ══════════════════════════════════════════════ -->
    <section style="background: var(--sp-red); padding-block: 48px;">
      <div class="sp-container">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
          <div *ngFor="let s of stats" class="text-center">
            <p class="font-heading text-white font-black" style="font-size: clamp(2rem, 4vw, 3rem);">
              {{ s.value }}
            </p>
            <p class="text-red-200 text-xs uppercase font-bold tracking-widest mt-1">{{ s.label }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════
         TRAININGSANGEBOTE SECTION
         ══════════════════════════════════════════════ -->
    <section class="sp-section" style="background: var(--sp-dark);">
      <div class="sp-container">

        <!-- Section header -->
        <div class="text-center max-w-2xl mx-auto mb-16">
          <div class="sp-section-label justify-center" style="justify-content: center;">Trainingsangebote Hamburg</div>
          <h2 class="font-heading text-3xl sm:text-4xl xl:text-5xl text-white mb-5">
            Das richtige Paket<br>für <span class="text-gradient-red">dein Ziel</span>
          </h2>
          <p class="text-slate-400">
            Vom hochintensiven 1:1 Einzeltraining bis zum taktischen Mannschaftstraining.
          </p>
        </div>

        <!-- Cards grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">

          <!-- Einzeltraining -->
          <div class="price-card group">
            <div class="feature-icon" style="background: rgba(230,57,70,0.15); color: var(--sp-red); width:56px; height:56px; border-radius:16px;">
              <i class="fa-solid fa-user-ninja text-xl"></i>
            </div>
            <div>
              <p class="sp-badge sp-badge-white mb-3" style="display:inline-flex;">1:1 Maximale Aufmerksamkeit</p>
              <h3 class="font-heading text-2xl text-white mb-2">Einzeltraining</h3>
              <p class="text-slate-400 text-sm leading-relaxed">
                Das effektivste Format. Technischer Feinschliff, Beidfüßigkeit, Handlungsschnelligkeit und Positionstraining.
              </p>
            </div>
            <div class="mt-auto pt-4 border-t border-white/08">
              <p class="text-3xl font-black text-white mb-1">ab 40€ <span class="text-sm font-normal text-slate-500">/ Einheit</span></p>
            </div>
            <a routerLink="/einzeltraining" class="btn btn-primary">Details & Buchen</a>
          </div>

          <!-- Kleingruppe (Featured) -->
          <div class="price-card price-card-featured group relative">
            <div class="absolute -top-4 left-1/2 -translate-x-1/2">
              <span class="sp-badge sp-badge-gold" style="box-shadow: 0 4px 20px -4px rgba(212,175,55,0.5);">
                <i class="fa-solid fa-fire"></i>
                SEHR BELIEBT
              </span>
            </div>
            <div class="feature-icon" style="background: rgba(212,175,55,0.15); color: var(--sp-gold); width:56px; height:56px; border-radius:16px;">
              <i class="fa-solid fa-users-viewfinder text-xl"></i>
            </div>
            <div>
              <p class="sp-badge sp-badge-gold mb-3" style="display:inline-flex;">2 bis 4 Spieler</p>
              <h3 class="font-heading text-2xl text-white mb-2">Kleingruppe</h3>
              <p class="text-slate-400 text-sm leading-relaxed">
                Ideal für Passschärfe, 1-gegen-1 Duelle und spielnahe wettkampforientierte Übungen mit hoher Dynamik.
              </p>
            </div>
            <div class="mt-auto pt-4 border-t border-white/08">
              <p class="text-3xl font-black text-white mb-1">20–25€ <span class="text-sm font-normal text-slate-500">/ Spieler</span></p>
            </div>
            <a routerLink="/kleingruppe" class="btn btn-gold">Details & Buchen</a>
          </div>

          <!-- Mannschaft -->
          <div class="price-card group">
            <div class="feature-icon" style="background: rgba(255,255,255,0.06); color: #94a3b8; width:56px; height:56px; border-radius:16px;">
              <i class="fa-solid fa-shield-halved text-xl"></i>
            </div>
            <div>
              <p class="sp-badge sp-badge-white mb-3" style="display:inline-flex;">Ergänzungstraining</p>
              <h3 class="font-heading text-2xl text-white mb-2">Mannschaft</h3>
              <p class="text-slate-400 text-sm leading-relaxed">
                Spezifische Zusatzpakete für Jugend- und Herrenteams zur Verbesserung von Gruppentaktik & Athletik.
              </p>
            </div>
            <div class="mt-auto pt-4 border-t border-white/08">
              <p class="text-3xl font-black text-white mb-1">ab 90€ <span class="text-sm font-normal text-slate-500">/ Team-Session</span></p>
            </div>
            <a routerLink="/mannschaft" class="btn btn-outline">Details & Anfrage</a>
          </div>

          <!-- Powercamp -->
          <div class="price-card group">
            <div class="feature-icon" style="background: rgba(34,197,94,0.12); color: #4ade80; width:56px; height:56px; border-radius:16px;">
              <i class="fa-solid fa-bolt text-xl"></i>
            </div>
            <div>
              <p class="sp-badge mb-3" style="display:inline-flex; background: rgba(34,197,94,0.12); border: 1px solid rgba(34,197,94,0.25); color: #4ade80;">Ferien-Intensivcamp</p>
              <h3 class="font-heading text-2xl text-white mb-2">Powercamp</h3>
              <p class="text-slate-400 text-sm leading-relaxed">
                Ganzheitliches Ferientraining mit Turnieren, Videoanalyse, Mittagessen und SoccerProf Ausrüstung.
              </p>
            </div>
            <div class="mt-auto pt-4 border-t border-white/08">
              <p class="text-3xl font-black text-white mb-1">80€ <span class="text-sm font-normal text-slate-500">/ Tag inkl. Verpflegung</span></p>
            </div>
            <a routerLink="/veranstaltungen" class="btn" style="background:#16a34a; color:#fff; border-radius:100px; padding:14px 32px; font-family:'Outfit',sans-serif; font-weight:700; font-size:0.9rem; letter-spacing:0.04em; text-transform:uppercase; transition:all 0.35s;">
              Camp Termine
            </a>
          </div>

        </div>

        <!-- CTA below cards -->
        <div class="text-center mt-12">
          <a routerLink="/preise" class="btn btn-outline">
            Alle Preise & Details ansehen
            <i class="fa-solid fa-arrow-right"></i>
          </a>
        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════
         TRAININGSMETHODE / 4-PHASEN SECTION
         ══════════════════════════════════════════════ -->
    <section class="sp-section" style="background: var(--sp-dark-2);">
      <div class="sp-divider"></div>
      <div class="sp-container py-0">

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">

          <!-- Text -->
          <div>
            <div class="sp-section-label">Trainingsmethode</div>
            <h2 class="font-heading text-3xl sm:text-4xl xl:text-5xl text-white mb-6">
              Die SoccerProf<br><span class="text-gradient-gold">4-Phasen-Methode</span>
            </h2>
            <p class="text-slate-400 text-base leading-relaxed mb-10">
              Unser strukturierter Trainingsansatz stellt sicher, dass jeder Spieler systematisch und nachhaltig besser wird. Von der Analyse bis zur Umsetzung im Spiel.
            </p>

            <div class="flex flex-col gap-5">
              <div *ngFor="let ph of phases; let i = index"
                class="flex items-start gap-5 p-5 rounded-2xl transition-all hover:bg-white/[0.03]"
                style="border: 1px solid rgba(255,255,255,0.05);">
                <div class="flex-shrink-0 w-12 h-12 rounded-xl flex items-center justify-center font-black text-sm"
                  [style.background]="ph.bg"
                  [style.color]="ph.color">
                  {{ i + 1 }}
                </div>
                <div>
                  <p class="text-white font-bold mb-1">{{ ph.title }}</p>
                  <p class="text-slate-500 text-sm leading-relaxed">{{ ph.desc }}</p>
                </div>
              </div>
            </div>

            <div class="mt-8">
              <a routerLink="/trainingsmethoden" class="btn btn-primary">
                Methode im Detail entdecken
                <i class="fa-solid fa-arrow-right"></i>
              </a>
            </div>
          </div>

          <!-- Images grid -->
          <div class="grid grid-cols-2 gap-4">
            <div class="img-card aspect-[3/4] rounded-2xl col-span-1 row-span-2">
              <img src="img/sami/Technik Fußstellung.avif" alt="Techniktraining" class="w-full h-full object-cover">
              <div class="img-card-overlay"></div>
              <div class="absolute bottom-4 left-4 right-4">
                <span class="sp-badge sp-badge-red text-xs">Technik</span>
              </div>
            </div>
            <div class="img-card aspect-square rounded-2xl">
              <img src="img/sami/Athletiktraining.avif" alt="Athletiktraining" class="w-full h-full object-cover">
              <div class="img-card-overlay"></div>
              <div class="absolute bottom-3 left-3 right-3">
                <span class="sp-badge sp-badge-white text-xs">Athletik</span>
              </div>
            </div>
            <div class="img-card aspect-square rounded-2xl">
              <img src="img/sami/Ich Taktiktafel.avif" alt="Taktiktraining" class="w-full h-full object-cover">
              <div class="img-card-overlay"></div>
              <div class="absolute bottom-3 left-3 right-3">
                <span class="sp-badge sp-badge-gold text-xs">Taktik</span>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ══════════════════════════════════════════════
         TESTIMONIALS
         ══════════════════════════════════════════════ -->
    <section class="sp-section" style="background: var(--sp-dark);">
      <div class="sp-container">

        <div class="text-center mb-16">
          <div class="sp-section-label justify-center" style="justify-content:center;">Eltern & Spieler über uns</div>
          <h2 class="font-heading text-3xl sm:text-4xl text-white">
            Das sagen <span class="text-gradient-gold">unsere Familien</span>
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div *ngFor="let t of testimonials" class="testimonial-card">
            <div class="stars mb-4">
              <i class="fa-solid fa-star" *ngFor="let _ of [1,2,3,4,5]"></i>
            </div>
            <blockquote class="text-slate-300 text-sm leading-relaxed italic mb-6">
              "{{ t.text }}"
            </blockquote>
            <div class="flex items-center gap-3 mt-auto pt-4 border-t border-white/08">
              <div class="w-10 h-10 rounded-full flex items-center justify-center font-black text-sm"
                style="background: linear-gradient(135deg, var(--sp-red), var(--sp-gold));">
                {{ t.name.charAt(0) }}
              </div>
              <div>
                <p class="text-white font-bold text-sm">{{ t.name }}</p>
                <p class="text-slate-500 text-xs">{{ t.role }}</p>
              </div>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- ══════════════════════════════════════════════
         BOTTOM CTA SECTION
         ══════════════════════════════════════════════ -->
    <section class="relative overflow-hidden" style="padding-block: var(--section-pad); background: var(--sp-dark-2);">
      <div class="sp-divider"></div>
      <!-- BG image -->
      <div class="absolute inset-0 opacity-10">
        <img src="img/bilderwebsite/Fußballtraining auf Kunstrasen.avif"
          alt="background" class="w-full h-full object-cover">
        <div class="absolute inset-0"
          style="background: linear-gradient(to right, var(--sp-dark-2) 30%, transparent 100%);">
        </div>
      </div>

      <div class="sp-container relative z-10">
        <div class="max-w-3xl">
          <div class="sp-badge sp-badge-gold mb-6">Jetzt starten</div>
          <h2 class="font-heading text-3xl sm:text-4xl xl:text-5xl text-white mb-6 leading-tight">
            Bereit für das<br><span class="text-gradient-red">nächste Level</span>?
          </h2>
          <p class="text-slate-400 text-lg leading-relaxed mb-10 max-w-xl">
            Sende uns eine unverbindliche Anfrage für ein Probetraining. Wir melden uns innerhalb von 24 Stunden zurück.
          </p>
          <div class="flex flex-col sm:flex-row gap-4">
            <a routerLink="/kontakt" class="btn btn-primary btn-lg">
              <i class="fa-solid fa-paper-plane"></i>
              Jetzt Probetraining anfragen
            </a>
            <a routerLink="/preise" class="btn btn-outline btn-lg">
              Alle Pakete & Preise
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Mobile sticky CTA bar -->
    <div class="mobile-cta-bar">
      <a routerLink="/kontakt" class="btn btn-primary flex-1" style="border-radius:14px; padding: 12px 16px; font-size:0.8rem;">
        <i class="fa-solid fa-calendar-check"></i>
        Probetraining anfragen
      </a>
      <a routerLink="/preise" class="btn btn-outline flex-1" style="border-radius:14px; padding: 12px 16px; font-size:0.8rem;">
        Pakete & Preise
      </a>
    </div>
  `,
})
export class HomeComponent implements OnInit, AfterViewInit {

  trainerFeatures = [
    {
      icon: 'fa-solid fa-crosshairs',
      iconBg: 'rgba(230,57,70,0.15)',
      iconColor: 'var(--sp-red)',
      title: 'Technische Präzision',
      desc: 'Detaillierter Fokus auf Ballkontrolle, Beidfüßigkeit und Schusstechnik.'
    },
    {
      icon: 'fa-solid fa-brain',
      iconBg: 'rgba(212,175,55,0.12)',
      iconColor: 'var(--sp-gold)',
      title: 'Spielintelligenz',
      desc: 'Spielverständnis, Positionsspiel und taktische Entscheidungsfähigkeit.'
    },
    {
      icon: 'fa-solid fa-dumbbell',
      iconBg: 'rgba(99,202,183,0.12)',
      iconColor: '#4ade80',
      title: 'Athletik & Kondition',
      desc: 'Explosive Schnelligkeit, Ausdauer und fußballspezifische Kraft.'
    },
    {
      icon: 'fa-solid fa-star',
      iconBg: 'rgba(139,92,246,0.12)',
      iconColor: '#a78bfa',
      title: 'Mentale Stärke',
      desc: 'Selbstvertrauen, Fokus und mentale Resilienz im Wettkampf.'
    },
  ];

  stats = [
    { value: '100%', label: 'Individuelle Betreuung' },
    { value: '1:1–1:4', label: 'Trainingsformate' },
    { value: 'HH', label: 'Standort Hamburg' },
    { value: '⚽', label: 'Anfänger & Pros' },
  ];

  phases = [
    {
      title: 'Analyse & Zielsetzung',
      desc: 'Individuelle Stärken-Schwächen-Analyse und Festlegung klarer Trainingsziele.',
      bg: 'rgba(230,57,70,0.15)',
      color: 'var(--sp-red)'
    },
    {
      title: 'Technik & Grundlagen',
      desc: 'Systematischer Aufbau der technischen Fähigkeiten auf solider Grundlage.',
      bg: 'rgba(212,175,55,0.12)',
      color: 'var(--sp-gold)'
    },
    {
      title: 'Taktik & Spielverständnis',
      desc: 'Entwicklung von Spielintelligenz und positionsspezifischem Know-how.',
      bg: 'rgba(99,202,183,0.12)',
      color: '#4ade80'
    },
    {
      title: 'Wettkampf & Transfer',
      desc: 'Umsetzung im echten Spiel – Selbstbewusstsein und Leistung auf dem Platz.',
      bg: 'rgba(139,92,246,0.12)',
      color: '#a78bfa'
    },
  ];

  testimonials = [
    {
      text: 'Absolut professionelles Training! Mein Sohn hat in nur wenigen Monaten enorme Fortschritte bei Ballkontrolle und Selbstbewusstsein auf dem Platz gemacht.',
      name: 'Angelika Mutter',
      role: 'Mutter eines Nachwuchsspielers'
    },
    {
      text: 'Sami schafft es, jeden Spieler individuell zu fördern. Die Trainingseinheiten sind intensiv, abwechslungsreich und machen einfach Spaß. Sehr empfehlenswert!',
      name: 'Markus K.',
      role: 'Vater eines Jugendspielers'
    },
    {
      text: 'Durch das Kleingruppentraining hat sich meine Technik deutlich verbessert. Die Atmosphäre ist motivierend und Sami gibt immer das Beste für seine Schüler.',
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
