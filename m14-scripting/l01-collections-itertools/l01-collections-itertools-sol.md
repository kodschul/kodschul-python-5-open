# Lab 14.1 – Lösung: Lieblingszahl und Versuche pro Stufe

Fertiger Stand: [project/examples/m14-scripting/l01-collections-itertools/guess_game/](../../project/examples/m14-scripting/l01-collections-itertools/guess_game/). Test im Ordner `project/`: `cd examples/m14-scripting/l01-collections-itertools`, dann `python -m guess_game`.

## Aufgabe 1: favourite_numbers() mit Counter

```python
from collections import Counter, defaultdict
```

```python
def favourite_numbers(guesses, count=3):
    """Gibt die meistgetippten Zahlen als (Zahl, Anzahl) zurück: [(7, 4), ...]."""
    return Counter(guesses).most_common(count)  # Counter zählt jede Zahl
```

Der Import steht bei den anderen Standardbibliothek-Importen oben in `logic.py`. Bei gleicher Anzahl stehen die Zahlen in der Reihenfolge, in der sie zuerst getippt wurden.

## Aufgabe 2: tries_per_level() mit defaultdict

```python
def tries_per_level(scores):
    """Gruppiert die Versuche nach Stufe: {"leicht": [3, 5], "schwer": [6]}."""
    groups = defaultdict(list)  # fehlender Schlüssel -> automatisch leere Liste
    for score in scores:
        groups[score.level].append(score.tries)
    return groups
```

Beide Funktionen rechnen nur und geben zurück; die Ausgabe bleibt in `ui.py` (Aufteilung aus Lab 6.1).

## Aufgabe 3: show_session() in ui.py

```python
def show_session(favourites, groups):
    """Zeigt Lieblingszahl und Versuche pro Stufe der laufenden Sitzung."""
    print("\nDiese Sitzung")
    if favourites:  # leer, wenn niemand eine Zahl getippt hat
        number, count = favourites[0]
        print(f"Lieblingszahl: {number} ({count}-mal getippt)")
        print("Meistgetippt (Zahl, Anzahl):", favourites)
    print("Versuche pro Stufe:")
    for level in sorted(groups):
        print(f"  {level}: {groups[level]}")
```

`favourites[0]` ist das Tupel mit der höchsten Anzahl; `number, count = …` entpackt es wie in Lab 4.2.

## Aufgabe 4: Sammeln in __main__.py

```python
    played = []  # Scores aller Runden dieser Sitzung
    all_guesses = []  # alle Tipps dieser Sitzung
    # with: lädt highscores.json beim Betreten, speichert beim Verlassen
    with storage.Scoreboard("highscores.json") as board:
        for game in ui.rounds(player, board):  # eine Runde pro Durchlauf
            score = ui.play_round(game)  # @timed hat score.seconds eingetragen
            ui.show_result(game, score)
            if game.stopped:  # Befehl quit: Runde zählt nicht
                break
            played.append(score)
            all_guesses.extend(game.guesses)  # hängt alle Tipps der Runde an
            storage.append_history(score)  # jede Runde, auch verlorene
            game.save_score(score)  # nur ein Gewinn kommt in die Bestenliste
            if score.won:
                by = ui.ask_ranking()
                ui.show_highscores(board.top(by), by)
        ui.show_statistics(logic.statistics(board.scores))
    favourites = logic.favourite_numbers(all_guesses)
    ui.show_session(favourites, logic.tries_per_level(played))
    ui.show_goodbye(name, [score.tries for score in played])
```

- `extend` statt `append`: `all_guesses` bleibt eine flache Liste von Zahlen, die `Counter` zählen kann.
- `played.append(score)` steht hinter `if game.stopped: break`, also zählt eine `quit`-Runde nicht.
- Die Comprehension (Lab 12.1) ersetzt die alte Liste `all_tries`.

## Aufgabe 5: Testlauf

Zwei Runden auf `leicht` (Tipps 5, 8, 10, dann 5, 5, 10, 7, 8, 6; Seed 3), Ende der echten Ausgabe:

![Terminal: Ende einer Sitzung mit zwei Runden auf leicht, Block Diese Sitzung mit Lieblingszahl 5 (2-mal getippt) und Versuche pro Stufe leicht [3, 5]](https://raw.githubusercontent.com/kodschul/kodschul-python-5-open/assets/m14/game-l01-session.png)

_Quelle: eigener Screenshot, Kurs-Repo, 08.11.2026._

Die zweite 5 in Runde 2 lehnt das Spiel als doppelten Tipp ab (Lab 4.2); `game.guesses` enthält sie nur einmal. Deshalb steht die 5 zweimal in der Zählung: einmal pro Runde.

Erste Runde sofort mit `quit` beendet:

```text
Tipp: quit
Spiel beendet. Die Zahl war 10.
Bisherige Tipps: []

Statistik der Bestenliste
Noch keine Einträge.

Diese Sitzung
Versuche pro Stufe:
Versuche pro Runde: []
Danke fürs Spielen, Anna!
```

## Erweiterung: log_levels.py

```python
# Log-Stufen zählen und Uhrzeiten nach Stufe gruppieren

from collections import Counter, defaultdict
from pathlib import Path

levels = Counter()  # leerer Zähler, wächst Zeile für Zeile
times = defaultdict(list)
with open(Path("../data/sample.log"), encoding="utf-8") as file:
    for line in file:
        parts = line.split(" ")  # Datum, Uhrzeit, Stufe, Text
        levels[parts[2]] += 1
        times[parts[2]].append(parts[1])

print("Stufen:", levels.most_common())
for level in sorted(times):
    print(f"{level}: erste {times[level][0]}, letzte {times[level][-1]}")
```

```text
$ python log_levels.py
Stufen: [('INFO', 21), ('ERROR', 11), ('WARN', 8)]
ERROR: erste 08:05:22, letzte 08:38:44
INFO: erste 08:02:06, letzte 08:45:50
WARN: erste 08:03:51, letzte 08:44:06
```

`most_common()` ohne Zahl liefert alle Einträge, sortiert nach Anzahl. Alternative: erst alle Stufen in eine Liste sammeln und am Ende `Counter(liste)` aufrufen.
