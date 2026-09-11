import os

workspace_dir = r"c:\Users\mario\Desktop\newsoccerprof"

from build_clean_soccerprof import get_head, get_header, get_footer, get_scripts

def make_page(filename, title, heading, subtitle, content_html, active_nav=""):
    full_html = f'''{get_head(title=title)}
<body class="bg-mesh relative grid-pattern antialiased text-slate-900 pb-20 sm:pb-0">

  {get_header(active_page=active_nav)}

  <!-- HERO HEADER FOR SUBPAGE -->
  <section class="pt-32 pb-16 bg-slate-900 text-white relative z-10 border-b border-slate-800">
    <div class="logo-particle-bg"></div>
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
    "Individuelles Fußballtraining für Kinder, Jugendliche und Erwachsene in Hamburg – die perfekte Ergänzung zum Vereinstraining.",
    '''<div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="glass-card p-8 rounded-3xl space-y-4">
        <h3 class="text-2xl font-black text-slate-900">Einzeltraining (1:1)</h3>
        <p class="text-slate-600 text-xs leading-relaxed">100% persönliche Aufmerksamkeit für maximale Weiterentwicklung in Technik, Taktik & Kognition.</p>
        <a href="einzeltraining.html" class="inline-block px-6 py-3 rounded-full bg-[#E63946] text-white font-bold text-xs uppercase shadow-red-glow">Details ansehen →</a>
      </div>
      <div class="glass-card p-8 rounded-3xl space-y-4">
        <h3 class="text-2xl font-black text-slate-900">Kleingruppentraining</h3>
        <p class="text-slate-600 text-xs leading-relaxed">Feste 5er-Gruppen für hohe Intensität, Teamgeist und spielnahe Zweikämpfe.</p>
        <a href="kleingruppe.html" class="inline-block px-6 py-3 rounded-full bg-slate-900 text-white font-bold text-xs uppercase">Details ansehen →</a>
      </div>
      <div class="glass-card p-8 rounded-3xl space-y-4">
        <h3 class="text-2xl font-black text-slate-900">Mannschaftstraining</h3>
        <p class="text-slate-600 text-xs leading-relaxed">Professionelle Taktik- und Technikschulung für Vereine direkt auf eurem Platz.</p>
        <a href="mannschaft.html" class="inline-block px-6 py-3 rounded-full bg-slate-900 text-white font-bold text-xs uppercase">Details ansehen →</a>
      </div>
    </div>''',
    active_nav="Training"
)

# 2. einzeltraining.html
make_page(
    "einzeltraining.html",
    "Einzeltraining (1:1) | SoccerProf Academy Hamburg",
    "1:1 Einzeltraining",
    "Maximale individuelle Betreuung mit Head Coach Sami Ghaouar (UEFA-B-Lizenz).",
    '''<div class="max-w-4xl mx-auto glass-card p-8 sm:p-12 rounded-3xl space-y-6">
      <h2 class="text-2xl font-black text-slate-900">Informationen zum Einzeltraining</h2>
      <p class="text-slate-700 text-sm leading-relaxed">
        Unser 1:1 Einzeltraining richtet sich an ambitionierte Kinder, Jugendliche und Erwachsene, die ihre Stärken gezielt ausbauen und Schwächen nachhaltig korrigieren möchten.
      </p>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs font-bold text-slate-800 pt-4">
        <div class="p-3 bg-slate-100 rounded-xl"><i class="fa-solid fa-check text-[#D4AF37] mr-2"></i> Technik &amp; Ballführung</div>
        <div class="p-3 bg-slate-100 rounded-xl"><i class="fa-solid fa-check text-[#D4AF37] mr-2"></i> Passgenauigkeit &amp; Taktik</div>
        <div class="p-3 bg-slate-100 rounded-xl"><i class="fa-solid fa-check text-[#D4AF37] mr-2"></i> Kognition &amp; Vororientierung</div>
        <div class="p-3 bg-slate-100 rounded-xl"><i class="fa-solid fa-check text-[#D4AF37] mr-2"></i> Individuelles Video-Feedback</div>
      </div>
      <div class="pt-6">
        <a href="kontakt.html" class="px-8 py-4 rounded-full bg-[#E63946] text-white font-black text-xs uppercase tracking-wider shadow-red-glow">Jetzt Einzeltraining anfragen</a>
      </div>
    </div>'''
)

# 3. kleingruppe.html
make_page(
    "kleingruppe.html",
    "Kleingruppentraining | SoccerProf Academy Hamburg",
    "Kleingruppentraining (5er-Gruppen)",
    "Gemeinsam trainieren, individuell gefördert werden.",
    '''<div class="max-w-4xl mx-auto glass-card p-8 sm:p-12 rounded-3xl space-y-6">
      <h2 class="text-2xl font-black text-slate-900">Training in festen 5er-Teams</h2>
      <p class="text-slate-700 text-sm leading-relaxed">
        In festen 5er-Gruppen verbinden wir die Vorteile von 1:1-Coaching mit echter Spielpraxis, Zweikämpfen und Teamgeist.
      </p>
      <div class="pt-6">
        <a href="kontakt.html" class="px-8 py-4 rounded-full bg-[#E63946] text-white font-black text-xs uppercase tracking-wider shadow-red-glow">Kleingruppe anfragen</a>
      </div>
    </div>'''
)

# 4. mannschaft.html
make_page(
    "mannschaft.html",
    "Mannschaftstraining | SoccerProf Academy Hamburg",
    "Mannschaftstraining für Vereine",
    "Gezielte Förderung von Vereinsmannschaften vor Ort.",
    '''<div class="max-w-4xl mx-auto glass-card p-8 sm:p-12 rounded-3xl space-y-6">
      <h2 class="text-2xl font-black text-slate-900">Vereinsförderung</h2>
      <p class="text-slate-700 text-sm leading-relaxed">
        Wir kommen direkt zu eurem Verein und führen spezifische Einheiten für Technik, Taktik und Gruppendynamik durch.
      </p>
      <div class="pt-6">
        <a href="kontakt.html" class="px-8 py-4 rounded-full bg-slate-900 text-white font-black text-xs uppercase tracking-wider">Mannschaftstraining anfragen</a>
      </div>
    </div>'''
)

# 5. trainingsmethoden.html
make_page(
    "trainingsmethoden.html",
    "Trainingsmethoden | SoccerProf Academy Hamburg",
    "Unsere Trainingsmethoden",
    "8 Säulen für eine ganzheitliche fußballerische Entwicklung.",
    '''<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div class="glass-card p-6 rounded-2xl space-y-2">
        <h3 class="text-lg font-black text-slate-900">1. Technik</h3>
        <p class="text-xs text-slate-600">Feinschliff an Ballannahme, Ballführung, Passpräzision und Beidfüßigkeit.</p>
      </div>
      <div class="glass-card p-6 rounded-2xl space-y-2">
        <h3 class="text-lg font-black text-slate-900">2. Kognition</h3>
        <p class="text-xs text-slate-600">Schnelle Entscheidungsfindung unter Zeitdruck und Erhöhung des Handlungstempos.</p>
      </div>
      <div class="glass-card p-6 rounded-2xl space-y-2">
        <h3 class="text-lg font-black text-slate-900">3. Koordination</h3>
        <p class="text-xs text-slate-600">Laufkoordination, Beweglichkeit und optimale Körperbeherrschung.</p>
      </div>
      <div class="glass-card p-6 rounded-2xl space-y-2">
        <h3 class="text-lg font-black text-slate-900">4. Kraft &amp; Ausdauer</h3>
        <p class="text-xs text-slate-600">Fußballspezifische Fitness und Athletik für spürbare Ausdauer.</p>
      </div>
    </div>''',
    active_nav="Trainingsmethoden"
)

# 6. preise.html
make_page(
    "preise.html",
    "Preise & Tarife | SoccerProf Academy Hamburg",
    "Preise & Konditionen",
    "Transparente Preisgestaltung für erstklassiges Fußballtraining in Hamburg.",
    '''<div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="glass-card p-8 rounded-3xl space-y-4">
        <h3 class="text-2xl font-black text-slate-900">Erstberatung</h3>
        <div class="text-3xl font-black text-[#E63946]">Kostenlos</div>
        <p class="text-xs text-slate-600">100% unverbindliches Beratungsgespräch mit Trainer Sami.</p>
        <a href="kontakt.html" class="block w-full text-center py-3 rounded-2xl bg-slate-900 text-white font-bold text-xs uppercase">Anfragen</a>
      </div>
      <div class="glass-card p-8 rounded-3xl space-y-4 border-2 border-[#E63946]">
        <h3 class="text-2xl font-black text-slate-900">Kleingruppe</h3>
        <div class="text-2xl font-black text-slate-900">Auf Anfrage</div>
        <p class="text-xs text-slate-600">Training in festen 5er-Gruppen.</p>
        <a href="kontakt.html" class="block w-full text-center py-3 rounded-2xl bg-[#E63946] text-white font-bold text-xs uppercase shadow-red-glow">Anfragen</a>
      </div>
      <div class="glass-card p-8 rounded-3xl space-y-4 border-2 border-[#D4AF37]">
        <h3 class="text-2xl font-black text-slate-900">Einzeltraining</h3>
        <div class="text-2xl font-black text-slate-900">Auf Anfrage</div>
        <p class="text-xs text-slate-600">Flexibel über 5er- und 10er-Karten.</p>
        <a href="kontakt.html" class="block w-full text-center py-3 rounded-2xl bg-slate-900 text-white font-bold text-xs uppercase">Anfragen</a>
      </div>
    </div>''',
    active_nav="Preise"
)

# 7. ueber-uns.html
make_page(
    "ueber-uns.html",
    "Über uns & Trainer Sami Ghaouar | SoccerProf Academy Hamburg",
    "Über SoccerProf Academy",
    "Erfahrenes Trainerteam für individuelle Talentförderung in Hamburg.",
    '''<div class="max-w-4xl mx-auto glass-card p-8 sm:p-12 rounded-3xl space-y-6">
      <h2 class="text-2xl font-black text-slate-900">Philosophie & Team</h2>
      <p class="text-slate-700 text-sm leading-relaxed">
        Unser Trainerteam besteht aus 2 Trainern. Wir haben uns darauf spezialisiert, jede:n Spieler:in individuell zu beraten und weiterzuentwickeln.
      </p>
      <div class="pt-4 border-t border-slate-200">
        <h3 class="text-xl font-black text-slate-900 mb-2">Head Coach Sami Ghaouar</h3>
        <ul class="text-xs text-slate-600 space-y-1 list-disc pl-5">
          <li>UEFA-B-Lizenz (2018) &amp; C-Lizenz (2014)</li>
          <li>Torwart-Trainer-Lizenz</li>
          <li>DFB-Fortbildung an der Sportschule Duisburg-Wedau</li>
          <li>Flügelspieler beim Hamburger SV (Regionalliga-Erfahrung)</li>
          <li>Seit 2012 Individual- und Nachwuchstrainer</li>
        </ul>
      </div>
    </div>''',
    active_nav="Über uns"
)

# 8. veranstaltungen.html
make_page(
    "veranstaltungen.html",
    "Veranstaltungen & Camps | SoccerProf Academy Hamburg",
    "Veranstaltungen, Camps & Events",
    "Feriencamps, Turniere und sportliche Kindergeburtstage.",
    '''<div class="max-w-4xl mx-auto glass-card p-8 rounded-3xl space-y-4">
      <h2 class="text-2xl font-black text-slate-900">SoccerProf Feriencamps</h2>
      <p class="text-slate-600 text-sm">
        Unsere beliebten Feriencamps bieten intensivstes Training kombiniert mit purem Fußballspaß.
      </p>
      <a href="kontakt.html" class="inline-block px-6 py-3 rounded-full bg-[#E63946] text-white font-bold text-xs uppercase">Camp-Termine anfragen →</a>
    </div>'''
)

# 9. jobs.html (Punkt 20)
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
        <a href="mailto:sami@soccerprof.de?subject=Bewerbung als Trainer bei SoccerProf" class="px-8 py-4 rounded-full bg-[#E63946] text-white font-black text-xs uppercase tracking-wider shadow-red-glow">Jetzt bewerben</a>
      </div>
    </div>'''
)

# 10. faq.html (Punkt 21)
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
          Von Bambini bis zur A-Jugend sowie ambitionierten Erwachsenen.
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

# 11. kontakt.html (Punkt 22)
make_page(
    "kontakt.html",
    "Kontakt & Standorte | SoccerProf Academy Hamburg",
    "Kontakt & Standorte",
    "Bist du an einem Training interessiert? Schreib uns oder ruf uns direkt an.",
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
          <button type="submit" class="w-full py-3.5 rounded-2xl bg-[#E63946] text-white font-black text-xs uppercase shadow-red-glow">Kostenloses Erstgespräch anfragen</button>
        </form>
      </div>
      <div class="lg:col-span-6 glass-card rounded-3xl overflow-hidden border-2 border-[#D4AF37]/60">
        <iframe title="SoccerProf Maps" width="100%" height="450" style="border:0;" loading="lazy" src="https://maps.google.com/maps?q=%C3%96jendorfer%20Weg%2080,%2022119%20Hamburg&t=&z=14&ie=UTF8&iwloc=&output=embed"></iframe>
      </div>
    </div>''',
    active_nav="Kontakt"
)

# 12. shop.html (Punkt 23)
make_page(
    "shop.html",
    "SoccerProf Shop | Trainingsekipment & Merchandise",
    "SoccerProf Shop",
    "Offizielles Equipment & Kleidung für SoccerProf-Spieler.",
    '''<div class="max-w-4xl mx-auto glass-card p-12 rounded-3xl text-center space-y-4">
      <i class="fa-solid fa-bag-shopping text-4xl text-[#D4AF37]"></i>
      <h2 class="text-2xl font-black text-slate-900">Demnächst verfügbar!</h2>
      <p class="text-slate-600 text-xs">Unser offizieller Shop mit SoccerProf Trikots, Bällen und Equipment öffnet in Kürze.</p>
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
