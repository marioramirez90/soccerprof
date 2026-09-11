import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-footer',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <footer class="bg-white text-slate-600 border-t border-slate-200">
      <div class="sp-container" style="padding-block: 64px 32px;">

        <!-- Top Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-14">

          <!-- Brand Column -->
          <div class="lg:col-span-1">
            <a routerLink="/" class="inline-block mb-4">
              <img src="img/logo/F3-3.avif" alt="SoccerProf Academy" class="h-10 w-auto">
            </a>
            <p class="text-slate-500 text-sm leading-relaxed mb-6 max-w-xs">
              Professionelles & individuelles Fußballtraining für Kinder, Jugendliche und ambitionierte Spieler in Hamburg.
            </p>
            <!-- Social icons -->
            <div class="flex items-center gap-3">
              <a href="https://instagram.com" target="_blank" rel="noopener"
                class="w-9 h-9 rounded-xl bg-slate-50 border border-slate-200 flex items-center justify-center text-slate-600 hover:text-red-600 hover:border-red-200 transition-all"
                title="Instagram">
                <i class="fa-brands fa-instagram text-sm"></i>
              </a>
              <a href="https://facebook.com" target="_blank" rel="noopener"
                class="w-9 h-9 rounded-xl bg-slate-50 border border-slate-200 flex items-center justify-center text-slate-600 hover:text-red-600 hover:border-red-200 transition-all"
                title="Facebook">
                <i class="fa-brands fa-facebook text-sm"></i>
              </a>
              <a href="https://youtube.com" target="_blank" rel="noopener"
                class="w-9 h-9 rounded-xl bg-slate-50 border border-slate-200 flex items-center justify-center text-slate-600 hover:text-red-600 hover:border-red-200 transition-all"
                title="YouTube">
                <i class="fa-brands fa-youtube text-sm"></i>
              </a>
              <a href="https://tiktok.com" target="_blank" rel="noopener"
                class="w-9 h-9 rounded-xl bg-slate-50 border border-slate-200 flex items-center justify-center text-slate-600 hover:text-red-600 hover:border-red-200 transition-all"
                title="TikTok">
                <i class="fa-brands fa-tiktok text-sm"></i>
              </a>
            </div>
          </div>

          <!-- Training Column -->
          <div>
            <h4 class="text-slate-900 font-heading font-bold mb-4 text-xs uppercase tracking-wider">Trainingsangebote</h4>
            <ul class="flex flex-col gap-2.5">
              <li><a routerLink="/einzeltraining" class="footer-link">Einzeltraining <span class="text-slate-400 text-xs ml-1">ab 40€</span></a></li>
              <li><a routerLink="/kleingruppe" class="footer-link">Kleingruppentraining <span class="text-slate-400 text-xs ml-1">20–25€</span></a></li>
              <li><a routerLink="/mannschaft" class="footer-link">Mannschaftstraining <span class="text-slate-400 text-xs ml-1">ab 90€</span></a></li>
              <li><a routerLink="/trainingsmethoden" class="footer-link">4-Phasen-Methode</a></li>
              <li><a routerLink="/veranstaltungen" class="footer-link">Powercamp & Events</a></li>
            </ul>
          </div>

          <!-- Info Column -->
          <div>
            <h4 class="text-slate-900 font-heading font-bold mb-4 text-xs uppercase tracking-wider">Informationen</h4>
            <ul class="flex flex-col gap-2.5">
              <li><a routerLink="/ueber-uns" class="footer-link">Über Sami Ghaouar</a></li>
              <li><a routerLink="/preise" class="footer-link">Preise & Pakete</a></li>
              <li><a routerLink="/jobs" class="footer-link">Trainer Jobs</a></li>
              <li><a routerLink="/faq" class="footer-link">Häufige Fragen (FAQ)</a></li>
              <li><a routerLink="/shop" class="footer-link">SoccerProf Fan-Shop</a></li>
              <li><a routerLink="/kontakt" class="footer-link">Kontakt Hamburg</a></li>
            </ul>
          </div>

          <!-- Contact Column -->
          <div>
            <h4 class="text-slate-900 font-heading font-bold mb-4 text-xs uppercase tracking-wider">Kontakt Hamburg</h4>
            <div class="flex flex-col gap-3">
              <div class="flex items-start gap-2.5">
                <i class="fa-solid fa-location-dot mt-1 text-red-600 text-xs flex-shrink-0"></i>
                <div>
                  <p class="text-slate-900 text-sm font-semibold">SoccerProf Academy</p>
                  <p class="text-slate-500 text-xs">Hamburg & Region</p>
                </div>
              </div>
              <div class="flex items-center gap-2.5">
                <i class="fa-solid fa-phone text-red-600 text-xs flex-shrink-0"></i>
                <a href="tel:+4917600000000" class="text-slate-600 hover:text-red-600 text-xs transition-colors">
                  +49 (0) 176 / 000 000 00
                </a>
              </div>
              <div class="flex items-center gap-2.5">
                <i class="fa-solid fa-envelope text-red-600 text-xs flex-shrink-0"></i>
                <a href="mailto:info@soccerprof.de" class="text-slate-600 hover:text-red-600 text-xs transition-colors">
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
        <div class="pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 border-t border-slate-100">
          <p class="text-slate-400 text-xs">© 2026 SoccerProf Academy Hamburg · Alle Rechte vorbehalten.</p>
          <div class="flex items-center gap-6">
            <a routerLink="/impressum" class="text-slate-400 hover:text-slate-600 text-xs transition-colors">Impressum</a>
            <a routerLink="/datenschutz" class="text-slate-400 hover:text-slate-600 text-xs transition-colors">Datenschutz</a>
            <a routerLink="/cookie-richtlinie" class="text-slate-400 hover:text-slate-600 text-xs transition-colors">Cookie-Richtlinie</a>
          </div>
        </div>
      </div>
    </footer>
  `,
  styles: [`
    .footer-link {
      color: #64748b;
      font-size: 0.85rem;
      text-decoration: none;
      transition: color 0.15s ease;
    }
    .footer-link:hover {
      color: #dc2626;
    }
  `]
})
export class FooterComponent {}
