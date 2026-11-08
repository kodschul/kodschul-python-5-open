# Lab 6.1 – Übung: Das Spiel als Paket

**Dauer:** ca. 20 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — das Spiel wird zum Paket `playground/guess_game/` und startet ab jetzt mit `python -m guess_game`; Lab 6.2 baut darauf auf.
**Arbeitsdatei:** `playground/guess_game/` (Ordner mit vier Dateien)
**Starter:** `starters/m06-l01-guess_game/` (Paket-Gerüst) und `starters/m06-l01-guess_game.py` (Spiel als eine Datei, Stand nach Lab 5.3)

## Vorbereitung

- Terminal im Ordner `project/`, `.venv` aktiv.
- Das eigene Spiel aus Lab 5.3 (oder 5.2) liegt in `playground/guess_game.py`. Ohne eigenen Stand: `starters/m06-l01-guess_game.py` öffnen, alles markieren (`Strg+A`, macOS `Cmd+A`), kopieren und damit den Inhalt von `playground/guess_game.py` ersetzen.
- Das Paket-Gerüst enthält schon `__init__.py`, in `logic.py` die neue Funktion `draw_secret` und in `ui.py` die vier kleinen Funktionen `show_banner`, `ask_name`, `ask_play_again`, `show_goodbye`. Die Stellen zum Ausfüllen sind mit `# TODO Lab 6.1` markiert.

## Aufgaben

1. Lege das Paket an: Rechtsklick im Explorer auf `starters/m06-l01-guess_game/` → **Copy**, Rechtsklick auf `playground/` → **Paste**, den eingefügten Ordner mit `F2` (macOS: `Enter`) in `guess_game` umbenennen. Benenne danach die alte Datei `playground/guess_game.py` in `guess_game_old.py` um.
2. Verschiebe die Regeln: Schneide in `guess_game_old.py` die Konstante `LEVELS` und die Funktionen `is_guess_correct` und `is_game_over` aus und füge sie in `guess_game/logic.py` an der TODO-Stelle ein.
3. Verschiebe die Ein- und Ausgabe: Schneide `ask_level`, `show_hint` und `play_round` aus und füge sie in `guess_game/ui.py` an der TODO-Stelle ein. Setze dort vor jede Regel `logic.` (`logic.LEVELS`, `logic.is_game_over`, `logic.is_guess_correct`) und ersetze `random.randint(low, high)` durch `logic.draw_secret(low, high)`.
4. Schreibe in `guess_game/__main__.py` die Funktion `main()`: Ablauf wie in der alten `main()`, aber Banner, Name, Nochmal-Frage und Abschied über `ui.show_banner()`, `ui.ask_name()`, `ui.ask_play_again()` und `ui.show_goodbye(name, all_tries)`, die Runde über `ui.play_round(name, level=level)`. Rufe `main()` am Dateiende nur innerhalb von `if __name__ == "__main__":` auf.
5. Starte das Paket: `cd playground`, dann `python -m guess_game`, eine Runde spielen. Prüfe danach im selben Terminal, dass sich die Regeln allein importieren lassen: `python -c "from guess_game import logic; print(logic.LEVELS)"`.

## Checkpoint

- `python -m guess_game` (im Ordner `playground/`) startet das Spiel; Ablauf und Texte sind dieselben wie vorher.
- `python -c "from guess_game import logic; print(logic.LEVELS)"` gibt das Dictionary der drei Stufen aus und startet kein Spiel.
- `logic.py` enthält kein `input` und kein `print`; `__main__.py` enthält kein `input` und kein `print`.
- `guess_game_old.py` wird nicht mehr gebraucht und darf gelöscht werden.

## Abschlusskriterien

- `playground/guess_game/` enthält `__init__.py`, `__main__.py`, `logic.py`, `ui.py`; das Spiel läuft mit `python -m guess_game`.

## Erweiterung

Schreibe ein eigenes Modul `playground/text_tools.py` mit zwei Funktionen: `shout(text)` gibt den Text in Großbuchstaben mit `!` zurück, `whisper(text)` in Kleinbuchstaben mit `...`. Ein Selbsttest unter `if __name__ == "__main__":` gibt je ein Beispiel aus. Importiere das Modul in `playground/use_text_tools.py` und gib `shout("hallo")` und `whisper("PSST")` aus. Starte im Terminal (Ordner `playground/`) `python text_tools.py` und `python use_text_tools.py` und vergleiche, wann der Selbsttest erscheint.
