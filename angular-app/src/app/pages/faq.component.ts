import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-faq',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="pt-32 pb-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-12">
        <span class="inline-block px-3 py-1 bg-[#E63946]/10 text-[#E63946] font-bold text-xs rounded-full uppercase mb-3">Antworten auf deine Fragen</span>
        <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tight">Häufig gestellte Fragen (FAQ)</h1>
      </div>
      <div class="glass-card p-8 md:p-12 rounded-3xl space-y-6 text-slate-700 leading-relaxed">
        
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

      </div>
    </div>
  `
})
export class FaqComponent {}
