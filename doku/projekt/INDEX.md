---
titel: INDEX.md — Routing Projekt Praxis Dr. Ofner-Martin & Kollegen
kategorie: Steuerung
kurzbeschreibung: Wo liegt was in diesem Projekt. Jede neue Datei sofort hier eintragen.
schlagworte: [Index, Routing, Dr. Ofner-Martin, Zahnarzt, Karlsdorf-Neuthard]
stand: 2026-10-01
version: 1.0
---

# INDEX — Projekt Dr. Ofner-Martin

## Inhalt

1. Steuerung
2. Webseite
3. Stufenordner
4. Externe Quellen

## 1. Steuerung

| Pfad | Inhalt | Wofür relevant |
|---|---|---|
| `00_projekt/CLAUDE.md` | Arbeitsregeln dieses Projekts | Immer zuerst |
| `00_projekt/status.md` | Stand je Stufe, Blocker, Lieferliste, Historie | Nächster Schritt |
| `00_projekt/projektprofil.md` | Eckdaten und Grundentscheidungen | Maßstab für jede Entscheidung |
| `00_projekt/stufenplan.md` | Die 8 Stufen (aus der Vorlage) | Plan |

## 2. Webseite

| Pfad | Inhalt | Wofür relevant |
|---|---|---|
| `website/LIESMICH.md` | Aufbau, Neu bauen, Farben, Bilder, Dienste, Prüfungen, offene Punkte | **Einstieg für jede Änderung an der Seite** |
| `website/dr-ofner-martin-vorschau.html` | Fertige Vorschau, eine Datei, 18 Unterseiten | An Ovidiu und die Kundin geben |
| `website/src/build.py` | Generator mit Seiten, JSON-LD, Alt-Texten | Änderungen eintragen, dann `python3 build.py` |
| `website/src/inhalt.py` | Praxisdaten, Leistungstexte, FAQ | Texte ändern |
| `website/src/stil.css`, `website/src/skript.js` | Gestaltung, Verhalten, Sprechzeiten | Optik, Öffnungszeiten, Urlaub (`AUSNAHMEN`) |
| `website/ref/` | AO-Banner und Barrierefreiheits-Widget | Nicht direkt ändern, AO-Standard |
| `website/fonts/`, `website/logo.svg`, Favicons | Schrift, Logo, Icons | Werden eingebettet |

## 3. Stufenordner

`01_…` bis `08_…` und `99_archiv/` aus der Vorlage, bisher ohne eigene Einträge. Die Arbeit von Stufe 1 bis 4 steckt in `website/`.

## 4. Externe Quellen

| Quelle | Inhalt |
|---|---|
| https://www.dr-ofner-martin.de/ | Alte Seite, Quelle aller Texte und Bilder (wird abgeschaltet) |
| https://dr-ofner-martin-karriere.de/ | Neue Karriereseite der Praxis, verlinkt im Menü |
| SharePoint `AO Consulting GmbH/Kunden/Praxis für Zahnmedizin Dr. med. dent. Christina Ofner-Martin & Kollegen/Logo` | Original-Logo (SVG) |
| `ao-mini-os-v0.2/Claude outputs/vorschau-marinello-GESAMT-2026-09-22-0858.html` | Technische Referenz (Live-Status, Banner, Widget, Rechtsseiten) |
| Google-Unternehmensprofil (goo.gl/maps/YdyosKknx4oXfY4UA) | Sterne, Bewertungsanzahl, Koordinaten |
