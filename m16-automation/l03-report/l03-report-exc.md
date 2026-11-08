# Lab 16.3 – Übung: Log-Bericht

**Dauer:** ca. 22 Minuten (zu zweit)
**Ändert die Zahlenraten-Projektbasis?** Ja — neben dem Paket entsteht `log_report.py`; das Paket `guess_game/` bleibt unverändert. Das ist Spiel v4, der Endstand von Tag 4.
**Arbeitsdatei:** `playground/log_report.py` (neben `playground/guess_game/`)
**Starter:** `starters/m16-l03-log_report.py` (Gerüst); das Spiel bleibt auf dem Stand nach Lab 16.2

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel liegt in `playground/guess_game/` (Stand Lab 15.3 oder 16.2). Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen und `examples/m16-automation/l02-server/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren.
- `starters/m16-l03-log_report.py` nach `playground/` kopieren und in `log_report.py` umbenennen. `python log_report.py ../data/logs` zeigt `Noch kein Bericht: 2 Zeilen vorbereitet`.
- Testdaten: `../data/logs/` (aus `playground/` gesehen) mit drei `game*.log` und `notes.txt`; Inhalt in der Theorie.

## Aufgaben

1. Ersetze in `main()` die ersten beiden `TODO`: Ist `args.folder` kein Ordner, gibt das Skript `Ordner nicht gefunden: <ordner>` aus, schreibt `logger.error(...)` und endet mit `sys.exit(1)`. Danach sammelt `paths` alle `game*.log` des Ordners sortiert; ist die Liste leer, folgt `Keine game*.log in <ordner> gefunden.`, `logger.warning(...)` und `sys.exit(1)`.
2. Fülle `read_results(paths, since)`: Öffne jede Datei mit `encoding="utf-8"`, wende `parse_log_line` auf jede Zeile an, überspringe `None` und Spiele vor `since` (Datum mit `date.fromisoformat(result["date"])` umwandeln, nur prüfen, wenn `since` nicht `None` ist) und hänge den Rest an `results` an.
3. Fülle `build_report(...)`: Zähle mit drei `Counter` die Ergebnisse (`"result"`), die Stufen (`"level"`) und die Namen der Gewinner. Hänge die Zeilen `<n> Spiele, <g> gewonnen, häufigste Stufe: <stufe> (<k> Spiele)`, `Meiste Gewinne:` und bis zu drei Zeilen `  Anna: 6` an. Gibt es keine Ergebnisse, kommt stattdessen nur `Keine Spiele gefunden.` dazu.
4. Ersetze im letzten `TODO` von `main()` die Platzhalterzeile: Jede Berichtszeile erscheint im Terminal und landet in `REPORT_FILE`, danach folgt `Gespeichert in report.txt`.
5. Teste `python log_report.py ../data/logs --since 2026-11-01`, dann ohne `--since`, dann `python log_report.py nichtda` und `python log_report.py ../data/logs --since gestern`; zeige nach jedem Lauf den Exit-Code an (PowerShell `$LASTEXITCODE`, macOS/Linux `echo $?`). Öffne zum Schluss `log_report.log` und `report.txt`.

## Checkpoint

- `--since 2026-11-01`: `Log-Dateien: 3` und `28 Spiele, 21 gewonnen, häufigste Stufe: mittel (15 Spiele)`, Exit-Code `0`.
- Ohne `--since`: Kopfzeile `(alle Einträge)` und 38 Spiele.
- `nichtda`: `Ordner nicht gefunden: nichtda`, Exit-Code `1`; `--since gestern`: argparse-Fehler, Exit-Code `2`.
- `log_report.log` enthält für jeden Lauf außer dem mit `--since gestern` eine `Start:`-Zeile und eine Abschluss- oder Fehlerzeile; `report.txt` enthält genau den Bericht aus dem Terminal.

## Abschlusskriterien

- `playground/log_report.py` enthält kein `TODO` mehr und läuft ohne Rückfragen.
- Das Skript endet mit `0` bei Erfolg, `1` ohne Ordner oder Log-Dateien, `2` bei falschem Aufruf.

## Erweiterung

Ergänze eine Option `--top` (`type=int`, Standard 3), die festlegt, wie viele Namen unter `Meiste Gewinne:` erscheinen. Teste `python log_report.py ../data/logs --top 5` und prüfe die Hilfe mit `python log_report.py --help`.
