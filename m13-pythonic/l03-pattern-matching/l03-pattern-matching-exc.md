# Lab 13.3 – Übung: Befehlsmenü per match

**Dauer:** ca. 20 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — beim `Tipp:` versteht das Spiel `hilfe`, `stufe schwer`, `bestenliste` und `quit`; die Stufe wird nur noch einmal am Anfang gefragt; Eingabeschleifen nutzen `:=`. Lab 14.1 baut darauf auf.
**Arbeitsdatei:** `playground/guess_game/` (geändert: `logic.py`, `players.py`, `ui.py`, `__main__.py`)
**Starter:** `starters/m13-l03-guess_game/` mit `__main__.py`, `logic.py`, `players.py`, `ui.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 13.2 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m13-pythonic/l02-context-managers/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m13-l03-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.
- Die Stellen sind im Starter mit `# TODO Lab 13.3` markiert.
- Eine alte `playground/highscores.json` löschen, damit `bestenliste` mit einer leeren Liste beginnt.

## Aufgaben

1. Ergänze in `logic.Game.__init__` die Attribute `self.next_level = level` und `self.stopped = False`, dazu eine Methode `stop()`, die `stopped` auf `True` setzt. `is_over()` gibt zusätzlich `True` zurück, wenn `self.stopped` wahr ist.
2. Ersetze in `ui.py` die Funktion `ask_number` durch `ask_command(prompt)`, die `input(prompt).strip().lower()` zurückgibt. In `players.py` liefert `HumanPlayer.next_guess()` jetzt `ui.ask_command("Tipp: ")` und `ComputerPlayer.next_guess()` den Tipp als Text: `str(guess)`.
3. Verschiebe in `ui.py` die Auswertung eines Tipps (`game.guess`, `except InvalidGuessError`, `on_hint`, Hinweise) aus der Schleife von `play_round` in eine neue Funktion `make_guess(game, number)`. Schreibe die Schleife mit `match text.split():` und den Fällen Zahl (`case [number] if number.isdigit():`), `hilfe` (neue Funktion `show_help()` mit einer Zeile pro Befehl), `stufe <stufe>` (setzt `game.next_level`, unbekannte Stufe → „Diese Stufe gibt es nicht.“), `bestenliste` (`show_highscores(game.scoreboard.top())`; bei leerer Liste gibt `show_highscores` „Noch keine Einträge.“ aus), `quit` (`game.stop()`) und `case _` mit „Bitte eine ganze Zahl oder einen Befehl eingeben (hilfe).“
4. Schreibe `ask_level()` und `ask_player_type()` mit `:=`, sodass `input` in jeder Funktion nur einmal vorkommt. Ändere `rounds()`: `ask_level()` einmal vor der Schleife, nach dem `yield` gilt `level = game.next_level`. Ergänze in `show_result` einen Zweig `elif game.stopped:` mit `Spiel beendet. Die Zahl war …`. Ergänze im Banner die Zeile „Beim Tipp versteht das Spiel auch Befehle, z. B. hilfe.“
5. Verlasse in `__main__.py` nach `ui.show_result(game, score)` die Schleife mit `break`, wenn `game.stopped` wahr ist. Starte `python -m guess_game` und gib nacheinander ein: `anna`, `mensch`, `leichtt`, `leicht`, `hilfe`, `abc`, `500`, `5`, `stufe schwer`, `stufe extrem`, `bestenliste`, danach raten bis zum Gewinn, Enter, `j`, einen Tipp und `quit`.

## Checkpoint

- `leichtt` ergibt `Diese Stufe gibt es nicht.` und dieselbe Frage noch einmal.
- `hilfe` zeigt die Befehle, `abc` die Meldung mit `(hilfe)`, `500` weiter `Der Tipp muss zwischen 1 und 10 liegen.`
- `stufe schwer` meldet `Die nächste Runde läuft auf Stufe schwer.`; nach `j` startet die Runde ohne Stufenfrage mit `Stufe schwer, Anna: Rate eine Zahl zwischen 1 und 100.`
- `bestenliste` vor dem ersten Gewinn zeigt `Noch keine Einträge.`
- `quit` zeigt `Spiel beendet. Die Zahl war …`, danach Statistik und Abschied ohne Frage `Nochmal spielen?`.
- Ein Lauf mit `computer` rät wie bisher und gewinnt.

## Abschlusskriterien

- `play_round` enthält ein `match` mit `case _` am Ende; `ask_number` gibt es nicht mehr.
- `ui.py` enthält in `ask_level` und `ask_player_type` je genau ein `input`.

## Erweiterung

Lege `playground/score_badge.py` an (im Ordner `playground/`, neben `guess_game/`) und schreibe eine Funktion `badge(score)` mit Klassenmustern für `Score`-Objekte aus `guess_game.logic`: ein Gewinn mit 1 Versuch ergibt „Volltreffer“, ein anderer Gewinn auf Stufe schwer „Profi“, jeder andere Gewinn „Geschafft“, alles Übrige „Nächstes Mal“. Teste mit vier selbst erzeugten `Score`-Objekten, z. B. `Score("Anna", "leicht", 1, 2.5, True, "2026-11-08")`. Start mit `python score_badge.py`.
