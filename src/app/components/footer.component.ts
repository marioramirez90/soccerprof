import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-footer',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <footer style="background: var(--sp-dark-2); border-top: 1px solid rgba(255,255,255,0.06);">
      <div class="sp-container" style="padding-block: 72px 40px;">

        <!-- Top Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">

          <!-- Brand Column -->
          <div class="lg:col-span-1">
            <a routerLink="/" class="inline-block mb-6">
              <img src="img/logo/F3-3.avif" alt="SoccerProf Academy" class="h-12 w-auto">
            </a>
            <p class="text-slate-500 text-sm leading-relaxed mb-6" style="max-width: 240px;">
              Professionelles & individuelles Fußballtraining für Kinder, Jugendliche und ambitionierte Spieler in Hamburg.
            </p>
            <!-- Social icons -->
            <div class="flex items-center gap-3">
              <a href="https://instagram.com" target="_blank" rel="noopener"
                class="w-9 h-9 rounded-xl flex items-center justify-center text-slate-400 hover:text-white transition-all"
                style="background: rgba(255,255,255,0.06);">
                <i class="fa-brands fa-instagram text-sm"></i>
              </a>
              <a href="https://facebook.com" target="_blank" rel="noopener"
                class="w-9 h-9 rounded-xl flex items-center justify-center text-slate-400 hover:text-white transition-all"
                style="background: rgba(255,255,255,0.06);">
                <i class="fa-brands fa-facebook text-sm"></i>
              </a>
              <a href="https://youtube.com" target="_blank" rel="noopener"
                class="w-9 h-9 rounded-xl flex items-center justify-center text-slate-400 hover:text-white transition-all"
                style="background: rgba(255,255,255,0.06);">
                <i class="fa-brands fa-youtube text-sm"></i>
              </a>
              <a href="https://tiktok.com" target="_blank" rel="noopener"
                class="w-9 h-9 rounded-xl flex items-center justify-center text-slate-400 hover:text-white transition-all"
                style="background: rgba(255,255,255,0.06);">
                <i class="fa-brands fa-tiktok text-sm"></i>
              </a>
            </div>
          </div>

          <!-- Training Column -->
          <div>
            <h4 class="text-white font-heading font-bold mb-5 text-sm uppercase tracking-wider"
              style="color: var(--sp-gold);">Trainingsangebote</h4>
            <ul class="flex flex-col gap-3">
              <li><a routerLink="/einzeltraining" class="footer-link">Einzeltraining <span class="text-slate-600 ml-1">ab 40€</span></a></li>
              <li><a routerLink="/kleingruppe" class="footer-link">Kleingruppentraining <span class="text-slate-600 ml-1">20–25€</span></a></li>
              <li><a routerLink="/mannschaft" class="footer-link">Mannschaftstraining <span class="text-slate-600 ml-1">ab 90€</span></a></li>
              <li><a routerLink="/trainingsmethoden" class="footer-link">4-Phasen Methode</a></li>
              <li><a routerLink="/veranstaltungen" class="footer-link">Powercamp <span class="text-slate-600 ml-1">80€/Tag</span></a></li>
            </ul>
          </div>

          <!-- Info Column -->
          <div>
            <h4 class="font-heading font-bold mb-5 text-sm uppercase tracking-wider"
              style="color: var(--sp-gold);">Informationen</h4>
            <ul class="flex flex-col gap-3">
              <li><a routerLink="/ueber-uns" class="footer-link">Über Sami Ghaouar</a></li>
              <li><a routerLink="/preise" class="footer-link">Preise & Pakete</a></li>
              <li><a routerLink="/jobs" class="footer-link">Jobs & Karriere</a></li>
              <li><a routerLink="/faq" class="footer-link">Häufige Fragen (FAQ)</a></li>
              <li><a routerLink="/shop" class="footer-link">SoccerProf Fan-Shop</a></li>
              <li><a routerLink="/kontakt" class="footer-link">Kontakt</a></li>
            </ul>
          </div>

          <!-- Contact Column -->
          <div>
            <h4 class="font-heading font-bold mb-5 text-sm uppercase tracking-wider"
              style="color: var(--sp-gold);">Kontakt Hamburg</h4>
            <div class="flex flex-col gap-4">
              <div class="flex items-start gap-3">
                <i class="fa-solid fa-location-dot mt-0.5 flex-shrink-0" style="color: var(--sp-red);"></i>
                <div>
                  <p class="text-white text-sm font-bold">SoccerProf Academy</p>
                  <p class="text-slate-500 text-sm">Hamburg & Umgebung</p>
                </div>
              </div>
              <div class="flex items-center gap-3">
                <i class="fa-solid fa-phone flex-shrink-0" style="color: var(--sp-red);"></i>
                <a href="tel:+4917600000000" class="text-slate-400 hover:text-white text-sm transition-colors">
                  +49 (0) 176 / 000 000 00
                </a>
              </div>
              <div class="flex items-center gap-3">
                <i class="fa-solid fa-envelope flex-shrink-0" style="color: var(--sp-red);"></i>
                <a href="mailto:info@soccerprof.de" class="text-slate-400 hover:text-white text-sm transition-colors">
                  info&#64;soccerprof.de
                </a>
              </div>
            </div>

            <!-- Mini CTA -->
            <div class="mt-6">
              <a routerLink="/kontakt" class="btn btn-primary btn-sm">
                Probetraining anfragen
              </a>
            </div>
          </div>
        </div>

        <!-- Bottom Bar -->
        <div class="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4"
          style="border-top: 1px solid rgba(255,255,255,0.06);">
          <p class="text-slate-600 text-xs">© 2026 SoccerProf Academy · Alle Rechte vorbehalten.</p>
          <div class="flex items-center gap-6">
            <a routerLink="/impressum" class="text-slate-600 hover:text-slate-400 text-xs transition-colors">Impressum</a>
            <a routerLink="/datenschutz" class="text-slate-600 hover:text-slate-400 text-xs transition-colors">Datenschutz</a>
            <a routerLink="/cookie-richtlinie" class="text-slate-600 hover:text-slate-400 text-xs transition-colors">Cookie-Richtlinie</a>
          </div>
        </div>
      </div>
    </footer>
  `,
  styles: [`
    .footer-link {
      color: #64748b;
      font-size: 0.875rem;
      text-decoration: none;
      transition: color 0.2s ease;
    }
    .footer-link:hover {
      color: #e8edf5;
    }
  `]
})
export class FooterComponent {}
