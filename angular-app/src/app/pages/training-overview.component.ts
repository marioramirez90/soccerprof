import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-training-overview',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <div class="pt-32 pb-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-12">
        <span class="inline-block px-3 py-1 bg-[#E63946]/10 text-[#E63946] font-bold text-xs rounded-full uppercase mb-3">Professional Soccer Training</span>
        <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tight">Trainingsangebote Übersicht</h1>
      </div>
      <div class="glass-card p-8 md:p-12 rounded-3xl space-y-6 text-slate-700 leading-relaxed">
        
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

      </div>
    </div>
  `
})
export class TrainingOverviewComponent {}
