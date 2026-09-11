import os

workspace_dir = r"c:\Users\mario\Desktop\newsoccerprof"

from build_clean_soccerprof import get_head, get_header, get_footer, get_scripts

def make_page(filename, title, heading, subtitle, content_html, active_nav=""):
    full_html = f'''{get_head(title=title)}
<body class="bg-mesh relative grid-pattern antialiased text-slate-900 pb-20 sm:pb-0">

  {get_header(active_page=active_nav)}

  <!-- HERO HEADER FOR SUBPAGE -->
  <section class="pt-32 pb-16 bg-[#090D16] text-white relative z-10 border-b border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="max-w-3xl text-left space-y-4" data-aos="fade-right">
        <div class="inline-block px-3.5 py-1 rounded-full bg-[#D4AF37]/20 text-[#D4AF37] font-black text-xs uppercase tracking-widest border border-[#D4AF37]/30">
          SoccerProf Academy Hamburg
        </div>
        <h1 class="text-3xl sm:text-4xl lg:text-5xl font-black text-white tracking-tight">{heading}</h1>
        <p class="text-slate-300 font-medium text-base sm:text-lg">{subtitle}</p>
      </div>
    </div>
  </section>

  <!-- CONTENT -->
  <main class="py-16 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      {content_html}
    </div>
  </main>

  {get_footer()}
  {get_scripts()}'''

    with open(os.path.join(workspace_dir, filename), "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Created {filename}")

# 1. training.html
make_page(
    "training.html",
    "Trainingsangebote | SoccerProf Academy Hamburg",
    "Unsere Trainingsangebote",
    "Was möchten deine Kinder, Teenager oder auch du selbst lernen? Jedes Fußballtraining wird individuell auf die Stärken und Schwächen der Spieler:innen angepasst.",
    '''<div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="glass-card p-8 rounded-3xl space-y-4">
        <span class="text-xs font-black uppercase text-[#D4AF37]">1:1 Betreuung</span>
        <h3 class="text-2xl font-black text-slate-900">Einzeltraining</h3>
        <p class="text-slate-600 text-xs leading-relaxed">Dein Kind spielt in einem Fußballverein, möchte aber privat noch mehr trainieren? Bestimmte Disziplinen sollen gefördert werden? Ab 40,00€ / Einheit.</p>
        <a href="einzeltraining.html" class="inline-block px-6 py-3 rounded-full bg-[#E63946] text-white font-bold text-xs uppercase shadow-red-glow">Details ansehen →</a>
      </div>
      <div class="glass-card p-8 rounded-3xl space-y-4">
        <span class="text-xs font-black uppercase text-[#D4AF37]">Feste 5er-Gruppen</span>
        <h3 class="text-2xl font-black text-slate-900">Kleingruppentraining</h3>
        <p class="text-slate-600 text-xs leading-relaxed">In festen 5er-Gruppen trainieren wir gemeinsam, um individuelle Stärken auszubauen und Schwächen zu verbessern. 20€ - 25€ / Spieler.</p>
        <a href="kleingruppe.html" class="inline-block px-6 py-3 rounded-full bg-slate-900 text-white font-bold text-xs uppercase">Details ansehen →</a>
      </div>
      <div class="glass-card p-8 rounded-3xl space-y-4">
        <span class="text-xs font-black uppercase text-[#D4AF37]">Für Vereine &amp; Betriebe</span>
        <h3 class="text-2xl font-black text-slate-900">Mannschaftstraining</h3>
        <p class="text-slate-600 text-xs leading-relaxed">Deine Mannschaft möchte Taktik, Technik oder den Gruppenzusammenhalt stärken? Ab 90,00€ / Einheit zzgl. Anfahrt.</p>
        <a href="mannschaft.html" class="inline-block px-6 py-3 rounded-full bg-slate-900 text-white font-bold text-xs uppercase">Details ansehen →</a>
      </div>
    </div>''',
    active_nav="Training"
)

# 2. einzeltraining.html
make_page(
    "einzeltraining.html",
    "Einzeltraining (1:1) | SoccerProf Academy Hamburg",
    "Regelmäßiges Einzeltraining",
    "Ab 40,00€/Trainingseinheit · mind. 60 Minuten · Intensiv, Anspruchsvoll und sofort erkennbare Entwicklung.",
    '''<div class="max-w-4xl mx-auto glass-card p-8 sm:p-12 rounded-3xl space-y-6">
      <h2 class="text-2xl font-black text-slate-900">1:1 Einzeltraining in Hamburg</h2>
      <p class="text-slate-700 text-sm leading-relaxed">
        Dein Kind spielt in einem Fußballverein, möchte aber privat noch mehr trainieren? Bestimmte Disziplinen sollen gefördert werden? Dann bist du bei uns genau richtig! Unser individuelles Training richtet sich gänzlich nach euren Wünschen, um dich oder deine Kinder auf eurem persönlichen sportlichen Weg zu begleiten.
      </p>
      
      <div class="border-t border-b border-slate-200/80 py-6 space-y-3">
        <h3 class="text-lg font-black text-slate-900">Der 4-Phasen Aufbau des Trainings:</h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
          <div class="p-4 bg-slate-100 rounded-xl"><strong class="text-slate-900">1. Aufwärmung:</strong> Technik, Koordination &amp; Kognitives-Training</div>
          <div class="p-4 bg-slate-100 rounded-xl"><strong class="text-slate-900">2. Einleitung:</strong> z.B. Tricks Ausführungsübungen</div>
          <div class="p-4 bg-slate-100 rounded-xl"><strong class="text-slate-900">3. Hauptteil:</strong> Gelernte Tricks in Zweikämpfen anwenden bei steigender Intensität</div>
          <div class="p-4 bg-slate-100 rounded-xl"><strong class="text-slate-900">4. Feedback:</strong> Ausführliche Trainingsanalyse und Reflexion</div>
        </div>
      </div>

      <div class="pt-4 flex flex-col sm:flex-row items-center justify-between gap-4">
        <div>
          <div class="text-2xl font-black text-[#E63946]">Ab 40,00 € / Einheit</div>
          <div class="text-xs text-slate-500 font-bold">Pakete auf Anfrage</div>
        </div>
        <a href="mailto:sami@soccerprof.de?subject=Anfrage Einzeltraining" class="btn-fill-red px-8 py-4 rounded-full bg-[#E63946] text-white font-black text-xs uppercase tracking-wider shadow-red-glow">Jetzt Termin Vereinbaren</a>
      </div>
    </div>'''
)

# 3. kleingruppe.html
make_page(
    "kleingruppe.html",
    "Kleingruppentraining | SoccerProf Academy Hamburg",
    "Kleingruppentraining",
    "75 Minuten Gruppentraining: 2-4 Spieler = 25€/Spieler | 5-6 Spieler = 20€/Spieler.",
    '''<div class="max-w-4xl mx-auto glass-card p-8 sm:p-12 rounded-3xl space-y-6">
      <h2 class="text-2xl font-black text-slate-900">Training in festen 5er-Teams</h2>
      <p class="text-slate-700 text-sm leading-relaxed">
        In festen 5er-Gruppen trainieren wir gemeinsam, um individuelle Stärken auszubauen und Schwächen zu verbessern. Die Gruppe fördert Motivation und Teamgeist. So lernen dein Kind oder du wichtiges Handwerkszeug, das in jedem Fußballspiel genutzt werden kann.
      </p>
      <div class="pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 border-t border-slate-200">
        <div>
          <div class="text-2xl font-black text-[#D4AF37]">20,00 € - 25,00 € / Spieler</div>
          <div class="text-xs text-slate-500 font-bold">75 Minuten Intensivtraining</div>
        </div>
        <a href="mailto:sami@soccerprof.de?subject=Anfrage Kleingruppentraining" class="btn-fill-gold px-8 py-4 rounded-full bg-[#D4AF37] text-slate-950 font-black text-xs uppercase tracking-wider shadow-gold-glow">Kleingruppe Anfragen</a>
      </div>
    </div>'''
)

# 4. mannschaft.html
make_page(
    "mannschaft.html",
    "Mannschaftstraining | SoccerProf Academy Hamburg",
    "Mannschafts-Training",
    "Ab 90 EUR pro Trainingseinheit zzgl. Anfahrt ab 20 EUR · Für Vereine & Betriebe/Firmen.",
    '''<div class="max-w-4xl mx-auto glass-card p-8 sm:p-12 rounded-3xl space-y-6">
      <h2 class="text-2xl font-black text-slate-900">Professionelles Mannschaftstraining</h2>
      <p class="text-slate-700 text-sm leading-relaxed">
        Deine Mannschaft möchte Taktik, Technik oder den Gruppenzusammenhalt stärken? Wir stellen ein individuelles privates Fußballtraining zusammen, um mit viel Spaß und Begeisterung Potenziale zu verbessern. Auch für Betriebe/Firmen möglich!
      </p>
      <div class="pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 border-t border-slate-200">
        <div>
          <div class="text-2xl font-black text-slate-900">Ab 90,00 € / Einheit</div>
          <div class="text-xs text-slate-500 font-bold">zzgl. Anfahrt ab 20 EUR</div>
        </div>
        <a href="mailto:sami@soccerprof.de?subject=Anfrage Mannschaftstraining" class="btn-fill-red px-8 py-4 rounded-full bg-slate-900 text-white font-black text-xs uppercase tracking-wider">Mannschaftstraining anfragen</a>
      </div>
    </div>'''
)

# 5. trainingsmethoden.html
make_page(
    "trainingsmethoden.html",
    "Trainingsmethoden | SoccerProf Academy Hamburg",
    "Unsere Trainingsmethoden",
    "Technik | Taktik | Kognitivtraining | Mentaltraining",
    '''<div class="space-y-8">
      <div class="glass-card p-8 rounded-3xl space-y-4">
        <h2 class="text-2xl font-black text-slate-900">Immer mit dabei: Viel Herz und gesunder Menschenverstand</h2>
        <p class="text-slate-700 text-sm leading-relaxed">
          So stellen wir sicher, dass unsere Schützlinge ganz ungezwungen das Beste aus sich herausholen können. Als ideale Ergänzung zum Verein schaffen wir die Möglichkeit, dass Fußballtalente über sich hinauswachsen.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="glass-card p-6 rounded-2xl space-y-2">
          <h3 class="text-lg font-black text-slate-900">1. Aufwärmung</h3>
          <p class="text-xs text-slate-600">Technik, Koordination, Kognitives-Training.</p>
        </div>
        <div class="glass-card p-6 rounded-2xl space-y-2">
          <h3 class="text-lg font-black text-slate-900">2. Einleitung</h3>
          <p class="text-xs text-slate-600">z.B. Tricks Ausführungsübungen.</p>
        </div>
        <div class="glass-card p-6 rounded-2xl space-y-2">
          <h3 class="text-lg font-black text-slate-900">3. Hauptteil</h3>
          <p class="text-xs text-slate-600">Gelernte Tricks in Zweikämpfen anwenden bei steigender Intensität.</p>
        </div>
        <div class="glass-card p-6 rounded-2xl space-y-2">
          <h3 class="text-lg font-black text-slate-900">4. Feedback</h3>
          <p class="text-xs text-slate-600">Ausführliche Trainingsanalyse und Reflexion.</p>
        </div>
      </div>
    </div>''',
    active_nav="Trainingsmethoden"
)

# 6. preise.html
make_page(
    "preise.html",
    "Preise & Tarife | SoccerProf Academy Hamburg",
    "Preise & Konditionen",
    "Transparente Preise für echtes Profi-Training in Hamburg.",
    '''<div class="space-y-12">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <div class="glass-card p-8 rounded-3xl space-y-4">
          <span class="text-xs font-black uppercase text-slate-500">Einzeltraining</span>
          <h3 class="text-2xl font-black text-slate-900">1:1 Coaching</h3>
          <div class="text-3xl font-black text-[#E63946]">Ab 40,00 €</div>
          <p class="text-xs text-slate-600">mind. 60 Minuten. Intensiv, Anspruchsvoll und sofort erkennbare Entwicklung.</p>
          <a href="kontakt.html" class="btn-fill-red block w-full text-center py-3.5 rounded-full bg-[#E63946] text-white font-black text-xs uppercase">Anfragen</a>
        </div>

        <div class="glass-card p-8 rounded-3xl space-y-4 border-2 border-[#D4AF37]">
          <span class="text-xs font-black uppercase text-[#D4AF37]">Kleingruppe</span>
          <h3 class="text-2xl font-black text-slate-900">5er-Gruppe</h3>
          <div class="text-3xl font-black text-slate-900">20,00 € - 25,00 €</div>
          <p class="text-xs text-slate-600">75 Minuten Gruppentraining (2-4 Spieler = 25€, 5-6 Spieler = 20€ per Spieler).</p>
          <a href="kontakt.html" class="btn-fill-gold block w-full text-center py-3.5 rounded-full bg-[#D4AF37] text-slate-950 font-black text-xs uppercase">Anfragen</a>
        </div>

        <div class="glass-card p-8 rounded-3xl space-y-4">
          <span class="text-xs font-black uppercase text-slate-500">Mannschaft</span>
          <h3 class="text-2xl font-black text-slate-900">Vereinstraining</h3>
          <div class="text-3xl font-black text-slate-900">Ab 90,00 €</div>
          <p class="text-xs text-slate-600">Pro Einheiten zzgl. Anfahrt ab 20€. Auch für Firmen/Betriebe möglich.</p>
          <a href="kontakt.html" class="btn-fill-red block w-full text-center py-3.5 rounded-full bg-slate-900 text-white font-black text-xs uppercase">Anfragen</a>
        </div>

      </div>

      <div class="glass-card p-8 rounded-3xl space-y-4">
        <h3 class="text-xl font-black text-slate-900">Weitere Leistungen &amp; Zusatzangebote:</h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 text-xs font-bold text-slate-700 pt-2">
          <div class="p-4 bg-slate-100 rounded-xl"><i class="fa-solid fa-shirt text-[#D4AF37] mr-2"></i> Trikot: 45,00 EUR</div>
          <div class="p-4 bg-slate-100 rounded-xl"><i class="fa-solid fa-clipboard text-[#D4AF37] mr-2"></i> Trainingsplan: ab 20,00 EUR/mtl.</div>
          <div class="p-4 bg-slate-100 rounded-xl"><i class="fa-solid fa-apple-whole text-[#D4AF37] mr-2"></i> Ernährungsplan: ab 30,00 EUR/mtl.</div>
          <div class="p-4 bg-slate-100 rounded-xl"><i class="fa-solid fa-cake-candles text-[#D4AF37] mr-2"></i> Kindergeburtstag: auf Anfrage</div>
        </div>
      </div>
    </div>''',
    active_nav="Preise"
)

# 7. ueber-uns.html
make_page(
    "ueber-uns.html",
    "Über uns & Trainer Sami Ghaouar | SoccerProf Academy Hamburg",
    "Über SoccerProf Academy",
    "Erhaltener Text von soccerprof.de",
    '''<div class="max-w-4xl mx-auto space-y-8">
      <div class="glass-card p-8 sm:p-12 rounded-3xl space-y-6">
        <h2 class="text-2xl font-black text-slate-900">Der TRAINER: "Man lernt nie aus."</h2>
        <p class="text-slate-700 text-sm leading-relaxed">
          Immer wieder begegnet uns dieser Spruch im Alltag, im Berufsleben und auch im Fußball trifft er definitiv zu. Damit das Weiterlernen gut klappt und vor allem richtig Spaß macht, unterstützen wir erfahrene Trainer Kinder, Jugendlichen und Erwachsene – egal, ob Anfänger:innen oder Fortgeschrittene.
        </p>
        <div class="pt-4 border-t border-slate-200">
          <h3 class="text-xl font-black text-slate-900 mb-2">Head Coach Sami Ghaouar</h3>
          <ul class="text-xs text-slate-600 space-y-1.5 list-disc pl-5">
            <li>UEFA-B-Lizenz (2018) &amp; C-Lizenz (2014)</li>
            <li>Torwart-Trainer-Lizenz</li>
            <li>DFB-Fortbildung an der Sportschule Duisburg-Wedau</li>
            <li>Flügelspieler beim Hamburger SV (Regionalliga-Erfahrung)</li>
            <li>Seit 2012 Individual- und Nachwuchstrainer in Hamburg</li>
          </ul>
        </div>
      </div>

      <div class="glass-card p-8 rounded-3xl space-y-3 border-2 border-[#D4AF37]">
        <div class="text-[#D4AF37] text-lg">★★★★★</div>
        <p class="text-sm italic font-medium text-slate-800">
          "Danke lieber Sami! Uns hat’s auch gefreut und die Kids sind ganz begeistert von dir 🤩. Weil du so ein cooler Fußballer bist 😎. Und vor allem nett 😊"
        </p>
        <div class="text-xs font-bold text-slate-500">— Angelika (Mutter)</div>
      </div>
    </div>''',
    active_nav="Über uns"
)

# 8. veranstaltungen.html
make_page(
    "veranstaltungen.html",
    "Veranstaltungen & Camps | SoccerProf Academy Hamburg",
    "Veranstaltungen & Powercamps",
    "Wir veranstalten regelmäßig Fußballturniere, Events oder Camps für unsere SoccerProf-Spieler:innen.",
    '''<div class="max-w-4xl mx-auto glass-card p-8 rounded-3xl space-y-6">
      <h2 class="text-2xl font-black text-slate-900">Powercamp "Fußball pur"</h2>
      <p class="text-slate-600 text-sm leading-relaxed">
        2-3 Tage á 2x90 Minuten inkl. gesundes hochwertiges Essen. 1 Trainer = max. 7 Spieler. 80 EUR pro Tag zzgl. individuelles SoccerProf-Trikot 40 EUR. Kleine Gruppen mit hoher Intensität, Entwicklung und Spaß steht im Vordergrund!
      </p>
      <div class="pt-4 border-t border-slate-200">
        <h3 class="text-lg font-black text-slate-900">Kindergeburtstage &amp; Turniere</h3>
        <p class="text-xs text-slate-600 mt-1">Auch Kindergeburtstage könnt ihr bei uns feiern. Wir organisieren regelmäßige interne und externe Turniere (Jg. 2009 - 2018).</p>
      </div>
      <a href="kontakt.html" class="btn-fill-red inline-block px-8 py-4 rounded-full bg-[#E63946] text-white font-black text-xs uppercase shadow-red-glow">Camp-Termine anfragen →</a>
    </div>'''
)

# 9. jobs.html
make_page(
    "jobs.html",
    "Jobs & Karriere | SoccerProf Academy Hamburg",
    "Werde Teil von SoccerProf",
    "Du liebst Fußball und möchtest Spieler individuell entwickeln? Werde Trainer in Hamburg!",
    '''<div class="max-w-4xl mx-auto glass-card p-8 sm:p-12 rounded-3xl space-y-6">
      <h2 class="text-2xl font-black text-slate-900">Stellenausschreibung: Fußballtrainer (m/w/d)</h2>
      <div class="space-y-4 text-xs text-slate-700">
        <div>
          <h4 class="font-black text-sm text-slate-900">Deine Aufgaben:</h4>
          <p class="mt-1">Durchführung von Einzeltrainings und Kleingruppentrainings im Kinder- und Jugendbereich in Hamburg.</p>
        </div>
        <div>
          <h4 class="font-black text-sm text-slate-900">Das bringst du mit:</h4>
          <p class="mt-1">Trainerlizenz (C- oder B-Lizenz wünschenswert), hohe Begeisterung für den Fußball und Zuverlässigkeit.</p>
        </div>
        <div>
          <h4 class="font-black text-sm text-slate-900">Das bieten wir:</h4>
          <p class="mt-1">Faire Vergütung, professionelles Equipment und ein starkes Team in Hamburg.</p>
        </div>
      </div>
      <div class="pt-4">
        <a href="mailto:sami@soccerprof.de?subject=Bewerbung als Trainer bei SoccerProf" class="btn-fill-red inline-block px-8 py-4 rounded-full bg-[#E63946] text-white font-black text-xs uppercase tracking-wider shadow-red-glow">Jetzt bewerben</a>
      </div>
    </div>'''
)

# 10. faq.html
make_page(
    "faq.html",
    "Häufig gestellte Fragen (FAQ) | SoccerProf Academy Hamburg",
    "Häufig gestellte Fragen (FAQ)",
    "Alle wichtigen Fragen und Antworten im Überblick.",
    '''<div class="max-w-4xl mx-auto space-y-4">
      <details class="glass-card rounded-2xl p-5 cursor-pointer border border-slate-200">
        <summary class="flex items-center justify-between font-black text-slate-900 text-base select-none">
          <span>Für welches Alter ist das Training geeignet?</span>
          <i class="fa-solid fa-chevron-down text-sm text-[#D4AF37] faq-icon"></i>
        </summary>
        <div class="pt-4 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-200/60 mt-3">
          Wir trainieren Kinder, Jugendliche sowie Erwachsene – egal, ob Anfänger:innen oder Fortgeschrittene.
        </div>
      </details>
      <details class="glass-card rounded-2xl p-5 cursor-pointer border border-slate-200">
        <summary class="flex items-center justify-between font-black text-slate-900 text-base select-none">
          <span>Wo findet das Training in Hamburg statt?</span>
          <i class="fa-solid fa-chevron-down text-sm text-[#D4AF37] faq-icon"></i>
        </summary>
        <div class="pt-4 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-200/60 mt-3">
          Öjendorfer Weg 80, 22119 Hamburg (Billstedt) sowie in Reinbek und Eimsbüttel.
        </div>
      </details>
    </div>'''
)

# 11. kontakt.html
make_page(
    "kontakt.html",
    "Kontakt & Standorte | SoccerProf Academy Hamburg",
    "Kontakt & Standorte",
    "SoccerProf Academy · Öjendorfer Weg 80, 22119 Hamburg",
    '''<div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
      <div class="lg:col-span-6 glass-card p-8 rounded-3xl space-y-6">
        <h3 class="text-xl font-black text-slate-900">SoccerProf Academy | Sami Ghaouar</h3>
        <p class="text-xs text-slate-600">Öjendorfer Weg 80 · 22119 Hamburg</p>
        <div class="space-y-2 text-xs font-bold">
          <div><i class="fa-solid fa-phone text-[#E63946] mr-2"></i> +49 176 841 565 42</div>
          <div><i class="fa-solid fa-envelope text-[#D4AF37] mr-2"></i> sami@soccerprof.de</div>
        </div>
        <form onsubmit="handleFormSubmit(event)" class="space-y-4 pt-4 border-t border-slate-200">
          <div>
            <label class="block text-xs font-extrabold uppercase mb-1">Name *</label>
            <input type="text" required placeholder="Vor- und Nachname" class="w-full px-4 py-3 rounded-2xl bg-white border border-slate-200 text-xs">
          </div>
          <div>
            <label class="block text-xs font-extrabold uppercase mb-1">E-Mail *</label>
            <input type="email" required placeholder="deine-email@beispiel.de" class="w-full px-4 py-3 rounded-2xl bg-white border border-slate-200 text-xs">
          </div>
          <button type="submit" class="btn-fill-red w-full py-3.5 rounded-2xl bg-[#E63946] text-white font-black text-xs uppercase shadow-red-glow">Kostenloses Beratungsgespräch anfragen</button>
        </form>
      </div>
      <div class="lg:col-span-6 glass-card rounded-3xl overflow-hidden border-2 border-[#D4AF37]/60">
        <iframe title="SoccerProf Maps" width="100%" height="450" style="border:0;" loading="lazy" src="https://maps.google.com/maps?q=%C3%96jendorfer%20Weg%2080,%2022119%20Hamburg&t=&z=14&ie=UTF8&iwloc=&output=embed"></iframe>
      </div>
    </div>''',
    active_nav="Kontakt"
)

# 12. shop.html
make_page(
    "shop.html",
    "SoccerProf Shop | Trainingsekipment & Merchandise",
    "SoccerProf Shop",
    "Offizielles Equipment & Kleidung für SoccerProf-Spieler.",
    '''<div class="max-w-4xl mx-auto glass-card p-12 rounded-3xl text-center space-y-4">
      <i class="fa-solid fa-bag-shopping text-4xl text-[#D4AF37]"></i>
      <h2 class="text-2xl font-black text-slate-900">Demnächst verfügbar!</h2>
      <p class="text-slate-600 text-xs">Unser offizieller Shop mit SoccerProf Trikots (45,00€), Bällen und Equipment öffnet in Kürze.</p>
      <a href="index.html" class="inline-block px-6 py-3 rounded-full bg-slate-900 text-white font-bold text-xs uppercase">Zurück zur Startseite</a>
    </div>'''
)

# 13. impressum.html, datenschutz.html, cookie-richtlinie.html
make_page(
    "impressum.html",
    "Impressum | SoccerProf Academy Hamburg",
    "Impressum",
    "Rechtliche Angaben gemäß § 5 TMG.",
    '''<div class="max-w-3xl mx-auto glass-card p-8 rounded-3xl text-xs space-y-4 text-slate-700">
      <h3 class="font-black text-sm text-slate-900">Angaben gemäß § 5 TMG:</h3>
      <p>SoccerProf Academy<br>Inhaber: Sami Ghaouar<br>Öjendorfer Weg 80<br>22119 Hamburg<br>Deutschland</p>
      <h3 class="font-black text-sm text-slate-900">Kontakt:</h3>
      <p>Telefon: +49 176 841 565 42<br>E-Mail: sami@soccerprof.de</p>
    </div>'''
)

make_page(
    "datenschutz.html",
    "Datenschutzrichtlinie | SoccerProf Academy Hamburg",
    "Datenschutzrichtlinie",
    "Informationen zur Verarbeitung personenbezogener Daten.",
    '''<div class="max-w-3xl mx-auto glass-card p-8 rounded-3xl text-xs space-y-4 text-slate-700">
      <h3 class="font-black text-sm text-slate-900">Datenschutz auf einen Blick</h3>
      <p>Wir nehmen den Schutz Deiner persönlichen Daten sehr ernst und halten uns an die gesetzlichen Datenschutzvorschriften (DSGVO).</p>
    </div>'''
)

make_page(
    "cookie-richtlinie.html",
    "Cookie-Richtlinie | SoccerProf Academy Hamburg",
    "Cookie-Richtlinie",
    "Informationen zur Verwendung von Cookies.",
    '''<div class="max-w-3xl mx-auto glass-card p-8 rounded-3xl text-xs space-y-4 text-slate-700">
      <p>Unsere Website nutzt ausschließlich technisch notwendige Session-Cookies, um die Sicherheit und Funktionsfähigkeit zu gewährleisten.</p>
    </div>'''
)

print("All subpages generated successfully!")
