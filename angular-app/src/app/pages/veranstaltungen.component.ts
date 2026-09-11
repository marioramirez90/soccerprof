import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-veranstaltungen',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="pt-32 pb-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-12">
        <span class="inline-block px-3 py-1 bg-[#E63946]/10 text-[#E63946] font-bold text-xs rounded-full uppercase mb-3">Feriencamps in Hamburg (80€/Tag)</span>
        <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tight">Powercamps & Events</h1>
      </div>
      <div class="glass-card p-8 md:p-12 rounded-3xl space-y-6 text-slate-700 leading-relaxed">
        
<p class="text-lg font-semibold text-slate-900">Unvergessliche Ferientage voller Fußball, Spaß &amp; Intensivität!</p>
<p>Unsere SoccerProf Powercamps finden in allen Hamburger Schulferien statt. Inbegriffen sind 2 Trainingseinheiten pro Tag, Mittagessen, Getränke, Teilnehmer-Trikot und Abschlussturnier.</p>

      </div>
    </div>
  `
})
export class VeranstaltungenComponent {}
