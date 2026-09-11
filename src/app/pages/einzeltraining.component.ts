import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-einzeltraining',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <div class="pt-32 pb-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-12">
        <span class="inline-block px-3 py-1 bg-[#E63946]/10 text-[#E63946] font-bold text-xs rounded-full uppercase mb-3">Intensivförderung ab 40€</span>
        <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tight">Individuelles Einzeltraining (1:1)</h1>
      </div>
      <div class="glass-card p-8 md:p-12 rounded-3xl space-y-6 text-slate-700 leading-relaxed">
        
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

      </div>
    </div>
  `
})
export class EinzeltrainingComponent {}
