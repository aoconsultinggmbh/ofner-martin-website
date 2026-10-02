---
titel: LIESMICH — Webseite Praxis Dr. Ofner-Martin & Kollegen
kategorie: Technik
kurzbeschreibung: Aufbau der Vorschau-Datei, wie neu gebaut wird, Farben, Schrift, Bilder, Prüfungen und offene Punkte vor dem Livegang.
schlagworte: [Vorschau, Generator, Einzeldatei, Zahnarzt, Karlsdorf-Neuthard, SEO, GEO]
stand: 2026-10-01
version: 0.6
---

# Praxis für Zahnmedizin Dr. med. dent. Christina Ofner-Martin & Kollegen

Neubau von www.dr-ofner-martin.de (Karlsdorf-Neuthard). Die Kundin hat beim bisherigen Anbieter (A+H Praxismarketing, Joomla) gekündigt. Texte wurden 1:1 übernommen, nur Rechtschreibung und Zeichensetzung korrigiert.

## Inhalt

1. Öffnen
2. Aufbau
3. Neu bauen
4. Gestaltung
5. Bilder
6. Externe Dienste
7. Geprüft
8. Offen vor dem Livegang

## 1. Öffnen

`dr-ofner-martin-vorschau.html` per Doppelklick im Browser öffnen. Alle Unterseiten liegen in dieser einen Datei und werden über Adressen wie `#/implantate` oder `#/kontakt` umgeschaltet.

## 2. Aufbau

| Pfad | Inhalt |
|---|---|
| `dr-ofner-martin-vorschau.html` | Die fertige Vorschau, eine Datei, CSS, JS, Schrift und Logo eingebettet |
| `src/build.py` | Generator: Kopf, Fuß, alle Seiten, JSON-LD, Einwilligungs-Konfiguration, Alt-Texte (`BILDER`, `GALERIE`) |
| `src/inhalt.py` | Praxisdaten, Leistungstexte, FAQ je Leistung |
| `src/stil.css` | Gestaltung |
| `src/skript.js` | Menü, Seitenwechsel, Live-Status „Jetzt geöffnet“ (Sprechzeiten, Feiertage BW, `AUSNAHMEN` für Urlaub), Einbettungen nach Einwilligung, Dr. Flex, Galerie, Formulare |
| `ref/` | AO-Standardbausteine aus dem Marinello-Projekt: Einwilligungsbanner (`script5.js`, `style3.css`) und Barrierefreiheits-Widget (`script7.js`, `style2.css`) |
| `fonts/` | Exo 2 (300 bis 700, latin, SIL OFL) |
| `logo.svg` | Praxislogo, aus der gelieferten SVG optimiert (SharePoint, Ordner Kunden/…/Logo) |
| `favicon-32.png`, `apple-touch-icon.png` | Favicon aus dem Logo-Symbol |

Unterseiten (18): Startseite, Praxis, Team, Leistungen, Prophylaxe, Kinderzahnheilkunde, Ästhetik, Zahnerhalt, Zahnersatz, Chirurgie, Implantate, Schienentherapie, Behandlungs-Highlights, Aktuelles, Kontakt, Impressum, Datenschutz, Gleichstellung.

Karriere ist nicht Teil dieser Seite. Menü und Fußzeile verlinken „Karriere machen“ auf https://dr-ofner-martin-karriere.de/ (neuer Tab).

## 3. Neu bauen

```
cd src
python3 build.py
```

**Änderungen immer in `src/` eintragen und neu bauen**, nie direkt in der HTML-Datei, sonst gehen sie beim nächsten Lauf verloren.

## 4. Gestaltung

- Farben aus dem Logo: Orange `#ff6600` (Deko), Text-Orange `#b04400`, Knopf-Orange `#b84700` (weiße Schrift 5,1 : 1), Anthrazit `#262626`, Creme `#faf7f3`
- Eckige Formen wie auf der alten Seite (Knöpfe 2 px, Karten 4 px), Wunsch Ovidiu
- Grundschrift 18 px, ruhiges Layout, Telefon überall sichtbar (Zielgruppe ältere Patienten, Inhaberin wenig internetaffin)
- Inhalt nutzt mindestens 80 % der Breite (max. 1600 px), Burger-Menü unter 1500 px
- Hero: Teamfoto in voller Breite, Textkarte ragt von unten ins Bild, Google-Sterne und „Seit 2000“

## 5. Bilder

Vorläufig von www.dr-ofner-martin.de geladen. Jedes Bild hat einen Kommentar `BILD-PLATZHALTER … Neu als <name>.webp`. Alt-Texte sind nach Sichtprüfung der echten Fotos am 30.09.2026 gesetzt. Neue Fotos und Videos liefert die Praxis nach, dann als WebP + JPG mit diesen Namen einbauen.

## 6. Externe Dienste (alle erst nach Einwilligung)

| Dienst | Wo | Kategorie |
|---|---|---|
| Dr. Flex Terminbuchung (`medicalPracticeId=56548`) | „Termine buchen“ | termin |
| Google Maps | Kontakt | karte |
| YouTube nocookie (`NfTi9toP9a8`, `XoSoamddnBk`) | Implantate, Behandlungs-Highlights | video |

Kein Google Tag Manager, kein Analytics (die alte Seite hatte GTM).

## 7. Geprüft (Stand 01.10.2026)

Automatisiert mit Playwright, Breiten 360 bis 1920 sowie iPhone SE, 15, Pro Max, iPad mini, iPad, iPad Pro hoch und quer: kein horizontales Scrollen, eine H1 je Seite, lückenlose Überschriften, keine toten Links, JSON-LD gültig, FAQ sichtbar = Schema, keine Fremdanfrage vor Einwilligung, Banner-Knöpfe gleich groß, Formulare, Live-Status mit Feiertagen. Mit echten Fotos und in Safari noch nicht geprüft.

## 8. Offen vor dem Livegang

- Neue Fotos/Videos einbauen, Bildnachweis aktualisieren
- Vom alten Webspace sichern: virtueller Rundgang `/drom-rundgang/`, `anamnese.pdf`, PDF „Parodontitis und Diabetes“
- Impressum: Berufshaftpflicht, neuer Hoster, Link Berufsordnung LZK BW bestätigen
- Datenschutz: Hoster + AVV, Formular-Versandweg und Speicherdauer, Anschrift Dr. Flex + AVV, Datum „Stand“
- FAQ-Antworten fachlich freigeben lassen
- Google-Bewertung (4,9 / 51, Stand 30.09.2026) vor Livegang aktualisieren
- Formulare an echten Versand anbinden
- `noindex` entfernen, Unterseiten für Livegang als echte URLs ausgeben, sitemap.xml und Weiterleitungen der alten Joomla-Adressen
