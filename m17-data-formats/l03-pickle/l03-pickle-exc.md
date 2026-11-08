# Lab 17.3 – Übung: Spiel speichern und fortsetzen

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — Befehl `speichern`, Option `--resume`, `Game.__getstate__`; Lab 18.2 ersetzt danach die JSON-Bestenliste durch SQLite.
**Arbeitsdatei:** `playground/guess_game/` (`storage.py`, `logic.py`, `ui.py`, `__main__.py`)
**Starter:** `starters/m17-l03-guess_game/` mit `__main__.py`, `logic.py`, `storage.py`, `ui.py` (Spielstand nach Lab 17.2; vorbereitet sind `ui.rounds(..., game=None)`, die Anzeige „Fortsetzung“ in `play_round` und in `main()` Name und Spieler aus einem fortgesetzten Spiel)

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Die vier Dateien aus `starters/m17-l03-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen. Auch mit eigenem Stand den Starter nehmen: Er enthält die vorbereiteten Teile.
- Ohne eigenen Stand: vorher Ordner `playground/guess_game/` löschen oder umbenennen und `examples/m17-data-formats/l02-excel/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren.
- Die Stellen zum Ändern tragen den Kommentar `# TODO Lab 17.3`.

## Aufgaben

1. Importiere in `storage.py` `pickle` und lege `SAVEGAME_FILE = Path("savegame.pkl")` an. Schreibe `save_game(game, path=SAVEGAME_FILE)` (Datei mit `"wb"` öffnen, `pickle.dump`) und `load_game(path=SAVEGAME_FILE)` (Datei mit `"rb"` öffnen, `pickle.load`, danach die Datei mit `path.unlink()` löschen, Spiel zurückgeben).
2. Ergänze in `logic.py` in `Game.__init__` das Attribut `self.saved = False`. Schreibe die Methode `__getstate__(self)`: Kopie von `self.__dict__`, darin `"scoreboard"` auf `None` setzen, Kopie zurückgeben.
3. Importiere in `ui.py` zusätzlich `storage`. Ergänze in `show_help` die Zeile `speichern     Spiel speichern und beenden (weiter mit --resume)` und in `play_round` den Fall `case ["speichern"]:` (erst `storage.save_game(game)`, dann `game.saved = True`, dann `game.stop()`). Ergänze in `show_result` vor `elif game.stopped:` einen Zweig für `game.saved` mit den Meldungen `Spielstand gespeichert in savegame.pkl.` und `Weiter beim nächsten Start: python -m guess_game --resume`.
4. Ergänze in `__main__.py` die Option `--resume` (`action="store_true"`). Bei `--resume`: fehlt `storage.SAVEGAME_FILE`, die Meldung `Kein gespeichertes Spiel gefunden (savegame.pkl).` ausgeben und mit `sys.exit(1)` enden, sonst `saved_game = storage.load_game()`. Setze im `with`-Block `saved_game.scoreboard = board` (nur wenn es ein gespeichertes Spiel gibt) und verlasse die Runden-Schleife nach dem Speichern mit `break`.
5. Starte `python -m guess_game --level schwer --name Anna --player mensch`, tippe zweimal und dann `speichern`. Starte `python -m guess_game --resume` und spiele die Runde zu Ende. Starte `python -m guess_game --resume` ein zweites Mal und zeige den Exit-Code an (PowerShell: `$LASTEXITCODE`, macOS/Linux: `echo $?`).

## Checkpoint

- Nach `speichern` liegt `playground/savegame.pkl` (gut 300 Bytes) im Ordner; die Geheimzahl wird nicht verraten.
- `--resume` zeigt `Fortsetzung. Bisherige Tipps: [...]` und dieselbe Zahl verbleibender Versuche wie vor dem Speichern; es fragt nicht nach Name, Spieler oder Stufe.
- Ein Gewinn nach dem Fortsetzen landet in der Bestenliste und in `history.csv`.
- Nach dem Fortsetzen ist `savegame.pkl` verschwunden; das zweite `--resume` meldet `Kein gespeichertes Spiel gefunden (savegame.pkl).`, Exit-Code `1`.

## Abschlusskriterien

- `savegame.pkl` enthält das laufende `Game` ohne Bestenliste (`__getstate__`), und `load_game` lädt nur diese selbst geschriebene Datei.
- Der Befehl `speichern` erscheint in der Hilfe; `--resume` funktioniert genau einmal pro gespeichertem Spiel.

## Erweiterung

Schreibe in `save_game` denselben Zustand zusätzlich als `savegame.json`: `json.dump(game.__getstate__(), file, ensure_ascii=False, indent=2, default=str)`. Speichere ein Spiel, öffne beide Dateien in VS Code und vergleiche Größe, Lesbarkeit und den Eintrag `player`.
