# Lab 11.4 – Review-Checkliste

Zum Abhaken beim Review des Zahlenraten-Pakets (eigener Stand in `playground/guess_game/` oder Beispiel `project/examples/m11-advanced-oop/l03-abstraction/guess_game/`). Spalte „Befund“: `ok` oder eine kurze Notiz mit Datei und Stelle. Suchen mit **Edit → Find in Files** (`Strg+Shift+F`, macOS `Cmd+Shift+F`), **files to include** auf den Paketordner gesetzt.

## Aufbau

| # | Prüfpunkt | So prüfen | Befund |
| --- | --- | --- | --- |
| 1 | Jede Datei hat eine Aufgabe: `logic` Regeln und Spieldaten, `players` Spieler, `ui` Ein-/Ausgabe, `storage` Dateien, `__main__` Ablauf | Kopfkommentar jeder Datei lesen, dann die Klassen und Funktionen darin | |
| 2 | Jede Klasse hat eine Aufgabe, die sich in einem Satz sagen lässt | Docstring der Klasse lesen: passt alles in der Klasse dazu? | |
| 3 | Kein Import im Kreis; `logic` importiert kein anderes Modul des Pakets | Suche `import`, Pfeile „wer importiert wen“ notieren | |

## Ein- und Ausgabe, Dateien

| # | Prüfpunkt | So prüfen | Befund |
| --- | --- | --- | --- |
| 4 | `input` steht nur in `ui.py` | Suche `input(` | |
| 5 | `print` steht nur in `ui.py` | Suche `print(`; Treffer in Docstrings und Kommentaren zählen nicht | |
| 6 | Dateizugriffe nur in `storage.py` | Suche `open(`, `json`, `Path`, `csv` | |
| 7 | Ein Wechsel auf eine Datenbank träfe nur eine Klasse | Wer ruft `load`, `save`, `add` auf? | |

## Klassen und Objekte

| # | Prüfpunkt | So prüfen | Befund |
| --- | --- | --- | --- |
| 8 | Interne Daten sind geschützt (`_` oder `__`, nur lesbare Properties) | In `Game` nach Attributen ohne `_` suchen, die von außen geändert werden könnten | |
| 9 | Vererbung nur bei „ist ein“, sonst Attribut („hat ein“) | Jede Klasse mit `(...)` hinter dem Namen prüfen | |
| 10 | Abstrakte Basisklasse erzwingt alle Pflichtmethoden | `Player` ansehen: welche Methoden sind `@abstractmethod`? | |
| 11 | Datenklassen nutzen `@dataclass`, Ausgabe und Vergleich über Magic Methods | `Score` ansehen | |

## Lesbarkeit

| # | Prüfpunkt | So prüfen | Befund |
| --- | --- | --- | --- |
| 12 | Gleiche Regel steht nur einmal im Code | Suche `replace(".", ",")` und nach doppelten Texten | |
| 13 | Namen sagen, was gemeint ist (englisch, `snake_case`, Klassen `CamelCase`) | Überfliegen; VS Code zeigt Ruff-Hinweise im Tab **Problems** | |
| 14 | Jede Klasse und Funktion hat einen Docstring in einem Satz | Überfliegen | |

## Ergebnis

- Klassendiagramm (Papier oder Mermaid) mit allen Klassen, Attributen, Methoden und Beziehungen.
- Zwei Verbesserungsvorschläge als Zeilen `Datei | Stelle | Beobachtung | Vorschlag`.
