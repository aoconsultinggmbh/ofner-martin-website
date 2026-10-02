# Praxis für Zahnmedizin Dr. med. dent. Christina Ofner-Martin & Kollegen, Karlsdorf-Neuthard

Neubau von www.dr-ofner-martin.de. Entwurf von Ovidiu (v0.6, Stand 01.10.2026),
Texte 1:1 von der bisherigen Seite (A+H Praxismarketing, gekündigt).

- **Vorschau:** https://ofner-martin.vorschau.ao-consult.de
- **Ziel-Domain:** www.dr-ofner-martin.de (Domain-Anbieter und Postfächer noch zu klären)
- **Karriereseite:** https://dr-ofner-martin-karriere.de/ (eigenes Projekt, nur verlinkt)

## Aufbau

| Ordner | Inhalt |
|---|---|
| `website/` | Die Seite. **Nur was hier liegt, geht online.** Zurzeit eine Datei `index.html` mit allen Unterseiten (`#/kontakt`, `#/implantate` …) |
| `doku/quelle/` | Generator (`src/build.py`, `src/inhalt.py`, Stil, Skript), AO-Bausteine (`ref/`), Schrift, LIESMICH |
| `doku/projekt/` | Projektprofil, Status, Stufenplan |
| `.github/workflows/` | `vorschau.yml` (main → Vorschau) und `livegang.yml` (live → All-Inkl per FTPS) |

## Ändern

Änderungen immer in `doku/quelle/src/` eintragen, dann:

```
cd doku/quelle/src && python3 build.py
cp ../dr-ofner-martin-vorschau.html ../../../website/index.html
```

Nie direkt in `website/index.html` ändern, sonst ist es beim nächsten Bauen weg.

## Die zwei Zweige

- **`main`** = Vorschau. Suchmaschinen ausgesperrt. Hier passiert die Arbeit.
- **`live`** = die echte Seite. Erst wenn `live` auf den Stand von `main` gesetzt
  wird, geht etwas zum Hoster. Nur auf ausdrückliche Freigabe.

## Vor dem Livegang zu erledigen

Allgemeine Liste: `doku/checkliste-livegang.md`. Projekteigen (Stand 02.10.2026):

1. **Fotos:** Alle 44 Bilder werden noch von der alten Seite www.dr-ofner-martin.de
   geladen. Vor dem Livegang (und bevor der alte Anbieter abschaltet) eigene Kopien
   bzw. die neuen Fotos der Praxis als WebP + JPG einbauen. Zuordnung Foto → Person
   von der Praxis bestätigen lassen. Bildeinwilligungen der Mitarbeiter einholen.
2. **Einzeldatei aufteilen** in echte Unterseiten, `sitemap.xml`, `robots.txt`,
   canonical, Weiterleitungen der alten Joomla-Adressen (`.htaccess`).
3. **Formular** an `anfrage-senden.php` anbinden (verschickt zurzeit nichts),
   Empfängeradresse mit der Praxis abstimmen, Testanfrage im Postfach.
4. **Impressum:** Berufshaftpflicht, neuer Hoster, Link Berufsordnung LZK BW.
5. **Datenschutz:** Hoster + Vertrag zur Auftragsverarbeitung, Formular-Versandweg,
   Dr. Flex (Anschrift + AVV), Datum „Stand". Gesundheitsdaten-Hinweis am Formular.
6. FAQ-Antworten fachlich freigeben lassen (Heilmittelwerbegesetz).
7. Google-Bewertung (4,9 / 51, Stand 30.09.2026) aktualisieren.
8. Vom alten Webspace sichern: Rundgang `/drom-rundgang/`, `anamnese.pdf`,
   PDF „Parodontitis und Diabetes".
9. Besucherzählung: Matomo ja/nein entscheiden.
10. Entwurfs-Hinweise (gelbe Kästen) entfernen, `noindex` raus.
