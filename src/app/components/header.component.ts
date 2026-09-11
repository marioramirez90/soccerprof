import { Component, signal, HostListener } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [CommonModule, RouterLink, RouterLinkActive],
  template: `
    <header id="main-header"
      class="sp-nav"
      [class.scrolled]="isScrolled()">
      <div class="sp-container w-full flex items-center justify-between">

        <!-- Brand Logo -->
        <a routerLink="/" class="flex items-center gap-3 group flex-shrink-0">
          <img src="img/logo/F3-3.avif"
            alt="SoccerProf Academy"
            class="h-10 sm:h-11 w-auto object-contain transition-transform duration-200 group-hover:scale-105">
        </a>

        <!-- Desktop Navigation -->
        <nav class="hidden lg:flex items-center gap-8">
          <a routerLink="/training" routerLinkActive="active" [routerLinkActiveOptions]="{exact:true}"
            class="sp-nav-link">Training</a>
          <a routerLink="/trainingsmethoden" routerLinkActive="active"
            class="sp-nav-link">Methoden</a>
          <a routerLink="/ueber-uns" routerLinkActive="active"
            class="sp-nav-link">Über uns</a>
          <a routerLink="/preise" routerLinkActive="active"
            class="sp-nav-link">Preise</a>
          <a routerLink="/faq" routerLinkActive="active"
            class="sp-nav-link">FAQ</a>
        </nav>

        <!-- Right Actions -->
        <div class="hidden md:flex items-center gap-4">
          <a routerLink="/shop"
            class="text-slate-600 hover:text-red-600 p-2 rounded-lg transition-colors"
            title="Fan-Shop">
            <i class="fa-solid fa-bag-shopping text-base"></i>
          </a>
          <a routerLink="/kontakt" class="btn btn-primary btn-sm">
            Probetraining anfragen
          </a>
        </div>

        <!-- Mobile Hamburger (Dark Bars) -->
        <button (click)="toggleMenu()"
          class="lg:hidden flex flex-col items-center justify-center w-10 h-10 gap-1.5 rounded-lg hover:bg-slate-100 transition-colors"
          aria-label="Navigation öffnen">
          <span class="block w-5 h-0.5 bg-slate-800 transition-all duration-300"
            [class.rotate-45]="isMenuOpen()"
            [class.translate-y-2]="isMenuOpen()"></span>
          <span class="block w-5 h-0.5 bg-slate-800 transition-all duration-300"
            [class.opacity-0]="isMenuOpen()"></span>
          <span class="block w-5 h-0.5 bg-slate-800 transition-all duration-300"
            [class.-rotate-45]="isMenuOpen()"
            [class.-translate-y-2]="isMenuOpen()"></span>
        </button>

      </div>

      <!-- Mobile Drawer -->
      <div *ngIf="isMenuOpen()"
        class="lg:hidden absolute top-full left-0 right-0 bg-white border-b border-slate-200 shadow-xl">
        <div class="sp-container py-6 flex flex-col gap-1">
          <a routerLink="/" (click)="closeMenu()" class="mobile-nav-link">Startseite</a>
          <a routerLink="/training" (click)="closeMenu()" class="mobile-nav-link">Training</a>
          <a routerLink="/einzeltraining" (click)="closeMenu()" class="mobile-nav-link pl-8 text-sm">↳ Einzeltraining</a>
          <a routerLink="/kleingruppe" (click)="closeMenu()" class="mobile-nav-link pl-8 text-sm">↳ Kleingruppe</a>
          <a routerLink="/mannschaft" (click)="closeMenu()" class="mobile-nav-link pl-8 text-sm">↳ Mannschaftstraining</a>
          <a routerLink="/trainingsmethoden" (click)="closeMenu()" class="mobile-nav-link">Trainingsmethoden</a>
          <a routerLink="/ueber-uns" (click)="closeMenu()" class="mobile-nav-link">Über uns</a>
          <a routerLink="/preise" (click)="closeMenu()" class="mobile-nav-link">Preise & Pakete</a>
          <a routerLink="/veranstaltungen" (click)="closeMenu()" class="mobile-nav-link">Powercamp</a>
          <a routerLink="/jobs" (click)="closeMenu()" class="mobile-nav-link">Jobs & Karriere</a>
          <a routerLink="/faq" (click)="closeMenu()" class="mobile-nav-link">FAQ</a>
          <a routerLink="/shop" (click)="closeMenu()" class="mobile-nav-link">Fan-Shop</a>
          <div class="pt-4 mt-2 border-t border-slate-100">
            <a routerLink="/kontakt" (click)="closeMenu()" class="btn btn-primary w-full">
              <i class="fa-solid fa-calendar-check text-xs"></i>
              Probetraining anfragen
            </a>
          </div>
        </div>
      </div>
    </header>
  `,
  styles: [`
    .mobile-nav-link {
      display: block;
      padding: 10px 14px;
      color: #334155;
      font-weight: 600;
      font-size: 0.95rem;
      border-radius: 8px;
      transition: all 0.2s ease;
      text-decoration: none;
    }
    .mobile-nav-link:hover {
      color: #dc2626;
      background: #f8fafc;
    }
  `]
})
export class HeaderComponent {
  isMenuOpen = signal(false);
  isScrolled = signal(false);

  @HostListener('window:scroll', [])
  onScroll() {
    this.isScrolled.set(window.scrollY > 15);
  }

  toggleMenu() {
    this.isMenuOpen.update(v => !v);
  }

  closeMenu() {
    this.isMenuOpen.set(false);
  }
}
