import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <!-- HERO SECTION -->
    <section class="relative pt-32 pb-20 md:pt-40 md:pb-28 overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="max-w-3xl text-left">
          
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-900/5 border border-slate-900/10 text-xs font-bold tracking-wider text-slate-700 uppercase mb-6 shadow-sm">
            <span class="w-2 h-2 rounded-full bg-[#E63946] animate-ping"></span>
            HAMBURG · KINDER, JUGENDLICHE &amp; AMBITIONIERTE SPIELER
          </div>

          <h1 class="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-extrabold text-slate-900 tracking-tight leading-[1.15] mb-6">
            PRIVATER FUßBALL-TRAINER FÜR INDIVIDUELLES TRAINING FÜR ANFÄNGER &amp; PROS.
          </h1>

          <div class="inline-block bg-amber-100/80 border border-amber-300 text-amber-900 px-4 py-2 rounded-xl text-sm font-extrabold mb-6 shadow-sm">
            DIE PERFEKTE ERGÄNZUNG ZUM FUßBALL VEREIN 👍 ⚽
          </div>

          <p class="text-lg sm:text-xl text-slate-600 font-normal leading-relaxed mb-8 max-w-2xl">
            Individuelles Fußballtraining für Kinder, Jugendliche und ambitionierte Spieler in Hamburg – abgestimmt auf die Stärken, Ziele und Entwicklung jedes Spielers. Einzeltraining und Kleingruppentraining als professionelle Ergänzung zum Vereinstraining.
          </p>

          <div class="flex flex-wrap items-center gap-4">
            <a routerLink="/kontakt" class="btn-fill-red px-8 py-4 rounded-xl bg-[#E63946] text-white font-extrabold text-base shadow-red-glow hover:shadow-2xl transition-all">
              <span>Jetzt Probetraining anfragen</span>
            </a>
            <a routerLink="/preise" class="btn-fill-gold px-8 py-4 rounded-xl bg-white border border-slate-300 text-slate-800 font-bold text-base hover:text-white shadow-sm transition-all">
              <span>Trainingspakete entdecken</span>
            </a>
          </div>

        </div>
      </div>
    </section>

    <!-- ÜBER MICH SECTION -->
    <section class="bg-[#090D16] text-white py-20 md:py-28 relative overflow-hidden border-y border-slate-800">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          
          <div class="lg:col-span-5 relative">
            <div class="relative rounded-3xl overflow-hidden shadow-2xl border border-slate-800 group">
              <img src="img/sami/sami.jpg" alt="Sami Ghaouar Head Coach SoccerProf" class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-700">
              <div class="absolute inset-0 bg-gradient-to-t from-[#090D16] via-transparent to-transparent opacity-80"></div>
              <div class="absolute bottom-6 left-6 right-6">
                <div class="inline-block px-3 py-1 bg-[#D4AF37] text-slate-950 text-xs font-black uppercase rounded-md mb-2">
                  Head Coach &amp; Gründer
                </div>
                <h3 class="text-2xl font-bold text-white">Sami Ghaouar</h3>
                <p class="text-slate-400 text-sm">Privater Fußballtrainer in Hamburg</p>
              </div>
            </div>
          </div>

          <div class="lg:col-span-7 space-y-6">
            <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-800 text-xs font-bold tracking-wider text-[#D4AF37] uppercase">
              ÜBER MICH / DER TRAINER
            </div>

            <h2 class="text-3xl sm:text-4xl font-extrabold text-white leading-tight">
              Individuelle Förderung mit Leidenschaft &amp; Fachkompetenz
            </h2>

            <p class="text-slate-300 text-base leading-relaxed">
              Mein Name ist <strong>Sami Ghaouar</strong>. Als erfahrener Privattrainer in Hamburg verfolge ich das Ziel, junge Talenten und ambitionierten Spielern die optimalen Werkzeuge an die Hand zu geben, um ihr volles Potenzial auszusschöpfen.
            </p>

            <p class="text-slate-300 text-base leading-relaxed">
              Ob Technik, Ballbeherrschung, Spielverständnis oder mentale Stärke: Im gezielten Einzel- und Kleingruppentraining gehen wir detailliert auf Stärken und Schwächen ein. Jeder Spieler erhält einen maßgeschneiderten Trainingsplan.
            </p>

            <div class="grid grid-cols-2 sm:grid-cols-3 gap-6 pt-4 border-t border-slate-800">
              <div>
                <p class="text-3xl font-black text-[#D4AF37]">100%</p>
                <p class="text-xs text-slate-400 uppercase font-bold mt-1">Individuell</p>
              </div>
              <div>
                <p class="text-3xl font-black text-[#E63946]">1:1 &amp; 1:4</p>
                <p class="text-xs text-slate-400 uppercase font-bold mt-1">Intensiv-Fokus</p>
              </div>
              <div>
                <p class="text-3xl font-black text-white">Hamburg</p>
                <p class="text-xs text-slate-400 uppercase font-bold mt-1">Flexibler Ort</p>
              </div>
            </div>

            <div class="pt-4">
              <a routerLink="/ueber-uns" class="inline-flex items-center gap-2 text-[#D4AF37] font-bold hover:underline text-sm">
                <span>Mehr über die SoccerProf Philosophie erfahren</span>
                <i class="fa-solid fa-arrow-right"></i>
              </a>
            </div>

          </div>

        </div>
      </div>
    </section>

    <!-- TRAININGSANGEBOTE / PAKETE SECTION -->
    <section class="py-20 md:py-28 relative">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="text-center max-w-3xl mx-auto mb-16">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-900/5 border border-slate-900/10 text-xs font-bold text-slate-700 uppercase mb-4">
            TRAININGSANGEBOTE HAMBURG
          </div>
          <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
            Das passende Trainingspaket für dein Ziel
          </h2>
          <p class="text-slate-600 mt-4 text-base">
            Vom hochintensiven 1:1 Einzeltraining bis zum taktischen Mannschaftstraining.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          
          <!-- Card 1: Einzeltraining -->
          <div class="glass-card p-8 rounded-3xl flex flex-col justify-between relative group">
            <div>
              <div class="w-14 h-14 rounded-2xl bg-red-100 text-[#E63946] flex items-center justify-center text-2xl font-bold mb-6">
                <i class="fa-solid fa-user-ninja"></i>
              </div>
              <h3 class="text-xl font-extrabold text-slate-900 mb-2">Einzeltraining</h3>
              <p class="text-xs text-slate-500 font-bold uppercase mb-4">1:1 Maximale Aufmerksamkeit</p>
              <p class="text-slate-600 text-sm leading-relaxed mb-6">
                Das effektivste Format. Technischer Feinschliff, Beidfüßigkeit, Handlungsschnelligkeit und Positionstraining.
              </p>
              <div class="mb-6">
                <span class="text-3xl font-black text-slate-900">ab 40€</span>
                <span class="text-xs text-slate-500 font-semibold"> / Einheit</span>
              </div>
            </div>
            <a routerLink="/einzeltraining" class="btn-fill-red text-center py-3 px-4 rounded-xl bg-[#E63946] text-white font-bold text-sm block">
              <span>Details &amp; Buchen</span>
            </a>
          </div>

          <!-- Card 2: Kleingruppe -->
          <div class="glass-card p-8 rounded-3xl flex flex-col justify-between relative group border-amber-300/60 shadow-lg">
            <div class="absolute -top-3 right-6 bg-[#D4AF37] text-slate-950 font-black text-[10px] uppercase px-3 py-1 rounded-full shadow-sm">
              SEHR BELIEBT
            </div>
            <div>
              <div class="w-14 h-14 rounded-2xl bg-amber-100 text-[#D4AF37] flex items-center justify-center text-2xl font-bold mb-6">
                <i class="fa-solid fa-users-viewfinder"></i>
              </div>
              <h3 class="text-xl font-extrabold text-slate-900 mb-2">Kleingruppe</h3>
              <p class="text-xs text-slate-500 font-bold uppercase mb-4">2 bis 4 Spieler</p>
              <p class="text-slate-600 text-sm leading-relaxed mb-6">
                Ideal für Passschärfe, 1-gegen-1 Duelle und spielnahe wettkampforientierte Übungen mit hoher Dynamik.
              </p>
              <div class="mb-6">
                <span class="text-3xl font-black text-slate-900">20 - 25€</span>
                <span class="text-xs text-slate-500 font-semibold"> / Spieler</span>
              </div>
            </div>
            <a routerLink="/kleingruppe" class="btn-fill-gold text-center py-3 px-4 rounded-xl bg-[#D4AF37] text-slate-950 font-extrabold text-sm block">
              <span>Details &amp; Buchen</span>
            </a>
          </div>

          <!-- Card 3: Mannschaft -->
          <div class="glass-card p-8 rounded-3xl flex flex-col justify-between relative group">
            <div>
              <div class="w-14 h-14 rounded-2xl bg-slate-100 text-slate-800 flex items-center justify-center text-2xl font-bold mb-6">
                <i class="fa-solid fa-shield-halved"></i>
              </div>
              <h3 class="text-xl font-extrabold text-slate-900 mb-2">Mannschaft</h3>
              <p class="text-xs text-slate-500 font-bold uppercase mb-4">Ergänzungstraining</p>
              <p class="text-slate-600 text-sm leading-relaxed mb-6">
                Spezifische Zusatzpakete für Jugend- und Herrenteams zur Verbesserung von Gruppentaktik &amp; Athletik.
              </p>
              <div class="mb-6">
                <span class="text-3xl font-black text-slate-900">ab 90€</span>
                <span class="text-xs text-slate-500 font-semibold"> / Team-Session</span>
              </div>
            </div>
            <a routerLink="/mannschaft" class="btn-fill-gold text-center py-3 px-4 rounded-xl bg-slate-900 text-white font-bold text-sm block hover:bg-slate-800">
              <span>Details &amp; Anfrage</span>
            </a>
          </div>

          <!-- Card 4: Powercamp -->
          <div class="glass-card p-8 rounded-3xl flex flex-col justify-between relative group">
            <div>
              <div class="w-14 h-14 rounded-2xl bg-emerald-100 text-emerald-600 flex items-center justify-center text-2xl font-bold mb-6">
                <i class="fa-solid fa-bolt"></i>
              </div>
              <h3 class="text-xl font-extrabold text-slate-900 mb-2">Powercamp</h3>
              <p class="text-xs text-slate-500 font-bold uppercase mb-4">Ferien-Intensivcamp</p>
              <p class="text-slate-600 text-sm leading-relaxed mb-6">
                Ganzheitliches Ferientraining mit Turnieren, Videoanalyse, Mittagessen und SoccerProf Ausrüstung.
              </p>
              <div class="mb-6">
                <span class="text-3xl font-black text-slate-900">80€</span>
                <span class="text-xs text-slate-500 font-semibold"> / Tag inkl. Verpflegung</span>
              </div>
            </div>
            <a routerLink="/veranstaltungen" class="btn-fill-red text-center py-3 px-4 rounded-xl bg-emerald-600 text-white font-bold text-sm block hover:bg-emerald-700">
              <span>Camp Termine</span>
            </a>
          </div>

        </div>
      </div>
    </section>

    <!-- TESTIMONIAL ANGELIKA MUTTER -->
    <section class="bg-slate-900 text-white py-16">
      <div class="max-w-4xl mx-auto px-4 text-center">
        <div class="text-amber-400 text-3xl mb-4">
          <i class="fa-solid fa-quote-left"></i>
        </div>
        <blockquote class="text-lg sm:text-xl font-medium italic text-slate-200 leading-relaxed mb-6">
          "Absolut professionelles Training! Mein Sohn hat in nur wenigen Monaten enorme Fortschritte bei Ballkontrolle und Selbstbewusstsein auf dem Platz gemacht."
        </blockquote>
        <div class="font-bold text-white">Angelika Mutter</div>
        <div class="text-xs text-slate-400">Begeisterte Mutter eines Nachwuchsspielers</div>
      </div>
    </section>
  `
})
export class HomeComponent {}
