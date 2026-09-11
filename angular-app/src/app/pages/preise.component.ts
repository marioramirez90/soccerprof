import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-preise',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="pt-32 pb-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-12">
        <span class="inline-block px-3 py-1 bg-[#E63946]/10 text-[#E63946] font-bold text-xs rounded-full uppercase mb-3">Transparente Konditionen</span>
        <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tight">Preise & Trainingspakete</h1>
      </div>
      <div class="glass-card p-8 md:p-12 rounded-3xl space-y-6 text-slate-700 leading-relaxed">
        
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

      </div>
    </div>
  `
})
export class PreiseComponent {}
