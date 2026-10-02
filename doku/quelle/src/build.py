# -*- coding: utf-8 -*-
"""Baut dr-ofner-martin-vorschau.html als eine einzige Datei.
Aufruf: python3 build.py  (im Ordner src)"""
import base64, json, html, re, pathlib
from inhalt import *

HIER = pathlib.Path(__file__).parent
REF = HIER.parent / 'ref'
FONTS = HIER.parent / 'fonts'
AUS = HIER.parent / 'dr-ofner-martin-vorschau.html'

def e(s):
    return html.escape(s, quote=True)

def b64(p):
    return base64.b64encode(pathlib.Path(p).read_bytes()).decode()

LOGO = (HIER.parent / 'logo.svg').read_text().strip()

def logo(titel=True):
    svg = LOGO.replace('<svg ', '<svg role="img" aria-labelledby="logo-t" ' if titel else '<svg aria-hidden="true" focusable="false" ', 1)
    if titel:
        svg = svg.replace('>', '><title id="logo-t">' + e(PRAXIS) + '</title>', 1)
    return svg

# Logo-Symbol (Praxisgebäude) für Favicon
ICON_PFADE = re.search(r'<g fill="rgb\(255,102,0\)">(.*?)</g>', LOGO).group(1)
FAVICON_SVG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="-12 -6 128 150"><rect x="-12" y="-6" width="128" height="150" rx="22" fill="#fff"/>'
               '<g fill="#ff6600" fill-rule="evenodd">' + ICON_PFADE + '</g></svg>')

# ---------------------------------------------------------------- Symbole
def sym(name):
    P = {
        'tel': '<path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z" fill="currentColor"/>',
        'mail': '<path d="M3 5h18a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zm1.4 2 7.6 5.4L19.6 7" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
        'kal': '<rect x="3" y="5" width="18" height="16" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 10h18M8 3v4M16 3v4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
        'ort': '<path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="10" r="2.6" fill="currentColor"/>',
        'uhr': '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 7v5l3 2" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
        'info': '<circle cx="12" cy="12" r="9.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 11v6M12 7.2v.1" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>',
        'doc': '<path d="M6 2h8l5 5v14a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1z M14 2v5h5M8 13h8M8 17h6" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
        'haken': '<path d="m5 12.5 4.2 4.2L19 7" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>',
        'burger': '<path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
        'play': '<circle cx="12" cy="12" r="11" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 8.2v7.6l6-3.8z" fill="currentColor"/>',
        'karte': '<path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2-6-2zM9 4v14M15 6v14" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>',
        'zahn': '<path d="M7.5 3C5 3 3.5 5 3.5 7.6c0 2.6 1 4.2 1.6 6.4.6 2.4.8 6.9 2.6 6.9 1.6 0 1.6-4.4 2.4-5.8.4-.7.9-1 1.9-1s1.5.3 1.9 1c.8 1.4.8 5.8 2.4 5.8 1.8 0 2-4.5 2.6-6.9.6-2.2 1.6-3.8 1.6-6.4C20.5 5 19 3 16.5 3c-1.9 0-2.9 1-4.5 1S9.4 3 7.5 3z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>',
        'stern': '<path d="m12 2.8 2.8 5.8 6.3.9-4.6 4.4 1.1 6.3L12 17.2l-5.6 3 1.1-6.3L2.9 9.5l6.3-.9z" fill="currentColor"/>',
        'insta': '<rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.3" cy="6.7" r="1.2" fill="currentColor"/>',
    }
    return '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">' + P[name] + '</svg>'

GOOGLE_G = ('<svg class="vertrauen__g" viewBox="0 0 48 48" aria-hidden="true" focusable="false"><path fill="#EA4335" d="M24 9.5c3.5 0 6.6 1.2 9 3.5l6.7-6.7C35.6 2.5 30.2 0 24 0 14.6 0 6.6 5.4 2.7 13.3l7.8 6C12.4 13.6 17.7 9.5 24 9.5z"/>'
            '<path fill="#4285F4" d="M46.1 24.5c0-1.6-.1-3.1-.4-4.5H24v9h12.4c-.5 2.9-2.2 5.3-4.6 6.9l7.5 5.8c4.4-4.1 6.8-10.1 6.8-17.2z"/>'
            '<path fill="#FBBC05" d="M10.5 28.7c-.5-1.4-.8-3-.8-4.7s.3-3.2.8-4.7l-7.8-6C1 16.6 0 20.2 0 24s1 7.4 2.7 10.7l7.8-6z"/>'
            '<path fill="#34A853" d="M24 48c6.5 0 11.9-2.1 15.8-5.8l-7.5-5.8c-2.1 1.4-4.9 2.3-8.3 2.3-6.3 0-11.6-4.1-13.5-9.8l-7.8 6C6.6 42.6 14.6 48 24 48z"/></svg>')

def sterne():
    return '<span class="sterne" aria-hidden="true">' + sym('stern') * 5 + '</span>'


# Alt-Texte und neue Dateinamen nach Sichtprüfung der echten Fotos (30.09.2026).
# Schlüssel: eindeutiger Teil der alten Bildadresse.
BILDER = {
    'praxis-ofner-martin-gruppe-dres': ('Die Zahnärztinnen Dr. Lena Berger, Dr. Christina Ofner-Martin und Katharina Gärtner in der Zahnarztpraxis in Karlsdorf-Neuthard', 'zahnaerztinnen-dr-ofner-martin-dr-berger-gaertner-karlsdorf-neuthard'),
    'schoene-zaehne-bruchsal-home-1': ('Heller Empfangsbereich mit weißer Empfangstheke in der Zahnarztpraxis Dr. Ofner-Martin', 'empfang-zahnarztpraxis-dr-ofner-martin-karlsdorf-neuthard'),
    'kinder-zahnarzt-bruchsal-karlsdorf-42ee42a8': ('Zwei Kinder putzen sich lachend die Zähne', 'kinderzahnheilkunde-zaehneputzen-karlsdorf-neuthard'),
    'schoene-zaehne-bruchsal-karlsdorf-neuthard-ed5e5912': ('Lächelnde junge Frau mit schönen, geraden Zähnen', 'zahnaesthetik-schoene-zaehne-karlsdorf-neuthard'),
    'zahnvorsorge-bruchsal-a83c1c82': ('Lachender Mann mit Brille und gepflegten Zähnen', 'prophylaxe-zahnvorsorge-karlsdorf-neuthard'),
    'zahnimplantate-bruchsal-karlsdorf-neuthard-20b4db0c': ('Ältere Frau beißt kraftvoll in einen grünen Apfel', 'zahnimplantate-fester-biss-karlsdorf-neuthard'),
    'aligner-9bbd1f7f': ('Durchsichtige Aligner-Schiene wird auf die Zähne gesetzt', 'aligner-unsichtbare-zahnspange-karlsdorf-neuthard'),
    'cerec-b1df636d': ('Dr. Christina Ofner-Martin zeigt einer Patientin den digitalen 3D-Scan am Bildschirm', 'cerec-3d-scan-dr-ofner-martin-karlsdorf-neuthard'),
    'lachgas-c6edab30': ('Patientin mit Nasenmaske entspannt während einer Lachgasbehandlung', 'lachgassedierung-zahnarzt-karlsdorf-neuthard'),
    'stellenangebote-zam-zfa-bruchsal': ('Zahnärztliches Team in weißer Kleidung legt die Hände zusammen, von unten fotografiert', 'stellenangebote-zfa-zahnarztpraxis-karlsdorf-neuthard'),
    'Screenshot%202025-07-11': ('Grafik „Werden Sie rauchfrei!“ mit einem lächelnden Zahn', 'rauchfrei-mundgesundheit-flyer-dkfz-bzaek'),
    '20250707_105909-COLLAGE': ('Collage vom Praxisausflug nach Mallorca: Kolleginnen mit Praxisshirt, Fortbildung im Konferenzraum, Hotelpool mit Palmen und eine Sandburg', 'praxisausflug-mallorca-2025-team-dr-ofner-martin'),
    'schmerz-frau-d50c2af0': ('Eine junge Frau liegt, leicht gekrümmt vor Schmerzen, auf einer Decke und hält ein großes Kissen fest im Arm', 'studie-mundgesundheit-schmerzen-frauen'),
    'zahnarztpraxis-karlsdorf-neuthard-dr-ofner-martin-0e95cc19': ('Wartebereich mit orangefarbener Sitzbank und moderner Kunst in der Zahnarztpraxis Dr. Ofner-Martin', 'wartebereich-zahnarztpraxis-karlsdorf-neuthard'),
    'praxis-team-dc640df7': ('Das gesamte Praxisteam der Zahnarztpraxis Dr. Ofner-Martin hinter der Empfangstheke', 'praxisteam-zahnarztpraxis-dr-ofner-martin-karlsdorf-neuthard'),
    'zahnarzt-bruchsal-dr-christina-ofner-martin-1': ('Porträt von Zahnärztin und Praxisinhaberin Dr. med. dent. Christina Ofner-Martin', 'zahnaerztin-dr-christina-ofner-martin-karlsdorf-neuthard'),
    'kinderzahnarzt-bruchsal-katharina-plewniok': ('Porträt von Zahnärztin Katharina Gärtner', 'zahnaerztin-katharina-gaertner-kinderzahnheilkunde-karlsdorf-neuthard'),
    'zahnaerztin-dr-lena-berger': ('Porträt von Zahnärztin Dr. Lena Berger', 'zahnaerztin-dr-lena-berger-karlsdorf-neuthard'),
    'leistungen-zahnarzt-bruchsal-karlsdorf-neuthard': ('Flur der Zahnarztpraxis mit Wartestühlen und farbenfrohem Wandbild', 'flur-zahnarztpraxis-dr-ofner-martin-karlsdorf-neuthard'),
    'zahnvorsorge-bruchsal-karlsdorf-neuthard-dc9e4e07': ('Lachender Mann mit Brille und gepflegten Zähnen vor orangem Hintergrund', 'prophylaxe-professionelle-zahnreinigung-karlsdorf-neuthard'),
    'kinderzahnarzt-bruchsal-karlsdorf-neuthard-a0d23473': ('Mädchen und Junge beim Zähneputzen', 'kinderzahnarzt-karlsdorf-neuthard-zahnputzschule'),
    'schoene-zaehne-bruchsal-karlsdorf-neuthard-f8138249': ('Lächelnde Frau mit hellen, ebenmäßigen Zähnen vor orangem Hintergrund', 'zahnaesthetik-veneers-bleaching-karlsdorf-neuthard'),
    'zahn-fuellung-bruchsal-karlsdorf-neuthard': ('Fröhliche junge Frau mit gesunden Zähnen', 'zahnerhalt-fuellung-keramikinlay-karlsdorf-neuthard'),
    'zahnersatz-bruchsal-karlsdorf-neuthard': ('Älterer Patient betrachtet lächelnd seinen neuen Zahnersatz im Handspiegel', 'zahnersatz-kronen-bruecken-karlsdorf-neuthard'),
    'weisheitszahn-entfernen-bruchsal': ('Zahnröntgenfilm im Halter neben weiteren Röntgenaufnahmen', 'zahnaerztliche-chirurgie-roentgen-karlsdorf-neuthard'),
    'zahnimplantate-bruchsal-karlsdorf-neuthard-de15c975': ('Ältere Frau beißt in einen grünen Apfel', 'zahnimplantate-implantologie-karlsdorf-neuthard'),
    'knirscherschiene-bruchsal-karlsdorf-neuthard': ('Durchsichtige Kunststoffschiene wird auf die Zähne gesetzt', 'knirscherschiene-schienentherapie-karlsdorf-neuthard'),
    'highlights-bruchsal-karlsdorf-neuthard': ('Dr. Christina Ofner-Martin erklärt einem Patienten den digitalen Zahnscan', 'behandlungs-highlights-cerec-scan-karlsdorf-neuthard'),
    'aktuelles-blog-zahnarzt-bruchsal': ('Lächelnde Frau liest auf einem orangen Sitzsack Neuigkeiten auf dem Smartphone', 'aktuelles-zahnarztpraxis-karlsdorf-neuthard'),
    'young-woman-who-can-sleep': ('Ein Paar liegt im Bett. Die Frau hält sich mit verzerrtem Blick die Ohren zu, der Mann schläft und schnarcht im Hintergrund', 'schnarchschiene-protrusionsschiene-karlsdorf-neuthard'),
    'IMG-20250116-WA0008': ('Das Praxisteam sitzt bei der Weihnachtsfeier an einer langen, festlich gedeckten Tafel im Restaurant', 'weihnachtsfeier-team-zahnarztpraxis-dr-ofner-martin'),
    'Screenshot%202025-01-03': ('Das Praxisteam in orangen und dunklen Praxisshirts hinter der Empfangstheke zum 25. Praxisjubiläum', 'praxisjubilaeum-25-jahre-dr-ofner-martin'),
    'kontakt-zahnarztpraxis-karlsdorf-neuthard-bruchsal': ('Eingang der Praxis für Zahnmedizin in der Salinenstraße 8 in Karlsdorf-Neuthard mit Praxisschild', 'eingang-zahnarztpraxis-salinenstrasse-karlsdorf-neuthard'),
}
GALERIE = [
    ('Empfangstheke und heller Flur der Zahnarztpraxis', 'empfang'),
    ('Sitzecke mit Tisch hinter Glaswänden', 'beratungsecke'),
    ('Wartezimmer mit orangefarbener Bank und Spielecke für Kinder', 'wartezimmer-spielecke'),
    ('Flur mit Kunstwerken und Sitzbank', 'flur-kunst'),
    ('Digitales Volumentomographie-Gerät (DVT) für 3D-Röntgenaufnahmen', 'dvt-roentgen'),
    ('Flur mit Wartestühlen und großem Wandbild', 'flur-wartestuehle'),
    ('Eingang der Praxis in der Salinenstraße 8 mit Praxisschild', 'eingang-salinenstrasse'),
    ('CEREC-Schleifeinheit fräst Zahnersatz aus einem Keramikblock', 'cerec-schleifeinheit'),
    ('Dr. Christina Ofner-Martin zeigt einem Patienten den 3D-Scan seiner Zähne', 'dr-ofner-martin-3d-scan'),
    ('Lachgasgerät mit Nasenmasken in verschiedenen Größen', 'lachgas-geraet'),
    ('CEREC SpeedFire Brennofen für Keramik-Zahnersatz', 'cerec-speedfire'),
    ('Wartebereich mit orangefarbener Sitzbank und Bildschirm', 'wartebereich'),
]

# ---------------------------------------------------------------- Bilder
def bild(pfad, alt, w, h, neu, lazy=True, cls='', prio=False):
    """Bild von der bisherigen Website. Kommentar nennt den späteren Dateinamen."""
    url = pfad if pfad.startswith('http') else ALT + pfad
    for schluessel, (a2, n2) in BILDER.items():
        if schluessel in pfad:
            alt, neu = a2, n2
            break
    attr = ' loading="lazy" decoding="async"' if lazy else ' decoding="async"'
    if prio:
        attr += ' fetchpriority="high"'
    c = f' class="{cls}"' if cls else ''
    return (f'<!-- BILD-PLATZHALTER: vorlaeufig von der alten Seite. Neu als {neu}.webp + .jpg einsetzen -->'
            f'<img src="{e(url)}" alt="{e(alt)}" width="{w}" height="{h}"{attr}{c}>')

# ---------------------------------------------------------------- Bausteine
def aria_weiter(t):
    return ' aria-label="Weiterlesen: ' + e(t) + '"'

def link(ziel, text, anker=None, cls='', extra=''):
    h = f'#/{ziel}' + (f'/{anker}' if anker else '')
    c = f' class="{cls}"' if cls else ''
    return f'<a{c} data-ziel="{ziel}" href="{h}"{extra}>{text}</a>'

def knopf_tel(cls='knopf knopf--voll', text=None):
    return f'<a class="{cls}" href="{TEL_LINK}">{sym("tel")}{text or "Anrufen: " + TEL}</a>'

def knopf_termin(cls='knopf', text='Termin online buchen'):
    return f'<button type="button" class="{cls}" data-termin>{sym("kal")}{text}</button>'

def brotkrumen(kette):
    li = [f'<li>{link("start", "Startseite")}</li>']
    for i, (ziel, text) in enumerate(kette):
        if i == len(kette) - 1:
            li.append(f'<li aria-current="page">{e(text)}</li>')
        else:
            li.append(f'<li>{link(ziel, e(text))}</li>')
    return f'<nav class="brotkrumen" aria-label="Sie sind hier"><div class="huelle"><ol>{"".join(li)}</ol></div></nav>'

def nw(t):
    return t.replace('Karlsdorf-Neuthard', '<span class="nw">Karlsdorf-Neuthard</span>')

def seitenkopf(k, obenzeile, h1, p, bildpfad, alt, w, h, neu):
    return (f'<section class="seitenkopf" aria-labelledby="{k}--titel"><div class="seitenkopf__bild">{bild(bildpfad, alt, w, h, neu, lazy=False)}</div>'
            f'<div class="huelle"><p class="obenzeile">{e(obenzeile)}</p><h1 id="{k}--titel">{nw(e(h1))}</h1>{f"<p>{p}</p>" if p else ""}</div></section>')

def zeiten_tabelle(k):
    zeilen = [(1, 'Montag', '08:00–19:00 Uhr'), (2, 'Dienstag', '08:00–19:00 Uhr'), (3, 'Mittwoch', '08:00–19:00 Uhr'),
              (4, 'Donnerstag', '08:00–19:00 Uhr'), (5, 'Freitag', '08:30–14:00 Uhr'), (6, 'Samstag', 'geschlossen'), (0, 'Sonntag', 'geschlossen')]
    tr = ''.join(f'<tr data-wochentag="{t}"><th scope="row">{n}</th><td>{z}</td></tr>' for t, n, z in zeilen)
    return (f'<div class="zeiten" id="{k}--sprechzeiten"><h2 id="{k}--zeiten-titel">Unsere Sprechzeiten</h2>'
            f'<p class="status-zeile" data-offen-anzeige><span data-status-lang>Wir sind für Sie vor Ort.</span></p>'
            f'<table aria-labelledby="{k}--zeiten-titel"><tbody>{tr}</tbody></table>'
            f'<div class="knopfreihe">{knopf_termin("knopf knopf--voll", "Termine buchen")}{knopf_tel("knopf", "Anrufen")}</div>'
            f'<div class="hinweis">{sym("doc")}<p><a href="{ANAMNESE}" target="_blank" rel="noopener">Download Anamnesebogen (PDF)</a><br>Bringen Sie zu Ihrem ersten Besuch bei uns gerne den bereits ausgefüllten Anamnesebogen mit.</p></div>'
            f'<div class="hinweis">{sym("info")}<p>Informationen zum zahnärztlichen Notdienst erhalten Sie unter <a href="{NOTDIENST_LINK}">{NOTDIENST}</a>.</p></div></div>')

def empfehlung(k, hell=True):
    return (f'<section class="abschnitt{" abschnitt--hell" if hell else ""}" aria-labelledby="{k}--empfehlung"><div class="huelle"><div class="kopfzeile kopfzeile--mitte">'
            f'<p class="obenzeile">Weiterempfehlung</p><h2 id="{k}--empfehlung">Sind Sie mit uns zufrieden?</h2><div class="strich"></div>'
            f'<p>Wir möchten, dass Sie mit der Betreuung und Behandlung in unserer Praxis zufrieden sind. Mit einer Weiterempfehlung helfen Sie anderen Patienten, die aktuell auf der Suche nach einer Zahnärztin / einem Zahnarzt sind, sich ein Bild über uns machen zu können. Daher würden wir uns sehr freuen, wenn Sie uns bei mindestens einem der folgenden Empfehlungsportale weiterempfehlen würden:</p>'
            f'<div class="empfehlung" style="justify-content:center"><a class="knopf" href="{JAMEDA}" target="_blank" rel="noopener">Jameda<span class="nur-vorleser"> (öffnet in neuem Fenster)</span></a>'
            f'<a class="knopf knopf--voll" href="{GOOGLE_BEWERTEN}" target="_blank" rel="noopener">Google<span class="nur-vorleser"> (öffnet in neuem Fenster)</span></a></div></div></div></section>')

def band(k):
    return (f'<section class="band" aria-labelledby="{k}--band"><div class="huelle"><div><h2 id="{k}--band">Wir freuen uns auf Ihren Besuch</h2>'
            f'<p>Vereinbaren Sie jetzt Ihren Termin: persönlich, telefonisch oder per E-Mail. Ihre Zahnarzt-Praxis in Karlsdorf-Neuthard bei Bruchsal.</p></div>'
            f'<div class="knopfreihe" style="margin:0"><a class="knopf knopf--weiss" href="{TEL_LINK}">{sym("tel")}{TEL}</a>{knopf_termin("knopf", "Termin online buchen")}</div></div></section>')

def faq_block(k, faqs):
    items = ''.join(f'<details class="falt"><summary><h3>{e(q)}</h3></summary><div class="falt__inhalt"><p>{e(a)}</p></div></details>' for q, a in faqs)
    return (f'<section id="{k}--fragen" aria-labelledby="{k}--fragen-titel"><h2 id="{k}--fragen-titel">Häufige Fragen</h2>{items}'
            f'<p class="entwurfshinweis">Antworten aus den Praxistexten zusammengestellt, bitte fachlich freigeben.</p></section>')

def video(k, vid, titel):
    return (f'<div class="einbettung" data-einbettung="video" data-quelle="https://www.youtube-nocookie.com/embed/{vid}?rel=0" data-titel="{e(titel)}">'
            f'<div class="einbettung__platz">{sym("play")}<p><strong style="color:#fff">{e(titel)}</strong></p>'
            f'<p>Beim Abspielen wird das Video von YouTube (Google) im erweiterten Datenschutzmodus geladen. Dabei wird Ihre IP-Adresse an Google übertragen. Mehr dazu in der {link("datenschutz", "Datenschutzerklärung")}.</p>'
            f'<button type="button" class="knopf knopf--hell" data-laden>Video laden und abspielen</button></div></div>')

def karte_einbettung():
    q = 'https://www.google.com/maps?q=Praxis+f%C3%BCr+Zahnmedizin+Dr.+Ofner-Martin,+Salinenstra%C3%9Fe+8,+76689+Karlsdorf-Neuthard&output=embed'
    return (f'<div class="einbettung einbettung--karte" data-einbettung="karte" data-quelle="{e(q)}" data-titel="Anfahrt zur Zahnarztpraxis Dr. Ofner-Martin auf Google Maps">'
            f'<div class="einbettung__platz">{sym("karte")}<p><strong style="color:#fff">Salinenstraße 8, 76689 Karlsdorf-Neuthard</strong></p>'
            f'<p>Die Karte wird von Google Maps geladen. Dabei wird Ihre IP-Adresse an Google übertragen. Mehr dazu in der {link("datenschutz", "Datenschutzerklärung")}.</p>'
            f'<div class="knopfreihe" style="justify-content:center;margin-top:.4rem"><button type="button" class="knopf knopf--hell" data-laden>Karte laden</button>'
            f'<a class="knopf knopf--hell" href="{GOOGLE_PROFIL}" target="_blank" rel="noopener">In Google Maps öffnen<span class="nur-vorleser"> (neues Fenster)</span></a></div></div></div>')

def seite(k, titel, besch, inhalt, menue=None):
    m = f' data-menue="{menue}"' if menue else ''
    return f'<main class="seite" id="{k}" data-seite="{k}" data-titel="{e(titel)}" data-besch="{e(besch)}"{m} hidden>{inhalt}</main>'

# ================================================================ STARTSEITE
def s_start():
    k = 'start'
    kacheln = [
        ('kinderzahnheilkunde', 'Kinderzahnheilkunde', '/media/yootheme/cache/42/kinder-zahnarzt-bruchsal-karlsdorf-42ee42a8.jpg', 'Kinderzahnheilkunde in Karlsdorf-Neuthard', 'kinderzahnheilkunde-karlsdorf-neuthard',
         '<p>Mit großer Geduld schaffen wir eine angstfreie und kinderfreundliche Atmosphäre für unsere kleinen Patienten, damit Ihr Kind von Anfang an gerne zum Zahnarzt geht.</p><p>Wir beraten Eltern kompetent und ausführlich, welche Therapie die richtige für das Kind ist. Durch stetige Weiterbildung gewährleisten wir die beste zahnmedizinische Versorgung Ihrer Kinder.</p>', 'Kinderzahnheilkunde in Karlsdorf-Neuthard'),
        ('aesthetik', 'Ästhetik', '/media/yootheme/cache/ed/schoene-zaehne-bruchsal-karlsdorf-neuthard-ed5e5912.jpg', 'Zahnästhetik in Karlsdorf-Neuthard', 'zahnaesthetik-veneers-karlsdorf-neuthard',
         '<p>Sie leiden unter Ihren schiefen Zähnen? Mit Veneers, das sind hauchdünne Verschalungen aus Keramik, verhelfen wir Ihnen zu ästhetisch schönen Zähnen. Gerne beraten wir Sie über die Korrektur von Zahnfehlstellungen, z. B. wenn Ihre Frontzähne davon betroffen sind (auch bei Zahnlücken).</p>', 'Ästhetisch schöne Zähne in Karlsdorf-Neuthard'),
        ('prophylaxe', 'Prophylaxe', '/media/yootheme/cache/a8/zahnvorsorge-bruchsal-a83c1c82.jpg', 'Zahnvorsorge in Karlsdorf-Neuthard', 'zahnvorsorge-prophylaxe-karlsdorf-neuthard',
         '<p>Unsere Mundhöhle ist Lebensraum für eine Vielzahl von Bakterien, die sich auf der Zahnoberfläche festsetzen und sich dort vermehren. Hier bilden sie zusammen mit Speiseresten, Zucker u. a. einen klebrigen Zahnbelag: die Plaque, Hauptursache von Zahnfleischentzündungen. Mit regelmäßiger Zahnvorsorge (Prophylaxe) können Sie vorbeugen.</p>', 'Prophylaxe in Karlsdorf-Neuthard'),
        ('implantate', 'Zahnimplantate', '/media/yootheme/cache/20/zahnimplantate-bruchsal-karlsdorf-neuthard-20b4db0c.jpg', 'Zahnimplantate in Karlsdorf-Neuthard', 'zahnimplantat-karlsdorf-neuthard',
         '<p>Ein Zahnimplantat ist eine kleine Schraube aus (vom Körper gut verträglichem) Titan, Roxolid® (Titan-Zirkonium-Legierung) oder Zirkondioxidkeramik, die in den Kieferknochen eingebracht wird. Das Implantat übernimmt die Funktion der fehlenden Zahnwurzel und bildet ein stabiles Fundament für den Ersatzzahn. Je nach individueller Mundsituation können ein bis mehrere Implantate eingesetzt werden, auch als Sofortimplantate.</p>', 'Zahnimplantate in Karlsdorf-Neuthard'),
    ]
    karten = ''.join(
        f'<article class="karte"><div class="karte__bild">{bild(p, alt, 720, 500, neu)}</div><div class="karte__text"><h3>{t}</h3>{txt}'
        f'{link(z, e(lt), cls="mehr")}</div></article>' for z, t, p, alt, neu, txt, lt in kacheln)
    hl = [
        ('aligner', 'Unsichtbare Zahnschienen', '/media/yootheme/cache/9b/aligner-9bbd1f7f.jpg', 'Unsichtbare Zahnspange für unauffällige Zahnkorrektur mit Alignern', 'aligner-unsichtbare-zahnspange-karlsdorf-neuthard',
         'Haben sich Ihre Zähne verschoben und sind nun nicht mehr gerade? Sie wollten schon immer harmonisch ausgeformte Zahnbögen? Mit der sogenannten Aligner-Behandlung können wir Ihnen helfen, Ihre Zähne zu korrigieren. Und das Beste daran: Niemand wird die unsichtbare Zahnspange bemerken.'),
        ('cerec', 'CEREC® 3D-System', '/media/yootheme/cache/b1/cerec-b1df636d.jpg', 'CEREC® 3D-System für abdruckfreien Zahnersatz', 'cerec-zahnersatz-eine-sitzung-karlsdorf-neuthard',
         'Schneller Zahnersatz in nur einer Sitzung ist bei uns dank des CEREC® 3D-Systems möglich, wie auch die Herstellung von Zahnersatz ohne Abdruck und damit ganz ohne Würgereiz, den Abdrücke bei Patienten manchmal verursachen. Profitieren auch Sie vom Einsatz modernster Technologie in unserer Zahnarzt-Praxis in Karlsdorf-Neuthard nahe Bruchsal.'),
        ('lachgas', 'Lachgas', '/media/yootheme/cache/c6/lachgas-c6edab30.jpg', 'Behandlung mit Lachgas in Karlsdorf-Neuthard', 'lachgas-zahnarzt-angstpatienten-karlsdorf-neuthard',
         'Entspannt und angstfrei beim Zahnarzt? Mit Lachgas wird der Zahnarztbesuch auch für ängstliche Patientinnen und Patienten zu einer positiven Erfahrung. Lachgas ist sowohl für Kinder als auch Erwachsene geeignet. Für Erwachsene besteht ein Vorteil der Sedierung mit Lachgas darin, dass sie nach der Behandlung wieder fahrtüchtig sind. Gerne beraten wir Sie vor Ihrer ersten Behandlung bei uns ausführlich zu diesem Thema.'),
    ]
    hlk = ''.join(f'<article class="karte"><div class="karte__bild">{bild(p, alt, 720, 500, neu)}</div><div class="karte__text"><h3>{t}</h3><p>{txt}</p>{link("highlights", "Mehr erfahren", anker=a, cls="mehr")}</div></article>' for a, t, p, alt, neu, txt in hl)
    stellen = ''.join(f'<li>{sym("haken")}<span>{e(s)}</span></li>' for s in STELLEN)
    news = [
        ('rauchfrei', 'Rauchfrei für Ihre Mundgesundheit', '11. Juli 2025', '/media/yootheme/cache/2f/Screenshot%202025-07-11%20140844-2fc6545d.png', 'Titelseite des Flyers zum Rauchstopp von Deutschem Krebsforschungszentrum und Bundeszahnärztekammer', 'rauchfrei-mundgesundheit-flyer',
         'Das Deutsche Krebsforschungszentrum und die Bundeszahnärztekammer haben einen neuen Flyer veröffentlicht, der die Risiken des Rauchens für die Mundgesundheit aufzeigt.'),
        ('mallorca', 'Hallo Mallorca: Praxisausflug 2025', '07. Juli 2025', '/media/yootheme/cache/e3/20250707_105909-COLLAGE-e312977b.jpg', 'Collage vom Praxisausflug nach Mallorca: Sonnenaufgang hinter Palmen, Hotelpool, Hauseingang, Sandburg und Kolleginnen mit Praxisshirt', 'praxisausflug-mallorca-2025-team',
         'Anlässlich des 25. Praxisjubiläums hat sich unsere Chefin etwas ganz Besonderes für uns überlegt: einen Fortbildungsurlaub nach Mallorca für das ganze Team!'),
        ('studie', 'Neue Studie über die Zusammenhänge von Mundgesundheit und Schmerzen', '24. April 2025', '/media/yootheme/cache/d5/schmerz-frau-d50c2af0.jpg', 'Eine junge Frau liegt, leicht gekrümmt vor Schmerzen, auf einer Decke und hält ein großes Kissen fest im Arm', 'studie-mundgesundheit-schmerzen-frauen',
         'Mundgesundheit und Schmerz: Neue Studie zeigt überraschende Zusammenhänge bei Frauen. Eine neue Studie der Universität Sydney hat einen deutlichen Zusammenhang zwischen schlechter Mundgesundheit und verschiedenen Schmerzzuständen bei Frauen aufgezeigt.'),
    ]
    newsk = ''.join(f'<article class="karte"><div class="karte__bild">{bild(p, alt, 400, 240, neu)}</div><div class="karte__text"><p class="karte__datum"><time>{d}</time></p><h3>{e(t)}</h3><p>{e(txt)}</p>{link("aktuelles", "Weiterlesen", anker=a, cls="mehr", extra=aria_weiter(t))}</div></article>' for a, t, d, p, alt, neu, txt in news)

    inhalt = f'''
<section class="hero" aria-labelledby="start--titel">
  <div class="hero__bild">{bild('/media/yootheme/cache/08/praxis-ofner-martin-gruppe-dres_dres-083e1bfa.jpg', 'Das Team der Zahnarztpraxis Dr. Ofner-Martin in Karlsdorf-Neuthard', 1920, 800, 'zahnarztpraxis-karlsdorf-neuthard-team-dr-ofner-martin', lazy=False, prio=True)}</div>
  <div class="huelle hero__inhalt"><div class="hero__karte hero__text">
    <div>
      <p class="obenzeile">Ihre Zahnarzt-Praxis in Karlsdorf-Neuthard</p>
      <h1 id="start--titel">Zahnarzt in <span class="nw">Karlsdorf-Neuthard</span><span>Dr. Christina Ofner-Martin &amp; Kollegen</span></h1>
      <p class="hero__claim">Implantologie, Ästhetische Zahnmedizin, Kinderzahnheilkunde und Prophylaxe in neuen, großzügig gestalteten und klimatisierten Räumen, nur wenige Minuten von Bruchsal.</p>
    </div>
    <div class="hero__rechts">
      <div class="knopfreihe">{knopf_tel()}{link('leistungen', 'Leistungen ansehen', cls='knopf')}</div>
      <div class="vertrauen">
        <!-- GOOGLE-BEWERTUNG: Stand 30.09.2026 ({GOOGLE_STERNE} Sterne, {GOOGLE_ANZAHL} Bewertungen). Vor Livegang und danach regelmäßig im Google-Profil prüfen. -->
        <a class="vertrauen__punkt" href="{GOOGLE_PROFIL}" target="_blank" rel="noopener">{GOOGLE_G}<span><span class="vertrauen__zahl">{GOOGLE_STERNE}</span> {sterne()}<span class="vertrauen__klein">{GOOGLE_ANZAHL} Google-Bewertungen<span class="nur-vorleser">: {GOOGLE_STERNE} von 5 Sternen, öffnet Google Maps in neuem Fenster</span></span></span></a>
        <div class="vertrauen__punkt"><img class="vertrauen__jubi" src="{ALT}/images/25jahrejubilaeum.svg" alt="" width="52" height="52" decoding="async"><span><span class="vertrauen__zahl">Seit {GRUENDUNG}</span><span class="vertrauen__klein">in eigener Praxis in Karlsdorf-Neuthard</span></span></div>
      </div>
    </div>
  </div></div>

</section>

<section class="abschnitt" aria-labelledby="start--willkommen"><div class="huelle zwei">
  <div>
    <p class="obenzeile">Dr. Christina Ofner-Martin &amp; Kollegen</p>
    <h2 id="start--willkommen">Willkommen in unserer Praxis</h2><div class="strich"></div>
    <p>Machen Sie sich hier einen ersten Eindruck von den neuen, großzügig gestalteten und klimatisierten Räumlichkeiten unserer Zahnarzt-Praxis in Karlsdorf-Neuthard sowie von unserem Praxisteam. Unser breitgefächertes Leistungsspektrum umfasst die Implantologie, die Ästhetische Zahnmedizin, Kinderzahnheilkunde, Prophylaxe (Zahnvorsorge) und vieles mehr. Um Sie immer nach modernsten zahnmedizinischen Standards zu behandeln, bilden wir uns kontinuierlich fort. Vereinbaren Sie jetzt Ihren Termin: persönlich, telefonisch oder per E-Mail. Auch eventuell vorhandene Ängste und Sorgen von Angstpatientinnen und -patienten nehmen wir ernst!</p>
    <p>Ob Sie direkt aus Karlsdorf-Neuthard kommen oder aus der näheren Region und einen Zahnarzt in der Nähe von Bruchsal suchen: Wir sind gerne für Sie da! Die Anfahrt zum Zahnarzt aus Bruchsal dauert nur wenige Minuten. Parkplätze sind in ausreichender Anzahl direkt an unserer Praxis vorhanden.</p>
    <p><em>Ihre Zahnärztinnen Dr. Christina Ofner-Martin &amp; Kolleginnen</em></p>
    <div class="knopfreihe">{link('team', 'Unser Team', cls='knopf')}{link('praxis', 'Unsere Praxis', cls='mehr')}</div>
  </div>
  <div class="zwei__bild">{bild('/images/home/schoene-zaehne-bruchsal-home-1.jpg', 'Lächelnde Patientin mit schönen Zähnen, Zahnarztpraxis nahe Bruchsal', 959, 613, 'schoene-zaehne-zahnarzt-bruchsal-karlsdorf')}</div>
</div></section>

<section class="abschnitt abschnitt--hell" aria-label="Sprechzeiten"><div class="huelle zwei zwei--gleich">
  <div><p class="obenzeile">Wir sind für Sie vor Ort</p><h2>So erreichen Sie uns</h2><div class="strich"></div>
    <p class="vorspann">{PRAXIS}<br>{ADRESSE_TEXT}</p>
    <p>Telefon: <a href="{TEL_LINK}">{TEL}</a><br>E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>
    <p>Kostenfreie Parkplätze direkt vor der Praxis. Aus Bruchsal sind Sie in wenigen Minuten bei uns.</p>
    <div class="knopfreihe">{link('kontakt', 'Kontakt &amp; Anfahrt', cls='knopf')}</div></div>
  {zeiten_tabelle(k)}
</div></section>

<section class="abschnitt" aria-labelledby="start--leistungen"><div class="huelle">
  <div class="kopfzeile"><p class="obenzeile">Schöne und gesunde Zähne</p><h2 id="start--leistungen">Unsere Leistungen</h2><div class="strich"></div></div>
  <div class="raster raster--4">{karten}</div>
  <div class="knopfreihe">{link('leistungen', 'Weitere Leistungen', cls='knopf knopf--voll')}</div>
</div></section>

<section class="abschnitt abschnitt--hell" aria-labelledby="start--highlights"><div class="huelle">
  <div class="kopfzeile"><p class="obenzeile">Unserer Zahnarzt-Praxis nahe Bruchsal</p><h2 id="start--highlights">Behandlungs-Highlights</h2><div class="strich"></div></div>
  <div class="raster raster--3">{hlk}</div>
  <div class="knopfreihe">{link('highlights', 'Alle Behandlungs-Highlights', cls='knopf')}</div>
</div></section>


{empfehlung(k, hell=False)}

<section class="abschnitt abschnitt--hell" aria-labelledby="start--aktuelles"><div class="huelle">
  <div class="kopfzeile"><p class="obenzeile">Aus unserer Praxis in Karlsdorf-Neuthard</p><h2 id="start--aktuelles">Aktuelles</h2><div class="strich"></div></div>
  <div class="raster raster--3">{newsk}</div>
  <div class="knopfreihe">{link('aktuelles', 'Alle Neuigkeiten', cls='knopf')}</div>
</div></section>
{band(k)}'''
    return seite(k, 'Zahnarzt-Praxis Karlsdorf-Neuthard | Dr. Ofner-Martin',
                 'Zahnarzt-Praxis in Karlsdorf-Neuthard bei Bruchsal von Dr. Christina Ofner-Martin & Kollegen. Ihre Zahnärztinnen für ganzheitliche Zahnmedizin.', inhalt)

# ================================================================ PRAXIS
def s_praxis():
    k = 'praxis'
    gal = ''.join(
        f'<button type="button" data-gross="{ALT}/images/impressionen/zahnarztpraxis-karlsdorf-neuthard-bruchsal-impressionen-{i:02d}.jpg" aria-label="Vergrößern: {e(GALERIE[i-1][0])}">'
        f'{bild(f"/images/impressionen/zahnarztpraxis-karlsdorf-neuthard-bruchsal-impressionen-{i:02d}.jpg", GALERIE[i-1][0], 1920, 1080, "zahnarztpraxis-karlsdorf-neuthard-" + GALERIE[i-1][1])}</button>'
        for i in range(1, 13))
    inhalt = f'''{brotkrumen([('praxis', 'Praxis')])}
{seitenkopf(k, 'Unsere Räume & Services', 'Zahnarztpraxis in Karlsdorf-Neuthard', 'Praxis für Zahnmedizin Dr. med. dent. Ofner-Martin &amp; Kollegen', '/media/yootheme/cache/dc/praxis-team-dc640df7.jpg', '', 1920, 800, '')}
<section class="abschnitt" aria-labelledby="praxis--anspruch"><div class="huelle zwei zwei--gleich">
  <div><h2 id="praxis--anspruch">Unser Anspruch</h2><div class="strich"></div>
  <p class="vorspann">Unser Anspruch ist es, dass Sie unsere Praxis mit einem Lächeln im Gesicht verlassen und gerne wieder zu uns kommen. Wir nehmen uns Zeit für Sie und hören Ihnen einfühlsam zu, damit wir Sie optimal betreuen und behandeln können und Sie sich im Anschluss über gesunde, schöne Zähne freuen können.</p>
  <h3>Individuelle Beratung im Vorfeld Ihrer Behandlung</h3>
  <p>Wir möchten Sie transparent und verständlich über die Behandlung aufklären und es ist uns auch wichtig, Ihre Wünsche und Ängste zu kennen. Natürlich sprechen wir bei Bedarf auch unter anderem über eventuelle Unverträglichkeiten, Behandlungsalternativen und ggf. über die Finanzierung von Zahnersatz.</p></div>
  <div class="block"><h2 style="font-size:1.6rem">Unsere Services auf einen Blick</h2>
  <p>Falls Sie mit dem Auto anreisen, stehen Ihnen direkt vor der Praxis ausreichend Gratis-Parkplätze zur Verfügung. Alle Behandlungsräume inklusive dem Wartezimmer sind klimatisiert, denn wir möchten, dass Sie sich zu jeder Jahreszeit bei uns wohlfühlen. Und da wir finden, dass sich unsere Patienten ein schönes Lächeln bzw. eventuell nötige aufwendige Behandlungen leisten können sollen, bieten wir Ihnen auch die Möglichkeit einer Ratenzahlung an: innerhalb von 6 oder 12 Monaten ohne Zinsen. Nutzen Sie auch unseren Recall-Service: Wir erinnern Sie auf Wunsch telefonisch und gratis an Ihre Termine und natürlich auch regelmäßig per Post an Ihre nächste Vorsorgeuntersuchung.</p>
  <ul class="stellen"><li>{sym('haken')}<span>Gratis-Parkplätze direkt vor der Praxis</span></li><li>{sym('haken')}<span>Klimatisierte Behandlungsräume und Wartezimmer</span></li><li>{sym('haken')}<span>Ratenzahlung in 6 oder 12 Monaten ohne Zinsen</span></li><li>{sym('haken')}<span>Recall-Service per Telefon und Post</span></li></ul></div>
</div></section>
<section class="abschnitt abschnitt--hell" aria-labelledby="praxis--galerie"><div class="huelle">
  <div class="kopfzeile"><p class="obenzeile">Impressionen</p><h2 id="praxis--galerie">Praxis für Zahnmedizin Dr. med. dent. Ofner-Martin &amp; Kollegen</h2><div class="strich"></div><p>Klicken Sie auf ein Bild, um es zu vergrößern.</p></div>
  <div class="galerie">{gal}</div>
</div></section>
<section class="abschnitt" aria-labelledby="praxis--rundgang"><div class="huelle zwei zwei--gleich">
  <div><p class="obenzeile">Ein virtueller Rundgang</p><h2 id="praxis--rundgang">Erkunden Sie unsere Praxis virtuell</h2><div class="strich"></div>
  <p>Schauen Sie sich schon vor Ihrem ersten Besuch in Ruhe in unseren Räumen um.</p>
  <!-- RUNDGANG: liegt bisher unter /drom-rundgang/ beim alten Anbieter. Dateien vor der Kündigung sichern und auf den neuen Webspace übernehmen. -->
  <div class="knopfreihe"><a class="knopf knopf--voll" href="{RUNDGANG}" target="_blank" rel="noopener">Rundgang starten<span class="nur-vorleser"> (öffnet in neuem Fenster)</span></a></div></div>
  {zeiten_tabelle(k)}
</div></section>
{empfehlung(k)}
{band(k)}'''
    return seite(k, 'Unsere Räume & Services | Zahnarztpraxis Dr. Ofner-Martin, Karlsdorf-Neuthard',
                 'In unserer Zahnarzt-Praxis in Karlsdorf-Neuthard bieten wir ganzheitliche Zahnheilkunde mit modernsten Techniken in klimatisierten Räumlichkeiten.', inhalt)

# ================================================================ TEAM
TEAM = [
    ('Dr. med. dent. Christina Ofner-Martin', 'Zahnärztin & Praxisinhaberin in Karlsdorf-Neuthard', '/images/team/zahnarzt-bruchsal-dr-christina-ofner-martin-1.jpg', 960, 780, 'zahnaerztin-dr-christina-ofner-martin-karlsdorf-neuthard',
     ['Studium der Zahnmedizin in Heidelberg (1985–1990)', '1990–1993 Vorbereitungsassistentin in Mannheim und Nussloch', '1993–2000 niedergelassene Zahnärztin in einer Gemeinschaftspraxis in Lampertheim', 'Seit 2000 niedergelassen in eigener Praxis in Karlsdorf-Neuthard', 'Seit 2004 Tätigkeitsschwerpunkt Implantologie'],
     ['Karlsruher Konferenz', 'Deutsche Gesellschaft für Implantologie (DGI)', 'Deutsche Gesellschaft für Ästhetische Zahnheilkunde (DGÄZ)', 'Deutsche Gesellschaft für Zahn-, Mund- und Kieferheilkunde (DGZMK)', 'Deutsche Gesellschaft für computergestützte Zahnheilkunde (DGCZ)', 'Seit Mai 2013 Mitglied ITI (International Team for Implantology)'],
     ['Tätigkeitsschwerpunkt Implantologie', 'Röntgen-Fachkunde für dentale Digitale Volumentomographie (DVT)', 'Implantatprothetik', 'Ästhetische Zahnheilkunde', 'Homöopathie', 'Endodontie', 'Parodontologie', 'CEREC® Masterkurs']),
    ('Zahnärztin Katharina Gärtner', 'Zahnärztin (auch für Kinder) in Karlsdorf-Neuthard', '/images/team/kinderzahnarzt-bruchsal-katharina-plewniok.jpg', 960, 780, 'zahnaerztin-katharina-gaertner-kinderzahnheilkunde-karlsdorf-neuthard',
     ['Studium der Zahnmedizin an der Universität Heidelberg (2009–2015)', '2016–2018 Vorbereitungsassistentin in Schwetzingen', 'Seit Februar 2018 angestellte Zahnärztin in der Praxis Dr. Ofner-Martin', 'Seit November 2018 Tätigkeitsschwerpunkt Zahnärztliche Chirurgie', 'Seit Februar 2020 Tätigkeitsschwerpunkt Kinderzahnheilkunde'],
     ['Deutsche Zahnärztliche Philipp-Pfaff-Gesellschaft e. V.'],
     ['Tätigkeitsschwerpunkt Kinderzahnheilkunde', 'Tätigkeitsschwerpunkt Zahnärztliche Chirurgie', 'Röntgen-Fachkunde für dentale Digitale Volumentomographie (DVT)']),
    ('Zahnärztin Dr. Lena Berger', 'Zahnärztin in Karlsdorf-Neuthard', '/images/team/zahnaerztin-dr-lena-berger-karlsdorf-neuthard.jpg', 1200, 971, 'zahnaerztin-dr-lena-berger-karlsdorf-neuthard',
     ['Studium der Zahnmedizin in Frankfurt am Main 2008–2013', 'Promotion 2014–2018', '2014–2016 Vorbereitungsassistenz in Karlsruhe', '2017–2022 angestellte Zahnärztin in Karlsruhe', '2022–2024 angestellte Zahnärztin in Durlach', 'Seit 2024 angestellte Zahnärztin in der Praxis Dr. Ofner-Martin'],
     ['DGOI', 'FVDZ'],
     ['Tätigkeitsschwerpunkt Konservierende Zahnheilkunde', 'Tätigkeitsschwerpunkt Parodontologie, Endodontologie', 'Curriculum Implantologie', 'Anwendung von Laser in der Zahnmedizin', 'Aligner-Therapie', 'Fokus Kinderzähne', 'Dentale Lachgassedierung']),
]

def s_team():
    k = 'team'
    def ul(xs):
        return '<ul>' + ''.join(f'<li>{e(x)}</li>' for x in xs) + '</ul>'
    personen = ''.join(
        f'<article class="person" aria-labelledby="team--p{i}"><div>{bild(p, n, w, h, neu)}</div><div><h2 id="team--p{i}">{e(n)}</h2><p class="person__rolle">{e(r)}</p>'
        f'<details class="falt" open><summary><h3>Lebenslauf</h3></summary><div class="falt__inhalt">{ul(lv)}</div></details>'
        f'<details class="falt"><summary><h3>Mitgliedschaften</h3></summary><div class="falt__inhalt">{ul(mg)}</div></details>'
        f'<details class="falt"><summary><h3>Fortbildungen</h3></summary><div class="falt__inhalt">{ul(fb)}</div></details></div></article>'
        for i, (n, r, p, w, h, neu, lv, mg, fb) in enumerate(TEAM))
    stellen = ''.join(f'<li>{sym("haken")}<span>{e(s)}</span></li>' for s in STELLEN)
    inhalt = f'''{brotkrumen([('team', 'Team')])}
{seitenkopf(k, 'Freundlich, kompetent und erfahren', 'Unser Team in Karlsdorf-Neuthard', 'Lernen Sie Dr. med. dent. Christina Ofner-Martin und Kolleginnen näher kennen.', '/media/yootheme/cache/dc/praxis-team-dc640df7.jpg', 'Gruppenfoto des Teams der Zahnarztpraxis Dr. med. dent. Ofner-Martin und Kollegen', 1920, 800, 'team-zahnarztpraxis-dr-ofner-martin-karlsdorf-neuthard')}
<section class="abschnitt" aria-label="Zahnärztinnen"><div class="huelle">{personen}</div></section>
<section class="band" aria-labelledby="team--band"><div class="huelle"><div><h2 id="team--band">Das gesamte Team der Zahnarztpraxis Dr. Ofner-Martin freut sich auf Ihren Besuch.</h2>
<p>Vereinbaren Sie jetzt ganz einfach online Ihren Termin oder rufen Sie uns an. Ihre Zahnarzt-Praxis in Karlsdorf-Neuthard bei Bruchsal.</p></div>
<div class="knopfreihe" style="margin:0">{knopf_termin("knopf knopf--weiss", "Jetzt online Termin vereinbaren")}<a class="knopf" href="{TEL_LINK}">{sym("tel")}{TEL}</a></div></div></section>'''
    return seite(k, 'Unser Team | Zahnarztpraxis Dr. Ofner-Martin & Kollegen, Karlsdorf-Neuthard',
                 'Zahnarzt-Praxis-Team in Karlsdorf-Neuthard. Lernen Sie hier Dr. med. dent. Ofner-Martin und Kollegen näher kennen!', inhalt)

# ================================================================ LEISTUNGEN
def s_leistungen():
    k = 'leistungen'
    zeichen = '<span class="kachel__zeichen">' + sym('zahn') + '</span>'
    kach = ''.join(link(z, zeichen + e(t), cls='kachel') for z, t in LEISTUNGEN)
    inhalt = f'''{brotkrumen([('leistungen', 'Leistungen')])}
{seitenkopf(k, 'Unsere Leistungen für Ihr Lächeln', 'Zahnmedizinische Leistungen in Karlsdorf-Neuthard', 'Praxis für Zahnmedizin Dr. med. dent. Ofner-Martin &amp; Kollegen', '/images/header/leistungen/leistungen-zahnarzt-bruchsal-karlsdorf-neuthard.jpg', 'Zahnmedizinische Leistungen der Zahnarztpraxis Dr. Ofner-Martin im Überblick', 1920, 900, 'zahnmedizinische-leistungen-karlsdorf-neuthard')}
<section class="abschnitt" aria-labelledby="leistungen--alle"><div class="huelle">
  <div class="kopfzeile"><h2 id="leistungen--alle">Alle Leistungen auf einen Blick</h2><div class="strich"></div><p>Wählen Sie ein Thema, um mehr zu erfahren.</p></div>
  <div class="raster raster--kacheln">{kach}</div>
</div></section>
<section class="abschnitt abschnitt--hell" aria-labelledby="leistungen--ansatz"><div class="huelle zwei">
  <div><h2 id="leistungen--ansatz">Unser Ansatz ist ganzheitlich</h2><div class="strich"></div>
  <p>Im Bereich der Zahn-, Mund- und Kieferheilkunde gewährleistet Ihnen unser Zahnärzte-Team um Frau Dr. med. dent. Christina Ofner-Martin eine Rundumversorgung. Hierbei sehen wir den Menschen als Ganzes und unterteilen ihn nicht in einzelne Fachgebiete.</p>
  <p>Unser Behandlungsspektrum umfasst die:</p>
  <ul><li>{link('prophylaxe', 'Prophylaxe')}, d. h. Prävention zur Vermeidung von Zahnverlust</li><li>{link('kinderzahnheilkunde', 'Kinderzahnheilkunde')}, d. h. speziell für Kinder zugeschnittene Therapiearten und Herangehensweisen</li><li>{link('aesthetik', 'Ästhetische Zahnheilkunde')}</li><li>{link('zahnerhalt', 'konservierende Zahnmedizin')}, d. h. den Erhalt Ihres natürlichen Zahnbestandes</li><li>{link('chirurgie', 'Zahnärztliche Chirurgie')}, z. B. die Versorgung mittels {link('implantate', 'Implantaten')}</li><li>{link('schienentherapie', 'Funktionstherapie')} bei Kiefergelenksbeschwerden</li><li>{link('highlights', 'Behandlungs-Highlights')}, z. B. Alignertherapie, Lachgas, DVT, Laserbehandlung usw.</li></ul>
  <p>Sie haben Angst vor dem anstehenden Zahnarztbesuch oder haben einen starken Würgereiz, wenn bei Ihnen eine Abformung für Zahnersatz genommen werden muss? Auch hierfür haben wir Lösungen, sprechen Sie uns jederzeit gerne darauf an. Bei Bedarf kann eine Behandlung unter Lachgas erfolgen. Seit Neuestem bieten wir in unserer Praxis in Karlsdorf-Neuthard auch die Möglichkeit der Herstellung mittels des sogenannten CEREC-Systems an. Haben Sie Fragen? {link('kontakt', 'Kontaktieren Sie uns.')}</p></div>
  {zeiten_tabelle(k)}
</div></section>
{band(k)}'''
    return seite(k, 'Unsere Leistungen für Ihr Lächeln | Zahnarzt Karlsdorf-Neuthard',
                 'Leistungen für ein schönes Lächeln mit ganzheitlicher Zahnmedizin in unserer Zahnarztpraxis in Karlsdorf-Neuthard bei Bruchsal.', inhalt)

def s_leistung(k, name):
    d = L[k]
    nav = ''.join(f'<li>{link(z, e(t))}</li>' for z, t in LEISTUNGEN)
    anker = d.get('anker', {})
    teile = []
    for i, (h2, body) in enumerate(d['abschnitte']):
        a = anker.get(h2) or re.sub(r'[^a-z0-9]+', '-', h2.lower().replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')).strip('-')
        if 'VIDEO' in body and 'video' in d:
            body = body.replace('[[VIDEO]]', video(k, *d['video']))
        teile.append(f'<section id="{k}--{a}" aria-labelledby="{k}--{a}-t"><h2 id="{k}--{a}-t">{e(h2)}</h2>{body}</section>')
    inhalt = f'''{brotkrumen([('leistungen', 'Leistungen'), (k, name)])}
{seitenkopf(k, d['obenzeile'], d['h1'], '', d['bild'], d['bildalt'], d['bw'], d['bh'], d['neu'])}
<div class="abschnitt"><div class="huelle mitnav">
  <nav class="seitennav" aria-label="Leistungen"><h2>Unsere Leistungen</h2><ul>{nav}</ul>
  <div class="knopfreihe" style="margin-top:1rem">{knopf_tel('knopf knopf--voll', 'Anrufen')}</div></nav>
  <div class="inhalt">{''.join(teile)}{faq_block(k, d['faq'])}</div>
</div></div>
{band(k)}'''
    return seite(k, d['titel'], d['besch'], inhalt, menue='leistungen')

# ================================================================ AKTUELLES
BEITRAEGE = [
    ('rauchfrei', 'Rauchfrei für Ihre Mundgesundheit', '11. Juli 2025', '2025-07-11', '/media/yootheme/cache/2f/Screenshot%202025-07-11%20140844-2fc6545d.png', 400, 240, 'Titelseite des Flyers zum Rauchstopp von Deutschem Krebsforschungszentrum und Bundeszahnärztekammer', 'rauchfrei-mundgesundheit-flyer',
     '<p>Das Deutsche Krebsforschungszentrum und die Bundeszahnärztekammer haben einen neuen Flyer veröffentlicht, der die Risiken des Rauchens für die Mundgesundheit aufzeigt.</p><p>Rauchen erhöht das Risiko für Mundkrebs, Parodontitis und andere Erkrankungen erheblich. Nach einem Rauchstopp verbessern sich nicht nur Geschmack, Geruch und die Heilung im Mund, sondern das Risiko für Karies, Zahnverlust und Krebs sinkt auch deutlich. Wer aufhört, schützt nicht nur die Mundgesundheit, sondern auch die allgemeine Gesundheit und Lebensqualität. Ein Rauchstopp lohnt sich also: für ein gesünderes Lächeln und ein längeres, besseres Leben.</p><p>Ausführlichere Informationen und weiteres Infomaterial erhalten Sie unter: <a href="https://www.dkfz.de" target="_blank" rel="noopener">Deutsches Krebsforschungszentrum</a></p>'),
    ('mallorca', 'Hallo Mallorca: Praxisausflug 2025', '07. Juli 2025', '2025-07-07', '/media/yootheme/cache/e3/20250707_105909-COLLAGE-e312977b.jpg', 400, 240, 'Collage vom Praxisausflug nach Mallorca: Sonnenaufgang hinter Palmen, Hotelpool, Hauseingang, Sandburg und Kolleginnen mit Praxisshirt', 'praxisausflug-mallorca-2025-team',
     '<p>Anlässlich des 25. Praxisjubiläums hat sich unsere Chefin etwas ganz Besonderes für uns überlegt: einen Fortbildungsurlaub nach Mallorca für das ganze Team! Ja, wir haben auch nicht schlecht gestaunt, als wir das erfahren haben.</p><p>Letzte Woche war es dann so weit und wir stiegen in den Flieger. Mit im Gepäck war ganz viel Vorfreude und auch ein wenig Flugangst. Letztere konnten wir aber alle überwinden und beim Anblick der wunderschönen Insel überwog nur noch die Vorfreude. Das Hotel mit Blick auf das Meer war eine tolle Wahl und im klimatisierten Konferenzraum konnte man es gut aushalten. Wir haben die Zeit genutzt, um verschiedene Themen zu vertiefen und unser Wissen aufzufrischen. In entspannter Atmosphäre (und vielleicht war es auch der Blick auf die Palmen vor dem Fenster 😉) lernt es sich gleich viel besser.</p><p>Im Anschluss hat uns Fr. Dr. Ofner-Martin noch auf Ausflüge eingeladen. Als ortserfahrene Urlauberin konnte sie uns ein paar wirklich schöne Ecken zeigen. Trotz wahnsinniger Hitze lernten wir die Insel kennen und ich glaube, manch eine wird sehr gerne wieder hierherkommen.</p><p>Diese gemeinsame Zeit war unglaublich wertvoll für das ganze Team. Am Pool oder gemeinsam im Meer schwimmend lernten wir uns einfach noch ein Stückchen näher kennen und gehen nun erholt und gestärkt wieder zum Praxisalltag über.</p><p>Ich glaube, ich spreche für alle, wenn ich sage, dass wir unsere Dankbarkeit kaum in Worte fassen können. Trotzdem: Vielen Dank für dieses einmalige Erlebnis, Fr. Dr. Ofner-Martin!</p>'),
    ('studie', 'Neue Studie über die Zusammenhänge von Mundgesundheit und Schmerzen', '24. April 2025', '2025-04-24', '/media/yootheme/cache/d5/schmerz-frau-d50c2af0.jpg', 400, 240, 'Eine junge Frau liegt, leicht gekrümmt vor Schmerzen, auf einer Decke und hält ein großes Kissen fest im Arm', 'studie-mundgesundheit-schmerzen-frauen',
     '<p><strong>Mundgesundheit und Schmerz: Neue Studie zeigt überraschende Zusammenhänge bei Frauen</strong></p><p>Eine neue Studie der Universität Sydney hat einen deutlichen Zusammenhang zwischen schlechter Mundgesundheit und verschiedenen Schmerzzuständen bei Frauen aufgezeigt, darunter Migräne, Bauchschmerzen und Fibromyalgie. Es ist die erste Untersuchung weltweit, die gezielt den Einfluss der Mundgesundheit und des oralen Mikrobioms auf chronische Schmerzen bei Frauen analysiert hat.</p><p>Kernaussagen der Studie:</p><ul><li>Frauen mit schlechter Mundgesundheit litten deutlich häufiger unter Migräne und chronischen Körper- sowie Bauchschmerzen.</li><li>60 % der Frauen mit schlechter Mundgesundheit berichteten über moderate bis starke Körperschmerzen, 49 % litten häufiger unter Migräne.</li><li>Es zeigte sich ein signifikanter Zusammenhang zwischen bestimmten oralen Mikroben und dem Auftreten von Schmerzen, insbesondere aus den Gattungen Dialister, Fusobacterium, Parvimonas und Solobacterium.</li><li>Eine schlechtere Mundgesundheit war ein statistisch signifikanter Prädiktor für häufige und chronische Migräne.</li><li>67 % der Studienteilnehmerinnen litten an Fibromyalgie.</li></ul><p>Was bedeutet das? Die Ergebnisse deuten auf eine mögliche Verbindung zwischen dem oralen Mikrobiom und dem Nervensystem hin. Damit wird die Mundgesundheit zu einem potenziell unterschätzten Faktor bei chronischen Schmerzerkrankungen, besonders bei Frauen.</p><p>Fazit: Die Studie unterstreicht, wie wichtig eine gute Mundhygiene nicht nur für die Zahngesundheit, sondern auch für das allgemeine körperliche Wohlbefinden sein kann. Weitere Forschung könnte neue Wege zur Schmerzlinderung und Prävention chronischer Erkrankungen eröffnen.</p><p><em>Quelle: Erdrich, S. et al. (2025), Frontiers in Pain Research</em></p>'),
    ('schnarchen', 'Besser schlafen dank individuell gefertigter Schnarchschienen', '', '', '/media/yootheme/cache/82/young-woman-who-can-sleep-because-her-husband-snores-82fed165.jpg', 600, 300, 'Ein Paar liegt im Bett. Die Frau hält sich mit verzerrtem Blick die Ohren zu, der Mann schläft und schnarcht im Hintergrund', 'schnarchschiene-protrusionsschiene-karlsdorf-neuthard',
     '<p>Schnarchen ist nicht nur störend, es kann auch ein ernstzunehmendes Gesundheitsrisiko darstellen. In unserer Zahnarztpraxis bieten wir ab sofort individuell angefertigte Protrusionsschienen, auch bekannt als Schnarchschienen, an. Diese effektive Therapie hilft dabei, das Schnarchen deutlich zu reduzieren und die Schlafqualität spürbar zu verbessern.</p><p><strong>Was ist eine Protrusionsschiene?</strong> Eine Protrusionsschiene wird individuell im Zahnlabor angefertigt und nachts getragen. Sie hält den Unterkiefer sanft in einer leicht vorgeschobenen Position. Dadurch bleiben die Atemwege offen, das typische Flattern des weichen Gaumens, das das Schnarchgeräusch verursacht, wird verhindert.</p><p>Die Vorteile auf einen Blick:</p><ul><li>Reduktion des Schnarchens und damit auch eine Entlastung für Partner:innen.</li><li>Besserer Schlaf: erholsamer für Sie und Ihr Umfeld.</li><li>Vorbeugung von Folgeerkrankungen: Schnarchen kann ein Anzeichen für obstruktive Schlafapnoe sein, die langfristig Herz-Kreislauf-Erkrankungen begünstigen kann.</li><li>Komfortabel und individuell angepasst für eine optimale Passform und maximale Wirksamkeit.</li></ul><p>Sprechen Sie uns gerne an. Wir beraten Sie individuell und finden gemeinsam heraus, ob eine Protrusionsschiene für Sie geeignet ist.</p>'),
    ('weihnachtsfeier', 'Weihnachtsfeier Team Dr. Ofner-Martin', '', '', '/media/yootheme/cache/0b/IMG-20250116-WA0008-0bcb8f7b.jpg', 600, 300, 'Das Team der Zahnarztpraxis Dr. Ofner-Martin bei der Weihnachtsfeier', 'weihnachtsfeier-team-zahnarztpraxis-dr-ofner-martin',
     '<p>Nun ist die Weihnachtsfeier schon einige Tage her, aber wir denken immer noch voller Freude daran. In gemütlicher Runde, begleitet von Kerzenlicht, Kaminfeuer und Aperol ;-) haben wir unsere letzte Weihnachtsfeier genossen. Die Stimmung war gut und auch das Essen des italienischen Restaurants.</p><p>Nach einer spannenden Rede unserer Chefin, mit tollen Aussichten für 2025, wurde noch ganz traditionell gewichtelt. Es gab liebevoll ausgewählte Geschenke für alle von uns.</p><p>Für den Zusammenhalt im Team sind solche Abende immens wichtig. Nicht nur an Weihnachten, sondern auch unterm Jahr versuchen wir daher immer wieder, Zeit auch außerhalb der Arbeit gemeinsam zu verbringen. Für dieses Jahr steht auf jeden Fall ein bisschen was auf dem Plan …</p>'),
    ('jubilaeum', '25 Jahre Ihre Praxis für Zahnmedizin Dr. Christina Ofner-Martin & Kollegen', '', '', '/media/yootheme/cache/33/Screenshot%202025-01-03%20133811-33071381.png', 600, 300, 'Das ganze Team der Zahnarztpraxis zum 25. Praxisjubiläum', 'praxisjubilaeum-25-jahre-dr-ofner-martin',
     '<p>2025 ist ein wichtiges Jahr: Wir feiern das 25. Praxisjubiläum und gratulieren unserer Chefin Fr. Dr. Christina Ofner-Martin zu diesem Meilenstein!</p><p>Begleitet wird sie seit ebenfalls 25 Jahren von unseren Kolleginnen Biggi und Manu und auch das Praxislabor Bachmann war von Anfang an dabei.</p><p>Vielen Dank für die tolle Zusammenarbeit und auf viele weitere gemeinsame Jahre!</p>'),
]

def s_aktuelles():
    k = 'aktuelles'
    b = ''.join(
        f'<article class="beitrag" id="{k}--{a}" aria-labelledby="{k}--{a}-t"><div>{bild(p, alt, w, h, neu)}</div><div>'
        + (f'<p class="karte__datum"><time datetime="{iso}">{d}</time></p>' if d else '')
        + f'<h2 id="{k}--{a}-t">{e(t)}</h2>{txt}</div></article>'
        for a, t, d, iso, p, w, h, alt, neu, txt in BEITRAEGE)
    inhalt = f'''{brotkrumen([('aktuelles', 'Aktuelles')])}
{seitenkopf(k, 'Neues aus der Praxis', 'Aktuelle Neuigkeiten aus unserer Praxis in Karlsdorf-Neuthard', 'Bleiben Sie auf dem neuesten Stand mit unseren aktuellen Neuigkeiten, Stellenangeboten oder speziellen bzw. geänderten Sprechzeiten.', '/media/yootheme/cache/4b/aktuelles-blog-zahnarzt-bruchsal-4b4231fb.jpg', 'Aktuelles aus der Zahnarztpraxis in Karlsdorf-Neuthard', 1920, 640, 'aktuelles-zahnarztpraxis-karlsdorf-neuthard')}
<section class="abschnitt abschnitt--hell" aria-labelledby="aktuelles--kurz"><div class="huelle">
  <div class="kopfzeile"><h2 id="aktuelles--kurz">Kurzmitteilungen von uns</h2><div class="strich"></div></div>
  <div class="kurz">
    <div class="block"><h3>Online-Terminbuchung</h3><p>Vielleicht haben Sie es schon gesehen: Ab sofort steht Ihnen die Möglichkeit, Ihren Termin online zu buchen, zur Verfügung. Einfach oben auf den Button „Termine buchen“ klicken. Die Buchung erfolgt über Dr. Flex. Eine Registrierung ist nicht erforderlich.</p>{knopf_termin('knopf knopf--voll', 'Termine buchen')}</div>
    <div class="block"><h3>Universal-Zahnpasten im Test</h3><p>Zahnpasta muss nicht teuer sein! Stiftung Warentest hat viele Universal-Zahnpasten für kleines Geld als „sehr gut“ bewertet. Nur am Verpackungsmüll und an den Zusatzstoffen müssen viele Firmen noch arbeiten. Das Gesamtergebnis kann kostenpflichtig auf der Website von Stiftung Warentest eingesehen werden.</p></div>
    <div class="block"><h3>Pressemitteilung von BZÄK und BVND</h3><p>Volkskrankheit Parodontitis und Diabetes. <span class="luecke">PDF-Datei vom alten Webspace übernehmen und hier verlinken.</span></p></div>
  </div>
</div></section>
<section class="abschnitt" aria-label="Beiträge"><div class="huelle huelle--breit">{b}</div></section>
{band(k)}'''
    return seite(k, 'Neues aus der Praxis | Zahnarztpraxis Dr. Ofner-Martin, Karlsdorf-Neuthard',
                 'Bleiben Sie auf dem neuesten Stand mit unseren aktuellen Neuigkeiten, Stellenangeboten oder speziellen bzw. geänderten Sprechzeiten.', inhalt)

# ================================================================ KONTAKT
def s_kontakt():
    k = 'kontakt'
    inhalt = f'''{brotkrumen([('kontakt', 'Kontakt & Anfahrt')])}
{seitenkopf(k, 'Kontakt & Anfahrt', 'Ihre Zahnarztpraxis in Karlsdorf-Neuthard', 'Öffnungszeiten, Termine und Kontakt für Ihre Zahnarztpraxis in Karlsdorf-Neuthard bei Bruchsal. Wir freuen uns über Ihre Anfrage.', '/media/yootheme/cache/b7/kontakt-zahnarztpraxis-karlsdorf-neuthard-bruchsal-b77d9de5.jpg', 'Zahnarztpraxis Dr. med. dent. Ofner-Martin & Kollegen in Karlsdorf-Neuthard', 1920, 800, 'kontakt-zahnarztpraxis-karlsdorf-neuthard-bruchsal')}
<section class="abschnitt" aria-labelledby="kontakt--daten"><div class="huelle zwei zwei--gleich" style="align-items:start">
  <div><h2 id="kontakt--daten">So erreichen Sie uns</h2><div class="strich"></div>
  <p class="vorspann"><strong>Praxis für Zahnmedizin</strong><br>Dr. med. dent. Christina Ofner-Martin &amp; Kollegen<br>Salinenstraße 8<br>76689 Karlsdorf-Neuthard</p>
  <p>Telefon: <a href="{TEL_LINK}">{TEL}</a><br>Fax: {FAX}<br>E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>
  <div class="knopfreihe">{knopf_tel()}{knopf_termin('knopf', 'Termine buchen')}</div>
  <h3 style="margin-top:2.5rem">Anfahrt</h3><p>Ob Sie direkt aus Karlsdorf-Neuthard kommen oder aus Bruchsal: Die Anfahrt dauert nur wenige Minuten. Gratis-Parkplätze gibt es direkt vor der Praxis.</p>
  {karte_einbettung()}</div>
  {zeiten_tabelle(k)}
</div></section>
<section class="abschnitt abschnitt--hell" id="kontakt--termin" aria-labelledby="kontakt--form-t"><div class="huelle huelle--schmal">
  <h2 id="kontakt--form-t">Schreiben Sie uns</h2><div class="strich"></div>
  <p>Für Terminwünsche erreichen Sie uns am schnellsten telefonisch unter <a href="{TEL_LINK}">{TEL}</a> oder über die Online-Terminbuchung.</p>
  <form class="formular" data-formular novalidate>
    <div class="zeile"><div class="feld"><label for="k-name">Name *</label><input id="k-name" name="name" required autocomplete="name"><p class="feld__fehler" id="k-name-fehler" hidden>Bitte geben Sie Ihren Namen an.</p></div>
    <div class="feld"><label for="k-tel">Telefon</label><input id="k-tel" type="tel" name="telefon" autocomplete="tel"></div></div>
    <div class="feld"><label for="k-mail">E-Mail *</label><input id="k-mail" type="email" name="email" required autocomplete="email"><p class="feld__fehler" id="k-mail-fehler" hidden>Bitte geben Sie eine gültige E-Mail-Adresse an.</p></div>
    <div class="feld"><label for="k-text">Ihre Nachricht *</label><textarea id="k-text" name="nachricht" required maxlength="1000"></textarea><p class="feld__zaehler" data-zaehler>0/1000</p><p class="feld__fehler" id="k-text-fehler" hidden>Bitte schreiben Sie uns eine Nachricht.</p></div>
    <p class="entwurfshinweis">Bitte senden Sie uns über das Formular keine Gesundheitsdaten. Für vertrauliche Angaben rufen Sie uns bitte an.</p>
    <label class="pruef"><input type="checkbox" id="k-ds" required><span><strong>Datenschutz-Hinweis:</strong> Durch Absenden dieses Formulars stimmen Sie der Speicherung und Verarbeitung Ihrer Daten gemäß unserer {link('datenschutz', 'Datenschutzerklärung')} zu. Ihre Daten werden von uns nur zur Beantwortung der Anfrage verwendet. *</span></label>
    <p class="feld__fehler" id="k-ds-fehler" hidden>Bitte bestätigen Sie den Datenschutz-Hinweis.</p>
    <div><button class="knopf knopf--voll" type="submit">Nachricht senden</button></div>
    <p class="entwurfshinweis">Entwurf: Das Formular prüft die Eingaben, verschickt aber noch nichts.</p>
  </form>
  <div class="danke" tabindex="-1" hidden><h3>Vielen Dank für Ihre Nachricht!</h3><p>Wir melden uns so bald wie möglich bei Ihnen.</p></div>
</div></section>
<section class="abschnitt" aria-labelledby="kontakt--fragen-titel"><div class="huelle huelle--schmal" id="kontakt--fragen">
  <h2 id="kontakt--fragen-titel">Häufige Fragen</h2>
  <details class="falt"><summary><h3>{e(KONTAKT_FAQ[0])}</h3></summary><div class="falt__inhalt"><p>{e(KONTAKT_FAQ[1])}</p></div></details>
  <details class="falt"><summary><h3>Was mache ich bei Zahnschmerzen außerhalb der Sprechzeiten?</h3></summary><div class="falt__inhalt"><p>Informationen zum zahnärztlichen Notdienst erhalten Sie unter {NOTDIENST}. Während der Sprechzeiten erreichen Sie die Zahnarztpraxis Dr. Ofner-Martin in Karlsdorf-Neuthard unter {TEL}.</p></div></details>
  <details class="falt"><summary><h3>Kann ich meinen Termin online buchen?</h3></summary><div class="falt__inhalt"><p>Ja. Die Zahnarztpraxis Dr. Ofner-Martin bietet eine Online-Terminbuchung über Dr. Flex an. Eine Registrierung ist nicht erforderlich.</p></div></details>
  <details class="falt"><summary><h3>Was bringe ich zum ersten Termin mit?</h3></summary><div class="falt__inhalt"><p>Bringen Sie zu Ihrem ersten Besuch in der Zahnarztpraxis Dr. Ofner-Martin gerne den bereits ausgefüllten Anamnesebogen mit. Er steht auf dieser Seite als PDF zum Download bereit.</p></div></details>
</div></section>'''
    return seite(k, 'Kontakt & Anfahrt | Zahnarztpraxis Dr. Ofner-Martin, Karlsdorf-Neuthard',
                 'Öffnungszeiten, Termine und Kontakt für Ihre Zahnarztpraxis in Karlsdorf-Neuthard bei Bruchsal. Wir freuen uns über Ihre Anfrage.', inhalt)

# ================================================================ RECHT
ENTWURF = '<div class="entwurf"><strong>Entwurf, keine Rechtsberatung.</strong> Diese Seite wurde für den Entwurf aufgebaut. Gelb markierte Stellen sind noch zu ergänzen oder zu bestätigen. Vor dem Livegang bitte anwaltlich oder durch die zuständige Kammer prüfen lassen.</div>'

def s_impressum():
    k = 'impressum'
    inhalt = f'''{brotkrumen([('impressum', 'Impressum')])}
<section class="abschnitt" aria-labelledby="impressum--titel"><div class="huelle huelle--schmal recht">
<h1 id="impressum--titel">Impressum</h1>{ENTWURF}
<h2>Angaben gemäß § 5 DDG</h2>
<p>Dr. med. dent. Christina Ofner-Martin<br>Praxis für Zahnmedizin Dr. med. dent. Christina Ofner-Martin &amp; Kollegen<br>Salinenstraße 8<br>76689 Karlsdorf-Neuthard</p>
<h2>Kontakt</h2>
<p>Telefon: <a href="{TEL_LINK}">07251 34 85 55</a><br>Fax: 07251 34 85 56<br>E-Mail: <a href="mailto:{MAIL}">{MAIL}</a><br>Web: www.dr-ofner-martin.de</p>
<h2>Berufsbezeichnung und berufsrechtliche Regelungen</h2>
<p><strong>Gesetzliche Berufsbezeichnung:</strong><br>Zahnärztin, die Approbation wurde in der Bundesrepublik Deutschland erteilt.</p>
<p><strong>Zuständige Zahnärztekammer (Aufsichtsbehörde):</strong><br>Landeszahnärztekammer Baden-Württemberg<br>Albstadtweg 9<br>70567 Stuttgart</p>
<p><strong>Zuständige Kassenzahnärztliche Vereinigung:</strong><br>KZV Baden-Württemberg, Bezirksdirektion Karlsruhe<br>Joseph-Meyer-Straße 8–10<br>68167 Mannheim</p>
<p><strong>Berufsrechtliche Regelungen:</strong></p>
<ul><li>Berufsordnung der Landeszahnärztekammer Baden-Württemberg</li><li>Heilberufe-Kammergesetz Baden-Württemberg</li><li>Gebührenordnung für Zahnärzte (GOZ)</li><li>Gesetz über die Ausübung der Zahnheilkunde</li></ul>
<p>Die Regelungen sind bei der Landeszahnärztekammer Baden-Württemberg abrufbar: <a href="https://lzk-bw.de" target="_blank" rel="noopener">lzk-bw.de</a> <span class="luecke">Genauen Link zur Berufsordnung bestätigen.</span></p>
<h2>Angaben zur Berufshaftpflichtversicherung</h2>
<p class="luecke">Name und Sitz des Versicherers sowie der räumliche Geltungsbereich der Versicherung sind noch einzutragen.</p>
<h2>Verbraucherstreitbeilegung</h2>
<p>Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
<h2>Konzeption, Gestaltung und Umsetzung</h2>
<p>AO Consulting GmbH<br>Zeiloch 13<br>76646 Bruchsal<br><a href="https://ao-consult.de" target="_blank" rel="noopener">ao-consult.de</a></p>
<h2>Webhosting</h2>
<p class="luecke">Neuen Hoster nach dem Umzug eintragen (bisher axevio host&amp;care beim alten Anbieter).</p>
<h2>Bildnachweis</h2>
<p>Fotos von Zahnersatz wurden uns freundlicherweise zur Verfügung gestellt von:<br>Dirk Bachmann, Am Mantel 1, 76646 Bruchsal, Telefon 07251 8 60 60, <a href="https://www.bachmann-dental.de" target="_blank" rel="noopener">www.bachmann-dental.de</a></p>
<p>Fotos Praxisräume &amp; Team:<br>Rocketmedia, Christian Zeibig, Am Baumgarten 21, 76689 Karlsdorf-Neuthard, Telefon 07251 440155, <a href="https://www.zeibig.com" target="_blank" rel="noopener">www.zeibig.com</a></p>
<p>Sonstige Fotos: istockphoto.com</p>
<p class="luecke">Nach dem Einbau der neuen Fotos und Videos den Bildnachweis aktualisieren.</p>
<h2>Haftung für Inhalte</h2>
<p>Als Diensteanbieter sind wir gemäß § 7 Abs. 1 DDG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 DDG sind wir als Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen. Verpflichtungen zur Entfernung oder Sperrung der Nutzung von Informationen nach den allgemeinen Gesetzen bleiben hiervon unberührt. Eine diesbezügliche Haftung ist jedoch erst ab dem Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung möglich. Bei Bekanntwerden von entsprechenden Rechtsverletzungen werden wir diese Inhalte umgehend entfernen.</p>
<h2>Haftung für Links</h2>
<p>Unser Angebot enthält Links zu externen Webseiten Dritter, auf deren Inhalte wir keinen Einfluss haben. Deshalb können wir für diese fremden Inhalte auch keine Gewähr übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten verantwortlich. Die verlinkten Seiten wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße überprüft. Rechtswidrige Inhalte waren zum Zeitpunkt der Verlinkung nicht erkennbar. Eine permanente inhaltliche Kontrolle der verlinkten Seiten ist jedoch ohne konkrete Anhaltspunkte einer Rechtsverletzung nicht zumutbar. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Links umgehend entfernen.</p>
<h2>Urheberrecht</h2>
<p>Die durch die Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechts bedürfen der schriftlichen Zustimmung des jeweiligen Autors oder Erstellers. Downloads und Kopien dieser Seite sind nur für den privaten, nicht kommerziellen Gebrauch gestattet. Soweit die Inhalte auf dieser Seite nicht vom Betreiber erstellt wurden, werden die Urheberrechte Dritter beachtet. Insbesondere werden Inhalte Dritter als solche gekennzeichnet. Sollten Sie trotzdem auf eine Urheberrechtsverletzung aufmerksam werden, bitten wir um einen entsprechenden Hinweis. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Inhalte umgehend entfernen.</p>
<h2>Geltung für Profile</h2>
<p>Das Impressum gilt auch für folgende Profile:</p>
<ul><li><a href="{JAMEDA}" target="_blank" rel="noopener">Jameda</a></li><li><a href="{GOOGLE_PROFIL}" target="_blank" rel="noopener">Google Unternehmensprofil</a></li><li><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a></li></ul>
</div></section>'''
    return seite(k, 'Impressum | Zahnarztpraxis Dr. Ofner-Martin, Karlsdorf-Neuthard',
                 'Impressum der Praxis für Zahnmedizin Dr. med. dent. Christina Ofner-Martin & Kollegen, Salinenstraße 8, 76689 Karlsdorf-Neuthard.', inhalt)

def s_datenschutz():
    k = 'datenschutz'
    inhalt = f'''{brotkrumen([('datenschutz', 'Datenschutz')])}
<section class="abschnitt" aria-labelledby="datenschutz--titel"><div class="huelle huelle--schmal recht">
<h1 id="datenschutz--titel">Datenschutzerklärung</h1>{ENTWURF}
<h2>1. Verantwortliche Stelle</h2>
<p>Verantwortlich für die Datenverarbeitung auf dieser Website ist:</p>
<p>Dr. med. dent. Christina Ofner-Martin, Zahnärztin<br>Praxis für Zahnmedizin Dr. med. dent. Christina Ofner-Martin &amp; Kollegen<br>Salinenstraße 8<br>76689 Karlsdorf-Neuthard<br>Telefon: <a href="{TEL_LINK}">{TEL}</a><br>E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>

<h2>2. Grundsatz</h2>
<p>Diese Website ist bewusst sparsam gebaut. Sie setzt keine Werbe- oder Analysedienste ein, bindet keine Schriften von fremden Servern ein und verwendet keine Cookies zu Werbezwecken. Eine Datenübertragung an Dritte findet nur statt, wenn Sie die Anfahrtskarte, ein Video oder die Online-Terminbuchung ausdrücklich laden.</p>
<p>Diese Erklärung beschreibt ausschließlich die Verarbeitung auf der Website. Für die Verarbeitung Ihrer Behandlungsdaten in der Praxis gilt die gesonderte Patienteninformation, die Sie vor Ort erhalten.</p>
<h2>3. Hosting und Server-Logfiles</h2>
<p>Beim Aufruf der Website übermittelt Ihr Browser technisch notwendige Daten an den Server. Der Anbieter speichert diese in sogenannten Logfiles: aufgerufene Seite, Datum und Uhrzeit, übertragene Datenmenge, Meldung über den erfolgreichen Abruf, Browsertyp und Version, Betriebssystem, Referrer-URL und IP-Adresse. Eine Zusammenführung dieser Daten mit anderen Datenquellen wird nicht vorgenommen.</p>
<p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO. Das berechtigte Interesse liegt im sicheren und störungsfreien Betrieb der Website.</p>
<p class="luecke">Name und Anschrift des neuen Hosters sowie die Speicherdauer der Logfiles und der Abschluss eines Auftragsverarbeitungsvertrags nach Art. 28 DSGVO sind noch einzutragen.</p>
<h2>4. Kontaktformular, E-Mail und Telefon</h2>
<p>Wenn Sie uns über das Kontaktformular, per E-Mail oder telefonisch erreichen, verarbeiten wir die von Ihnen mitgeteilten Angaben, um Ihre Anfrage zu bearbeiten. Pflichtangaben im Formular sind Name, E-Mail-Adresse und Ihre Nachricht. Ihre Daten werden von uns nur zur Beantwortung der Anfrage verwendet.</p>
<p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO, soweit es um die Anbahnung einer Behandlung geht, im Übrigen Art. 6 Abs. 1 lit. f DSGVO. Bitte senden Sie uns über das Formular keine Gesundheitsdaten.</p>
<p class="luecke">Der Versandweg des Formulars und die Speicherdauer der Anfragen sind vor dem Livegang festzulegen und hier einzutragen.</p>
<h2>5. Einwilligungsverwaltung</h2>
<p>Beim ersten Aufruf fragt ein Fenster, ob Karte, Videos und Online-Terminbuchung geladen werden dürfen. Ihre Entscheidung speichern wir im lokalen Speicher Ihres Browsers, nicht in einem Cookie. Gespeichert werden ausschließlich die gewählten Kategorien und der Zeitpunkt der Entscheidung, keine Kennung und keine Daten über Sie.</p>
<p>Rechtsgrundlage für die Speicherung ist § 25 Abs. 2 Nr. 2 TDDDG, für die Dokumentation Art. 6 Abs. 1 lit. c DSGVO in Verbindung mit Art. 7 Abs. 1 DSGVO. Die Speicherung gilt 12 Monate. Sie können Ihre Entscheidung jederzeit über den Link „Cookie-Einstellungen“ in der Fußzeile jeder Seite ändern oder widerrufen.</p>
<h2>6. Barrierefreiheits-Einstellungen</h2>
<p>Über das Symbol unten rechts lassen sich Kontrast, Schriftgröße und weitere Darstellungsoptionen einstellen. Diese Einstellungen werden ausschließlich im lokalen Speicher Ihres Browsers abgelegt, damit sie beim nächsten Besuch erhalten bleiben. Es werden keine Daten an uns oder an Dritte übertragen.</p>
<h2>7. Schriften</h2>
<p>Die verwendete Schrift „Exo 2“ ist in die Website eingebettet und wird vom selben Server ausgeliefert. Es besteht keine Verbindung zu Google Fonts oder einem anderen fremden Schriftdienst.</p>
<h2>8. Anfahrtskarte über Google Maps</h2>
<p>Auf der Kontaktseite können Sie eine Karte von Google Maps laden. Vor Ihrer Zustimmung wird keine Verbindung zu Google aufgebaut, es wird lediglich ein Platzhalter angezeigt. Wenn Sie die Karte laden, überträgt Ihr Browser Daten an die Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland. Dazu gehören Ihre IP-Adresse, Angaben zu Ihrem Gerät und die aufgerufene Seite. Eine Verarbeitung in den USA ist möglich. Google ist unter dem EU-US Data Privacy Framework zertifiziert.</p>
<p>Rechtsgrundlage ist Ihre Einwilligung nach Art. 6 Abs. 1 lit. a DSGVO und § 25 Abs. 1 TDDDG. Sie können die Einwilligung jederzeit über die Fußzeile widerrufen. Nach dem Widerruf wird die Seite neu geladen, damit keine bereits eingebundene Karte bestehen bleibt.</p>
<h2>9. Videos über YouTube</h2>
<p>Auf den Seiten „Implantate“ und „Behandlungs-Highlights“ können Sie Informationsvideos abspielen. Die Videos werden erst nach Ihrem Klick über den erweiterten Datenschutzmodus von YouTube (youtube-nocookie.com) geladen. Anbieter ist die Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland. Beim Laden werden Ihre IP-Adresse und Geräteangaben an Google übertragen, eine Verarbeitung in den USA ist möglich. Rechtsgrundlage ist Ihre Einwilligung nach Art. 6 Abs. 1 lit. a DSGVO und § 25 Abs. 1 TDDDG.</p>
<h2>10. Online-Terminbuchung über Dr. Flex</h2>
<p>Für die Online-Terminbuchung nutzen wir den Dienst Dr. Flex. Das Buchungsfenster wird erst geladen, wenn Sie „Termine buchen“ wählen und zustimmen. Dabei werden Ihre IP-Adresse, Geräteangaben und die Angaben, die Sie für die Buchung eingeben, an den Anbieter übertragen. Rechtsgrundlage für das Laden ist Ihre Einwilligung nach Art. 6 Abs. 1 lit. a DSGVO und § 25 Abs. 1 TDDDG, für die Terminbuchung selbst Art. 6 Abs. 1 lit. b DSGVO.</p>
<p class="luecke">Vollständige Firmierung und Anschrift von Dr. Flex, Hinweis auf den Auftragsverarbeitungsvertrag und Speicherdauer der Termindaten ergänzen.</p>
<h2>11. Bilder</h2>
<p class="luecke">Nur im Entwurf: Die Fotos werden vorläufig noch von der bisherigen Adresse www.dr-ofner-martin.de geladen. Vor dem Livegang liegen alle Bilder auf dem eigenen Webspace, dann entfällt dieser Hinweis.</p>
<h2>12. Verschlüsselung</h2>
<p>Diese Website nutzt aus Sicherheitsgründen und zum Schutz der Übertragung vertraulicher Inhalte eine SSL- bzw. TLS-Verschlüsselung. Eine verschlüsselte Verbindung erkennen Sie an „https://“ und dem Schloss-Symbol in der Adresszeile Ihres Browsers.</p>
<h2>13. Links zu Bewertungsportalen und sozialen Netzwerken</h2>
<p>Verweise auf Jameda, Google, Instagram und unsere eigene Karriereseite dr-ofner-martin-karriere.de sind einfache Links. Beim Laden unserer Seite werden keine Daten an diese Anbieter übertragen. Erst wenn Sie einen dieser Links anklicken, verlassen Sie unsere Website und es gelten die Datenschutzbestimmungen des jeweiligen Anbieters.</p>
<h2>14. Ihre Rechte</h2>
<p>Sie haben das Recht auf Auskunft über die zu Ihrer Person gespeicherten Daten (Art. 15 DSGVO), auf Berichtigung (Art. 16 DSGVO), auf Löschung (Art. 17 DSGVO), auf Einschränkung der Verarbeitung (Art. 18 DSGVO), auf Datenübertragbarkeit (Art. 20 DSGVO) und auf Widerspruch gegen Verarbeitungen, die auf einem berechtigten Interesse beruhen (Art. 21 DSGVO). Eine erteilte Einwilligung können Sie jederzeit mit Wirkung für die Zukunft widerrufen. Dazu reicht eine formlose Mitteilung per E-Mail an <a href="mailto:{MAIL}">{MAIL}</a>.</p>
<h2>15. Beschwerderecht</h2>
<p>Sie haben das Recht, sich bei einer Datenschutz-Aufsichtsbehörde zu beschweren. Zuständig ist der Landesbeauftragte für den Datenschutz und die Informationsfreiheit Baden-Württemberg, Lautenschlagerstraße 20, 70173 Stuttgart.</p>
<h2>16. Widerspruch gegen Werbe-Mails</h2>
<p>Der Nutzung von im Rahmen der Impressumspflicht veröffentlichten Kontaktdaten zur Übersendung von nicht ausdrücklich angeforderter Werbung und Informationsmaterialien wird hiermit widersprochen.</p>
<h2>17. Änderungen dieser Erklärung</h2>
<p>Wir passen diese Erklärung an, wenn sich die Technik der Website oder die Rechtslage ändert. Es gilt jeweils die hier veröffentlichte Fassung.</p>
<p>Stand: <span class="luecke">Datum vor dem Livegang eintragen</span></p>
</div></section>'''
    return seite(k, 'Datenschutz | Zahnarztpraxis Dr. Ofner-Martin, Karlsdorf-Neuthard',
                 'Datenschutzerklärung der Zahnarztpraxis Dr. Ofner-Martin in Karlsdorf-Neuthard. Ohne Werbedienste, mit lokaler Schrift, Karte und Videos erst nach Einwilligung.', inhalt)

def s_gleichstellung():
    k = 'gleichstellung'
    inhalt = f'''{brotkrumen([('gleichstellung', 'Gleichstellung')])}
<section class="abschnitt" aria-labelledby="gleichstellung--titel"><div class="huelle huelle--schmal recht">
<h1 id="gleichstellung--titel">Hinweis zur Gleichstellung</h1>
<h2>Sprache auf dieser Website</h2>
<p>Wir sprechen auf dieser Website nach Möglichkeit alle Menschen gleichermaßen an. Wo aus Gründen der Lesbarkeit nur eine Sprachform verwendet wird, zum Beispiel „Patienten“ oder „Zahnarzt“, sind damit ausdrücklich alle Geschlechter gemeint.</p>
<h2>Gleichbehandlung in der Praxis</h2>
<p>In der Praxis für Zahnmedizin Dr. med. dent. Christina Ofner-Martin &amp; Kollegen werden alle Patientinnen und Patienten sowie alle Mitarbeitenden gleich behandelt, unabhängig von Geschlecht, Herkunft, Religion, Weltanschauung, Behinderung, Alter oder sexueller Identität.</p>
<h2>Barrierefreiheit</h2>
<p>Diese Website ist so gebaut, dass sie sich mit der Tastatur bedienen lässt und mit Vorleseprogrammen funktioniert. Über das Symbol unten rechts lassen sich Kontrast, Schriftgröße, Zeilenabstand und weitere Darstellungsoptionen anpassen. Wenn Ihnen eine Barriere auffällt, schreiben Sie uns bitte an <a href="mailto:{MAIL}">{MAIL}</a>. Wir bessern nach.</p>
</div></section>'''
    return seite(k, 'Gleichstellungshinweis | Zahnarztpraxis Dr. Ofner-Martin, Karlsdorf-Neuthard',
                 'Hinweis zur Gleichstellung und zur Barrierefreiheit der Website der Zahnarztpraxis Dr. Ofner-Martin in Karlsdorf-Neuthard.', inhalt)

# ================================================================ KOPF / FUSS
KARRIERE = 'https://dr-ofner-martin-karriere.de/'
KARRIERE_LINK = f'<a href="{KARRIERE}" target="_blank" rel="noopener">Karriere machen<span class="nur-vorleser"> (öffnet die Karriereseite in neuem Fenster)</span></a>'

def kopf():
    nav = [('start', 'Startseite'), ('praxis', 'Praxis'), ('team', 'Team'), ('leistungen', 'Leistungen'), ('aktuelles', 'Aktuelles'), ('kontakt', 'Kontakt')]
    links = ''.join(link(z, e(t)) for z, t in nav) + KARRIERE_LINK
    return f'''<div class="sprunglinks"><a href="#inhalt-start" data-sprung>Zum Inhalt springen</a><a href="#/kontakt">Zum Kontakt springen</a></div>
<header>
  <div class="oben"><div class="huelle">
    <div class="status" data-sprechzeiten data-offen-anzeige>
      <button class="status__knopf" type="button" aria-expanded="false" aria-controls="sprechzeiten-panel"><span class="status__punkt" aria-hidden="true"></span><span data-status-kurz>Sprechzeiten</span></button>
      <div class="status__panel" id="sprechzeiten-panel" hidden>
        <p class="status__lage" data-status-lang></p>
        <ul class="status__liste" data-status-liste></ul>
        <p class="status__feiertag" data-status-feiertag hidden></p>
        <p class="status__fuss">Gesetzliche Feiertage in Baden-Württemberg sind berücksichtigt. Zahnärztlicher Notdienst: <a href="{NOTDIENST_LINK}">{NOTDIENST}</a></p>
      </div>
    </div>
    <div class="oben__rechts">
      <a class="oben__punkt oben__punkt--weg" href="{NOTDIENST_LINK}">{sym('info')}Notdienst: {NOTDIENST}</a>
      <a class="oben__punkt oben__punkt--weg" href="mailto:{MAIL}">{sym('mail')}{MAIL}</a>
      <a class="oben__punkt" href="{TEL_LINK}">{sym('tel')}{TEL}</a>
    </div>
  </div></div>
  <div class="leiste"><div class="huelle">
    <a class="marke" data-ziel="start" href="#/start" aria-label="Zur Startseite">{logo(False)}</a>
    <button class="burger" type="button" data-menue-auf aria-expanded="false" aria-controls="menue">{sym('burger')}Menü</button>
    <nav class="menue" id="menue" aria-label="Hauptmenü">
      <button class="menue__zu" type="button" data-menue-zu>Schließen</button>
      {links}
      {knopf_termin('knopf knopf--voll', 'Termine buchen')}
    </nav>
  </div></div>
  <div class="menue-schleier"></div>
</header>'''

def fuss():
    lz = ''.join(f'<li>{link(z, e(t))}</li>' for z, t in LEISTUNGEN)
    return f'''<footer>
  <div class="huelle">
    <div class="fuss__raster">
      <div><div class="fuss__marke">{logo(False)}</div>
        <h3>Kontakt</h3>
        <p>Praxis für Zahnmedizin<br>Dr. med. dent. Christina Ofner-Martin &amp; Kollegen<br>Salinenstraße 8<br>76689 Karlsdorf-Neuthard</p>
        <p>Telefon: <a href="{TEL_LINK}">{TEL}</a><br>E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p></div>
      <div><h3>Sprechzeiten</h3>
        <table class="fuss__zeiten"><tbody><tr data-wochentag="1,2,3,4"><th scope="row">Mo–Do</th><td>08:00–19:00</td></tr><tr data-wochentag="5"><th scope="row">Fr</th><td>08:30–14:00</td></tr><tr><th scope="row">Sa, So</th><td>geschlossen</td></tr></tbody></table>
        <p style="margin-top:1rem">Notdienst: <a href="{NOTDIENST_LINK}">{NOTDIENST}</a></p></div>
      <div><h3>Leistungen</h3><ul>{lz}</ul></div>
      <div><h3>Rechtliches</h3><ul><li>{link('impressum', 'Impressum')}</li><li>{link('datenschutz', 'Datenschutzerklärung')}</li><li>{link('gleichstellung', 'Gleichstellung')}</li><li><button type="button" class="fuss__knopf" data-einwilligung-oeffnen>Cookie-Einstellungen</button></li><li>{link('kontakt', 'Kontakt')}</li><li>{KARRIERE_LINK}</li></ul>
        <h3 style="margin-top:2rem">Empfehlung &amp; Social Media</h3><ul><li><a href="{JAMEDA}" target="_blank" rel="noopener">Jameda Rezension</a></li><li><a href="{GOOGLE_BEWERTEN}" target="_blank" rel="noopener">Google Rezension</a></li><li><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a></li></ul></div>
    </div>
    <div class="fuss__unten"><span>© <span data-jahr>2026</span> {e(PRAXIS)}</span><span>Webdesign: <a href="https://ao-consult.de" target="_blank" rel="noopener">AO Consulting GmbH</a></span></div>
  </div>
</footer>
<div class="aktionsleiste" aria-label="Schnellzugriff">{knopf_tel('knopf', 'Anrufen')}{knopf_termin('knopf knopf--voll', 'Termin')}</div>
<dialog class="dialog" id="termin-dialog" aria-labelledby="termin-dialog-t"><div class="dialog__inhalt">
  <h2 id="termin-dialog-t">Online-Terminbuchung laden?</h2>
  <p>Die Terminbuchung läuft über den Dienst Dr. Flex. Beim Laden werden Ihre IP-Adresse und Geräteangaben an Dr. Flex übertragen. Mehr dazu in der {link('datenschutz', 'Datenschutzerklärung')}.</p>
  <p>Lieber persönlich? Rufen Sie uns an: <a href="{TEL_LINK}">{TEL}</a></p>
  <div class="knopfreihe"><button type="button" class="knopf knopf--voll" data-termin-ja>Terminbuchung laden</button><button type="button" class="knopf" data-dialog-zu>Abbrechen</button></div>
</div></dialog>
<dialog class="lupe" id="lupe" aria-label="Bild vergrößert"><button type="button" class="lupe__zu">Schließen</button><img src="data:," alt=""></dialog>'''

# ================================================================ JSON-LD
def jsonld():
    url = 'https://www.dr-ofner-martin.de/'
    zeiten = [
        {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday'], 'opens': '08:00', 'closes': '19:00'},
        {'@type': 'OpeningHoursSpecification', 'dayOfWeek': 'Friday', 'opens': '08:30', 'closes': '14:00'},
    ]
    graph = [
        {'@type': 'WebSite', '@id': url + '#website', 'url': url, 'name': PRAXIS, 'inLanguage': 'de-DE', 'publisher': {'@id': url + '#praxis'}},
        {'@type': ['Dentist', 'MedicalBusiness', 'LocalBusiness'], '@id': url + '#praxis', 'name': PRAXIS, 'alternateName': KURZNAME,
         'url': url, 'telephone': '+49 7251 348555', 'faxNumber': '+49 7251 348556', 'email': MAIL,
         'image': ALT + '/media/yootheme/cache/08/praxis-ofner-martin-gruppe-dres_dres-083e1bfa.jpg',
         'address': {'@type': 'PostalAddress', 'streetAddress': 'Salinenstraße 8', 'postalCode': '76689', 'addressLocality': 'Karlsdorf-Neuthard', 'addressRegion': 'Baden-Württemberg', 'addressCountry': 'DE'},
         'geo': {'@type': 'GeoCoordinates', 'latitude': 49.1335008, 'longitude': 8.5478166},
         'hasMap': GOOGLE_PROFIL, 'openingHoursSpecification': zeiten, 'foundingDate': GRUENDUNG,
         'areaServed': ['Karlsdorf-Neuthard', 'Bruchsal', 'Landkreis Karlsruhe'],
         'medicalSpecialty': ['Dentistry'], 'isAcceptingNewPatients': True, 'priceRange': '€€',
         'founder': {'@id': url + '#dr-ofner-martin'},
         'sameAs': [JAMEDA, INSTAGRAM, GOOGLE_PROFIL],
         'availableService': [{'@type': 'MedicalProcedure', 'name': t, 'url': url + '#/' + z} for z, t in LEISTUNGEN[:-1]]},
        {'@type': 'Person', '@id': url + '#dr-ofner-martin', 'name': 'Dr. med. dent. Christina Ofner-Martin', 'jobTitle': 'Zahnärztin und Praxisinhaberin', 'worksFor': {'@id': url + '#praxis'},
         'alumniOf': 'Universität Heidelberg', 'memberOf': ['Deutsche Gesellschaft für Implantologie (DGI)', 'Deutsche Gesellschaft für Ästhetische Zahnheilkunde (DGÄZ)', 'International Team for Implantology (ITI)']},
    ]
    for z, t in LEISTUNGEN:
        graph.append({'@type': 'FAQPage', '@id': url + '#/' + z + '#fragen', 'url': url + '#/' + z, 'name': 'Häufige Fragen: ' + t,
                      'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in L[z]['faq']]})
    # Hinweis: aggregateRating wird bewusst NICHT gesetzt. Google-Rezensionen als
    # eigene Bewertung auszuzeichnen kann eine manuelle Maßnahme von Google auslösen.
    return json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, indent=1)

EINWILLIGUNG_KONF = '''window.AO_EINWILLIGUNG = {
  datenschutz: '#/datenschutz',
  impressum: '#/impressum',
  kategorien: [{
    id: 'termin', name: 'Online-Terminbuchung',
    kurz: 'Lädt das Buchungsfenster von Dr. Flex, damit Sie Termine online buchen können. Erst dann wird Ihre IP-Adresse an Dr. Flex übertragen. Ohne Zustimmung erreichen Sie uns telefonisch.',
    dienste: [{ name: 'Dr. Flex', anbieter: 'Dr. Flex (Anschrift laut Datenschutzerklärung, vor Livegang ergänzen)', zweck: 'Online-Terminbuchung für die Zahnarztpraxis Dr. Ofner-Martin.', art: 'Nachladen eines Skripts von dr-flex.de, Übertragung der IP-Adresse und der Buchungsangaben.', dauer: 'Ihre Entscheidung aus diesem Fenster speichern wir 12 Monate.' }]
  }, {
    id: 'karte', name: 'Karte',
    kurz: 'Lädt die Anfahrtskarte von Google Maps. Erst dann wird Ihre IP-Adresse an Google übertragen. Ohne Zustimmung sehen Sie die Adresse als Text und einen Link zu Google Maps.',
    dienste: [{ name: 'Google Maps', anbieter: 'Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland', zweck: 'Zeigt die Lage der Praxis in Karlsdorf-Neuthard und ermöglicht die Routenplanung.', art: 'Einbettung über iframe, Übertragung der IP-Adresse und von Geräteangaben, Verarbeitung auch in den USA möglich.', dauer: 'Siehe Datenschutzerklärung von Google. Ihre Entscheidung speichern wir 12 Monate.' }]
  }, {
    id: 'video', name: 'Videos',
    kurz: 'Lädt die Informationsvideos zu Implantaten und CEREC von YouTube im erweiterten Datenschutzmodus. Erst dann wird Ihre IP-Adresse an Google übertragen.',
    dienste: [{ name: 'YouTube', anbieter: 'Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland', zweck: 'Spielt Informationsvideos zu Behandlungen ab.', art: 'Einbettung über youtube-nocookie.com, Übertragung der IP-Adresse, Verarbeitung auch in den USA möglich.', dauer: 'Siehe Datenschutzerklärung von Google. Ihre Entscheidung speichern wir 12 Monate.' }]
  }, {
    id: 'notwendig', name: 'Notwendig', pflicht: true,
    kurz: 'Hält die Website funktionsfähig und speichert Ihre Entscheidung aus diesem Fenster. Ohne diese Funktionen lässt sich die Seite nicht sinnvoll anzeigen.',
    dienste: [{ name: 'Einwilligungsspeicher', anbieter: 'Praxis für Zahnmedizin Dr. med. dent. Christina Ofner-Martin & Kollegen, Salinenstraße 8, 76689 Karlsdorf-Neuthard', zweck: 'Speichert, welchen Diensten Sie zugestimmt haben, damit Sie nicht bei jedem Aufruf erneut gefragt werden.', art: 'Lokaler Speicher im Browser, kein Cookie', dauer: '12 Monate' }]
  }]
};'''

# ================================================================ ZUSAMMENBAU
def schriften():
    teile = []
    for w in (300, 400, 500, 600, 700):
        f = FONTS / f'exo-2-latin-{w}-normal.woff2'
        teile.append(f"@font-face{{font-family:'Exo 2';font-style:normal;font-display:swap;font-weight:{w};src:url(data:font/woff2;base64,{b64(f)}) format('woff2')}}")
    return '/* Exo 2, SIL Open Font License 1.1, lokal eingebettet (keine Verbindung zu Google) */\n' + '\n'.join(teile)

def favicon_png(pfad):
    return 'data:image/png;base64,' + b64(pfad)

def bauen():
    css = schriften() + '\n' + (HIER / 'stil.css').read_text() + '\n' + (REF / 'style2.css').read_text() + '\n' + (REF / 'style3.css').read_text()
    # Eckige Formen wie auf der bisherigen Praxisseite, auch in Banner und Widget
    css += '\n:root{--ein-radius:4px}\n.ein-hinter button,.ein-hinter a[class]{border-radius:2px!important}\n.bf-panel button,.bf-schalter{border-radius:3px!important}\n'
    js_ein = (REF / 'script5.js').read_text()
    js_bf = (REF / 'script7.js').read_text()
    js = (HIER / 'skript.js').read_text()
    seiten = [s_start(), s_praxis(), s_team(), s_leistungen()] + [s_leistung(z, t) for z, t in LEISTUNGEN] + [s_aktuelles(), s_kontakt(), s_impressum(), s_datenschutz(), s_gleichstellung()]
    fav_svg = 'data:image/svg+xml;base64,' + base64.b64encode(FAVICON_SVG.encode()).decode()
    fav32 = HIER.parent / 'favicon-32.png'
    apple = HIER.parent / 'apple-touch-icon.png'
    fav_png = f'<link rel="icon" type="image/png" sizes="32x32" href="{favicon_png(fav32)}">' if fav32.exists() else ''
    apple_l = f'<link rel="apple-touch-icon" href="{favicon_png(apple)}">' if apple.exists() else ''
    doc = f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!--
  VORSCHAU dr-ofner-martin.de, AO Consulting, Stand 30.09.2026
  Eine Datei, alle Unterseiten als <main class="seite"> mit Seitenwechsel über #/kuerzel.
  Änderungswünsche bitte in dieser Datei (bzw. im Generator src/build.py) umsetzen.
  Bilder kommen vorläufig von www.dr-ofner-martin.de, siehe Kommentare BILD-PLATZHALTER.
-->
<title>Zahnarzt-Praxis Karlsdorf-Neuthard | Dr. Ofner-Martin</title>
<meta name="description" content="Zahnarzt-Praxis in Karlsdorf-Neuthard bei Bruchsal von Dr. Christina Ofner-Martin &amp; Kollegen. Ihre Zahnärztinnen für ganzheitliche Zahnmedizin.">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#333333">
<meta property="og:type" content="website">
<meta property="og:locale" content="de_DE">
<meta property="og:title" content="Zahnarzt-Praxis Karlsdorf-Neuthard | Dr. Ofner-Martin">
<meta property="og:description" content="Implantologie, Ästhetische Zahnmedizin, Kinderzahnheilkunde und Prophylaxe in Karlsdorf-Neuthard bei Bruchsal.">
<meta property="og:image" content="{ALT}/media/yootheme/cache/08/praxis-ofner-martin-gruppe-dres_dres-083e1bfa.jpg">
<link rel="icon" type="image/svg+xml" href="{fav_svg}">
{fav_png}
{apple_l}
<script>document.documentElement.classList.add('js');</script>
<style>
{css}
</style>
<script type="application/ld+json">
{jsonld()}
</script>
</head>
<body>
{kopf()}
<div id="inhalt-start" tabindex="-1"></div>
{''.join(seiten)}
{fuss()}
<script>
{EINWILLIGUNG_KONF}
</script>
<script>
{js_ein}
</script>
<script>
{js_bf}
</script>
<script>
{js}
</script>
</body>
</html>
'''
    AUS.write_text(doc, encoding='utf-8')
    return AUS

if __name__ == '__main__':
    p = bauen()
    print(p, p.stat().st_size)
