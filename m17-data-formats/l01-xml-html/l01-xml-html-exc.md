# Lab 17.1 – Übung: Stufen aus XML, Bestenliste als HTML

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — `logic.py` liest die Stufen aus der neuen Paketdatei `guess_game/levels.xml`, das neue Modul `export.py` schreibt `highscores.html`; Lab 17.2 ergänzt dort den Excel-Export.
**Arbeitsdatei:** `playground/guess_game/` (`logic.py`, `ui.py`, `export.py`, `__main__.py`)
**Starter:** `starters/m17-l01-guess_game/` mit `__main__.py`, `export.py`, `levels.xml`, `logic.py`, `ui.py` (Spielstand nach Lab 16.3, dazu `levels.xml` fertig und `export.py` mit vorbereitetem Seitenkopf)

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Eigenes Spiel aus Lab 16.3: die zwei Dateien `levels.xml` und `export.py` aus `starters/m17-l01-guess_game/` per **Copy**/**Paste** nach `playground/guess_game/` kopieren.
- Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m16-automation/l03-report/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m17-l01-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.
- Fehlt `playground/highscores.json` oder ist die Liste leer, zwei Runden spielen: `python -m guess_game --name Anna --level leicht --player computer`, die Frage `Bestenliste nach …` mit Enter bestätigen, `Nochmal spielen?` erst mit `j`, dann mit `n` beantworten.
- Die Stellen zum Ändern tragen den Kommentar `# TODO Lab 17.1`.

## Aufgaben

1. Öffne `guess_game/levels.xml` und vergleiche die Werte mit dem Dictionary `LEVELS` in `logic.py`. Importiere in `logic.py` `xml.etree.ElementTree as ET` und `Path`, lege `LEVELS_FILE = Path(__file__).parent / "levels.xml"` an und schreibe `load_levels(path=LEVELS_FILE)`: für jedes `<level>` die Texte von `low`, `high`, `tries` als `int` und das Attribut `name` lesen, als Dictionary zurückgeben. Ersetze das Dictionary durch `LEVELS = load_levels()` und starte `python -m guess_game --name Anna --level leicht --player computer`.
2. Ersetze in `ui.py` den festen Text `leicht/mittel/schwer` in `ask_level` und `show_help` durch `"/".join(logic.LEVELS)`. Ändere `Score.points()` in `logic.py` so, dass eine Stufe ohne Punkteregel `0` Punkte ergibt (`LEVEL_POINTS.get(...)`). Ergänze in `levels.xml` eine Stufe `extrem` (1 bis 1000, 10 Versuche) und starte `python -m guess_game --name Ben --player computer`.
3. Ergänze in `export.py` in `export_html` pro Score eine Tabellenzeile `<tr>` mit sieben Zellen `<td>` (Platz, Name, Stufe, Versuche, Dauer, Punkte, Datum); den Namen mit `html.escape(...)` einsetzen. Bei leerer Liste kommt die Zeile `<tr><td colspan="7">Noch keine Einträge.</td></tr>` in die Tabelle.
4. Ergänze in `ui.py` die Funktion `show_export(path, count)` mit der Meldung `Bestenliste exportiert: highscores.html (3 Einträge)`. Ergänze in `__main__.py` die Option `--export` mit `choices=["html"]`, die Funktion `run_export(args)` (Top 10 aus `storage.Scoreboard("highscores.json")`, dann `export.export_html` und `ui.show_export`) und in `main()` den Werkzeug-Modus direkt nach dem `--backup`-Block.
5. Starte `python -m guess_game --export html` und öffne `playground/highscores.html` im Browser (im Explorer von VS Code Rechtsklick auf die Datei → **Reveal in File Explorer** bzw. **Reveal in Finder**, dann Doppelklick). Starte danach `python -m guess_game --export pdf`.

## Checkpoint

- Nach Aufgabe 1 läuft das Spiel wie vorher; `load_levels()` liefert `{'leicht': (1, 10, 5), 'mittel': (1, 50, 7), 'schwer': (1, 100, 7)}`.
- Nach Aufgabe 2 fragt das Spiel `Stufe (leicht/mittel/schwer/extrem): `, und mit `extrem` rät der Computer zwischen 1 und 1000.
- `--export html` meldet `Bestenliste exportiert: highscores.html (…)`; der Browser zeigt die Überschrift „Bestenliste Zahlenraten“ und eine Tabelle, die beste Runde zuerst.
- `--export pdf` endet mit `invalid choice: 'pdf' (choose from html)`.

## Abschlusskriterien

- Im Code von `logic.py` steht kein Stufen-Dictionary mehr; alle Stufen kommen aus `guess_game/levels.xml`.
- `highscores.html` enthält eine Zeile pro Eintrag der Bestenliste, Namen laufen durch `html.escape`.

## Erweiterung

Schreibe `playground/cheap_items.py`, das aus `../data/shopping_items.html` mit BeautifulSoup alle Artikel unter 2 € mit ihrer Einheit ausgibt, z. B. `Orangen: 0,99 € (pro Stück)`. Die Einheit steht im Element mit `class="unit"`.
