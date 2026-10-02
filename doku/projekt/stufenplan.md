---
titel: Stufenplan — Webseitenprojekt Praxis Dr. Ofner-Martin & Kollegen
kategorie: Steuerung
kurzbeschreibung: Die 8 Stufen für ein Kundenwebseiten-Projekt, mit Zwischenzielen und Start-/Abschluss-Prompts. Detaillierte Arbeitsprompts liegen in der prompt.md der jeweiligen Stufe.
stand: 2026-10-01
version: 1.0
---

# Stufenplan — 8 Stufen bis zur fehlerfreien, datenschutzsicheren Webseite

**Ziel:** www.dr-ofner-martin.de neu bzw. überarbeitet, live bis <ZIELDATUM>.

## Ablauflogik

```
S1 Fundament ─→ S2 Architektur ─→ S3 Inhalte ─→ S4 PROTOTYP ══ FREIGABE-GATE (Kunde!) ══╗
                                                                                         ║
                    ┌────────────────────────────────────────────────────────────────────╝
                    ↓
              S5 Umsetzung ──┬──→ S7 Launch ─→ S8 Betrieb (Zyklus)
                             │
              S6 Datenschutz ┘  (parallel ab Mitte S5, fertig vor S7)
```

**Das Gate in Stufe 4 ist hart:** Ohne die schriftliche Freigabe des Kunden wird Stufe 5 nicht begonnen. Beim Kundenprojekt zählt hier zusätzlich der Feedbackschleifen-Zähler aus `status.md` — die vereinbarte Zahl steht im Projektprofil.

## Die Stufen im Überblick

| # | Stufe | Fertig, wenn … | Besonderheit im Kundenprojekt |
|---|---|---|---|
| 1 | Fundament & Ist-Analyse | Zugänge, URL-Inventar, Baseline, Technikentscheidungen, Keyword-Recherche | Zusätzlich: Liste, was der Kunde liefern muss, mit Terminen — der häufigste Blocker |
| 2 | Strategie & Architektur | Botschaften, Sitemap, Conversion-Strecke, Wireframes, SEO/GEO-Strategie | Haupt-CTA laut Projektprofil; bei Patiententerminen keine Gesundheitsdaten im Formular |
| 3 | Inhalte & Texte | Alle Texte fertig, Belege-Register vollständig, FAQ, Bildbedarf | **Fachliche Freigabe durch den Kunden** — er muss prüfen, ob Leistungen korrekt beschrieben sind (Haftung!). HWG/Berufsordnung beachten |
| 4 | **Prototyp & Freigabe** | **Schriftliche Kundenfreigabe mit Datum dokumentiert** | Feedback gebündelt an diesem Gate, Schleifen zählen |
| 5 | Umsetzung & Technik | Alle Seiten gebaut, Lighthouse mobil ≥ 95, Tests protokolliert | Bei Terminbuchung: Ende-zu-Ende-Test bis ins Zielsystem |
| 6 | Datenschutz, Recht & Tracking | Netzwerkmitschnitt: nichts lädt vor Einwilligung; Pflichtangaben inkl. **berufsrechtlicher Angaben**; AV-Vertrag mit dem Kunden | HWG-Check der Texte; Bildeinwilligungen liegen vor |
| 7 | Launch & Migration | Live, 0 Redirect-Fehler, Mails kommen an, 48h-Nachkontrolle, Übergabe | Übergabe an den Kunden bzw. in den Betreuungsvertrag |
| 8 | Betrieb & Optimierung | Monatsreport, Änderungslog, Content-Nachschub | Läuft im Rahmen des Betreuungsvertrags |

## Start- und Abschluss-Prompts

**Start-Prompt (je Stufe N):**
> Starte Stufe N des Webseitenprojekts „Praxis Dr. Ofner-Martin & Kollegen". Lies `00_projekt/CLAUDE.md`, `INDEX.md`, `status.md` und `projektprofil.md`, dann arbeite den Arbeitsprompt aus `0N_stufe-N_.../prompt.md` ab.

**Abschluss-Prompt (je Stufe N):**
> Schließe Stufe N ab: prüfe die Häkchen des Zwischenziels in `0N_stufe-N_.../prompt.md`, dokumentiere offene Punkte mit Verantwortlichem und Termin, aktualisiere `INDEX.md` und setze in `status.md` Stufe N auf „fertig" und Stufe N+1 auf „nächster Schritt".

**Sonderfälle:**
- **Stufe 4:** Nicht abschließen ohne dokumentierte schriftliche Kundenfreigabe in `04_.../output/feedback-und-freigabe.md`.
- **Stufe 7:** Nicht live gehen ohne Rollback-Plan, Sicherung und Zustimmung des Kunden. Nach dem Livegang die 48-Stunden-Nachkontrolle abwarten, bevor weitergebaut wird.

## Wenn der Plan nicht hält

| Grund | Umgang |
|---|---|
| Kunde liefert Material nicht | Nachfassen dokumentieren (2× Team, dann Projektleitung). Blocker in `status.md`. Stufen, die kein Material brauchen, laufen weiter |
| Feedbackschleifen überschritten | Nicht stillschweigend schlucken: benennen, aufs Projektprofil verweisen, Entscheidung der Projektleitung einholen |
| Rechtsfrage offen | Launch ohne den betroffenen Baustein (z. B. Pixel deaktiviert), Nachrüstung nach Klärung |
