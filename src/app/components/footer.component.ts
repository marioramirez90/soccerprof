import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-footer',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <footer class="bg-[#090D16] text-white pt-16 pb-12 border-t border-slate-800 relative overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-12">
          
          <!-- Column 1: Brand Info -->
          <div>
            <a routerLink="/" class="inline-block mb-6">
              <img src="img/logo/F3-3.avif" alt="SoccerProf Logo" class="h-14 w-auto brightness-110 drop-shadow-lg">
            </a>
            <p class="text-slate-400 text-sm leading-relaxed mb-6">
              Professionelles &amp; individuelles Fußballtraining für Kinder, Jugendliche und ambitionierte Spieler in Hamburg.
            </p>
            <div class="flex items-center gap-3">
              <a href="https://instagram.com" target="_blank" class="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center text-slate-300 hover:bg-[#E63946] hover:text-white transition-all">
                <i class="fa-brands fa-instagram"></i>
              </a>
              <a href="https://facebook.com" target="_blank" class="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center text-slate-300 hover:bg-[#E63946] hover:text-white transition-all">
                <i class="fa-brands fa-facebook"></i>
              </a>
              <a href="https://youtube.com" target="_blank" class="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center text-slate-300 hover:bg-[#E63946] hover:text-white transition-all">
                <i class="fa-brands fa-youtube"></i>
              </a>
            </div>
          </div>

          <!-- Column 2: Navigation -->
          <div>
            <h4 class="font-heading text-lg font-bold mb-5 text-[#D4AF37]">Trainingsangebote</h4>
            <ul class="space-y-3 text-sm text-slate-400">
              <li><a routerLink="/einzeltraining" class="hover:text-white transition-colors">Einzeltraining (ab 40€)</a></li>
              <li><a routerLink="/kleingruppe" class="hover:text-white transition-colors">Kleingruppentraining (20-25€)</a></li>
              <li><a routerLink="/mannschaft" class="hover:text-white transition-colors">Mannschaftstraining (ab 90€)</a></li>
              <li><a routerLink="/trainingsmethoden" class="hover:text-white transition-colors">4-Phasen Trainingsmethode</a></li>
              <li><a routerLink="/veranstaltungen" class="hover:text-white transition-colors">Powercamp (80€/Tag)</a></li>
            </ul>
          </div>

          <!-- Column 3: Quick Links -->
          <div>
            <h4 class="font-heading text-lg font-bold mb-5 text-[#D4AF37]">Informationen</h4>
            <ul class="space-y-3 text-sm text-slate-400">
              <li><a routerLink="/ueber-uns" class="hover:text-white transition-colors">Über Sami Ghaouar</a></li>
              <li><a routerLink="/preise" class="hover:text-white transition-colors">Preise &amp; Pakete</a></li>
              <li><a routerLink="/jobs" class="hover:text-white transition-colors">Jobs &amp; Karriere</a></li>
              <li><a routerLink="/faq" class="hover:text-white transition-colors">Häufige Fragen (FAQ)</a></li>
              <li><a routerLink="/shop" class="hover:text-white transition-colors">SoccerProf Fan-Shop</a></li>
            </ul>
          </div>

          <!-- Column 4: Contact -->
          <div>
            <h4 class="font-heading text-lg font-bold mb-5 text-[#D4AF37]">Kontakt Hamburg</h4>
            <div class="space-y-3 text-sm text-slate-400">
              <p class="flex items-start gap-3">
                <i class="fa-solid fa-location-dot text-[#E63946] mt-1"></i>
                <span>SoccerProf Academy<br>Hamburg &amp; Umgebung</span>
              </p>
              <p class="flex items-center gap-3">
                <i class="fa-solid fa-phone text-[#E63946]"></i>
                <a href="tel:+4917600000000" class="hover:text-white transition-colors">+49 (0) 176 / 000 000 00</a>
              </p>
              <p class="flex items-center gap-3">
                <i class="fa-solid fa-envelope text-[#E63946]"></i>
                <a href="mailto:info@soccerprof.de" class="hover:text-white transition-colors">info&#64;soccerprof.de</a>
              </p>
            </div>
          </div>

        </div>

        <div class="pt-8 border-t border-slate-800/80 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-500 gap-4">
          <p>© 2026 SoccerProf Academy. Alle Rechte vorbehalten.</p>
          <div class="flex items-center gap-6">
            <a routerLink="/impressum" class="hover:text-slate-400 transition-colors">Impressum</a>
            <a routerLink="/datenschutz" class="hover:text-slate-400 transition-colors">Datenschutz</a>
            <a routerLink="/cookie-richtlinie" class="hover:text-slate-400 transition-colors">Cookie-Richtlinie</a>
          </div>
        </div>
      </div>
    </footer>
  `
})
export class FooterComponent {}
