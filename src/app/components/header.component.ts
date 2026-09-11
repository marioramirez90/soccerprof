import { Component, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [CommonModule, RouterLink, RouterLinkActive],
  template: `
    <header id="main-header" class="fixed top-0 left-0 w-full z-50 glass-nav transition-all duration-300 shadow-sm">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
        <!-- Brand Logo -->
        <a routerLink="/" class="flex items-center gap-3 group">
          <img src="img/logo/F3-3.avif" alt="SoccerProf Academy Logo"
            class="h-12 sm:h-14 w-auto object-contain group-hover:scale-105 transition-transform drop-shadow-sm">
        </a>

        <!-- Desktop Navigation Links -->
        <nav class="hidden lg:flex items-center gap-7 text-sm font-bold">
          <a routerLink="/training" routerLinkActive="text-[#E63946] active" [routerLinkActiveOptions]="{exact: true}" class="nav-link-anim text-slate-700 hover:text-[#E63946]">Training</a>
          <a routerLink="/trainingsmethoden" routerLinkActive="text-[#E63946] active" class="nav-link-anim text-slate-700 hover:text-[#E63946]">Trainingsmethoden</a>
          <a routerLink="/ueber-uns" routerLinkActive="text-[#E63946] active" class="nav-link-anim text-slate-700 hover:text-[#E63946]">Über uns</a>
          <a routerLink="/preise" routerLinkActive="text-[#E63946] active" class="nav-link-anim text-slate-700 hover:text-[#E63946]">Preise</a>
          <a routerLink="/kontakt" routerLinkActive="text-[#E63946] active" class="nav-link-anim text-slate-700 hover:text-[#E63946]">Kontakt</a>
        </nav>

        <!-- Right Action Group: Shop & Primary CTA -->
        <div class="hidden sm:flex items-center gap-4">
          <a routerLink="/shop"
            class="p-2.5 rounded-full text-slate-700 hover:text-[#E63946] hover:bg-slate-100 transition-colors relative"
            title="Fan-Shop">
            <i class="fa-solid fa-bag-shopping text-lg"></i>
          </a>

          <a routerLink="/kontakt"
            class="btn-fill-red inline-flex items-center justify-center px-6 py-2.5 rounded-full bg-[#E63946] text-white font-bold text-sm tracking-wide shadow-red-glow hover:shadow-xl transition-all">
            <span>Probetraining anfragen</span>
          </a>
        </div>

        <!-- Mobile Menu Toggle Button -->
        <button (click)="toggleMenu()" class="lg:hidden p-2 rounded-lg text-slate-700 hover:bg-slate-100 transition-colors" aria-label="Menu Toggle">
          <i [class]="isMenuOpen() ? 'fa-solid fa-xmark text-2xl' : 'fa-solid fa-bars text-2xl'"></i>
        </button>
      </div>

      <!-- Mobile Navigation Drawer -->
      <div *ngIf="isMenuOpen()" class="lg:hidden bg-white/95 backdrop-blur-xl border-b border-slate-200 px-6 py-6 transition-all duration-300">
        <div class="flex flex-col gap-4 font-bold">
          <a routerLink="/" (click)="closeMenu()" class="py-2 text-slate-800 hover:text-[#E63946]">Startseite</a>
          <a routerLink="/training" (click)="closeMenu()" class="py-2 text-slate-800 hover:text-[#E63946]">Training</a>
          <a routerLink="/einzeltraining" (click)="closeMenu()" class="py-2 pl-4 text-slate-600 hover:text-[#E63946]">↳ Einzeltraining</a>
          <a routerLink="/kleingruppe" (click)="closeMenu()" class="py-2 pl-4 text-slate-600 hover:text-[#E63946]">↳ Kleingruppe</a>
          <a routerLink="/mannschaft" (click)="closeMenu()" class="py-2 pl-4 text-slate-600 hover:text-[#E63946]">↳ Mannschaftstraining</a>
          <a routerLink="/trainingsmethoden" (click)="closeMenu()" class="py-2 text-slate-800 hover:text-[#E63946]">Trainingsmethoden</a>
          <a routerLink="/ueber-uns" (click)="closeMenu()" class="py-2 text-slate-800 hover:text-[#E63946]">Über uns</a>
          <a routerLink="/preise" (click)="closeMenu()" class="py-2 text-slate-800 hover:text-[#E63946]">Preise & Pakete</a>
          <a routerLink="/veranstaltungen" (click)="closeMenu()" class="py-2 text-slate-800 hover:text-[#E63946]">Powercamp & Events</a>
          <a routerLink="/jobs" (click)="closeMenu()" class="py-2 text-slate-800 hover:text-[#E63946]">Jobs & Karriere</a>
          <a routerLink="/faq" (click)="closeMenu()" class="py-2 text-slate-800 hover:text-[#E63946]">FAQ</a>
          <a routerLink="/shop" (click)="closeMenu()" class="py-2 text-slate-800 hover:text-[#E63946]">Shop</a>
          <a routerLink="/kontakt" (click)="closeMenu()" class="mt-2 text-center py-3 bg-[#E63946] text-white rounded-xl font-bold shadow-lg">Probetraining anfragen</a>
        </div>
      </div>
    </header>
  `
})
export class HeaderComponent {
  isMenuOpen = signal(false);

  toggleMenu() {
    this.isMenuOpen.update(v => !v);
  }

  closeMenu() {
    this.isMenuOpen.set(false);
  }
}
