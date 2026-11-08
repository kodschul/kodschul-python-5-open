# Lab 20.2 – Lösung: Showcase und Ausblick

Die Lösung zeigt ein Beispiel für die Referenzlösung Zwei-Personen-Modus aus Lab 20.1 ([code/m20-final-project/two_players.py](../../project/code/m20-final-project/two_players.py)). Eigene Pitches sehen anders aus; entscheidend ist, dass Problem, Startbefehl und Erkenntnis konkret sind.

## Aufgabe 1: 5-Zeilen-Pitch

```markdown
# Zahlenraten zu zweit
**Problem:** Das Spiel kannte nur eine Person, ein Vergleich zu zweit fehlte.
**Lösung:** `two_players.py` lässt zwei Personen nacheinander raten und kürt, wer weniger Versuche braucht.
**Start:** `python two_players.py --level leicht` im Ordner mit `guess_game/`.
**Gelernt:** Ein neues Skript kann das Paket wiederverwenden, ohne es zu ändern.
```

Weitere Beispiele für die Zeile **Gelernt**:

| Wahlaufgabe | Gelernt |
| --- | --- |
| Eigene Stufe per CLI | Weil die Stufen ein Dictionary sind, reicht eine Zeile für eine neue Stufe. |
| Zeitlimit je Tipp | Ein weiterer `case` mit Bedingung vor dem alten ändert das Verhalten, ohne den Rest anzufassen. |
| Wochenbericht | Ein gutes Log ist eine Datenquelle: Der Bericht entsteht ohne Änderung am Spiel. |

## Aufgabe 2: Demo vorbereiten

- Terminal in `playground/`, `(.venv)` sichtbar, Befehl `python two_players.py --level leicht` eingetippt.
- Schrift: **View → Appearance → Zoom In** zwei- bis dreimal.
- Code-Ausschnitt: `winner_text` in `two_players.py` (zehn Zeilen ab `# beide gewonnen`).
- Ersatz: das Bild des Laufs aus der Lösung von Lab 20.1.

## Aufgabe 3: Probe mit Timer

Beispiel für den Ablauf (gesprochen):

| Zeit | Gesagt bzw. gezeigt |
| --- | --- |
| 0:00 | „Zahlenraten konnte nur eine Person spielen. Zu zweit gab es keinen Vergleich.“ |
| 0:15 | Enter: Namen `anna`, `ben`, zwei Runden auf leicht, Ergebnis „Ben gewinnt: 2 zu 3 Versuchen.“ |
| 1:15 | `winner_text`: „Gewinn vor Verlust, sonst vergleicht `<` die Versuche, so wie beim Sortieren der Bestenliste.“ |
| 1:40 | „Gelernt: Das Paket bleibt unverändert, das Skript nutzt nur seine Bausteine. Als Nächstes: Tests mit pytest.“ |
| 1:55 | Ende |

Gekürzt wurde in der Probe: keine Erklärung von argparse, keine dritte Runde.

## Aufgabe 4: Nächster Schritt

```markdown
**Nächster Schritt:** Testen mit pytest (https://docs.pytest.org/): Tests für `winner_text` schreiben, je einen für Gewinn, Verlust und Unentschieden.
```

Weitere passende Einträge:

| Richtung | Erste Aufgabe am eigenen Spiel |
| --- | --- |
| Flask | eine Seite `/bestenliste`, die die Top 10 aus `game.db` als Tabelle zeigt |
| Jupyter | `analyze.py` in ein Notebook mit einer Zelle pro Auswertung umbauen |
| Packaging | `pyproject.toml` aus Lab 20.1 anlegen, `pip install .`, dann `guess-game --help` |
| scikit-learn | aus `rounds` vorhersagen, ob eine Runde mit Stufe und bisherigen Versuchen gewonnen wird |

## Aufgabe 5: Vorstellung

Kein festes Ergebnis. Kriterien: unter 2 Minuten, Programm läuft live (oder Ersatzbild), genau ein Code-Ausschnitt, Erkenntnis in einem Satz.

## Erweiterung

`test_logic.py` mit dem vierten Test (alle vier bestehen mit pytest 9.2.0 und Python 3.14):

```python
import pytest

from guess_game import logic, players

# ... test_valid_name, test_guess_out_of_range, test_score_points aus der Theorie ...


def test_computer_guesses_middle():
    computer = players.ComputerPlayer()
    computer.start_round(1, 100)
    assert computer.next_guess() == "50"  # Mitte von 1 bis 100
    computer.on_hint(50, "zu hoch")
    assert computer.next_guess() == "25"  # Mitte von 1 bis 49
```

```text
$ pytest -v
...
test_logic.py::test_valid_name PASSED                                    [ 25%]
test_logic.py::test_guess_out_of_range PASSED                            [ 50%]
test_logic.py::test_score_points PASSED                                  [ 75%]
test_logic.py::test_computer_guesses_middle PASSED                       [100%]

============================== 4 passed in 0.06s ===============================
```

`next_guess()` gibt Text zurück (wie eine Tastatureingabe), deshalb `"50"` statt `50`. Der Computer druckt dabei `Tipp: 50`; pytest zeigt Ausgaben nur bei fehlgeschlagenen Tests.
