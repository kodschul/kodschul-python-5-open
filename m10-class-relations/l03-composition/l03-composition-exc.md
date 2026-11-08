# Lab 10.3 – Übung: Komposition

**Dauer:** ca. 12 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — neue Klasse `Scoreboard` in `storage.py`; `Game` bekommt einen `Player` und ein `Scoreboard` und speichert selbst nichts in Dateien. Modul 11 macht aus den Ergebnissen eigene `Score`-Objekte.
**Arbeitsdatei:** `playground/guess_game/` (geändert: `storage.py`, `logic.py`, `ui.py`, `__main__.py`)
**Starter:** `starters/m10-l03-guess_game/` mit `__main__.py`, `logic.py`, `storage.py`, `ui.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 10.2 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m10-class-relations/l02-polymorphism/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m10-l03-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.
- Die Stellen für die Änderungen sind im Starter mit `# TODO Lab 10.3` markiert.

## Aufgaben

1. Schreibe in `storage.py` die Klasse `Scoreboard`: `__init__(self, path=HIGHSCORES_FILE)` speichert `self.path` und lädt `self.scores = self.load()`. Mach aus `load_highscores`, `save_highscore` und `top_five` die Methoden `load()`, `save()` (schreibt `self.scores` als JSON), `add(result)` (anhängen, dann speichern) und `top_five()`. `get_tries` und `append_history` bleiben Funktionen.
2. Ändere in `logic.py` den Kopf zu `Game.__init__(self, player, scoreboard, level="leicht")`: Speichere beide Objekte als `self.player` und `self.scoreboard`; `self.name` entfällt, `result()` nimmt den Namen aus `self.player.name`.
3. Ergänze in `Game` die Methode `save_score()`: Nur bei einem Gewinn übergibt sie `self.result()` an `self.scoreboard.add(...)`.
4. Ändere in `ui.py` die Funktion zu `play_round(game)`: Der Spieler kommt aus `game.player`; `game.name` wird überall zu `player.name`.
5. Erzeuge in `__main__.py` vor der Rundenschleife `scoreboard = storage.Scoreboard()`, pro Runde `logic.Game(player, scoreboard, level)`, rufe nach `append_history` `game.save_score()` auf und zeige bei Gewinn `scoreboard.top_five()`. Spiele eine Runde mit `computer`, beende, starte neu und gewinne eine Runde als `mensch`.

## Checkpoint

- Nach dem zweiten Start zeigt die Bestenliste beide Gewinne, sortiert nach Versuchen (z. B. Jürgen mit 1 Versuch vor Computer mit 4).
- `history.csv` hat für jede gespielte Runde eine Zeile.
- In `logic.py` kommen `open`, `json` und `Path` nicht vor (Suche mit Strg+F / Cmd+F).

## Abschlusskriterien

- `Scoreboard` hat `__init__`, `load`, `save`, `add`, `top_five`; die alten Funktionen `load_highscores`, `save_highscore`, `top_five` gibt es nicht mehr.
- `Game` erhält `player` und `scoreboard` als Objekte und speichert über `save_score()`.

## Erweiterung

Lege `playground/ebike.py` an: Eine Klasse `Battery` hat einen Ladestand `percent` (Standard 100) und eine Methode `use(amount)`, die ihn senkt, aber nie unter 0. Ein `EBike` **hat** einen Akku, der von außen übergeben wird; `ride(km)` verbraucht 2 % pro Kilometer und gibt z. B. `Stadtrad: 20 km gefahren, Akku 60 %` aus. Fahre 20 und 40 km, setze dann einen neuen Akku mit 80 % ein und fahre 10 km. Start mit `python ebike.py`.
