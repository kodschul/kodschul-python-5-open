# Lab 8.3 – Übung: Spielverlauf in history.csv

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — jede Runde, auch eine verlorene, landet als Zeile in `history.csv`. Damit ist Spiel v2 fertig; Tag 3 baut darauf auf.
**Arbeitsdatei:** `playground/guess_game/` (geändert: `storage.py`, `__main__.py`)
**Starter:** `starters/m08-l03-guess_game/` mit `__main__.py`, `storage.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 8.2 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m08-files/l02-json/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m08-l03-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.

## Aufgaben

1. Ergänze in `storage.py` `import csv` sowie zwei Konstanten: `HISTORY_FILE = Path("history.csv")` und `HISTORY_COLUMNS = ["Datum", "Name", "Stufe", "Versuche", "Dauer", "gewonnen"]`.
2. Schreibe `append_history(result)`. Speichere zuerst in `is_new`, ob die Datei noch fehlt. Baue dann ein Dictionary `row` mit den Spaltennamen als Schlüsseln: Dauer mit Komma statt Punkt, `gewonnen` als `"ja"` oder `"nein"` (Bedingungsausdruck aus Lab 3.1).
3. Öffne in `append_history` die Datei im Modus `"a"` mit `encoding="utf-8-sig"` und `newline=""`, erzeuge einen `csv.DictWriter` mit `fieldnames=HISTORY_COLUMNS` und `delimiter=";"`, schreibe die Kopfzeile nur, wenn `is_new` wahr ist, und dann `row`.
4. Rufe in `__main__.py` nach jeder Runde, vor der Prüfung auf `result["won"]`, `storage.append_history(result)` auf.
5. Spiele eine gewonnene und eine verlorene Runde. Öffne `playground/history.csv` in VS Code und, falls vorhanden, in Excel, LibreOffice Calc oder Numbers.

## Checkpoint

- `history.csv` beginnt mit `Datum;Name;Stufe;Versuche;Dauer;gewonnen`.
- Jede Runde ergibt eine Zeile, die verlorene mit `nein`.
- Nach einem Neustart kommen neue Zeilen dazu, die Kopfzeile steht nur einmal in der Datei.
- Ein Tabellenprogramm zeigt sechs Spalten mit Umlauten und Kommazahlen.
- Die Bestenliste aus Lab 8.2 funktioniert weiter.

## Abschlusskriterien

- `storage.py` enthält `HISTORY_FILE`, `HISTORY_COLUMNS` und `append_history` mit `csv.DictWriter`, `delimiter=";"`, `newline=""` und `utf-8-sig`.
- `__main__.py` protokolliert jede Runde, gewonnen oder verloren.

## Erweiterung

Lege `playground/win_rate.py` an: Das Skript liest `history.csv` mit `csv.DictReader` (`delimiter=";"`, `encoding="utf-8-sig"`), zählt pro Stufe die gespielten und die gewonnenen Runden in zwei Dictionaries und gibt je Stufe `leicht: 1 von 2 gewonnen (50 %)` aus. Start im Ordner `playground/` mit `python win_rate.py`.
