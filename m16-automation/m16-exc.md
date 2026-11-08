# Modul 16 – Transferübung: Lernzeit-Bericht

**Einsatz:** optional, Selbstlernen; kein eigener Zeitslot
**Dauer:** ca. 30 Minuten
**Ändert die Zahlenraten-Projektbasis?** Nein — eigenständiges Automatisierungsskript, das Kommandozeile (Lab 14.2), Dateisystem (Lab 14.3), Regex (Lab 15.2), Logging (Lab 15.3), `Counter` (Lab 14.1) und Exit-Codes ohne Vorlage kombiniert. Referenz für den Aufbau: Spiel v4 mit [project/examples/m16-automation/l03-report/log_report.py](../project/examples/m16-automation/l03-report/log_report.py).
**Arbeitsdatei:** `playground/study_report.py` (neu)
**Starter:** keiner, leere Datei
**Daten:** [project/data/study/](../project/data/study/) (`study_2026-10.log`, `study_2026-11.log`, `todo.txt`)

## Ausgangslage

Eine Studentin notiert jede Lerneinheit als Zeile in einer Textdatei pro Monat:

```text
2026-11-03 19:00 Programmieren 90 min
2026-11-03 20:30 Statistik 20 min
2026-11-03 Mathe lange gelernt
```

Ein Skript soll am Sonntagabend ohne Rückfragen zusammenrechnen, wie viel Zeit seit einem Stichtag in jedes Fach geflossen ist. Zeilen ohne Uhrzeit oder ohne Minutenangabe (wie die dritte) zählen nicht, werden aber im eigenen Protokoll vermerkt. `todo.txt` ist keine Lern-Datei und bleibt außen vor.

Gewünschte Ausgabe:

```text
$ python playground/study_report.py data/study --since 2026-11-01
Lernzeit seit 2026-11-01 (2 Dateien)
  Englisch: 3 h 40 min
  Programmieren: 3 h 15 min
  Mathe: 3 h 5 min
  Statistik: 2 h 10 min
Summe: 12 h 10 min
```

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `project/`.
- Neue Datei `playground/study_report.py` anlegen. Start mit `python playground/study_report.py data/study`.

## Aufgaben

1. Schreibe `parse_args()` mit `argparse`: Positionsargument `folder` (`type=Path`), Option `--since` (`type=date.fromisoformat`) und Option `--subject` (nur ein Fach, z. B. `Mathe`).
2. Schreibe ein Regex-Muster mit den benannten Gruppen `date`, `subject` und `minutes` für Zeilen wie `2026-11-03 19:00 Programmieren 90 min` und eine Funktion `parse_line(line)`, die `(Datum als date, Fach, Minuten als int)` oder `None` zurückgibt.
3. Schreibe `main()`: Protokoll mit `logging.basicConfig(filename="study_report.log", ...)`, eine `Start:`-Zeile im Log, dann Ordner prüfen und alle `study*.log` sortiert sammeln. Fehlt der Ordner oder gibt es keine Datei, endet das Skript mit Meldung, Log-Eintrag und `sys.exit(1)`.
4. Summiere die Minuten pro Fach in einem `Counter`; überspringe Zeilen vor `--since` und, wenn angegeben, andere Fächer als `--subject`. Unpassende Zeilen landen als `WARNING` im Log. Gib die Fächer mit `most_common()` (meiste Zeit zuerst) als `Englisch: 3 h 40 min` und zum Schluss die Summe aus (`//` und `%` aus Lab 2.3).
5. Teste `data/study --since 2026-11-01`, `data/study` (ohne Stichtag), `data/study --subject Mathe`, einen Tippfehler im Ordnernamen und `data` (ein Ordner ohne `study*.log`); zeige jeweils den Exit-Code an und lies danach `study_report.log`.

## Checkpoint

- Die Ausgabe mit `--since 2026-11-01` entspricht der gewünschten Ausgabe.
- Ohne Stichtag: `Lernzeit gesamt (2 Dateien)` und `Summe: 18 h 5 min`; mit `--subject Mathe` nur die Zeile `Mathe: 3 h 25 min`.
- Tippfehler im Ordner und `data` enden mit einer Meldung und Exit-Code `1`; `--since morgen` endet mit Exit-Code `2`.
- `study_report.log` enthält pro Lauf eine `Start:`-Zeile und die übersprungene Zeile `2026-11-03 Mathe lange gelernt` als `WARNING`.

## Abschlusskriterien

- `playground/study_report.py` läuft ohne `input()`, liest nur `study*.log` und endet mit `0`, `1` oder `2` je nach Ergebnis.

## Erweiterung

Ergänze eine Option `--report`: Ist sie gesetzt (`action="store_true"`), schreibt das Skript den Bericht zusätzlich nach `study_report.txt` im aktuellen Ordner, wie `log_report.py` es mit `report.txt` tut.
