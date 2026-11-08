# Lab 12.1 – Lösung: Statistik der Bestenliste

Fertiger Stand: [project/examples/m12-functional/l01-comprehensions/guess_game/](../../project/examples/m12-functional/l01-comprehensions/guess_game/). Test im Ordner `project/`: `cd examples/m12-functional/l01-comprehensions`, dann `python -m guess_game`.

## Aufgabe 1: average(numbers)

```python
def average(numbers):
    """Gibt den Durchschnitt einer Zahlenliste mit einer Nachkommastelle zurück."""
    return round(sum(numbers) / len(numbers), 1)
```

`average([3, 7, 3])` ergibt `4.3`. Die Funktion steht in `logic.py`, weil sie rechnet und nichts ausgibt.

## Aufgabe 2: Gewinner als Set

```python
def statistics(scores):
    """Wertet eine Liste von Scores aus: Gewinner, Versuche, Schnitt pro Stufe."""
    # Set-Comprehension: jeder Name nur einmal
    winners = {score.name for score in scores}
```

Geschweifte Klammern mit nur einem Wert vorne ergeben ein Set: Anna mit drei Gewinnen erscheint einmal.

## Aufgabe 3: Versuche pro Spieler

```python
    # Dict-Comprehension mit Listen-Comprehension als Wert
    tries_per_player = {
        name: [score.tries for score in scores if score.name == name]
        for name in winners
    }
```

Die äußere Comprehension läuft über die Namen, die innere sammelt für jeden Namen die passenden Versuche. Ruff formatiert sie über drei Zeilen; das ist erlaubt, Python liest alles zwischen den Klammern als einen Ausdruck.

## Aufgabe 4: Durchschnitt pro Stufe und Rückgabe

```python
    levels = {score.level for score in scores}  # gespielte Stufen
    average_per_level = {
        level: average([score.tries for score in scores if score.level == level])
        for level in levels
    }
    return {
        "winners": winners,
        "tries_per_player": tries_per_player,
        "average_per_level": average_per_level,
    }
```

Über `levels` statt über `logic.LEVELS` zu laufen verhindert `ZeroDivisionError`: Eine nie gespielte Stufe hätte eine leere Liste.

Prüfung mit `data/highscores_sample.json` (Reihenfolge in Sets und daraus gebauten Dictionaries kann abweichen):

```text
{'winners': {'Computer', 'Ben', 'Anna', 'Jürgen'}, 'tries_per_player': {'Computer': [6], 'Ben': [5, 4], 'Anna': [3, 7], 'Jürgen': [2]}, 'average_per_level': {'schwer': 6.5, 'leicht': 3.0, 'mittel': 5.0}}
```

## Aufgabe 5: Ausgabe und Test

`__main__.py`, nach der Rundenschleife:

```python
        play_again = ui.ask_play_again()
    ui.show_statistics(logic.statistics(scoreboard.scores))
    ui.show_goodbye(name, all_tries)
```

`scoreboard.scores` enthält schon die neue Runde: `game.save_score()` hat sie hinzugefügt. Lauf mit vorbereiteter Bestenliste (Eingaben `anna`, `mensch`, `leicht`, `5`, `8`, `10`, `n`):

```text
Statistik der Bestenliste
Gewinner: ['Anna', 'Ben', 'Computer', 'Jürgen']
Versuche pro Spieler:
  Anna: [3, 7, 3]
  Ben: [5, 4]
  Computer: [6]
  Jürgen: [2]
Durchschnitt pro Stufe:
  leicht: 3,0 Versuche
  mittel: 5,0 Versuche
  schwer: 6,5 Versuche
Versuche pro Runde: [3]
Danke fürs Spielen, Anna!
```

Den ganzen Lauf zeigt das Bild in der Theorie. Ohne vorbereitete Datei sieht die Statistik kürzer aus, z. B. `Gewinner: ['Anna']`, `leicht: 3,0 Versuche`.

## Erweiterung

```python
names = [" Mango", "apfel ", "MANGO", "Birne"]
prices = {"mango": 1.99, "apfel": 0.45, "birne": 0.89}

clean_names = {name.strip().lower() for name in names}
print("Namen:", sorted(clean_names))

discounted = {
    name: round(price * 0.9, 2) for name, price in prices.items() if price > 0.5
}
print("Rabattpreise:", discounted)
```

```text
Namen: ['apfel', 'birne', 'mango']
Rabattpreise: {'mango': 1.79, 'birne': 0.8}
```

`prices.items()` liefert Paare aus Schlüssel und Wert (Lab 4.3); `for name, price in ...` entpackt sie. Der Apfel fehlt, weil 0,45 € die Bedingung nicht erfüllt.
