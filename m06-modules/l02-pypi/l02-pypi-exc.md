# Lab 6.2 – Übung: Farbige Hinweise mit rich

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — „Zu hoch.“ erscheint rot, „Zu niedrig.“ blau, die Gewinnzeile grün; Lab 6.3 baut darauf auf.
**Arbeitsdatei:** `playground/guess_game/ui.py`
**Starter:** `starters/m06-l02-guess_game/` mit `ui.py`

## Vorbereitung

- Terminal im Ordner `project/playground/` (`cd playground`), `.venv` aktiv.
- Das eigene Paket aus Lab 6.1 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m06-modules/l01-modules/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m06-l02-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.

## Aufgaben

1. Prüfe, dass `rich` installiert ist: `pip show rich` zeigt `Version: 15.0.0`. Fehlt es, installiere die Kurspakete mit `pip install -r ../requirements.txt` (`..` steht für den Ordner eine Ebene höher, also `project/`).
2. Importiere in `ui.py` das Ausgabe-Werkzeug `Console` aus `rich.console` (eine Zeile über `from guess_game import logic`, getrennt durch eine Leerzeile) und lege unter den Importen `console = Console()` an.
3. Ändere `show_hint`: „Zu hoch.“ mit `console.print(..., style="red")`, „Zu niedrig.“ mit `style="blue"`.
4. Gib in `play_round` die Zeile „Richtig, … Benötigte Versuche: …“ mit `console.print` und `style="green"` aus. Alle anderen Ausgaben bleiben `print`.
5. Starte mit `python -m guess_game` und spiele so, dass alle drei Farben vorkommen (einmal zu hoch, einmal zu niedrig, dann ein Treffer).

## Checkpoint

- „Zu hoch.“ ist rot, „Zu niedrig.“ blau, „Richtig, …“ grün; alle anderen Zeilen sind unverändert.
- Ohne aktive venv bricht der Start mit `ModuleNotFoundError: No module named 'rich'` ab; mit aktiver venv läuft das Spiel.

## Abschlusskriterien

- `ui.py` importiert `Console`, legt einmal `console = Console()` an und nutzt `console.print` für die drei Meldungen.

## Erweiterung

Zeige die Stufen als Tabelle: Lege `playground/levels_table.py` an, importiere `Console`, `Table` (aus `rich.table`) und `logic` aus dem eigenen Paket. Baue eine Tabelle „Schwierigkeitsstufen“ mit den Spalten Stufe, Zahlenbereich, Versuche und fülle sie in einer Schleife über `logic.LEVELS.items()`. `add_row` erwartet Text: Zahlen mit einem f-String umwandeln. Start im Ordner `playground/`: `python levels_table.py`.
