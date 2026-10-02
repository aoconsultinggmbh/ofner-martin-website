---
titel: CLAUDE.md — Steuerdatei Webseitenprojekt Praxis Dr. Ofner-Martin & Kollegen
kategorie: Steuerung
kurzbeschreibung: Kompakte Arbeitsanweisung für jede Session in diesem Kundenprojekt. Aufbau, Regeln, Agenten-Team, Definition of Done.
schlagworte: [Steuerung, Arbeitsregeln, Agenten-Team, Kundenprojekt]
stand: 2026-10-01
version: 1.0
---

# CLAUDE.md — Webseitenprojekt „Praxis Dr. Ofner-Martin & Kollegen"

> **Diese Datei wird zu Beginn JEDER Session zuerst gelesen.** Danach `INDEX.md`, `status.md`, `projektprofil.md`. Erst dann wird gearbeitet.
> (In Codex heißt diese Datei AGENTS.md — Inhalt identisch.)

---

## 1. Worum es geht

Für die Praxis für Zahnmedizin Dr. med. dent. Christina Ofner-Martin & Kollegen in Karlsdorf-Neuthard wird www.dr-ofner-martin.de neu gebaut, inhaltlich wie die bisherige Seite, aber frischer, moderner und für ältere Patienten leicht bedienbar. Hauptaktion ist Anrufen oder Online-Termin über Dr. Flex. Fertig ist das Projekt, wenn die Seite fehlerfrei live ist, die alten Joomla-Adressen umgeleitet sind und der Datenschutz-Prüfbericht keine offenen Punkte hat.

**Die Seite selbst liegt in `website/`, Einstieg `website/LIESMICH.md`.** Änderungen nur im Generator `website/src/` und neu bauen.

**Alle Entscheidungen stehen in `projektprofil.md`.** Diese Datei regelt nur das *Wie* der Zusammenarbeit.

## 2. Reihenfolge beim Session-Start (verbindlich)

1. `00_projekt/CLAUDE.md` — diese Datei
2. `00_projekt/INDEX.md` — wo liegt was
3. `00_projekt/status.md` — Stand und nächster Schritt
4. `00_projekt/projektprofil.md` — die Entscheidungen, gegen die alles geprüft wird
5. Dann die laut `status.md` **nächste** Stufe: `0N_stufe-N_.../prompt.md`

## 3. Ordneraufbau

```
Projekt-Praxis Dr. Ofner-Martin & Kollegen/
├── 00_projekt/     ← CLAUDE.md · INDEX.md · status.md · stufenplan.md · projektprofil.md
├── 01_stufe-1_fundament-und-ist-analyse/
├── 02_stufe-2_strategie-und-architektur/
├── 03_stufe-3_inhalte-und-texte/
├── 04_stufe-4_prototyp-und-freigabe/     ← Freigabe-Gate
├── 05_stufe-5_umsetzung-und-technik/
├── 06_stufe-6_datenschutz-recht-tracking/
├── 07_stufe-7_launch-und-migration/
├── 08_stufe-8_betrieb-seo-geo/
└── 99_archiv/
```

Jeder Stufenordner enthält: `prompt.md` (Zwischenziel, Arbeitsprompt, häufige Fehler) · `input/` · `output/` · `notizen.md`.

## 4. Arbeitsregeln (verbindlich)

1. **Session-Start** in der Reihenfolge aus Abschnitt 2.
2. **Session-Ende:** Keine Session endet, bevor `INDEX.md` und `status.md` aktuell sind. Neue Dateien sofort in den Index.
3. **Nachfragen statt raten**, sobald eine Entscheidung das Projekt prägt oder nach außen sichtbar wird. Beim Kunden immer mit **Vorlage und Empfehlung** fragen, nicht offen — er ist Fachmann für seine Praxis, nicht für Webseiten.
4. **Ein Fakt gehört in genau eine Datei.**
5. **Keine Zahl auf die Seite, die nicht im Belege-Register mit Quelle und Freigabe steht.**
6. **Fachliche Inhalte muss der Kunde freigeben.** Bei Heilberufen ist das Haftungsthema, keine Formalie: Er muss prüfen, ob die beschriebene Leistung wirklich so angeboten wird.
7. **Rechtlicher Rahmen:** DSGVO, § 25 TDDDG (nichts lädt vor der Einwilligung), UWG — und bei Heilberufen zusätzlich **Heilmittelwerbegesetz** und **Berufsordnung**: keine Erfolgsversprechen, Vorsicht bei Vorher-Nachher-Darstellungen. Berufsrechtliche Pflichtangaben gehören ins Impressum.
8. **Gesundheitsdaten niemals im Formular.** Bei Patiententerminbuchung wird kein Behandlungsgrund und keine Beschwerde abgefragt.
9. **Bildrechte vor Verwendung.** Kein Mitarbeiterfoto ohne schriftliche Einwilligung, kein Patientenbild ohne Einwilligung.
10. **Nichts an der Live-Seite ändern, bevor Stufe 7 erreicht ist.** Bis dahin wird auf einer Vorschau-Adresse gebaut.
11. **Feedbackschleifen zählen.** Die im Projektprofil vereinbarte Zahl wird mitgeführt; wird sie überschritten, wird das benannt, nicht stillschweigend geschluckt.
12. **Kennzahlen immer mit Datum.**
13. **Sprache:** Deutsch. Anrede auf der Seite laut Projektprofil (bei Patientenseiten meist „Sie").

## 5. Agenten-Team

**Teamleiter = du, das stärkste verfügbare Modell.** Bei dir bleiben: Planung, Architektur, Technikentscheidungen, alle Texte, alles mit Rechts- oder Datenschutzbezug, Qualitätskontrolle, jede finale Entscheidung und jede Kundenkommunikation.

**Subagenten** übernehmen abgegrenzte Fleißarbeit:

| Subagent | Auftrag | Liefert |
|---|---|---|
| **Recherche** | Wettbewerber im Umkreis, Suchbegriffe und Patientenfragen, Anbietervergleiche | Stichpunktliste mit Quellen |
| **Datei-Zusammenfassung** | Kundenmaterial und Onboarding-Unterlagen eindampfen | Kurzfassung mit Quellenangabe |
| **Rohtext** | Erstfassungen für Leistungsunterseiten, FAQ, Meta-Angaben | Entwürfe zum Redigieren |
| **Inventar / Prüfung** | URL-Listen, Linkprüfung, fehlende Alt-Texte, Überschriftenhierarchie | Tabelle oder Fundliste |
| **Auswertung** | Zahlen aus Exporten in Tracker-Tabellen | gefüllte Tabelle |

**Delegationsregeln:**
- Jede Delegation nennt Ziel, nötigen Kontext, Ausgabeformat — und dass komprimiert zurückgeliefert wird.
- Jeder Subagent bekommt mit: **nur lesen, nichts ändern**, außer der Auftrag sagt ausdrücklich etwas anderes.
- Der Teamleiter prüft **jedes** Ergebnis. **Im Zweifel macht er es selbst.**
- Medizinische und rechtliche Aussagen von Subagenten werden nie ungeprüft übernommen.
- Kein Rohtext geht unredigiert in eine Output-Datei oder auf die Seite.

## 6. Definition of Done je Session

- [ ] Arbeit der Stufe liegt dokumentiert im `output/`
- [ ] `notizen.md` hält Entscheidungen und offene Punkte fest
- [ ] `INDEX.md` führt alle neuen und geänderten Dateien
- [ ] `status.md` nennt Stand, Datum, nächsten Schritt, Blocker
- [ ] Neue offene Entscheidungen stehen in `projektprofil.md`, Abschnitt 8

## 7. Wo Kontext liegt (nur lesend)

| Quelle | Wofür |
|---|---|
| `input/` der jeweiligen Stufe | Kundenmaterial, Zugänge, Onboarding-Unterlagen |
| `../../Claude Code/AO-Consulting-Bestandsaufnahme/` | Hauseigenes Fachwissen: Praxiswebseiten, Design, Bewerbermarkt, Google for Jobs, Recht |
| `../../Claude Code/AO Neukundengewinnung/` | Einwände und Formulierungen, die auch bei Patientenseiten tragen |
| `../Projekt-AO-Consulting-Webseite/` | Referenzprojekt — dort steht, wie die Stufen einmal vollständig durchlaufen wurden |

**In fremde Ordner wird nie geschrieben.**
