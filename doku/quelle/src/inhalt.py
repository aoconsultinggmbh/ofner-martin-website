# -*- coding: utf-8 -*-
"""Inhalte der Praxis Dr. Ofner-Martin. Texte 1:1 von dr-ofner-martin.de
(Stand 30.09.2026), nur Rechtschreibung und Zeichensetzung korrigiert.
Gedankenstriche in Sätzen wurden nach AO-Schreibstil durch Komma, Doppelpunkt
oder Klammer ersetzt. FAQ-Antworten sind aus den vorhandenen Texten abgeleitet
und müssen von der Praxis fachlich freigegeben werden."""

ALT = 'https://www.dr-ofner-martin.de'

TEL = '07251 34 85 55'
TEL_LINK = 'tel:+497251348555'
FAX = '07251 34 85 56'
MAIL = 'praxis@dr-ofner-martin.de'
NOTDIENST = '0621 38000804'
NOTDIENST_LINK = 'tel:+4962138000804'
GOOGLE_PROFIL = 'https://goo.gl/maps/YdyosKknx4oXfY4UA'
GOOGLE_BEWERTEN = 'https://g.page/r/CRmO4XmD8NG7EBM/review'
JAMEDA = 'https://www.jameda.de/karlsdorf-neuthard/zahnaerzte/implantologie/dr-christina-ofner-martin/uebersicht/80318581_1/'
INSTAGRAM = 'https://www.instagram.com/zahnarzt.ofner.martin/'
ANAMNESE = ALT + '/images/anamnesebogen/anamnese.pdf'
RUNDGANG = ALT + '/drom-rundgang/index.htm'

# Google-Bewertung, Stand 30.09.2026 laut Google-Unternehmensprofil
GOOGLE_STERNE = '4,9'
GOOGLE_ANZAHL = '51'
GRUENDUNG = '2000'

# Reihenfolge der Leistungen wie auf der bisherigen Seite
LEISTUNGEN = [
    ('prophylaxe', 'Prophylaxe'),
    ('kinderzahnheilkunde', 'Kinderzahnheilkunde'),
    ('aesthetik', 'Ästhetische Zahnheilkunde'),
    ('zahnerhalt', 'Zahnerhalt'),
    ('zahnersatz', 'Zahnersatz (Prothetik)'),
    ('chirurgie', 'Zahnärztliche Chirurgie'),
    ('implantate', 'Implantate'),
    ('schienentherapie', 'Funktions- & Schienentherapie'),
    ('highlights', 'Behandlungs-Highlights'),
]

STELLEN = [
    'Zahnmedizinische Fachangestellte (m/w/d) für Prophylaxe und Assistenz',
    'Zahnarzt/eine Zahnärztin als Vorbereitungsassistent (m/w/d)',
    'Empfangsmitarbeiter / Rezeptionskraft (m/w/d), Zahnarztpraxis',
    'Zahnärztin / einen Zahnarzt (m/w/d)',
    'Quereinsteiger / Zahnmedizinische Fachangestellte (ZFA) (m/w/d) für Rezeption',
    'Zahnmedizinische Fachangestellte (ZFA) (m/w/d) für Rezeption',
]

PRAXIS = 'Praxis für Zahnmedizin Dr. med. dent. Christina Ofner-Martin & Kollegen'
KURZNAME = 'Zahnarztpraxis Dr. Ofner-Martin'
ADRESSE_TEXT = 'Salinenstraße 8, 76689 Karlsdorf-Neuthard'
ZEITEN_TEXT = 'Montag bis Donnerstag von 8:00 bis 19:00 Uhr und Freitag von 8:30 bis 14:00 Uhr'

KONTAKT_FAQ = (
    'Wie erreiche ich die Zahnarztpraxis Dr. Ofner-Martin in Karlsdorf-Neuthard?',
    f'Die {PRAXIS} liegt in der {ADRESSE_TEXT}, nur wenige Minuten von Bruchsal entfernt. '
    f'Direkt an der Praxis gibt es ausreichend kostenfreie Parkplätze. Telefonisch ist die Praxis unter {TEL} erreichbar, '
    f'per E-Mail unter {MAIL}. Die Sprechzeiten sind {ZEITEN_TEXT}.'
)

# ---------------------------------------------------------------- Leistungen
# Jede Leistung: kuerzel, titel, obenzeile (alte Unterzeile), h1, besch, bild,
# bildalt, abschnitte (html), faq [(frage, antwort)]
L = {}

L['prophylaxe'] = dict(
    titel='Prophylaxe in Karlsdorf-Neuthard | Dr. med. dent. Ofner-Martin',
    besch='Zahnvorsorge und Prophylaxe in Karlsdorf-Neuthard bei Bruchsal: Vorbeugung von Erkrankungen. Wir beraten Sie zur Optimierung Ihrer Mundhygiene und Ihrer Ernährung.',
    obenzeile='Dauerhaft natürlich lächeln',
    h1='Prophylaxe in Karlsdorf-Neuthard',
    bild='/media/yootheme/cache/dc/zahnvorsorge-bruchsal-karlsdorf-neuthard-dc9e4e07.jpg', bw=1920, bh=820,
    bildalt='Zahnvorsorge in der Zahnarztpraxis Dr. Ofner-Martin in Karlsdorf-Neuthard',
    neu='prophylaxe-zahnreinigung-karlsdorf-neuthard',
    abschnitte=[
        ('Vorbeugung & Vorsorge', '<p>Unsere Mundhöhle ist Lebensraum für eine Vielzahl von Bakterien, die sich auf der Zahnoberfläche festsetzen und sich dort vermehren. Hier bilden sie zusammen mit Speiseresten, Zucker u. a. einen klebrigen Zahnbelag: die Plaque, Hauptursache von Zahnfleischentzündungen. Dem können Sie durch entsprechende Zahnvorsorge (Prophylaxe) entgegenwirken.</p>'),
        ('Individualprophylaxe (IP)', '<p>Prophylaxe bedeutet die Verhütung und Vorbeugung von Erkrankungen. Im Rahmen unserer Individualprophylaxe wird Ihre momentane Situation eingeschätzt und diagnostiziert. Es erfolgt eine persönliche Anleitung mit individuellen Instruktionen. Es werden Ihnen unter anderem verschiedene Hilfsmittel zur Optimierung Ihrer häuslichen Mundhygiene gezeigt und erklärt. Da Karies und Parodontose auch viel mit Ernährung zu tun haben, werden wir auch darüber mit Ihnen sprechen. Abschließend werden wir eine Professionelle Zahnreinigung (kurz PZR) durchführen.</p>'),
        ('Professionelle Zahnreinigung (PZR)', '<p>Trotz intensiver Mundhygiene können unter Umständen Zahnbeläge in schwer zugänglichen Nischen und Zahnzwischenräumen nicht vollständig entfernt werden. Deshalb ist eine regelmäßige Professionelle Zahnreinigung in der Zahnarztpraxis erforderlich (1 bis 2x im Jahr).</p><p>Die Professionelle Zahnreinigung umfasst:</p><ul><li>Harte und weiche Beläge auf den Zahnoberflächen und den Zwischenräumen werden vollständig entfernt.</li><li>Bei Bedarf werden Verfärbungen, die durch Kaffee, Tee, Nikotin entstehen, mittels Pulverstrahl schonend entfernt.</li><li>Eine gründliche Politur mit professionellen Hilfsmitteln glättet die Oberflächen, sodass sich neuer Zahnbelag schwerer festsetzen kann.</li><li>Eine abschließende Fluoridierung trägt zur Remineralisation des Zahnschmelzes bei und schützt vor neuen Säureangriffen.</li></ul>'),
    ],
    faq=[
        ('Wie oft sollte eine Professionelle Zahnreinigung gemacht werden?', 'Die Zahnarztpraxis Dr. Ofner-Martin empfiehlt eine regelmäßige Professionelle Zahnreinigung ein- bis zweimal im Jahr. Denn trotz intensiver Mundhygiene lassen sich Beläge in schwer zugänglichen Nischen und Zahnzwischenräumen zu Hause oft nicht vollständig entfernen.'),
        ('Was gehört zur Professionellen Zahnreinigung?', 'Bei der PZR in der Praxis Dr. Ofner-Martin werden harte und weiche Beläge vollständig entfernt, bei Bedarf Verfärbungen durch Kaffee, Tee oder Nikotin mit Pulverstrahl schonend gelöst, die Zähne gründlich poliert und abschließend fluoridiert. Die Fluoridierung unterstützt die Remineralisation des Zahnschmelzes.'),
        ('Was ist Individualprophylaxe?', 'Bei der Individualprophylaxe schätzt das Team der Zahnarztpraxis Dr. Ofner-Martin Ihre momentane Situation ein, zeigt Ihnen passende Hilfsmittel für die häusliche Mundhygiene und spricht mit Ihnen auch über Ernährung, weil Karies und Parodontose viel damit zu tun haben. Zum Abschluss folgt eine Professionelle Zahnreinigung.'),
        ('Wo bekomme ich eine Zahnreinigung in Karlsdorf-Neuthard?', KONTAKT_FAQ[1]),
    ],
)

L['kinderzahnheilkunde'] = dict(
    titel='Kinderzahnheilkunde in Karlsdorf-Neuthard | Dr. Ofner-Martin',
    besch='Kinderzahnarzt in Karlsdorf-Neuthard bei Bruchsal: entspannt und fröhlich. Kinderzahnheilkunde von der Kinderzahnputzschule bis zur Lachgasbehandlung für ängstliche Kinder.',
    obenzeile='Ihr Zahnarzt für Kinder',
    h1='Kinderzahnheilkunde in Karlsdorf-Neuthard',
    bild='/media/yootheme/cache/a0/kinderzahnarzt-bruchsal-karlsdorf-neuthard-a0d23473.jpg', bw=1920, bh=820,
    bildalt='Kinderzahnheilkunde in der Zahnarztpraxis Dr. Ofner-Martin in Karlsdorf-Neuthard',
    neu='kinderzahnarzt-karlsdorf-neuthard-zahnputzschule',
    abschnitte=[
        ('Zahnputzschule für Kinder', '<p>„Wir lernen nicht für die Schule, sondern für das Leben.“ Genauso ist es auch mit dem Zähneputzen. Als Kinder-Zahnarzt in Karlsdorf-Neuthard trainieren wir gemeinsam mit Ihrem Kind die richtige Zahnpflege. Bei unseren halbjährlichen Terminen werden die Zähne angefärbt, die Putzleistung beurteilt und ggf. die Technik verbessert. Ihr Kind zeigt die erlernte Putztechnik und die Fluoridierung („Zahnmarmelade“) wird aufgetragen. Einmal jährlich übernehmen die gesetzlichen Krankenversicherungen die Belagsentfernung. Außerdem sprechen wir bei Bedarf über die zahnfreundliche Ernährung Ihres Kindes.</p>'),
        ('Professionelle Zahnreinigung für Kinder', '<p>Unsere kleinen Patienten dürfen genauso wie Mama und Papa regelmäßig zur professionellen Zahnreinigung (PZR) kommen. Milchzähne und bleibende Zähne werden mit Ultraschall und speziellen Polierbürsten und Polierpaste gesäubert, sodass keine Beläge übrig bleiben!</p>'),
        ('Fissurenversiegelung', '<p>Die Backenzähne bestehen aus Höckern und Fissuren (Furchen). Häufig sind diese kleinen Fissuren schwer zu reinigen, sodass eine Karies droht. Im Rahmen einer Fissurenversiegelung werden die Furchen mit einem dünnfließenden Kunststoff aufgefüllt. Ihrem Kind kann so eine adäquate Zahnpflege zuhause erleichtert werden.</p>'),
        ('Kinderbehandlung mit Lachgas', '<p>Für den Fall, dass unsere kleinen Patienten viel Angst vor der Behandlung haben, gibt es die Möglichkeit, die anstehende Behandlung unter Lachgassedierung durchzuführen. Ihr Kind ist bei vollem Bewusstsein und kann mit uns jederzeit kommunizieren. Eine Lachgassedierung ist schonender als eine Vollnarkose. Übrigens eignet sich Lachgas auch für große Patienten ;-)</p>'),
        ('Platzhalter', '<p>Manchmal ist es leider so, dass ein Milchzahn nicht erhaltungswürdig ist, z. B. wenn das Loch zu groß ist oder der Zahn eine Fistel gebildet hat. Der Milchzahn wird entfernt und eine Zahnlücke entsteht. Um zu verhindern, dass die anderen Zähne in die Lücke wandern und der neue Zahn am Durchbruch gehindert wird, wird empfohlen, einen Platzhalter einzusetzen. Es gibt zwei Arten von Platzhaltern: festsitzende und herausnehmbare Platzhalter. Wir verwenden ausschließlich festsitzende Platzhalter. Diese werden fest am Nachbarzahn angebracht und halten die Lücke offen. Das Risiko für Zahnfehlstellungen wird minimiert. Alternativ kann man herausnehmbare Platzhalter anfertigen lassen, die jedoch oftmals nicht regelmäßig genug getragen werden. Bei der Variante des festsitzenden Platzhalters fallen Kosten an.</p>'),
        ('Fluorose / MIH / Kreidezähne', '<p>Die Fluorose erkennt man an weißen Flecken, hauptsächlich an den Frontzähnen. Es handelt sich dabei nicht um Karies. <a data-ziel="aesthetik" href="#/aesthetik/dentalfluorose">Hier erfahren Sie alles rund um das Thema Dentalfluorose.</a> Mittels einer speziellen Technik können wir diese weißen Flecken ohne Bohren und somit völlig schmerzfrei entfernen. Davon abzugrenzen ist die Molaren-Incisiven-Hypomineralisation, kurz MIH oder auch „Kreidezähne“ genannt. Der Zahnschmelz von Backen- und Frontzähnen ist verändert und entwickelt bräunliche Flecken. Die Zähne können zum Teil sehr schmerzempfindlich sein und bilden schneller Karies als „gesunde“ Zähne. Kreidezähne müssen regelmäßig kontrolliert werden, um frühzeitig therapeutische Maßnahmen zu ergreifen.</p>'),
        ('Milchzahnfüllungen', '<p>Kariöse Milchzähne können mit plastischen Füllungsmaterialien („Zahnknete“) wieder aufgebaut werden. Diese Leistung übernimmt die gesetzliche Krankenkasse komplett.</p>'),
        ('Milchzahnkronen', '<p>Ist der Defekt im Milchzahn zu groß, sodass eine Füllung nicht möglich ist, kommen Milchzahnkronen („Ritterzähne“) aus medizinischem Stahl zum Einsatz. Die Zähne sind somit optimal gestärkt und das Kauen macht wieder Spaß. Ritterzähne werden von den gesetzlichen Krankenkassen übernommen.</p>'),
        ('Milchzahnendodontie', '<p>Unser Ziel ist es, die Milchzähne so lange wie möglich zu erhalten, am besten bis es Zeit für den Zahnwechsel ist. Neben Füllungen oder Ritterzähnen können wir auch mittels Wurzelbehandlungen das Leben der Milchzähne verlängern. Auch hier erfolgt die Behandlung auf kindgerechte Art und Weise.</p>'),
        ('Kariesinaktivierung mit SDF', '<p>Eine aktuelle Pilotstudie hat gezeigt, dass Silberdiaminfluorid (kurz SDF) als äußerst erfolgreich zur Behandlung von schwer zugänglicher Karies in Zahnzwischenräumen eingesetzt werden kann. Das bedeutet, diese Behandlung eignet sich vor allem für Kinder, deren Kooperation bei einer Füllungstherapie häufig eher gering ist. Die frühkindliche Karies ist eine der häufigsten Erkrankungen des Kindesalters. Wichtig zu wissen ist, dass die Anwendung von SDF lediglich zu einer Inaktivierung der Karies führt. Damit lässt sich eine weitere Therapie bis zum natürlichen Zahnwechsel oder einer gestiegenen Bereitschaft des Kindes hinauszögern. Die mit SDF behandelten Stellen verfärben sich dauerhaft dunkelschwarz. Darunter leidet zwar die Ästhetik, die antimikrobiellen und remineralisierenden Eigenschaften von SDF machen es aber zu einem wertvollen Werkzeug in der modernen Zahnmedizin. Sprechen Sie uns gerne darauf an.</p>'),
    ],
    faq=[
        ('Was passiert in der Zahnputzschule für Kinder?', 'In der Zahnputzschule der Zahnarztpraxis Dr. Ofner-Martin werden bei halbjährlichen Terminen die Zähne angefärbt, die Putzleistung beurteilt und die Technik bei Bedarf verbessert. Anschließend zeigt das Kind die erlernte Putztechnik und die Fluoridierung („Zahnmarmelade“) wird aufgetragen. Einmal jährlich übernehmen die gesetzlichen Krankenversicherungen die Belagsentfernung.'),
        ('Was hilft, wenn mein Kind große Angst vor der Behandlung hat?', 'Die Zahnarztpraxis Dr. Ofner-Martin bietet für ängstliche Kinder eine Behandlung unter Lachgassedierung an. Das Kind bleibt bei vollem Bewusstsein und kann jederzeit mit dem Behandlungsteam kommunizieren. Eine Lachgassedierung ist schonender als eine Vollnarkose.'),
        ('Welche Leistungen für Milchzähne übernimmt die gesetzliche Krankenkasse?', 'Füllungen für Milchzähne mit plastischen Füllungsmaterialien („Zahnknete“) übernimmt die gesetzliche Krankenkasse komplett, ebenso Milchzahnkronen aus medizinischem Stahl („Ritterzähne“). Für festsitzende Platzhalter fallen dagegen Kosten an.'),
        ('Gibt es einen Kinderzahnarzt in Karlsdorf-Neuthard?', f'Ja. Die {PRAXIS} behandelt in der {ADRESSE_TEXT} auch Kinder, mit großer Geduld und in kinderfreundlicher Atmosphäre. Zahnärztin Katharina Gärtner hat ihren Tätigkeitsschwerpunkt in der Kinderzahnheilkunde. Termine gibt es unter {TEL}.'),
    ],
)

L['aesthetik'] = dict(
    titel='Zahnästhetik in Karlsdorf-Neuthard | Dr. med. dent. Ofner-Martin',
    besch='Zahnästhetik in Karlsdorf-Neuthard: ästhetisch schöne Zähne mit Bleaching, Dentalfluorose-Behandlung oder durch Veneers.',
    obenzeile='Natürlich schöne Zähne',
    h1='Zahnästhetik in Karlsdorf-Neuthard',
    bild='/media/yootheme/cache/f8/schoene-zaehne-bruchsal-karlsdorf-neuthard-f8138249.jpg', bw=1920, bh=820,
    bildalt='Ästhetische Zahnheilkunde in der Zahnarztpraxis Dr. Ofner-Martin in Karlsdorf-Neuthard',
    neu='zahnaesthetik-veneers-bleaching-karlsdorf-neuthard',
    anker={'Dentalfluorose-Behandlung': 'dentalfluorose'},
    abschnitte=[
        ('Veneers', '<p>Schiefe Zähne? Veneers helfen! Dabei handelt es sich um 0,5 mm dünne, im zahnmedizinischen Labor hergestellte Keramikverblendschalen. Nachdem nur minimal Zahnhartsubstanz entfernt wurde, werden die Veneers auf den Zahnoberflächen adhäsiv befestigt. Veneers werden u. a. zur Korrektur schiefer Zähne eingesetzt.</p><p>Methoden zur Problemlösung:</p><ul><li>zahnsubstanzschonende Korrektur umfangreicher kariöser Läsionen</li><li>große interdentale Lücken schließen (häufig zwischen den beiden vorderen Frontzähnen)</li><li>gedrehte Zähne harmonisch in den Zahnbogen einfügen</li><li>Aufhellung von Zähnen (falls Bleaching, vor allem bei gräulichen Zähnen, nicht zum gewünschten Ergebnis führte)</li><li>Wiederherstellung der Zahnkronen bei Zahnfrakturen</li><li>Verbesserung der Zahnform</li></ul>'),
        ('Dentalfluorose-Behandlung', '<h3>Schöne Zähne ohne Bohren? Weiße Flecken ade!</h3><p>Sie haben weiße Flecken auf den Zähnen trotz guter Mundhygiene, sodass der erste Blick im Spiegel auf Ihre Zähne wandert? Mit der Einführung der Infiltrationsmethode kostet der Zahnarztbesuch keine Überwindung mehr. Mit dieser Methode ist es möglich, weiße Flecken auf Front- oder Seitenzähnen unsichtbar zu machen, ganz ohne Bohren, Spritze und Schmerzen!</p>'
         '<details class="falt"><summary><h4 class="nur-titel" style="font:inherit;margin:0;display:inline">Wie entstehen weiße Flecken auf den Zähnen?</h4></summary><div class="falt__inhalt"><p>Zähne können aus unterschiedlichen Gründen weiße Flecken aufweisen. Einerseits können die sog. White Spots während dem Tragen einer festen Zahnspange entstehen, da Brackets auf den Außenflächen der Zähne geklebt werden. Dadurch ist das Zähneputzen an diesen Stellen erschwert, sodass der Schmelz kleine kariöse Ränder um die geklebten Brackets entwickeln kann. Wenn die Zahnspange vom Kieferorthopäden dann abgenommen wird, werden diese weißen Läsionen sichtbar. Eine andere Ursache für fleckige Zähne ist die Dentalfluorose. Eine ausreichende Fluoridzufuhr ist wichtig, um Zähne vor Karies zu schützen (es ersetzt natürlich nicht das Zähneputzen). Wird zu viel Fluorid zugeführt, kann sich dieses schon vor dem Zahndurchbruch im Schmelz der bleibenden Zähne einlagern. Wenn der Zahnwechsel dann ansteht, brechen die neuen Zähne schon mit weißen Flecken durch, die ein Leben lang bestehen bleiben. Zähne mit Fluorose sind nicht schmerzempfindlicher, stellen für viele Patienten jedoch ein kosmetisches Problem dar.</p></div></details>'
         '<details class="falt"><summary><h4 style="font:inherit;margin:0;display:inline">Wie läuft die Behandlung ab?</h4></summary><div class="falt__inhalt"><p>Zunächst werden die betroffenen Zähne gereinigt, z. B. in Form einer professionellen Zahnreinigung. Im Anschluss wird ein Zahnfleischschutz aufgetragen und das betroffene Zahngebiet mit Watterollen trockengelegt. Dann werden die zu behandelnden Zähne angeätzt, abgespült und getrocknet. Dieser Vorgang wird unter Umständen wiederholt, bis die Zahnoberfläche leicht angeraut ist. Somit kann in einem nächsten Schritt der Infiltrant in die vorbehandelte Oberfläche des Zahnes eindringen. Die Flüssigkeit wird nun lichtgehärtet und die Zähne zuletzt noch poliert.</p></div></details>'
         '<details class="falt"><summary><h4 style="font:inherit;margin:0;display:inline">Sollte man lieber kein Fluorid nehmen?</h4></summary><div class="falt__inhalt"><p>Fluorid ist sehr wichtig, um Karies vorzubeugen. Gerade in kariesaktiven Gebissen darf darauf nicht verzichtet werden. Daher gilt: Fluorid, unbedingt! Die Dosierung macht’s! Bei Kindern sollte mit dem Durchbruch der ersten Milchzähne 1x täglich mit einer fluoridhaltigen Kinderzahnpasta (500 ppm Fluorid) geputzt werden. Ab dem Grundschulalter können Kinder auf Junior- bzw. Erwachsenenzahnpasten umsteigen, die einen Fluoridgehalt von mindestens 1000 ppm enthalten. Im Haushalt sollte kein fluoridiertes Speisesalz zum Einsatz kommen, da die Gefahr einer Überfluoridierung besteht. Vom Arzt verschriebene Fluoridtabletten sind nicht notwendig. Wenn darauf verzichtet wird, sollten Sie darauf achten, dass trotzdem genügend Vitamin D Ihrem Kind zur Verfügung steht. Vitamin D kann in Form von Ölen oder Tabletten zugeführt werden. Ohne die richtige Putztechnik bringt jedoch die beste Zahnpasta nichts. Wir beraten Jung und Alt gerne bei der Auswahl der richtigen Zahnbürste und Zahnpasta. Vereinbaren Sie doch einmal einen Termin bei unseren Prophylaxehelferinnen! Wir beraten Sie gerne zu diesem und anderen Themen ausführlich, denn Ihre Zahngesundheit liegt uns sehr am Herzen! <a data-ziel="kontakt" href="#/kontakt">Hier können Sie Kontakt zu uns aufnehmen.</a> Wir freuen uns über Ihren Besuch in unserer Zahnarztpraxis in Karlsdorf-Neuthard, unweit von Bruchsal.</p><p>Der nachfolgende Link verweist Sie auf ein Video, in dem die Behandlungsschritte noch einmal erklärt werden: <a href="https://vimeo.com/80063442" rel="noopener" target="_blank">vimeo.com/80063442</a> <span class="nur-vorleser">(öffnet in neuem Fenster)</span></p></div></details>'
         '<details class="falt"><summary><h4 style="font:inherit;margin:0;display:inline">Quellen</h4></summary><div class="falt__inhalt"><ul><li><a href="https://www.zwp-online.info/fachgebiete/prophylaxe/grundlagen/mikroinvasivitaet-durch-kariesinfiltration" rel="noopener" target="_blank">zwp-online.info: Mikroinvasivität durch Kariesinfiltration</a></li><li><a href="http://www.dgzmk.de/uploads/tx_szdgzmkdocuments/20120313_Final_Leitl_Fluoridierung_Kurzversion_12.03.2012.pdf" rel="noopener" target="_blank">DGZMK: Leitlinie Fluoridierung (Kurzversion, PDF)</a></li><li><a href="https://www.bzaek.de/fileadmin/PDFs/pati/bzaekdgzmk/2_01_fluoridierung.pdf" rel="noopener" target="_blank">BZÄK: Fluoridierung (PDF)</a></li></ul></div></details>'),
        ('Bleaching', '<h3>Das Home-Bleaching</h3><p>Das Aufhellen mit individuell angefertigten oder konfektionierten Schienen mit peroxidhaltigem Aufhellungsgel.</p><h3>Das In-Office-Bleaching</h3><p>Diese Aufhellung wird in der Praxis vom Behandler direkt am Stuhl vorgenommen. Dabei wird das Aufhellungsmittel direkt auf die Zähne aufgebracht und der gewünschte Effekt nach einer gewissen Einwirkzeit erzielt.</p><h3>Internes Bleaching</h3><p>Nach einer Wurzelkanalbehandlung kann es passieren, dass sich der Zahn nach einiger Zeit dunkel verfärbt. Vor allem im Frontzahnbereich kann dies störend sein. Mittels internem Bleaching kann man die Zahnfarbe korrigieren. Man bringt dazu ein Gemisch aus Natriumperborat und Wasserstoffperoxid in den nervtoten Zahn ein und verschließt ihn mit einer provisorischen Füllung. Nach ca. 3 Tagen wird das Ergebnis überprüft. Der Vorgang kann dann ggf. wiederholt werden.</p>'),
    ],
    faq=[
        ('Was sind Veneers?', 'Veneers sind etwa 0,5 mm dünne, im zahnmedizinischen Labor hergestellte Keramikverblendschalen. In der Zahnarztpraxis Dr. Ofner-Martin werden sie nach minimalem Abtrag von Zahnhartsubstanz adhäsiv auf den Zahnoberflächen befestigt, etwa um schiefe Zähne zu korrigieren, Lücken zu schließen oder die Zahnform zu verbessern.'),
        ('Lassen sich weiße Flecken auf den Zähnen ohne Bohren entfernen?', 'Ja. Mit der Infiltrationsmethode kann die Zahnarztpraxis Dr. Ofner-Martin weiße Flecken auf Front- oder Seitenzähnen unsichtbar machen, ganz ohne Bohren, Spritze und Schmerzen. Die Zähne werden gereinigt, angeätzt und getrocknet, dann dringt ein Infiltrant ein, wird lichtgehärtet und poliert.'),
        ('Welche Arten von Bleaching gibt es?', 'Die Praxis Dr. Ofner-Martin unterscheidet drei Wege: Home-Bleaching mit Schienen und peroxidhaltigem Gel, In-Office-Bleaching direkt am Behandlungsstuhl und internes Bleaching für einen nach einer Wurzelkanalbehandlung dunkel verfärbten Zahn.'),
        ('Wo kann ich mich in Karlsdorf-Neuthard zu Zahnästhetik beraten lassen?', f'In der {PRAXIS}, {ADRESSE_TEXT}, nahe Bruchsal. Dr. Christina Ofner-Martin ist Mitglied der Deutschen Gesellschaft für Ästhetische Zahnheilkunde (DGÄZ). Termine vereinbaren Sie unter {TEL}.'),
    ],
)

L['zahnerhalt'] = dict(
    titel='Zahnerhaltung in Karlsdorf-Neuthard | Dr. Ofner-Martin',
    besch='Zahnerhaltung in Karlsdorf-Neuthard: Unser Hauptziel ist es, Zähne zu erhalten. Informationen zu Zahnerhalt und Füllungen in unserer Zahnarztpraxis.',
    obenzeile='Gesunde Zahnsubstanz erhalten',
    h1='Zahnerhalt & Füllungen in Karlsdorf-Neuthard',
    bild='/media/yootheme/cache/6c/zahn-fuellung-bruchsal-karlsdorf-neuthard-6c65a276.jpg', bw=1920, bh=820,
    bildalt='Zahnerhaltung und Füllungstherapie in der Zahnarztpraxis Dr. Ofner-Martin',
    neu='zahnerhalt-fuellung-keramikinlay-karlsdorf-neuthard',
    abschnitte=[
        ('Wir möchten Ihre natürlichen Zähne erhalten', '<p>Ihre Mundgesundheit liegt uns am Herzen. Deshalb ist es unser Hauptziel, Ihre natürlichen Zähne zu erhalten. Es kann jedoch trotz regelmäßiger Pflege zu kleinen Defekten an der Zahnhartsubstanz kommen. Ist dies der Fall, können diese (meist kariösen) Defekte mit Hilfe von Füllungen therapiert und so der Zahn vor weiterer Zerstörung geschützt werden. Hierfür bieten sich verschiedene Füllungsmaterialien und dadurch bedingt auch verschiedene Therapien an:</p><p>Die am häufigsten verwendete Füllungsart ist die sogenannte Komposit- bzw. Kunststofffüllung. Komposit wird als Füllungsmaterial für kleinere bis mittlere Defekte benutzt. Es ist eine Zusammensetzung aus Keramik und Kunststoffpartikeln. Dieses Material hat im Vergleich zum früher verwendeten Amalgam den Vorteil, dass es zahnfarben ist. Die gesetzlichen Krankenkassen übernehmen derartige Komposit-Füllungen leider nicht komplett. In welcher Höhe sich die Zuzahlung beläuft, wird Ihnen selbstverständlich vor dem Füllungstermin erklärt. Seit Juli 2018 werden bei Kindern bis zum vollendeten 15. Lebensjahr Komposit-Füllungen von den Krankenkassen vollständig übernommen. Wie bei jedem zahnmedizinischen Werkstoff gibt es auch bei den Kompositen Vor- sowie Nachteile, welche je nach Situation durch unser Ärzteteam patientenindividuell eingeschätzt und bewertet werden. Bei größeren Defekten kann es beispielsweise sein, dass eine Füllungstherapie mit Komposit nicht mehr möglich ist, da Komposit beim Aushärten schrumpft und somit der Zahn unter Schrumpfungsstress gestellt wird. Hierdurch kann es zu Mikrofrakturen der verbleibenden Zahnhartsubstanz kommen, weshalb in solchen Fällen eher auf andere Füllungsmaterialien bzw. Formen wie Inlays oder Onlays zurückgegriffen werden sollte.</p><p>Eine Alternative zu den oben beschriebenen Kompositfüllungen kann die Versorgung des Zahnes mithilfe einer Keramikfüllung, auch Keramik-Inlay genannt, sein. Sie wird dem Zahn in Form und Farbe nachempfunden. Keramik ist gut verträglich und reagiert nicht mit anderen zahnmedizinischen Werkstoffen. Man spricht in diesem Zusammenhang auch von einer hohen Biokompatibilität des Werkstoffes Keramik. Temperaturempfindlichkeiten sind nicht zu erwarten. Die Herstellung eines Keramik-Inlays kann über zwei Wege erfolgen:</p>'),
        ('Labside-Methode', '<p>Bei der ersten Option, der sogenannten „Labside-Methode“, schichtet der Zahntechniker das Inlay individuell mit unterschiedlichen Keramikmassen. Auf diese Weise entstehen hochästhetische Versorgungen, welche insbesondere im vorderen Seitenzahngebiet sinnvoll sind. Auch die Wahl der Keramik ist ein wichtiger Bestandteil der zahnärztlichen Therapie Ihrer Zähne. Hierbei arbeiten wir Hand in Hand mit den Zahntechnikern zusammen, um ein optimales Ergebnis zu erzielen. Werden die Zähne beispielsweise durch nächtliches oder stressinduziertes <a data-ziel="schienentherapie" href="#/schienentherapie">Zähneknirschen</a> hohen Belastungen ausgesetzt, sollte die Wahl des Materials auf eine monolithische Lithium-Disilikat-Keramik fallen, da diese besonders resistent gegenüber dem sog. Chipping bzw. Teilfrakturen ist.</p>'),
        ('Chairside-Methode', '<p>Die zweite Option, die sogenannte „Chairside-Methode“, ist die Herstellung der Keramik-Inlays über das in unserer Praxis vorhandene <a data-ziel="highlights" href="#/highlights/cerec">CEREC®-System</a>. Hierbei wird nach der Präparation des Zahnes eine digitale Abformung durch einen Intraoralscanner genommen. Anschließend erfolgt das patientenindividuelle Design des Keramik-Inlays durch unser Zahnärzteteam und das Fräsen des Inlays innerhalb von kürzester Zeit in unserer Praxis. Diese Option eignet sich besonders für die Versorgung kleinerer Defekte im Seitenzahnbereich.</p><p>Sie haben Fragen rund um das Thema Füllungen bzw. Füllungstherapien oder wollen einen Termin für ein Beratungsgespräch vereinbaren? Unser Team steht Ihnen jederzeit zur Verfügung.</p>'),
    ],
    faq=[
        ('Welche Füllung wird am häufigsten verwendet?', 'Am häufigsten verwendet die Zahnarztpraxis Dr. Ofner-Martin die zahnfarbene Komposit- bzw. Kunststofffüllung für kleinere bis mittlere Defekte. Komposit besteht aus Keramik- und Kunststoffpartikeln. Bei größeren Defekten sind Inlays oder Onlays oft die bessere Wahl, weil Komposit beim Aushärten schrumpft.'),
        ('Übernimmt die Krankenkasse Kunststofffüllungen?', 'Bei Erwachsenen übernehmen die gesetzlichen Krankenkassen Komposit-Füllungen nicht komplett. Die Höhe der Zuzahlung erklärt die Praxis Dr. Ofner-Martin vor dem Füllungstermin. Seit Juli 2018 werden Komposit-Füllungen bei Kindern bis zum vollendeten 15. Lebensjahr vollständig übernommen.'),
        ('Was ist der Unterschied zwischen Labside- und Chairside-Inlay?', 'Beim Labside-Verfahren schichtet ein Zahntechniker das Keramik-Inlay individuell, das eignet sich besonders für hochästhetische Versorgungen. Beim Chairside-Verfahren fertigt die Zahnarztpraxis Dr. Ofner-Martin das Inlay nach einem Intraoralscan mit dem CEREC®-System selbst, innerhalb kürzester Zeit. Das eignet sich besonders für kleinere Defekte im Seitenzahnbereich.'),
        ('Wo bekomme ich Keramik-Inlays in Karlsdorf-Neuthard?', f'Die {PRAXIS} fertigt Keramik-Inlays in der eigenen Praxis in der {ADRESSE_TEXT} und arbeitet für Labside-Versorgungen mit zahntechnischen Laboren zusammen. Beratungstermine unter {TEL}.'),
    ],
)

L['zahnersatz'] = dict(
    titel='Zahnersatz in Karlsdorf-Neuthard | Dr. med. dent. Ofner-Martin',
    besch='Zahnersatz und Prothetik in Karlsdorf-Neuthard: individuelle Versorgung mit Kronen, Brücken und herausnehmbarem Zahnersatz, wenn Zahnverlust droht.',
    obenzeile='Wenn Zahnverlust droht',
    h1='Zahnersatz in Karlsdorf-Neuthard',
    bild='/media/yootheme/cache/00/zahnersatz-bruchsal-karlsdorf-neuthard-0075c7fd.jpg', bw=1920, bh=820,
    bildalt='Zahnersatz und Prothetik aus der Zahnarztpraxis Dr. Ofner-Martin',
    neu='zahnersatz-kronen-bruecken-karlsdorf-neuthard',
    abschnitte=[
        ('Zahnersatz / Prothetik', '<p>Der Verlust eines Zahnes zieht eine Reihe von Beeinträchtigungen des gesamten Kausystems nach sich. Wenn Zahnverlust droht, bietet die Zahnmedizin eine Reihe von Möglichkeiten für die individuelle Versorgung mit Zahnersatz (Prothetik). Dieser kann festsitzend sein, wie zum Beispiel Kronen oder Brücken aus Vollkeramik oder verschiedenen Metalllegierungen. Festsitzender Zahnersatz kann auch auf <a data-ziel="implantate" href="#/implantate">Implantaten</a> befestigt werden. Sollten mehrere Zähne fehlen, kann ein herausnehmbarer Zahnersatz die Lösung sein. Welche Lösung für Sie in Frage kommt, besprechen wir mit Ihnen in einem ausführlichen unverbindlichen Beratungsgespräch, bei dem wir Ihnen alle Versorgungsmöglichkeiten aufzeigen und erklären, damit Sie gut informiert die für Sie optimale Lösung auswählen können.</p>'),
        ('Qualitäts-Zahnersatz „Made in Germany“', '<p>Qualitativ hochwertiger Zahnersatz in perfekter Ästhetik wird durch die Zusammenarbeit mit erstklassigen zahntechnischen Meisterlaboren in unserer Region sichergestellt. So dürfen Sie sich auf heimische Qualität „made in Germany“ ebenso verlassen wie auf optimale Zusammenarbeit mit einem Zahntechniker vor Ort. Ist es erforderlich, kommt der Zahntechniker auch zu uns in die Praxis und berät Sie zur optimalen Lösung.</p>'),
    ],
    faq=[
        ('Welche Arten von Zahnersatz gibt es?', 'Die Zahnarztpraxis Dr. Ofner-Martin bietet festsitzenden Zahnersatz wie Kronen oder Brücken aus Vollkeramik oder verschiedenen Metalllegierungen, festsitzenden Zahnersatz auf Implantaten und, wenn mehrere Zähne fehlen, herausnehmbaren Zahnersatz.'),
        ('Wo wird der Zahnersatz hergestellt?', 'Die Praxis Dr. Ofner-Martin arbeitet mit zahntechnischen Meisterlaboren aus der Region zusammen, also Qualität „made in Germany“. Bei Bedarf kommt der Zahntechniker in die Praxis und berät direkt vor Ort.'),
        ('Wie finde ich heraus, welcher Zahnersatz zu mir passt?', 'In einem ausführlichen, unverbindlichen Beratungsgespräch zeigt Ihnen das Team der Zahnarztpraxis Dr. Ofner-Martin alle Versorgungsmöglichkeiten und erklärt sie, damit Sie gut informiert entscheiden können. Auf Wunsch ist auch eine zinsfreie Ratenzahlung über 6 oder 12 Monate möglich.'),
        ('Wo bekomme ich Zahnersatz in Karlsdorf-Neuthard?', KONTAKT_FAQ[1]),
    ],
)

L['chirurgie'] = dict(
    titel='Zahnärztliche Chirurgie in Karlsdorf-Neuthard | Dr. Ofner-Martin',
    besch='Zahnärztliche Chirurgie in Karlsdorf-Neuthard: Zahnextraktionen, Wurzelspitzenresektionen und Knochenaufbau inklusive fachmännischer Beratung.',
    obenzeile='Sanfte Eingriffe',
    h1='Zahnärztliche Chirurgie in Karlsdorf-Neuthard',
    bild='/media/yootheme/cache/1a/weisheitszahn-entfernen-bruchsal-1aa69e24.jpg', bw=1920, bh=820,
    bildalt='Zahnärztliche Chirurgie in der Zahnarztpraxis Dr. Ofner-Martin',
    neu='zahnaerztliche-chirurgie-karlsdorf-neuthard',
    abschnitte=[
        ('Zahnextraktionen', '<p>Sollte ein Zahn einmal irreparabel zerstört sein, führen wir auch Extraktionen bzw. Zahnentfernungen in unserer Praxis durch. Hierfür wird der entsprechende Bereich betäubt, daraufhin erfolgt die schmerzfreie Extraktion des betroffenen Zahnes. Gerne können wir auch zusätzliche Maßnahmen ergreifen, um den Eingriff für Sie zu erleichtern. Z. B. kann eine leichte Sedierung mittels Lachgas erfolgen.</p>'),
        ('Wurzelspitzenresektionen', '<p>In manchen Situationen kann eine sog. Wurzelspitzenresektion nötig werden, um einen Zahn zu erhalten. Hierbei wird die Wurzelspitze des Zahnes unter einer entsprechenden Betäubung gekappt und anschließend mit einem speziellen Zement verschlossen.</p>'),
        ('Knochenaufbau', '<p>Ein sog. Knochenaufbau (auch Augmentation) kann manchmal vor der Insertion eines Implantates notwendig sein. Hierfür wird in einer minimalinvasiven Operation sog. Knochenersatzmaterial auf bereits vorhandenen (meist stark abgebauten) Knochen appliziert und mit einer resorbierbaren Membran abgedeckt. Nach einer individuellen Einheilphase kann nun in einem weiteren Schritt z. B. ein Implantat in die entsprechende Region inseriert werden. Sie haben weitere Fragen zu <a data-ziel="implantate" href="#/implantate">Implantaten</a>? Schauen Sie gerne bei uns in der Praxis vorbei, unsere ZahnärztInnen beraten Sie gerne.</p>'),
    ],
    faq=[
        ('Tut eine Zahnentfernung weh?', 'In der Zahnarztpraxis Dr. Ofner-Martin wird der betroffene Bereich vor einer Extraktion betäubt, sodass die Zahnentfernung schmerzfrei erfolgt. Auf Wunsch kann zusätzlich eine leichte Sedierung mit Lachgas den Eingriff erleichtern.'),
        ('Was ist eine Wurzelspitzenresektion?', 'Bei einer Wurzelspitzenresektion wird die Wurzelspitze eines Zahnes unter Betäubung gekappt und anschließend mit einem speziellen Zement verschlossen. Die Praxis Dr. Ofner-Martin setzt diesen Eingriff ein, um einen Zahn zu erhalten.'),
        ('Wann ist ein Knochenaufbau nötig?', 'Ein Knochenaufbau (Augmentation) kann vor dem Einsetzen eines Implantats notwendig sein, wenn der Kieferknochen stark abgebaut ist. Dabei wird Knochenersatzmaterial minimalinvasiv aufgebracht und mit einer resorbierbaren Membran abgedeckt. Nach der Einheilphase kann das Implantat gesetzt werden.'),
        ('Wer führt zahnärztliche Chirurgie in Karlsdorf-Neuthard durch?', f'Die {PRAXIS} in der {ADRESSE_TEXT}. Zahnärztin Katharina Gärtner hat seit November 2018 den Tätigkeitsschwerpunkt Zahnärztliche Chirurgie. Termine unter {TEL}.'),
    ],
)

L['implantate'] = dict(
    titel='Zahnimplantate in Karlsdorf-Neuthard | Dr. Ofner-Martin',
    besch='Zahnimplantate und Implantologie in Karlsdorf-Neuthard: hochwertiger Zahnersatz aus gut verträglichem Titan ersetzt Ihre Zahnwurzel.',
    obenzeile='Langfristig stabiler Zahnersatz',
    h1='Zahnimplantate in Karlsdorf-Neuthard',
    bild='/media/yootheme/cache/de/zahnimplantate-bruchsal-karlsdorf-neuthard-de15c975.jpg', bw=1920, bh=820,
    bildalt='Zahnimplantate in der Zahnarztpraxis Dr. Ofner-Martin in Karlsdorf-Neuthard',
    neu='zahnimplantate-implantologie-karlsdorf-neuthard',
    video=('NfTi9toP9a8', 'Informationsvideo zu Zahnimplantaten'),
    abschnitte=[
        ('Zahnersatz durch Zahnimplantate', '<p>Die Implantologie in Karlsdorf-Neuthard: Ein Zahnimplantat ist eine kleine Schraube aus (vom Körper gut verträglichem) Titan, Roxolid® (Titan-Zirkonium-Legierung) oder Zirkondioxidkeramik, die in den Kieferknochen eingebracht wird. Das Implantat übernimmt die Funktion der fehlenden Zahnwurzel und bildet ein stabiles Fundament für den Ersatzzahn. Je nach individueller Mundsituation können ein bis mehrere Implantate eingesetzt werden, auch als Sofortimplantate. Das Zahnimplantat wird bei der Implantologie in unserer Zahnarztpraxis in Karlsdorf-Neuthard ambulant und unter örtlicher Betäubung in den Kieferknochen eingebracht und bildet dadurch eine solide Basis für die langfristige und stabile Verankerung des Zahnersatzes.</p>[[VIDEO]]'),
        ('Vorteile Zahnimplantate', '<div class="vorteile"><div class="block"><h3>Gesunde Zähne bleiben erhalten</h3><p>Im Vergleich zu konventionellen Brücken müssen bei Implantaten die natürlichen, gesunden Nachbarzähne nicht zu einem Stumpf beschliffen werden, um die neuen Zähne zu tragen. Gesunde Zahnsubstanz, die bei konventionellen Verfahren beschädigt werden muss, bleibt so erhalten.</p></div><div class="block"><h3>Effektiver Schutz vor Knochenverlust</h3><p>Wie natürliche Zahnwurzeln leiten Implantate die Kaukräfte gleichmäßig in den Kieferknochen. Dieser wird dadurch, ähnlich wie bei natürlichen Zähnen, beim Kauen belastet. Diese Belastung ist notwendig, um den Knochen zu erhalten. Eine konventionelle Lösung hingegen führt fast immer zu Knochenverlust. Negative Folgen des Knochenverlustes sind Einschränkungen in Funktion und Aussehen.</p></div><div class="block"><h3>Sicherer Halt</h3><p>Der sichere Halt der „Dritten“ ist ein weiterer Vorteil der Zahnimplantate. Die Nachteile herkömmlicher Prothesen, wie zum Beispiel schmerzhafte Druckstellen und mangelnder Halt, werden Ihnen erspart. Bei vollständig zahnlosem Kiefer führt die Versorgung mit Implantaten zu einer vollständigen Wiederherstellung der Kaufunktion und erhöht somit die Lebensqualität.</p></div></div>'),
        ('Verschiedene Einsatzmöglichkeiten', '<p>Bei einem fehlenden Einzelzahn bietet ein Implantat die ästhetisch hochwertigste Möglichkeit, die vorhandene Zahnlücke zu schließen. Fehlen mehrere Zähne, kann durch das Einbringen von zwei oder mehreren Implantaten ein herausnehmbarer Zahnersatz vermieden werden. Eine Verbesserung des Haltes bei Zahnlosigkeit kann mit einer Stegprothese (individuell gefräst oder konfektioniert), einer Prothese mit Locator / Novaloc oder einer Prothese mit Konus erzielt werden. Gern informieren wir Sie in einem ausführlichen Beratungsgespräch, welche der oben genannten Möglichkeiten für Sie die beste Lösung ist.</p>'),
    ],
    faq=[
        ('Was ist ein Zahnimplantat?', 'Ein Zahnimplantat ist eine kleine Schraube aus gut verträglichem Titan, Roxolid® (Titan-Zirkonium-Legierung) oder Zirkondioxidkeramik, die in den Kieferknochen eingebracht wird. Es übernimmt die Funktion der fehlenden Zahnwurzel und bildet in der Zahnarztpraxis Dr. Ofner-Martin das stabile Fundament für den Ersatzzahn.'),
        ('Wie wird ein Implantat eingesetzt?', 'In der Zahnarztpraxis Dr. Ofner-Martin wird das Zahnimplantat ambulant und unter örtlicher Betäubung in den Kieferknochen eingebracht. Je nach Mundsituation sind ein oder mehrere Implantate möglich, auch als Sofortimplantate.'),
        ('Welche Vorteile haben Implantate gegenüber einer Brücke?', 'Bei Implantaten müssen gesunde Nachbarzähne nicht beschliffen werden. Implantate leiten die Kaukräfte wie natürliche Zahnwurzeln in den Kiefer und schützen so vor Knochenverlust. Außerdem geben sie den „Dritten“ sicheren Halt ohne Druckstellen.'),
        ('Wer setzt Zahnimplantate in Karlsdorf-Neuthard?', f'Dr. med. dent. Christina Ofner-Martin hat seit 2004 den Tätigkeitsschwerpunkt Implantologie und ist Mitglied der DGI sowie seit 2013 des ITI (International Team for Implantology). Die Praxis liegt in der {ADRESSE_TEXT}, Telefon {TEL}.'),
    ],
)

L['schienentherapie'] = dict(
    titel='Schienentherapie in Karlsdorf-Neuthard | Dr. Ofner-Martin',
    besch='Zähneknirschen im Schlaf? Mit der Schienentherapie in Karlsdorf-Neuthard schützen Sie Ihre Zahnsubstanz vor Abnutzung und unterbrechen das Zähneknirschen.',
    obenzeile='Knirscherschienen',
    h1='Schienentherapie in Karlsdorf-Neuthard',
    bild='/media/yootheme/cache/d6/knirscherschiene-bruchsal-karlsdorf-neuthard-d6146ea6.jpg', bw=1920, bh=820,
    bildalt='Knirscherschiene aus der Zahnarztpraxis Dr. Ofner-Martin',
    neu='knirscherschiene-schienentherapie-karlsdorf-neuthard',
    abschnitte=[
        ('Aufbissschienen', '<p>Eine Aufbissschiene, oft auch Knirscherschiene genannt, dient der Behandlung von Erkrankungen des Kausystems (Myoarthropathie). Bei Kiefergelenksproblemen (CMD, craniomandibuläre Dysfunktion), Zähneknirschen oder Zungenpressen wird eine durchsichtige Kunststoffschiene individuell angefertigt, die in der Regel nachts getragen wird. Sie entlastet das Kiefergelenk bzw. schützt vor Abnutzung der Zahnsubstanz und unterbricht das Zähneknirschen.</p>'),
        ('Ursachen', '<p>Stress in Beruf, Schule oder Familie, aber auch andere Ängste und Sorgen verursachen das Zähneknirschen oder das Pressen der Zähne und der Zunge. Diese Ursachen lassen sich nicht immer beeinflussen. Mit einer exakten Schienentherapie jedoch kann der Teufelskreis der weiteren Symptomkette wie Muskelverspannungen, Spannungskopfschmerz, chronische Müdigkeit, Konzentrationsstörungen etc. unterbrochen werden.</p>'),
        ('Ziel der Schienentherapie', '<p>Ziel ist es, durch die Schienentherapie Über- und Fehlbelastungen der Zähne und Kiefergelenke zu beseitigen, um so die oben genannten Symptome zu vermeiden.</p>'),
    ],
    faq=[
        ('Wofür ist eine Knirscherschiene gut?', 'Eine Aufbissschiene, auch Knirscherschiene genannt, entlastet das Kiefergelenk, schützt die Zahnsubstanz vor Abnutzung und unterbricht das Zähneknirschen. Die Zahnarztpraxis Dr. Ofner-Martin fertigt sie individuell als durchsichtige Kunststoffschiene an, die in der Regel nachts getragen wird.'),
        ('Was sind typische Ursachen für Zähneknirschen?', 'Häufig verursachen Stress in Beruf, Schule oder Familie sowie Ängste und Sorgen das Zähneknirschen oder Pressen. Folgen können Muskelverspannungen, Spannungskopfschmerz, chronische Müdigkeit und Konzentrationsstörungen sein. Eine exakte Schienentherapie kann diesen Kreislauf unterbrechen.'),
        ('Hilft eine Schiene bei CMD?', 'Ja, bei Kiefergelenksproblemen wie der craniomandibulären Dysfunktion (CMD) setzt die Praxis Dr. Ofner-Martin Aufbissschienen ein. Ziel ist es, Über- und Fehlbelastungen der Zähne und Kiefergelenke zu beseitigen.'),
        ('Wo bekomme ich eine Knirscherschiene in Karlsdorf-Neuthard?', KONTAKT_FAQ[1]),
    ],
)

L['highlights'] = dict(
    titel='Behandlungs-Highlights in Karlsdorf-Neuthard | Dr. Ofner-Martin',
    besch='Lachgassedierung, Dentale Volumentomographie (DVT), Laserbehandlung, CEREC® 3D-System und Alignertherapie in Karlsdorf-Neuthard für Ihre Zähne.',
    obenzeile='Unsere Behandlungs-Highlights',
    h1='Behandlungs-Highlights in Karlsdorf-Neuthard',
    bild='/media/yootheme/cache/a8/highlights-bruchsal-karlsdorf-neuthard-a8b3134e.jpg', bw=1920, bh=820,
    bildalt='Moderne Behandlungstechnik in der Zahnarztpraxis Dr. Ofner-Martin',
    neu='cerec-lachgas-dvt-aligner-karlsdorf-neuthard',
    video=('XoSoamddnBk', 'Informationsvideo zum CEREC® 3D-System'),
    anker={'CEREC® 3D-System': 'cerec', 'Lachgassedierung': 'lachgas', 'Alignertherapie': 'aligner'},
    abschnitte=[
        ('Alignertherapie', '<p>Für kleinere, aber ästhetisch wichtige Zahnfehlstellungen gibt es die Möglichkeit einer sogenannten Alignertherapie. Bei diesem schonenden kieferorthopädischen Eingriff erhalten Sie mehrere durchsichtige Schienen, welche nach und nach Ihre Zahnfehlstellung korrigieren. Sie haben Interesse an einer Behandlung mit Alignern? Vereinbaren Sie gerne einen Termin bei uns in der Praxis, unsere ZahnärztInnen beraten Sie gerne.</p>'),
        ('CEREC® 3D-System', '<p>Ob Inlays, Teilkronen, Kronen und Brücken: Seit Neuestem bieten wir einen besonderen Service für unsere Patienten: Zahnersatz innerhalb weniger Stunden! Mittels CAD/CAM-Technik können wir nun ganz unkompliziert Inlays, Teilkronen, Kronen, Brücken etc. herstellen.</p><p>Mittels CEREC® bringen wir Medizin und digitale Technologien zusammen. Abdruckfreier Zahnersatz, ganz ohne Würgereiz: Durch moderne Intraoralscan- und CAD/CAM-Technik ist es uns möglich, Inlays, Teilkronen, Kronen und Brücken in nur einer einzigen Sitzung herstellen zu können.</p><p>Zunächst wird der Zahn wie gewohnt vorbehandelt. Doch anstatt dass nun der konventionelle Abdruck folgt, der für viele Patienten unangenehm ist, scannen wir mit einer speziellen Kamera alle Zähne ab, sodass am Computer ein dreidimensionales Modell von Ihrem Ober- und Unterkiefer entsteht.</p><p>Wir können die geplante Restauration nach Ihren Bedürfnissen gestalten und leiten den Datensatz an die Schleifeinheit weiter. Die Fräsmaschine verarbeitet die empfangenen Daten und schleift innerhalb weniger Minuten aus einem Keramikblock Ihren Zahnersatz (subtraktives Verfahren). Man kann nun die Restauration veredeln, indem man durch Effektfarben ein besonders natürliches Aussehen erzeugt.</p><p>Es wird ein metallfreier Werkstoff, z. B. Keramik, verwendet. Dieser ist sehr gut verträglich, stabil und erfüllt höchste ästhetische Ansprüche. Des Weiteren wird das Herstellen und Tragen eines Provisoriums überflüssig. Ein weiterer Vorteil ist, dass mit CEREC ein abdruckfreier Zahnersatz möglich ist, was besonders für Angstpatienten und Personen mit Würgereiz interessant ist.</p><p>Künftig müssen Sie weniger Zeit beim Zahnarzt einplanen, da wir nur eine einzige Sitzung benötigen, um Ihre Zähne zu versorgen. Dies erleichtert vor allem viel beschäftigten Patienten, den Zahnarztbesuch in den Terminkalender zu integrieren. Kurzum: Der Weg zum neuen Zahnersatz war noch nie so einfach wie jetzt!</p><p>Übrigens: Wussten Sie, dass es auch bei umfassenderen zahnärztlichen Arbeiten (z. B. bei größeren Brücken) möglich ist, auf einen herkömmlichen Abdruck zu verzichten? Wir haben mit der neuesten CEREC-Generation die Möglichkeit, den digitalen Abdruck an den Zahntechniker zu übermitteln. Mithilfe dieses Datensatzes kann dann extern der gewünschte Zahnersatz gefertigt werden.</p>[[VIDEO]]'),
        ('Lachgassedierung', '<p>Haben Sie Angst vor dem Zahnarzt? Gerne können Sie sich bei uns mit Lachgas sedieren lassen. Unsere Praxisräumlichkeiten sowie unser Personal sind bestens mit entsprechenden Gerätschaften ausgestattet. Bei der Lachgassedierung handelt es sich um ein Verfahren, welches beispielsweise in den USA fast standardmäßig bei zahnärztlichen Behandlungen angewandt wird. Lachgas sorgt dafür, dass Sie entspannt und auch würgefrei bei uns behandelt werden können. Gleichzeitig sind Sie jedoch voll bei Bewusstsein und jederzeit ansprechbar.</p>'),
        ('Dentale Volumentomographie (DVT)', '<p>Präzise Bildgebung für präzise Behandlung. In der Zahnmedizin hat sich die dentale Volumentomographie (DVT) zu einem unverzichtbaren Werkzeug entwickelt, um präzise Diagnosen zu stellen und Behandlungen zu planen.</p><p>Dieses hochmoderne Gerät bietet Patienten und Zahnärzten eine Vielzahl von Vorteilen, die über die herkömmliche Röntgenaufnahme hinausgehen. Die DVT-Technologie ermöglicht eine dreidimensionale Darstellung der Mundhöhle, der Kiefer und der umliegenden Strukturen mit einer deutlich höheren Detailgenauigkeit als herkömmliche Röntgenaufnahmen. Für Patienten bedeutet die Verwendung eines dentalen Volumentomographie-Geräts eine deutlich geringere Strahlenbelastung im Vergleich zu herkömmlichen CT-Scans, da die Aufnahme gezielt auf den Bereich des Mundes und der Kiefer beschränkt ist. Die hochauflösenden Bilder, die durch die DVT-Technologie erzeugt werden, ermöglichen es Zahnärzten, Behandlungen individuell zu planen und anzupassen. Zum Beispiel können Implantate präzise an die anatomischen Gegebenheiten des Patienten angepasst werden. Auch komplexe zahnärztliche Eingriffe wie Wurzelkanalbehandlungen oder Weisheitszahnextraktionen können dank der detaillierten 3D-Bilder effizienter und sicherer durchgeführt werden. Ein weiterer Vorteil des dentalen Volumentomographie-Geräts liegt in seiner Vielseitigkeit. Es kann für eine Vielzahl von zahnärztlichen Anwendungen eingesetzt werden, einschließlich der Diagnose von Parodontalerkrankungen, der Bewertung von Kiefergelenksstörungen und Zahnfehlstellungen.</p><p>Insgesamt bietet das dentale Volumentomographie-Gerät Patienten und Zahnärzten eine fortschrittliche Bildgebungslösung, die präzise Diagnosen ermöglicht, die Strahlenbelastung minimiert und eine individuelle Behandlungsplanung unterstützt. Mit seiner Fähigkeit, hochauflösende 3D-Bilder zu liefern, trägt es wesentlich zur Verbesserung der zahnärztlichen Versorgung und der Patientenerfahrung bei.</p>'),
        ('Laserbehandlung', '<p>Die photodynamische Therapie mittels HELBO®-Laser ist ein wichtiges Hilfsmittel bei der Beseitigung von bakteriellen Infektionen im Mundraum. Sie findet hauptsächlich im Anschluss an die Parodontitistherapie statt.</p><h3>Vorteile</h3><ul><li>Eine Parodontitistherapie mit HELBO®-Laser ist effektiver in der Keimreduktion als ohne.</li><li>Bereiche, die desinfizierende Mundspüllösungen nicht erreichen, werden durch den HELBO®-Laser abgedeckt.</li><li>Die Behandlung ist schmerzfrei, fördert die Wundheilung und lindert vorher vorhandene Schmerzen.</li><li>Auf Antibiotika oder chirurgische Eingriffe kann in den meisten Fällen verzichtet werden.</li></ul><h3>Ablauf</h3><ul><li>Einen positiven Effekt der Laserbehandlung setzt eine vorangegangene professionelle Zahnreinigung oder Parodontitis-Behandlung voraus.</li><li>Eine Farbstofflösung wird in die Zahnfleischtasche eingebracht.</li><li>Die überschüssige Farbstofflösung wird ausgespült.</li><li>Die Zahnfleischtasche wird mit sanftem Laser belichtet, wobei das eintreffende Licht mit der Farbstofflösung reagiert. Der entstehende aktive Sauerstoff zerstört die Bakterien.</li></ul><h3>Weitere Einsatzmöglichkeiten des HELBO®-Lasers</h3><ul><li>Periimplantitisbehandlung</li><li>Desinfektion im chirurgischen Bereich</li><li>Aphten</li><li>Herpes</li></ul>'),
    ],
    faq=[
        ('Kann Zahnersatz in einer einzigen Sitzung entstehen?', 'Ja. Mit dem CEREC® 3D-System stellt die Zahnarztpraxis Dr. Ofner-Martin Inlays, Teilkronen, Kronen und Brücken in nur einer Sitzung her. Statt eines Abdrucks werden die Zähne mit einer speziellen Kamera gescannt, eine Fräsmaschine schleift den Zahnersatz dann in wenigen Minuten aus einem Keramikblock. Ein Provisorium ist nicht nötig.'),
        ('Bin ich nach einer Lachgasbehandlung fahrtüchtig?', 'Laut Zahnarztpraxis Dr. Ofner-Martin besteht ein Vorteil der Lachgassedierung für Erwachsene darin, dass sie nach der Behandlung wieder fahrtüchtig sind. Während der Behandlung bleiben Sie voll bei Bewusstsein und jederzeit ansprechbar.'),
        ('Welche Vorteile hat die DVT gegenüber einem CT?', 'Die dentale Volumentomographie liefert dreidimensionale Bilder von Mundhöhle und Kiefer mit hoher Detailgenauigkeit und einer deutlich geringeren Strahlenbelastung als herkömmliche CT-Scans, weil die Aufnahme gezielt auf Mund und Kiefer beschränkt ist. Die Praxis Dr. Ofner-Martin nutzt sie unter anderem zur präzisen Planung von Implantaten.'),
        ('Gibt es in Karlsdorf-Neuthard eine unsichtbare Zahnspange?', f'Ja. Die {PRAXIS} bietet für kleinere, ästhetisch wichtige Zahnfehlstellungen die Alignertherapie mit durchsichtigen Schienen an. Die Praxis liegt in der {ADRESSE_TEXT}, Terminvereinbarung unter {TEL}.'),
    ],
)
