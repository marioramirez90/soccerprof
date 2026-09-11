import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-kleingruppe',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <div class="pt-32 pb-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-12">
        <span class="inline-block px-3 py-1 bg-[#E63946]/10 text-[#E63946] font-bold text-xs rounded-full uppercase mb-3">Dynamisches Wetteifer-Training (20 - 25€)</span>
        <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tight">Kleingruppentraining (2 - 4 Spieler)</h1>
      </div>
      <div class="glass-card p-8 md:p-12 rounded-3xl space-y-6 text-slate-700 leading-relaxed">
        
<p class="text-lg font-semibold text-slate-900">Trainieren mit Freunden unter professioneller Wettkampfdynamik.</p>
<p>Das Kleingruppentraining vereint die Vorteile des intensiven Einzeltrainings mit realen Spielsituationen wie 1v1, 2v2, Überzahl/Unterzahl sowie schnellem Umschaltspiel.</p>
<p class="font-bold text-slate-900">Preise: 20€ bis 25€ pro Spieler und Einheit.</p>
<div class="pt-4">
  <a routerLink="/kontakt" class="btn-fill-gold inline-block px-8 py-3.5 rounded-xl bg-[#D4AF37] text-slate-950 font-bold">Gruppe anfragen</a>
</div>

      </div>
    </div>
  `
})
export class KleingruppeComponent {}
