import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-trainingsmethoden',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="pt-32 pb-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-12">
        <span class="inline-block px-3 py-1 bg-[#E63946]/10 text-[#E63946] font-bold text-xs rounded-full uppercase mb-3">Methodik & Philosophie</span>
        <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tight">Unsere 4-Phasen Trainingsmethode</h1>
      </div>
      <div class="glass-card p-8 md:p-12 rounded-3xl space-y-6 text-slate-700 leading-relaxed">
        
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

      </div>
    </div>
  `
})
export class TrainingsmethodenComponent {}
