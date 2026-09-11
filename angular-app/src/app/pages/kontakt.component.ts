import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-kontakt',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="pt-32 pb-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-12">
        <span class="inline-block px-3 py-1 bg-[#E63946]/10 text-[#E63946] font-bold text-xs rounded-full uppercase mb-3">Wir freuen uns auf dich</span>
        <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tight">Kontakt & Probetraining Anfragen</h1>
      </div>
      <div class="glass-card p-8 md:p-12 rounded-3xl space-y-6 text-slate-700 leading-relaxed">
        
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

      </div>
    </div>
  `
})
export class KontaktComponent {}
