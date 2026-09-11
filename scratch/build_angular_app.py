import os
import shutil

BASE_DIR = r"c:\Users\mario\Desktop\newsoccerprof"
ANGULAR_DIR = os.path.join(BASE_DIR, "angular-app")
SRC_DIR = os.path.join(ANGULAR_DIR, "src")
APP_DIR = os.path.join(SRC_DIR, "app")
PUBLIC_DIR = os.path.join(ANGULAR_DIR, "public")

# Copy img folder to public/img
src_img = os.path.join(BASE_DIR, "img")
dst_img = os.path.join(PUBLIC_DIR, "img")
if os.path.exists(src_img):
    if os.path.exists(dst_img):
        shutil.rmtree(dst_img)
    shutil.copytree(src_img, dst_img)
    print("Copied img to public/img successfully.")

comp_dir = os.path.join(APP_DIR, "components")
pages_dir = os.path.join(APP_DIR, "pages")
os.makedirs(comp_dir, exist_ok=True)
os.makedirs(pages_dir, exist_ok=True)

# Helper function to generate subpage component
def create_subpage(filename, class_name, title, subtitle, content_html, use_router_link=False):
    imports = "import { Component } from '@angular/core';\nimport { CommonModule } from '@angular/common';\n"
    comp_imports = "CommonModule"
    if use_router_link:
        imports += "import { RouterLink } from '@angular/router';\n"
        comp_imports += ", RouterLink"

    code = f"""{imports}
@Component({{
  selector: 'app-{filename[:-13]}',
  standalone: true,
  imports: [{comp_imports}],
  template: `
    <div class="pt-32 pb-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-12">
        <span class="inline-block px-3 py-1 bg-[#E63946]/10 text-[#E63946] font-bold text-xs rounded-full uppercase mb-3">{subtitle}</span>
        <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tight">{title}</h1>
      </div>
      <div class="glass-card p-8 md:p-12 rounded-3xl space-y-6 text-slate-700 leading-relaxed">
        {content_html}
      </div>
    </div>
  `
}})
export class {class_name} {{}}
"""
    with open(os.path.join(pages_dir, filename), "w", encoding="utf-8") as f:
        f.write(code)

# 1. MAIN.TS
MAIN_TS = """import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app';

bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));
"""
with open(os.path.join(SRC_DIR, "main.ts"), "w", encoding="utf-8") as f:
    f.write(MAIN_TS)

# 2. INDEX.HTML
INDEX_HTML = """<!DOCTYPE html>
<html lang="de" class="scroll-smooth">
<head>
  <meta charset="utf-8">
  <title>SoccerProf Academy | Privater Fußballtrainer Hamburg</title>
  <base href="/">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="SoccerProf bietet ein privates, professionelles und individuelles Fussballtraining für Kinder, Jugendliche und auch Erwachsene in Hamburg.">
  <link rel="icon" type="image/x-icon" href="img/favicon.ico">
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
  
  <!-- FontAwesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  
  <!-- AOS CSS -->
  <link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css" />
</head>
<body class="bg-mesh relative grid-pattern antialiased text-slate-900 pb-20 sm:pb-0">
  <app-root></app-root>
  <script src="https://unpkg.com/aos@next/dist/aos.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      if (typeof AOS !== 'undefined') {
        AOS.init({ duration: 800, once: true, offset: 50 });
      }
    });
  </script>
</body>
</html>
"""
with open(os.path.join(SRC_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(INDEX_HTML)

# 3. STYLES.CSS
STYLES_CSS = """@import "tailwindcss";

@layer base {
  body {
    font-family: 'Plus Jakarta Sans', sans-serif;
    background-color: #F8FAFC;
    color: #0F172A;
    overflow-x: hidden;
  }
  h1, h2, h3, .font-heading {
    font-family: 'Outfit', sans-serif;
  }
}

.bg-mesh {
  background-image: 
    radial-gradient(at 10% 20%, rgba(212, 175, 55, 0.08) 0px, transparent 50%),
    radial-gradient(at 90% 10%, rgba(230, 57, 70, 0.08) 0px, transparent 50%),
    radial-gradient(at 50% 80%, rgba(15, 23, 42, 0.05) 0px, transparent 50%),
    radial-gradient(circle at 50% 50%, rgba(248, 250, 252, 0.85) 0%, #F8FAFC 100%);
}

.grid-pattern {
  background-size: 40px 40px;
  background-image: 
    linear-gradient(to right, rgba(15, 23, 42, 0.03) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(15, 23, 42, 0.03) 1px, transparent 1px);
}

.glass-card {
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(226, 232, 240, 0.9);
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.glass-card:hover {
  border-color: #D4AF37;
  transform: translateY(-6px);
  box-shadow: 0 20px 40px -15px rgba(212, 175, 55, 0.2);
}

.glass-nav {
  background: rgba(255, 255, 255, 0.88);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(226, 232, 240, 0.8);
}

.nav-link-anim {
  position: relative;
  transition: color 0.3s ease;
}

.nav-link-anim::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0%;
  height: 2px;
  background: #E63946;
  transition: width 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  border-radius: 2px;
}

.nav-link-anim:hover::after, .nav-link-anim.active::after {
  width: 100%;
}

.btn-fill-red {
  position: relative;
  overflow: hidden;
  z-index: 1;
  transition: color 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease, box-shadow 0.4s ease;
}

.btn-fill-red::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #C52233 0%, #900C1C 100%);
  z-index: -1;
  transform: translateY(100%);
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  border-radius: inherit;
}

.btn-fill-red:hover::before, .btn-fill-red:active::before {
  transform: translateY(0%);
}

.btn-fill-gold {
  position: relative;
  overflow: hidden;
  z-index: 1;
  transition: color 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease, box-shadow 0.4s ease;
}

.btn-fill-gold::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #D4AF37 0%, #B38F24 100%);
  z-index: -1;
  transform: translateY(100%);
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  border-radius: inherit;
}

.btn-fill-gold:hover::before, .btn-fill-gold:active::before {
  transform: translateY(0%);
}

#logo-bg-overlay {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 2;
  overflow: hidden;
  perspective: 1000px;
  transform-style: preserve-3d;
}

.global-logo-particle {
  position: absolute;
  width: 52px;
  height: 52px;
  background-image: url('/img/logo/F3-3.avif');
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  transform-origin: center center;
  will-change: transform, opacity;
  backface-visibility: hidden;
  filter: drop-shadow(0 6px 14px rgba(0,0,0,0.15));
}
"""
with open(os.path.join(SRC_DIR, "styles.css"), "w", encoding="utf-8") as f:
    f.write(STYLES_CSS)

# 4. HEADER COMPONENT
HEADER_TS = """import { Component, signal } from '@angular/core';
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
"""
with open(os.path.join(comp_dir, "header.component.ts"), "w", encoding="utf-8") as f:
    f.write(HEADER_TS)

# 5. FOOTER COMPONENT
FOOTER_TS = """import { Component } from '@angular/core';
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
"""
with open(os.path.join(comp_dir, "footer.component.ts"), "w", encoding="utf-8") as f:
    f.write(FOOTER_TS)

# 6. 3D LOGO OVERLAY COMPONENT
LOGO_OVERLAY_TS = """import { Component, OnInit, OnDestroy, HostListener } from '@angular/core';
import { CommonModule } from '@angular/common';

interface Particle {
  baseX: number;
  baseY: number;
  baseZ: number;
  rotSpeed: number;
  currentZ: number;
  style: any;
}

@Component({
  selector: 'app-logo-bg-overlay',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div id="logo-bg-overlay">
      <div *ngFor="let p of particles" 
        class="global-logo-particle"
        [ngStyle]="p.style">
      </div>
    </div>
  `
})
export class LogoBgOverlayComponent implements OnInit, OnDestroy {
  particles: Particle[] = [];
  private animFrameId: number | null = null;

  ngOnInit() {
    this.initParticles();
    this.updatePositions();
  }

  ngOnDestroy() {
    if (this.animFrameId !== null) {
      cancelAnimationFrame(this.animFrameId);
    }
  }

  @HostListener('window:scroll', [])
  onScroll() {
    this.updatePositions();
  }

  private initParticles() {
    const total = 18;
    this.particles = [];

    for (let i = 0; i < total; i++) {
      const baseX = 8 + (i % 6) * 16 + (Math.random() * 8 - 4);
      const baseY = 10 + Math.floor(i / 6) * 28 + (Math.random() * 12 - 6);
      const baseZ = -700 + (i * 65);
      const rotSpeed = 0.15 + Math.random() * 0.35;

      this.particles.push({
        baseX,
        baseY,
        baseZ,
        rotSpeed,
        currentZ: baseZ,
        style: {}
      });
    }
  }

  private updatePositions() {
    const scrollY = window.scrollY || window.pageYOffset || 0;
    const loopSpan = 1150;

    this.particles.forEach((p, i) => {
      let z = p.baseZ + scrollY * 0.75;
      let shiftCount = Math.floor((z - (-700)) / loopSpan);
      let currentZ = z - (shiftCount * loopSpan);
      if (currentZ > 450) currentZ -= loopSpan;
      if (currentZ < -700) currentZ += loopSpan;

      const normZ = (currentZ - (-700)) / 1150;
      let opacity = 0;
      if (normZ < 0.15) opacity = normZ / 0.15;
      else if (normZ > 0.82) opacity = (1 - normZ) / 0.18;
      else opacity = 1;

      opacity = Math.max(0, Math.min(0.24, opacity * 0.24));
      const rot = (scrollY * p.rotSpeed + i * 35) % 360;

      p.style = {
        left: p.baseX + '%',
        top: p.baseY + '%',
        transform: `translate3d(0, 0, ${currentZ}px) rotate(${rot}deg)`,
        opacity: opacity
      };
    });
  }
}
"""
with open(os.path.join(comp_dir, "logo-bg-overlay.component.ts"), "w", encoding="utf-8") as f:
    f.write(LOGO_OVERLAY_TS)

# 7. HOME COMPONENT
HOME_TS = """import { Component } from '@angular/core';
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
"""
with open(os.path.join(pages_dir, "home.component.ts"), "w", encoding="utf-8") as f:
    f.write(HOME_TS)

# GENERATE ALL SUBPAGES WITH EXACT ROUTER LINK USAGE
create_subpage("training-overview.component.ts", "TrainingOverviewComponent", "Trainingsangebote Übersicht", "Professional Soccer Training", """
<p class="text-lg">Das SoccerProf Trainingskonzept kombiniert modernes europäisches Nachwuchstraining mit hochintensiver Einzelförderung. Wir bieten individuelle Trainingskonzepte für jede Entwicklungsstufe.</p>
<div class="grid grid-cols-1 md:grid-cols-3 gap-6 pt-6">
  <div class="p-6 bg-slate-50 rounded-2xl border border-slate-200">
    <h3 class="font-bold text-xl mb-2 text-slate-900">Einzeltraining</h3>
    <p class="text-sm text-slate-600 mb-4">1:1 Fokussierung ab 40€ / Einheit.</p>
    <a routerLink="/einzeltraining" class="text-[#E63946] font-bold text-sm hover:underline">Mehr erfahren →</a>
  </div>
  <div class="p-6 bg-slate-50 rounded-2xl border border-slate-200">
    <h3 class="font-bold text-xl mb-2 text-slate-900">Kleingruppentraining</h3>
    <p class="text-sm text-slate-600 mb-4">2-4 Spieler von 20€ bis 25€ / Spieler.</p>
    <a routerLink="/kleingruppe" class="text-[#E63946] font-bold text-sm hover:underline">Mehr erfahren →</a>
  </div>
  <div class="p-6 bg-slate-50 rounded-2xl border border-slate-200">
    <h3 class="font-bold text-xl mb-2 text-slate-900">Mannschaftstraining</h3>
    <p class="text-sm text-slate-600 mb-4">Ergänzungstraining ab 90€ / Einheit.</p>
    <a routerLink="/mannschaft" class="text-[#E63946] font-bold text-sm hover:underline">Mehr erfahren →</a>
  </div>
</div>
""", use_router_link=True)

create_subpage("einzeltraining.component.ts", "EinzeltrainingComponent", "Individuelles Einzeltraining (1:1)", "Intensivförderung ab 40€", """
<p class="text-lg font-semibold text-slate-900">Maximale Aufmerksamkeit für deinen maximalen Leistungsfortschritt.</p>
<p>Im 1:1 Einzeltraining korrigieren wir kleinste Bewegungsdetails, schulen die beidfüßige Ballbeherrschung, verbessern die erste Touch-Qualität und arbeiten gezielt an positionsbezogenen Anforderungen.</p>
<ul class="list-disc pl-6 space-y-2 text-slate-700">
  <li>Detaillierte Stärken-Schwächen-Analyse</li>
  <li>Passschärfe, Dribbling &amp; Finten unter Zeitdruck</li>
  <li>Handlungsschnelligkeit &amp; kognitives Training</li>
  <li>Individuelle Terminabsprache an flexiblen Plätzen in Hamburg</li>
</ul>
<div class="pt-4">
  <a routerLink="/kontakt" class="btn-fill-red inline-block px-8 py-3.5 rounded-xl bg-[#E63946] text-white font-bold">Jetzt Einzeltraining vereinbaren</a>
</div>
""", use_router_link=True)

create_subpage("kleingruppe.component.ts", "KleingruppeComponent", "Kleingruppentraining (2 - 4 Spieler)", "Dynamisches Wetteifer-Training (20 - 25€)", """
<p class="text-lg font-semibold text-slate-900">Trainieren mit Freunden unter professioneller Wettkampfdynamik.</p>
<p>Das Kleingruppentraining vereint die Vorteile des intensiven Einzeltrainings mit realen Spielsituationen wie 1v1, 2v2, Überzahl/Unterzahl sowie schnellem Umschaltspiel.</p>
<p class="font-bold text-slate-900">Preise: 20€ bis 25€ pro Spieler und Einheit.</p>
<div class="pt-4">
  <a routerLink="/kontakt" class="btn-fill-gold inline-block px-8 py-3.5 rounded-xl bg-[#D4AF37] text-slate-950 font-bold">Gruppe anfragen</a>
</div>
""", use_router_link=True)

create_subpage("mannschaft.component.ts", "MannschaftComponent", "Mannschafts- & Teamtraining", "Vereinsergänzung ab 90€", """
<p class="text-lg font-semibold text-slate-900">Gezielte Impulse für dein gesamtes Team.</p>
<p>Wir kommen direkt zu deinem Verein in Hamburg und führen spezialisierte Einheiten für Jugend- und Herrenmannschaften durch (Taktik, Athletik, Umschaltspiel, Torschuss-Intensität).</p>
<div class="pt-4">
  <a routerLink="/kontakt" class="btn-fill-red inline-block px-8 py-3.5 rounded-xl bg-[#E63946] text-white font-bold">Mannschaftstraining buchen</a>
</div>
""", use_router_link=True)

create_subpage("trainingsmethoden.component.ts", "TrainingsmethodenComponent", "Unsere 4-Phasen Trainingsmethode", "Methodik & Philosophie", """
<div class="space-y-6">
  <div class="p-6 bg-slate-50 rounded-2xl border border-slate-200">
    <h3 class="text-xl font-bold text-[#E63946]">Phase 1: Aufwärmung &amp; Kognitionsaktivierung</h3>
    <p class="text-slate-600 mt-2">Dynamisches Aufwärmen, Bewegungsschulung und Aktivierung des zentralen Nervensystems.</p>
  </div>
  <div class="p-6 bg-slate-50 rounded-2xl border border-slate-200">
    <h3 class="text-xl font-bold text-[#D4AF37]">Phase 2: Technischer Hauptteil &amp; Präzision</h3>
    <p class="text-slate-600 mt-2">Fokus auf Passqualität, Erstkontakt, Dribbling und beidfüßige Ballführung.</p>
  </div>
  <div class="p-6 bg-slate-50 rounded-2xl border border-slate-200">
    <h3 class="text-xl font-bold text-slate-900">Phase 3: Spielnahe Wettkampfformen</h3>
    <p class="text-slate-600 mt-2">Anwendung der erlernten Techniken unter Zeit- und Gegnerdruck in variablen Spielformen.</p>
  </div>
  <div class="p-6 bg-slate-50 rounded-2xl border border-slate-200">
    <h3 class="text-xl font-bold text-emerald-600">Phase 4: Feedback, Analyse &amp; Regeneration</h3>
    <p class="text-slate-600 mt-2">Auswertung der Fortschritte, individuelle Hausaufgaben und gezieltes Cool-Down.</p>
  </div>
</div>
""", use_router_link=False)

create_subpage("preise.component.ts", "PreiseComponent", "Preise & Trainingspakete", "Transparente Konditionen", """
<p class="text-lg">Alle Preise auf einen Blick – Faire Konditionen für professionelles Privattraining in Hamburg.</p>
<div class="overflow-x-auto pt-4">
  <table class="w-full text-left border-collapse">
    <thead>
      <tr class="border-b-2 border-slate-300 text-slate-900 font-bold">
        <th class="py-3 px-4">Trainingsart</th>
        <th class="py-3 px-4">Teilnehmer</th>
        <th class="py-3 px-4">Preis</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-slate-200">
      <tr>
        <td class="py-4 px-4 font-bold">Einzeltraining</td>
        <td class="py-4 px-4">1 Spieler</td>
        <td class="py-4 px-4 text-[#E63946] font-extrabold">ab 40€ / Einheit</td>
      </tr>
      <tr>
        <td class="py-4 px-4 font-bold">Kleingruppe</td>
        <td class="py-4 px-4">2 – 4 Spieler</td>
        <td class="py-4 px-4 text-[#D4AF37] font-extrabold">20€ – 25€ / Spieler</td>
      </tr>
      <tr>
        <td class="py-4 px-4 font-bold">Mannschaftstraining</td>
        <td class="py-4 px-4">Ganzes Team</td>
        <td class="py-4 px-4 font-extrabold">ab 90€ / Einheit</td>
      </tr>
      <tr>
        <td class="py-4 px-4 font-bold">Powercamp (Ferien)</td>
        <td class="py-4 px-4">Gruppe</td>
        <td class="py-4 px-4 text-emerald-600 font-extrabold">80€ / Tag (inkl. Verpflegung)</td>
      </tr>
    </tbody>
  </table>
</div>
""", use_router_link=False)

create_subpage("ueber-uns.component.ts", "UeberUnsComponent", "Über SoccerProf & Sami Ghaouar", "Philosophie & Expertise", """
<p class="text-lg">SoccerProf steht für leidenschaftliche Talentförderung im Raum Hamburg. Gründer und Cheftrainer Sami Ghaouar vereint fundiertes Fachwissen mit praxisnaher Trainingserfahrung.</p>
<p>Unser Ziel ist es, Spieler nicht nur sportlich, sondern auch in ihrer Persönlichkeit, Disziplin und Eigenverantwortung zu stärken.</p>
""", use_router_link=False)

create_subpage("veranstaltungen.component.ts", "VeranstaltungenComponent", "Powercamps & Events", "Feriencamps in Hamburg (80€/Tag)", """
<p class="text-lg font-semibold text-slate-900">Unvergessliche Ferientage voller Fußball, Spaß &amp; Intensivität!</p>
<p>Unsere SoccerProf Powercamps finden in allen Hamburger Schulferien statt. Inbegriffen sind 2 Trainingseinheiten pro Tag, Mittagessen, Getränke, Teilnehmer-Trikot und Abschlussturnier.</p>
""", use_router_link=False)

create_subpage("jobs.component.ts", "JobsComponent", "Jobs & Karriere bei SoccerProf", "Werde Teil unseres Trainerteams", """
<p class="text-lg">Du bist begeisterter Fußballtrainer in Hamburg und möchtest Nachwuchstalente individuell fördern?</p>
<p>Wir suchen regelmäßig engagierte Honorartrainer für Einzel- und Kleingruppentraining. Sende deine Bewerbung an <strong>info&#64;soccerprof.de</strong>.</p>
""", use_router_link=False)

create_subpage("faq.component.ts", "FaqComponent", "Häufig gestellte Fragen (FAQ)", "Antworten auf deine Fragen", """
<div class="space-y-4">
  <div class="p-5 bg-slate-50 rounded-xl border border-slate-200">
    <h3 class="font-bold text-slate-900 text-lg">Wo findet das Training in Hamburg statt?</h3>
    <p class="text-slate-600 mt-2">Der Trainingsort wird individuell vereinbart (z.B. Sportplätze, Kunstrasenanlagen oder öffentliche Parks in deiner Nähe in Hamburg).</p>
  </div>
  <div class="p-5 bg-slate-50 rounded-xl border border-slate-200">
    <h3 class="font-bold text-slate-900 text-lg">Für welche Altersklassen ist das Training geeignet?</h3>
    <p class="text-slate-600 mt-2">Wir trainieren Kinder ab 6 Jahren, Jugendliche aller Leistungsstufen sowie Herren- und Damen-Amateurspieler.</p>
  </div>
  <div class="p-5 bg-slate-50 rounded-xl border border-slate-200">
    <h3 class="font-bold text-slate-900 text-lg">Wie kann ich ein Probetraining vereinbaren?</h3>
    <p class="text-slate-600 mt-2">Einfach über unser Kontaktformular oder telefonisch anfragen. Wir melden uns umgehend zur Terminabsprache.</p>
  </div>
</div>
""", use_router_link=False)

create_subpage("kontakt.component.ts", "KontaktComponent", "Kontakt & Probetraining Anfragen", "Wir freuen uns auf dich", """
<div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
  <div class="space-y-6">
    <p class="text-lg">Du hast Fragen oder möchtest direkt ein Probetraining buchen? Schreib uns eine Nachricht!</p>
    <div class="space-y-4 text-slate-700">
      <p class="flex items-center gap-3"><i class="fa-solid fa-envelope text-[#E63946] text-xl"></i> <span>info&#64;soccerprof.de</span></p>
      <p class="flex items-center gap-3"><i class="fa-solid fa-phone text-[#E63946] text-xl"></i> <span>+49 (0) 176 / 000 000 00</span></p>
      <p class="flex items-center gap-3"><i class="fa-solid fa-location-dot text-[#E63946] text-xl"></i> <span>Hamburg &amp; Umgebung</span></p>
    </div>
  </div>
  <form class="space-y-4 bg-slate-50 p-6 rounded-2xl border border-slate-200">
    <div>
      <label class="block text-xs font-bold uppercase text-slate-700 mb-1">Name</label>
      <input type="text" placeholder="Dein Name" class="w-full p-3 rounded-xl border border-slate-300 focus:outline-none focus:border-[#E63946]">
    </div>
    <div>
      <label class="block text-xs font-bold uppercase text-slate-700 mb-1">E-Mail</label>
      <input type="email" placeholder="deine@email.de" class="w-full p-3 rounded-xl border border-slate-300 focus:outline-none focus:border-[#E63946]">
    </div>
    <div>
      <label class="block text-xs font-bold uppercase text-slate-700 mb-1">Nachricht</label>
      <textarea rows="4" placeholder="Gewünschte Trainingsart, Alter, Ort..." class="w-full p-3 rounded-xl border border-slate-300 focus:outline-none focus:border-[#E63946]"></textarea>
    </div>
    <button type="button" class="btn-fill-red w-full py-3.5 bg-[#E63946] text-white font-bold rounded-xl shadow-md">Nachricht senden</button>
  </form>
</div>
""", use_router_link=False)

create_subpage("shop.component.ts", "ShopComponent", "SoccerProf Fan-Shop", "Bekleidung & Trainingsequipment", """
<p class="text-lg">Demnächst verfügbar: Offizielle SoccerProf Trikots, Trainings-Shirts, Hoodies und Zubehör für dein Training!</p>
""", use_router_link=False)

create_subpage("impressum.component.ts", "ImpressumComponent", "Impressum", "Rechtliche Angaben", """
<p class="font-bold">SoccerProf Academy Hamburg</p>
<p>Inhaber: Sami Ghaouar<br>Hamburg, Deutschland</p>
<p>E-Mail: info&#64;soccerprof.de</p>
""", use_router_link=False)

create_subpage("datenschutz.component.ts", "DatenschutzComponent", "Datenschutzerklärung", "Datenschutz & Sicherheit", """
<p>Verantwortlicher für die Datenverarbeitung auf dieser Website ist Sami Ghaouar, SoccerProf Academy Hamburg.</p>
<p>Wir verarbeiten personenbezogene Daten streng vertraulich und gemäß DSGVO.</p>
""", use_router_link=False)

create_subpage("cookie-richtlinie.component.ts", "CookieRichtlinieComponent", "Cookie-Richtlinie", "Informationen zu Cookies", """
<p>Diese Website verwendet nur technisch notwendige Cookies zur Gewährleistung der Grundfunktionen.</p>
""", use_router_link=False)

# 8. APP ROUTES
ROUTES_TS = """import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home.component';
import { TrainingOverviewComponent } from './pages/training-overview.component';
import { EinzeltrainingComponent } from './pages/einzeltraining.component';
import { KleingruppeComponent } from './pages/kleingruppe.component';
import { MannschaftComponent } from './pages/mannschaft.component';
import { TrainingsmethodenComponent } from './pages/trainingsmethoden.component';
import { PreiseComponent } from './pages/preise.component';
import { UeberUnsComponent } from './pages/ueber-uns.component';
import { VeranstaltungenComponent } from './pages/veranstaltungen.component';
import { JobsComponent } from './pages/jobs.component';
import { FaqComponent } from './pages/faq.component';
import { KontaktComponent } from './pages/kontakt.component';
import { ShopComponent } from './pages/shop.component';
import { ImpressumComponent } from './pages/impressum.component';
import { DatenschutzComponent } from './pages/datenschutz.component';
import { CookieRichtlinieComponent } from './pages/cookie-richtlinie.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'training', component: TrainingOverviewComponent },
  { path: 'einzeltraining', component: EinzeltrainingComponent },
  { path: 'kleingruppe', component: KleingruppeComponent },
  { path: 'mannschaft', component: MannschaftComponent },
  { path: 'trainingsmethoden', component: TrainingsmethodenComponent },
  { path: 'preise', component: PreiseComponent },
  { path: 'ueber-uns', component: UeberUnsComponent },
  { path: 'veranstaltungen', component: VeranstaltungenComponent },
  { path: 'jobs', component: JobsComponent },
  { path: 'faq', component: FaqComponent },
  { path: 'kontakt', component: KontaktComponent },
  { path: 'shop', component: ShopComponent },
  { path: 'impressum', component: ImpressumComponent },
  { path: 'datenschutz', component: DatenschutzComponent },
  { path: 'cookie-richtlinie', component: CookieRichtlinieComponent },
  { path: '**', redirectTo: '' }
];
"""
with open(os.path.join(APP_DIR, "app.routes.ts"), "w", encoding="utf-8") as f:
    f.write(ROUTES_TS)

# 9. APP CONFIG
CONFIG_TS = """import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter, withInMemoryScrolling } from '@angular/router';
import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes, withInMemoryScrolling({ scrollPositionRestoration: 'enabled' }))
  ]
};
"""
with open(os.path.join(APP_DIR, "app.config.ts"), "w", encoding="utf-8") as f:
    f.write(CONFIG_TS)

# 10. APP COMPONENT (app.ts)
APP_TS = """import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './components/header.component';
import { FooterComponent } from './components/footer.component';
import { LogoBgOverlayComponent } from './components/logo-bg-overlay.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HeaderComponent, FooterComponent, LogoBgOverlayComponent],
  template: `
    <app-logo-bg-overlay></app-logo-bg-overlay>
    <app-header></app-header>
    <main class="min-h-screen">
      <router-outlet></router-outlet>
    </main>
    <app-footer></app-footer>
  `
})
export class AppComponent {}
"""
with open(os.path.join(APP_DIR, "app.ts"), "w", encoding="utf-8") as f:
    f.write(APP_TS)

print("Angular application generated cleanly with zero unused imports!")
