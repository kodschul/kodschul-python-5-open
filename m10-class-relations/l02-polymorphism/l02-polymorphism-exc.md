# Lab 10.2 – Übung: Polymorphie

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — neue Klasse `ComputerPlayer` rät per Intervallhalbierung; das Spiel fragt „Wer rät? (mensch/computer)“. Lab 10.3 gibt `Game` einen Spieler und eine Bestenliste.
**Arbeitsdatei:** `playground/guess_game/` (geändert: `players.py`, `ui.py`, `__main__.py`)
**Starter:** `starters/m10-l02-guess_game/` mit `__main__.py`, `players.py`, `ui.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 10.1 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m10-class-relations/l01-inheritance/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m10-l02-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.
- Die Stellen für die Änderungen sind im Starter mit `# TODO Lab 10.2` markiert.

## Aufgaben

1. Ergänze in `players.py` die Klasse `Player`: `__init__` setzt zusätzlich `self.low = 0` und `self.high = 0`; neue Methode `start_round(self, low, high)` speichert beide Werte; neue Methode `on_hint(self, guess, hint)` tut nichts (Körper `pass`).
2. Schreibe `ComputerPlayer(Player)`: `__init__(self)` ruft `super().__init__("Computer")` auf; `next_guess` berechnet die Mitte `(self.low + self.high) // 2`, zeigt sie mit `ui.show_guess(guess)` an und gibt sie zurück.
3. Überschreibe in `ComputerPlayer` die Methode `on_hint`: Bei `"zu hoch"` wird `self.high` zu `guess - 1`, bei `"zu niedrig"` wird `self.low` zu `guess + 1`.
4. Ergänze in `ui.py` die Funktionen `ask_player_type()` (fragt „Wer rät? (mensch/computer): “ so lange, bis `mensch` oder `computer` kommt; sonst „Bitte mensch oder computer eingeben.“) und `show_guess(guess)` (druckt `Tipp: 50`). Rufe in `play_round` vor der Schleife `player.start_round(game.low, game.high)` und nach jedem gültigen Tipp `player.on_hint(guess, hint)` auf.
5. Lass in `__main__.py` nach dem Namen `ui.ask_player_type()` entscheiden: `computer` → `players.ComputerPlayer()`, sonst `players.HumanPlayer(name)`. Starte das Spiel, wähle `computer` und die Stufe `schwer`, spiele drei Runden.

## Checkpoint

- Mit `computer` tippt das Spiel selbst: bei Stufe schwer zuerst `Tipp: 50`, danach 25 oder 75 usw.
- Der Computer gewinnt jede Runde: höchstens 4 Versuche bei leicht, höchstens 7 bei schwer.
- Mit `mensch` läuft das Spiel wie in Lab 10.1; eine falsche Antwort wie `robot` wird erneut abgefragt.
- `play_round` enthält kein `if`, das nach Mensch oder Computer fragt.

## Abschlusskriterien

- `Player` hat `start_round`, `next_guess` und `on_hint`; `HumanPlayer` ist unverändert.
- `ComputerPlayer` nutzt `super().__init__("Computer")` und überschreibt `next_guess` und `on_hint`.

## Erweiterung

Schreibe in `players.py` einen `RandomPlayer`, der von `ComputerPlayer` erbt, „Zufall“ heißt und in `next_guess` eine Zufallszahl zwischen `low` und `high` tippt (`random.randint`, Lab 3.2); `on_hint` übernimmt er unverändert. Ersetze in `__main__.py` vorübergehend `players.ComputerPlayer()` durch `players.RandomPlayer()` und spiele fünf Runden auf schwer: Wie oft gewinnt der Zufall?
