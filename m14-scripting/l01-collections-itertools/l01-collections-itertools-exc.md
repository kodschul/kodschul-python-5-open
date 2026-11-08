# Lab 14.1 – Übung: Lieblingszahl und Versuche pro Stufe

**Dauer:** ca. 13 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — am Ende jeder Sitzung zeigt das Spiel den Block „Diese Sitzung“ mit Lieblingszahl und Versuchen pro Stufe; alle späteren Starter enthalten ihn.
**Arbeitsdatei:** `playground/guess_game/` (geändert: `logic.py`, `ui.py`, `__main__.py`)
**Starter:** `starters/m14-l01-guess_game/` mit `__main__.py`, `logic.py`, `ui.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 13.3 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m13-pythonic/l03-pattern-matching/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m14-l01-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.

## Aufgaben

1. Importiere in `logic.py` oben `Counter` und `defaultdict` aus `collections`. Schreibe an der Stelle `# TODO Lab 14.1` die Funktion `favourite_numbers(guesses, count=3)`: Sie gibt die `count` meistgetippten Zahlen als Liste von Tupeln `(Zahl, Anzahl)` zurück.
2. Schreibe darunter `tries_per_level(scores)`: Sie gruppiert die Versuche aller `Score`-Objekte nach Stufe (`score.level` → Liste von `score.tries`) und gibt das `defaultdict` zurück.
3. Schreibe in `ui.py` an der Stelle `# TODO Lab 14.1` die Funktion `show_session(favourites, groups)`. Sie gibt aus:

   ```text

   Diese Sitzung
   Lieblingszahl: 5 (2-mal getippt)
   Meistgetippt (Zahl, Anzahl): [(5, 2), (8, 2), (10, 2)]
   Versuche pro Stufe:
     leicht: [3, 5]
   ```

   Die beiden Zeilen zur Lieblingszahl erscheinen nur, wenn `favourites` nicht leer ist; das erste Tupel entpacken mit `number, count = favourites[0]`. Die Stufen alphabetisch mit `sorted(groups)` durchlaufen.
4. Ersetze in `__main__.py` die Liste `all_tries` durch zwei Listen: `played` (pro Runde `played.append(score)`) und `all_guesses` (pro Runde `all_guesses.extend(game.guesses)`). Rufe nach dem `with`-Block `ui.show_session(...)` mit `logic.favourite_numbers(all_guesses)` und `logic.tries_per_level(played)` auf und übergib `show_goodbye` die Liste `[score.tries for score in played]`.
5. Starte `python -m guess_game`, spiele zwei Runden auf `leicht` und tippe dabei eine Zahl in beiden Runden. Starte danach noch einmal und beende die erste Runde sofort mit `quit`.

## Checkpoint

- Nach zwei Runden steht am Ende `Diese Sitzung`, eine Zeile `Lieblingszahl: … (2-mal getippt)` und `Versuche pro Stufe:` mit `leicht: [x, y]`.
- `Versuche pro Runde:` zeigt dieselben Zahlen wie die Zeile `leicht:`.
- Nach `quit` in der ersten Runde zeigt `Diese Sitzung` nur `Versuche pro Stufe:` ohne Lieblingszahl, und das Spiel endet ohne Traceback.

## Abschlusskriterien

- `logic.py` enthält `Counter(...).most_common(...)` und `defaultdict(list)`, aber kein `print`.
- `__main__.py` enthält kein `all_tries` mehr.

## Erweiterung

Lege `playground/log_levels.py` an: Das Skript liest `../data/sample.log` Zeile für Zeile (Aufbau: Datum, Uhrzeit, Stufe, Text), zählt mit einem `Counter`, wie oft jede Stufe (`INFO`, `WARN`, `ERROR`) vorkommt, und sammelt mit `defaultdict(list)` die Uhrzeiten je Stufe. Ausgabe: die Stufen nach Häufigkeit und pro Stufe die erste und die letzte Uhrzeit. Start im Ordner `playground/` mit `python log_levels.py`.
