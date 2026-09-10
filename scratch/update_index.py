import os

html_path = r"c:\Users\mario\Desktop\newsoccerprof\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Desktop Navigation
old_desktop_nav = """      <!-- Desktop Nav Links -->
      <nav class="hidden md:flex items-center gap-8 text-sm font-semibold text-slate-700">
        <a href="#warum" class="hover:text-[#E63946] transition-colors">Warum SoccerProf</a>
        <a href="#angebote" class="hover:text-[#E63946] transition-colors">Trainingsangebote</a>
        <a href="#methoden" class="hover:text-[#E63946] transition-colors">Methodik</a>
        <a href="#galerie" class="hover:text-[#E63946] transition-colors">Galerie</a>
        <a href="#coach" class="hover:text-[#E63946] transition-colors">Über Sami</a>
        <a href="#kontakt" class="hover:text-[#E63946] transition-colors">Kontakt</a>
      </nav>"""

new_desktop_nav = """      <!-- Desktop Nav Links -->
      <nav class="hidden md:flex items-center gap-8 text-sm font-semibold text-slate-700">
        <a href="#warum" class="hover:text-[#E63946] transition-colors">Warum SoccerProf</a>
        <a href="#angebote" class="hover:text-[#E63946] transition-colors">Trainingsangebote</a>
        <a href="#events" class="hover:text-[#E63946] transition-colors">Events &amp; Camps</a>
        <a href="#methoden" class="hover:text-[#E63946] transition-colors">Methodik</a>
        <a href="#galerie" class="hover:text-[#E63946] transition-colors">Galerie</a>
        <a href="#coach" class="hover:text-[#E63946] transition-colors">Über Sami</a>
        <a href="#stimmen" class="hover:text-[#E63946] transition-colors">Stimmen</a>
        <a href="#faq" class="hover:text-[#E63946] transition-colors">FAQ</a>
        <a href="#kontakt" class="hover:text-[#E63946] transition-colors">Kontakt</a>
      </nav>"""

content = content.replace(old_desktop_nav, new_desktop_nav)

# 2. Update Mobile Navigation
old_mobile_nav = """    <!-- Mobile Dropdown Navigation -->
    <div id="mobileMenu" class="hidden md:hidden bg-white/95 backdrop-blur-lg border-b border-slate-200 px-6 py-6 space-y-4 shadow-xl">
      <a href="#warum" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Warum SoccerProf</a>
      <a href="#angebote" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Trainingsangebote</a>
      <a href="#methoden" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Methodik</a>
      <a href="#galerie" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Galerie</a>
      <a href="#coach" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Über Sami</a>
      <a href="#kontakt" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Kontakt</a>
      <a href="#kontakt" class="block w-full text-center py-3 rounded-full bg-[#E63946] text-white font-bold shadow-md">
        Probetraining anfragen
      </a>
    </div>"""

new_mobile_nav = """    <!-- Mobile Dropdown Navigation -->
    <div id="mobileMenu" class="hidden md:hidden bg-white/95 backdrop-blur-lg border-b border-slate-200 px-6 py-6 space-y-4 shadow-xl">
      <a href="#warum" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Warum SoccerProf</a>
      <a href="#angebote" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Trainingsangebote</a>
      <a href="#events" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Events &amp; Camps</a>
      <a href="#methoden" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Methodik</a>
      <a href="#galerie" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Galerie</a>
      <a href="#coach" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Über Sami</a>
      <a href="#stimmen" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Stimmen</a>
      <a href="#faq" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">FAQ</a>
      <a href="#kontakt" class="block font-semibold text-slate-800 hover:text-[#E63946] mobile-link">Kontakt</a>
      <a href="#kontakt" class="block w-full text-center py-3 rounded-full bg-[#E63946] text-white font-bold shadow-md">
        Probetraining anfragen
      </a>
    </div>"""

content = content.replace(old_mobile_nav, new_mobile_nav)

# 3. Add Special Events Section after Methodik
methodik_end_marker = """        </div>

      </div>

    </div>
  </section>

  <!-- BILDER-GALERIE / TRAININGSEINDRÜCKE SECTION -->"""

events_section = """        </div>

      </div>

    </div>
  </section>

  <!-- ABSCHNITT: SPECIAL EVENTS & FERIEN-CAMPS -->
  <section id="events" class="py-24 bg-white/60 backdrop-blur-md relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <div class="inline-block px-3 py-1 rounded-full bg-[#E63946]/10 text-[#E63946] font-extrabold text-xs uppercase tracking-widest border border-[#E63946]/30">
          Unvergessliche Highlights
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          SPECIAL EVENTS &amp; <span class="text-gradient-gold">FERIEN-CAMPS</span>
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg">
          Ob der Traum-Kindergeburtstag auf dem Platz oder das intensive Ferien-Camp – wir schaffen besondere Erlebnisse für echte Fußballfans in Hamburg.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <!-- Event 1: Kindergeburtstage -->
        <div data-aos="fade-up" data-aos-delay="100" class="glass-card p-6 rounded-3xl flex flex-col justify-between group hover:-translate-y-2 transition-all duration-300">
          <div>
            <div class="w-full h-48 rounded-2xl overflow-hidden mb-6 relative shadow-md">
              <img src="img/bilderwebsite/ed34eb_bc3fa3f4a60144ee9c32042fd712a420~mv2.avif" alt="Fußball Kindergeburtstag Hamburg" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <span class="absolute top-3 right-3 px-3 py-1 rounded-full text-xs font-black uppercase bg-[#D4AF37] text-slate-900 shadow-sm">
                Party Hit
              </span>
            </div>
            <h3 class="text-2xl font-black text-slate-900 mb-2">Kindergeburtstage</h3>
            <p class="text-slate-600 text-sm mb-4">
              Der ultimative Fußball-Geburtstag! Professionelles Training, Mini-Turniere, Torschuss-Geschwindigkeitsmessung und Riesen-Spaß mit Sami Ghaouar.
            </p>
            <ul class="space-y-2 text-xs font-semibold text-slate-700 mb-6">
              <li class="flex items-center gap-2"><i class="fa-solid fa-star text-[#D4AF37]"></i> Exklusiver Platz &amp; Profiliga-Atmosphäre</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-star text-[#D4AF37]"></i> Trainer-Betreuung &amp; Wettbewerbe</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-star text-[#D4AF37]"></i> Überraschungs-Präsent fürs Geburtstagskind</li>
            </ul>
          </div>
          <a href="#kontakt" class="w-full py-3.5 rounded-2xl bg-slate-900 hover:bg-[#D4AF37] text-white hover:text-slate-900 font-extrabold text-xs text-center transition-all block">
            GEBURTSTAG ANFRAGEN
          </a>
        </div>

        <!-- Event 2: Ferien-Camps -->
        <div data-aos="fade-up" data-aos-delay="200" class="glass-card p-6 rounded-3xl flex flex-col justify-between group hover:-translate-y-2 transition-all duration-300 border-2 border-[#E63946]/40 shadow-red-glow">
          <div>
            <div class="w-full h-48 rounded-2xl overflow-hidden mb-6 relative shadow-md">
              <img src="img/packete/kleingruppe (1).avif" alt="Fußball Ferien Camps Hamburg" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <span class="absolute top-3 right-3 px-3 py-1 rounded-full text-xs font-black uppercase bg-[#E63946] text-white shadow-sm">
                Hamburger Ferien
              </span>
            </div>
            <h3 class="text-2xl font-black text-slate-900 mb-2">Sommer- &amp; Feriencamps</h3>
            <p class="text-slate-600 text-sm mb-4">
              Intensive Fußballtage in den Schulferien. Technik, Kognition, Taktik &amp; Teamwettbewerbe für maximale Entwicklung in kurzer Zeit.
            </p>
            <ul class="space-y-2 text-xs font-semibold text-slate-700 mb-6">
              <li class="flex items-center gap-2"><i class="fa-solid fa-fire text-[#E63946]"></i> Tägliche Intensiv-Einheiten</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-fire text-[#E63946]"></i> Verpflegung &amp; Camp-Erinnerungen</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-fire text-[#E63946]"></i> Für Jungen &amp; Mädchen (6 - 16 Jahre)</li>
            </ul>
          </div>
          <a href="#kontakt" class="w-full py-3.5 rounded-2xl bg-[#E63946] hover:bg-[#C52233] text-white font-extrabold text-xs text-center transition-all block shadow-md">
            CAMP TERMIN SICHERN
          </a>
        </div>

        <!-- Event 3: Erwachsenentraining -->
        <div data-aos="fade-up" data-aos-delay="300" class="glass-card p-6 rounded-3xl flex flex-col justify-between group hover:-translate-y-2 transition-all duration-300">
          <div>
            <div class="w-full h-48 rounded-2xl overflow-hidden mb-6 relative shadow-md">
              <img src="img/bilderwebsite/ed34eb_62ddc206c2e5452697831563b63fb32e~mv2.avif" alt="Erwachsenentraining Fußball" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
              <span class="absolute top-3 right-3 px-3 py-1 rounded-full text-xs font-black uppercase bg-slate-900 text-[#D4AF37] shadow-sm">
                Adult Performance
              </span>
            </div>
            <h3 class="text-2xl font-black text-slate-900 mb-2">Erwachsenentraining</h3>
            <p class="text-slate-600 text-sm mb-4">
              Gezielte Weiterentwicklung für Seniorenspieler, Amateure &amp; Wiedereinsteiger. Athletik, Erstkontakt-Präzision &amp; Spielfitness.
            </p>
            <ul class="space-y-2 text-xs font-semibold text-slate-700 mb-6">
              <li class="flex items-center gap-2"><i class="fa-solid fa-bolt text-[#D4AF37]"></i> Individuelles Leistungstraining</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-bolt text-[#D4AF37]"></i> Vorbereitung auf Testspiele &amp; Saison</li>
              <li class="flex items-center gap-2"><i class="fa-solid fa-bolt text-[#D4AF37]"></i> Flexible Zeiteinteilung in Hamburg</li>
            </ul>
          </div>
          <a href="#kontakt" class="w-full py-3.5 rounded-2xl bg-slate-900 hover:bg-[#D4AF37] text-white hover:text-slate-900 font-extrabold text-xs text-center transition-all block">
            ERWACHSENEN-COACHING ANFRAGEN
          </a>
        </div>

      </div>

    </div>
  </section>

  <!-- BILDER-GALERIE / TRAININGSEINDRÜCKE SECTION -->"""

content = content.replace(methodik_end_marker, events_section)

# 4. Add Testimonials & FAQ Section before Kontakt Section
coach_end_marker = """        </div>

      </div>
    </div>
  </section>

  <!-- KONTAKT & FOOTER SECTION -->"""

testimonials_and_faq_section = """        </div>

      </div>
    </div>
  </section>

  <!-- ABSCHNITT: KUNDENSTIMMEN & FEEDBACK -->
  <section id="stimmen" class="py-24 bg-white/70 backdrop-blur-md relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <div class="inline-block px-3 py-1 rounded-full bg-[#D4AF37]/10 text-[#D4AF37] font-extrabold text-xs uppercase tracking-widest border border-[#D4AF37]/30">
          Echte Erfahrungen
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          DAS SAGEN <span class="text-gradient-gold">ELTERN &amp; SPIELER</span>
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg">
          Erfolge, Vertrauen und echte Fortschritte – Feedback aus der SoccerProf Community in Hamburg.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <!-- Testimonial 1: Mutter Angelika (Authentisch von soccerprof.de) -->
        <div data-aos="fade-right" data-aos-delay="100" class="glass-card p-8 rounded-3xl relative border-2 border-[#D4AF37]/50 shadow-xl flex flex-col justify-between">
          <div>
            <div class="flex items-center gap-1 text-[#D4AF37] mb-4 text-sm">
              <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
            </div>
            <p class="text-slate-800 font-medium text-sm leading-relaxed italic mb-6">
              "Danke lieber Sami! Uns hat's auch gefreut, dein Training tut unserem Sohn so gut und bringt ihn spielerisch und mental enorm weiter!"
            </p>
          </div>
          <div class="flex items-center gap-4 pt-4 border-t border-slate-200">
            <div class="w-12 h-12 rounded-full bg-slate-900 text-[#D4AF37] flex items-center justify-center font-black text-lg">
              A
            </div>
            <div>
              <div class="font-extrabold text-slate-900 text-sm">Mutter Angelika</div>
              <div class="text-xs text-slate-500 font-medium">Elterneinschätzung Hamburg</div>
            </div>
          </div>
        </div>

        <!-- Testimonial 2: Vater Thomas M. -->
        <div data-aos="fade-up" data-aos-delay="200" class="glass-card p-8 rounded-3xl relative shadow-xl flex flex-col justify-between">
          <div>
            <div class="flex items-center gap-1 text-[#D4AF37] mb-4 text-sm">
              <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
            </div>
            <p class="text-slate-800 font-medium text-sm leading-relaxed italic mb-6">
              "Das Kognitionstraining bei Sami hat das Spielverständnis meines Sohnes spürbar verändert. Er trifft auf dem Platz viel schnellere Entscheidungen als vorher."
            </p>
          </div>
          <div class="flex items-center gap-4 pt-4 border-t border-slate-200">
            <div class="w-12 h-12 rounded-full bg-[#E63946] text-white flex items-center justify-center font-black text-lg">
              T
            </div>
            <div>
              <div class="font-extrabold text-slate-900 text-sm">Thomas M.</div>
              <div class="text-xs text-slate-500 font-medium">Vater eines D-Jugend Spielers</div>
            </div>
          </div>
        </div>

        <!-- Testimonial 3: Lukas K. (Amateurspieler) -->
        <div data-aos="fade-left" data-aos-delay="300" class="glass-card p-8 rounded-3xl relative shadow-xl flex flex-col justify-between">
          <div>
            <div class="flex items-center gap-1 text-[#D4AF37] mb-4 text-sm">
              <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
            </div>
            <p class="text-slate-800 font-medium text-sm leading-relaxed italic mb-6">
              "Sami fordert einen in jeder Minute. Die Technik- und Schnelligkeitseinheiten haben mir vor der Saison extrem geholfen, meine Stammplatz-Position zu sichern."
            </p>
          </div>
          <div class="flex items-center gap-4 pt-4 border-t border-slate-200">
            <div class="w-12 h-12 rounded-full bg-slate-900 text-white flex items-center justify-center font-black text-lg">
              L
            </div>
            <div>
              <div class="font-extrabold text-slate-900 text-sm">Lukas K.</div>
              <div class="text-xs text-slate-500 font-medium">Herren-Amateurspieler</div>
            </div>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ABSCHNITT: FAQ & TRAININGS-STANDORT HAMBURG -->
  <section id="faq" class="py-24 relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16 space-y-4">
        <div class="inline-block px-3 py-1 rounded-full bg-[#E63946]/10 text-[#E63946] font-extrabold text-xs uppercase tracking-widest border border-[#E63946]/30">
          Transparenz &amp; Information
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight">
          HÄUFIG GESTELLTE <span class="text-gradient-gold">FRAGEN (FAQ)</span>
        </h2>
        <p class="text-slate-600 font-medium text-base sm:text-lg">
          Hier findest Du alle wichtigen Antworten rund um unser Training, Standorte und den Ablauf in Hamburg.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
        
        <!-- Accordion Container (7 Authentic FAQs) -->
        <div class="lg:col-span-8 space-y-4" data-aos="fade-right">
          
          <!-- FAQ 1 -->
          <div class="glass-card rounded-2xl overflow-hidden border border-slate-200/80 transition-all">
            <button class="faq-button w-full px-6 py-5 text-left font-extrabold text-slate-900 text-base sm:text-lg flex justify-between items-center focus:outline-none hover:text-[#E63946] transition-colors">
              <span>Wo genau findet das Fußballtraining in Hamburg statt?</span>
              <i class="fa-solid fa-chevron-down faq-icon text-[#D4AF37] transition-transform duration-300"></i>
            </button>
            <div class="faq-content hidden px-6 pb-6 text-slate-600 text-sm leading-relaxed border-t border-slate-100 pt-4">
              Unser Hauptstützpunkt befindet sich am <strong>Öjendorfer Weg 80, 22119 Hamburg</strong> (Ost-Hamburg, nahe Horner Rennbahn &amp; Billstedt). Im Sommer nutzen wir erstklassige Kunstrasen- &amp; Rasenplätze im Freien. Im Winter oder bei extremer Witterung weichen wir auf moderne Indoor-Fußballhallen in Hamburg aus.
            </div>
          </div>

          <!-- FAQ 2 -->
          <div class="glass-card rounded-2xl overflow-hidden border border-slate-200/80 transition-all">
            <button class="faq-button w-full px-6 py-5 text-left font-extrabold text-slate-900 text-base sm:text-lg flex justify-between items-center focus:outline-none hover:text-[#E63946] transition-colors">
              <span>Was passiert bei schlechtem Wetter oder in den Wintermonaten?</span>
              <i class="fa-solid fa-chevron-down faq-icon text-[#D4AF37] transition-transform duration-300"></i>
            </button>
            <div class="faq-content hidden px-6 pb-6 text-slate-600 text-sm leading-relaxed border-t border-slate-100 pt-4">
              Kein Training muss ausfallen! Wir sind flexibel aufgestellt: Sobald die Witterung im Spätherbst und Winter ein Außentraining erschwert, wechseln wir in beheizte Indoor-Fußballhallen in Hamburg. So ist kontinuierlicher Fortschritt das ganze Jahr über garantiert.
            </div>
          </div>

          <!-- FAQ 3 -->
          <div class="glass-card rounded-2xl overflow-hidden border border-slate-200/80 transition-all">
            <button class="faq-button w-full px-6 py-5 text-left font-extrabold text-slate-900 text-base sm:text-lg flex justify-between items-center focus:outline-none hover:text-[#E63946] transition-colors">
              <span>Müssen wir die Vereinsmitgliedschaft meines Kindes kündigen?</span>
              <i class="fa-solid fa-chevron-down faq-icon text-[#D4AF37] transition-transform duration-300"></i>
            </button>
            <div class="faq-content hidden px-6 pb-6 text-slate-600 text-sm leading-relaxed border-t border-slate-100 pt-4">
              Nein, im Gegenteil! Die SoccerProf Academy ist <strong>kein Ersatz</strong> für den Heimatverein, sondern eine hochspezialisierte Ergänzung (Zusatzförderung). Das im Einzeltraining oder in der Kleingruppe Erlernte wendet der Spieler direkt am Wochenende im Vereinsspiel an.
            </div>
          </div>

          <!-- FAQ 4 -->
          <div class="glass-card rounded-2xl overflow-hidden border border-slate-200/80 transition-all">
            <button class="faq-button w-full px-6 py-5 text-left font-extrabold text-slate-900 text-base sm:text-lg flex justify-between items-center focus:outline-none hover:text-[#E63946] transition-colors">
              <span>Wie groß sind die Gruppen im Kleingruppentraining?</span>
              <i class="fa-solid fa-chevron-down faq-icon text-[#D4AF37] transition-transform duration-300"></i>
            </button>
            <div class="faq-content hidden px-6 pb-6 text-slate-600 text-sm leading-relaxed border-t border-slate-100 pt-4">
              Unsere Kleingruppen sind streng limitiert auf <strong>maximal 5 Spieler</strong>. Nur so gewährleisten wir, dass Trainer Sami Ghaouar jede Bewegung genau korrigieren kann und die Kids dennoch echten Gegnerdruck und Spielspaß erleben.
            </div>
          </div>

          <!-- FAQ 5 -->
          <div class="glass-card rounded-2xl overflow-hidden border border-slate-200/80 transition-all">
            <button class="faq-button w-full px-6 py-5 text-left font-extrabold text-slate-900 text-base sm:text-lg flex justify-between items-center focus:outline-none hover:text-[#E63946] transition-colors">
              <span>Dürfen Eltern beim Training zuschauen?</span>
              <i class="fa-solid fa-chevron-down faq-icon text-[#D4AF37] transition-transform duration-300"></i>
            </button>
            <div class="faq-content hidden px-6 pb-6 text-slate-600 text-sm leading-relaxed border-t border-slate-100 pt-4">
              Ja, selbstverständlich! Eltern sind herzlich eingeladen, das Training vom Spielfeldrand zu verfolgen. Wir legen Wert auf ein offenes, familiäres und vertrauensvolles Verhältnis zu den Familien unserer Spieler.
            </div>
          </div>

          <!-- FAQ 6 -->
          <div class="glass-card rounded-2xl overflow-hidden border border-slate-200/80 transition-all">
            <button class="faq-button w-full px-6 py-5 text-left font-extrabold text-slate-900 text-base sm:text-lg flex justify-between items-center focus:outline-none hover:text-[#E63946] transition-colors">
              <span>Gibt es Leistungsdruck oder Pflicht-Turniere?</span>
              <i class="fa-solid fa-chevron-down faq-icon text-[#D4AF37] transition-transform duration-300"></i>
            </button>
            <div class="faq-content hidden px-6 pb-6 text-slate-600 text-sm leading-relaxed border-t border-slate-100 pt-4">
              Nein. Bei uns geht es um die Freude an der eigenen Weiterentwicklung und den individuellen Fortschritt. Es gibt keinen negativen Leistungsdruck und keine Verpflichtungen zu Wochenendturnieren.
            </div>
          </div>

          <!-- FAQ 7 -->
          <div class="glass-card rounded-2xl overflow-hidden border border-slate-200/80 transition-all">
            <button class="faq-button w-full px-6 py-5 text-left font-extrabold text-slate-900 text-base sm:text-lg flex justify-between items-center focus:outline-none hover:text-[#E63946] transition-colors">
              <span>Wie buche ich ein erstes Probetraining?</span>
              <i class="fa-solid fa-chevron-down faq-icon text-[#D4AF37] transition-transform duration-300"></i>
            </button>
            <div class="faq-content hidden px-6 pb-6 text-slate-600 text-sm leading-relaxed border-t border-slate-100 pt-4">
              Fülle einfach unser kurzes Online-Kontaktformular aus oder sende Sami Ghaouar eine direkte Nachricht per <strong>WhatsApp an +49 176 841 565 42</strong>. Wir melden uns umgehend zur Terminabsprache.
            </div>
          </div>

        </div>

        <!-- Sidebar: Location & Weather Flex Feature Box -->
        <div class="lg:col-span-4 space-y-6" data-aos="fade-left">
          
          <div class="glass-card p-8 rounded-3xl border-2 border-[#D4AF37] shadow-xl space-y-6">
            <div class="w-14 h-14 rounded-2xl bg-slate-900 text-[#D4AF37] flex items-center justify-center text-2xl font-bold shadow-md">
              <i class="fa-solid fa-cloud-sun-rain"></i>
            </div>
            <h3 class="text-xl font-black text-slate-900">Ganzjährig optimal versorgt</h3>
            <p class="text-slate-600 text-xs leading-relaxed">
              Wir passen uns der Jahreszeit in Hamburg an, damit die Trainingsqualität zu 100% konstant bleibt:
            </p>

            <div class="space-y-4 pt-2">
              <div class="flex items-start gap-3 p-3 rounded-2xl bg-amber-500/10 border border-amber-500/20">
                <i class="fa-solid fa-sun text-amber-600 text-lg mt-0.5 shrink-0"></i>
                <div>
                  <div class="font-extrabold text-slate-900 text-xs">SOMMERMONATE</div>
                  <div class="text-[11px] text-slate-600">Freiluft &amp; Kunstrasen-Anlagen in Hamburg Ost.</div>
                </div>
              </div>

              <div class="flex items-start gap-3 p-3 rounded-2xl bg-blue-500/10 border border-blue-500/20">
                <i class="fa-solid fa-snowflake text-blue-600 text-lg mt-0.5 shrink-0"></i>
                <div>
                  <div class="font-extrabold text-slate-900 text-xs">WINTERMONATE</div>
                  <div class="text-[11px] text-slate-600">Beheizte Indoor-Fußballhallen in Hamburg.</div>
                </div>
              </div>
            </div>

            <div class="pt-4 border-t border-slate-200">
              <a href="#kontakt" class="w-full py-3 rounded-xl bg-slate-900 hover:bg-[#E63946] text-white font-bold text-xs flex items-center justify-center gap-2 transition-colors">
                <i class="fa-solid fa-map-location-dot"></i>
                <span>Standort im Detail anfragen</span>
              </a>
            </div>
          </div>

          <!-- Quick WhatsApp Card -->
          <div class="p-6 rounded-3xl bg-gradient-to-br from-[#25D366] to-[#1da851] text-white shadow-xl space-y-3">
            <div class="flex items-center gap-3">
              <i class="fa-brands fa-whatsapp text-3xl"></i>
              <span class="font-black text-lg">Direkte Fragen?</span>
            </div>
            <p class="text-xs text-white/90 leading-relaxed">
              Schreib Sami direkt auf WhatsApp. Er antwortet in der Regel innerhalb weniger Stunden!
            </p>
            <a href="https://wa.me/4917684156542?text=Hallo%20Sami,%20ich%20habe%20eine%20Frage%20zum%20Training!" target="_blank" class="inline-block px-5 py-2.5 rounded-full bg-white text-slate-900 font-extrabold text-xs shadow-md hover:bg-slate-100 transition-colors">
              Jetzt chatten
            </a>
          </div>

        </div>

      </div>

    </div>
  </section>

  <!-- KONTAKT & FOOTER SECTION -->"""

content = content.replace(coach_end_marker, testimonials_and_faq_section)

# 5. Add FAQ JavaScript listener
old_form_script = """    // Form submission handler
    function handleFormSubmit(e) {
      e.preventDefault();
      const successBox = document.getElementById('formSuccess');
      successBox.classList.remove('hidden');
      setTimeout(() => {
        window.location.href = "https://wa.me/4917684156542?text=" + encodeURIComponent("Hallo Sami, ich habe gerade eine Probetraining-Anfrage auf deiner Website gestellt!");
      }, 1500);
    }"""

new_form_script = """    // FAQ Accordion Toggle
    document.querySelectorAll('.faq-button').forEach(button => {
      button.addEventListener('click', () => {
        const content = button.nextElementSibling;
        const icon = button.querySelector('.faq-icon');
        const isOpen = !content.classList.contains('hidden');
        
        document.querySelectorAll('.faq-content').forEach(c => c.classList.add('hidden'));
        document.querySelectorAll('.faq-icon').forEach(i => i.style.transform = 'rotate(0deg)');
        
        if (!isOpen) {
          content.classList.remove('hidden');
          if (icon) icon.style.transform = 'rotate(180deg)';
        }
      });
    });

    // Form submission handler
    function handleFormSubmit(e) {
      e.preventDefault();
      const successBox = document.getElementById('formSuccess');
      successBox.classList.remove('hidden');
      setTimeout(() => {
        window.location.href = "https://wa.me/4917684156542?text=" + encodeURIComponent("Hallo Sami, ich habe gerade eine Probetraining-Anfrage auf deiner Website gestellt!");
      }, 1500);
    }"""

content = content.replace(old_form_script, new_form_script)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html successfully with authentic content, FAQs, events & testimonials!")
