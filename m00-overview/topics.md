# Themen: Python Programmierung

| Modul | Titel | Tag | Labs (Minuten) | Kernthemen |
| --- | --- | --- | --- | --- |
| [1](../m01-introduction/l01-overview/l01-overview-thx.md) | Python kennenlernen | 1 | 1.1 Python im Überblick (20)<br>1.2 Arbeitsumgebung (30) | Interpreter vs. Compiler, Geschichte, Einsatzgebiete, REPL, VS Code, venv |
| [2](../m02-basics/l01-syntax/l01-syntax-thx.md) | Grundlagen der Sprache | 1 | 2.1 Syntax (20)<br>2.2 Variablen und Eingabe (25)<br>2.3 Operatoren (20)<br>2.4 Strings (25) | Einrückung, PEP 8, Ruff, `int`/`float`/`str`/`bool`, `input()`, f-Strings, Vergleiche, Slicing |
| [3](../m03-control-flow/l01-conditions/l01-conditions-thx.md) | Steuerung des Programmflusses | 1 | 3.1 Bedingungen (25)<br>3.2 Zufall (15)<br>3.3 Schleifen (30)<br>3.4 Kombinieren (20) | `if`/`elif`/`else`, `random`, `while`, `for`, `range`, `break`, `while True` |
| [4](../m04-collections/l01-lists/l01-lists-thx.md) | Datensammlungen | 1 | 4.1 Listen (25)<br>4.2 Tupel und Sets (20)<br>4.3 Dictionaries (30) | Liste, Tupel, Set, Dictionary, `len`/`sorted`/`sum`, Modul `array` · **Spiel v1** |
| [5](../m05-functions/l01-basics/l01-basics-thx.md) | Eigene Funktionen | 2 | 5.1 Definieren und aufrufen (25)<br>5.2 Parameter und Rückgabe (25)<br>5.3 Laufzeitmodell (25) | `def`, `return`, Standardwerte, `*args`, Type Hints, Scope, Aufrufstapel, Rekursion |
| [6](../m06-modules/l01-modules/l01-modules-thx.md) | Module und Pakete | 2 | 6.1 Eigene Module (30)<br>6.2 PyPI und pip (30)<br>6.3 Datum und Zeit (30) | `import`, Paket, `__main__`, `python -m`, `pip`, `requirements.txt`, `rich`, `datetime` |
| [7](../m07-exceptions/l01-tracebacks/l01-tracebacks-thx.md) | Fehlerbehandlung | 2 | 7.1 Fehlermeldungen lesen (15)<br>7.2 Fehler abfangen (30)<br>7.3 Fehler auslösen (20)<br>7.4 Debuggen (25) | Traceback, `try`/`except`/`else`/`finally`, `raise`, `assert`, Haltepunkte |
| [8](../m08-files/l01-text-files/l01-text-files-thx.md) | Dateioperationen | 2 | 8.1 Textdateien (25)<br>8.2 JSON (25)<br>8.3 CSV (25) | `pathlib`, `with open`, UTF-8, `json`, `csv.DictReader` · **Spiel v2** |
| [9](../m09-oop-basics/l01-objects/l01-objects-thx.md) | Grundlagen der Objektorientierung | 3 | 9.1 Warum Objekte? (20)<br>9.2 Klassen (30)<br>9.3 Kapselung (25) | Klasse, Objekt, `__init__`, `self`, `_intern`, `@property` |
| [10](../m10-class-relations/l01-inheritance/l01-inheritance-thx.md) | Beziehungen zwischen Klassen | 3 | 10.1 Vererbung (30)<br>10.2 Polymorphie (25)<br>10.3 Komposition (20)<br>10.4 Mehrfachvererbung (15) | `super()`, eigene Fehlerklassen, Duck Typing, „hat ein“, MRO, Mixin |
| [11](../m11-advanced-oop/l01-magic-methods/l01-magic-methods-thx.md) | Fortgeschrittene Objektorientierung | 3 | 11.1 Magic Methods (30)<br>11.2 Dataclasses (25)<br>11.3 Abstrakte Klassen (20)<br>11.4 Code-Review (15) | `__str__`, `__eq__`, `__lt__`, `@dataclass`, `ABC`, Klassendiagramm |
| [12](../m12-functional/l01-comprehensions/l01-comprehensions-thx.md) | Funktionale Programmierung | 3 | 12.1 Comprehensions (25)<br>12.2 lambda, map, filter (20)<br>12.3 Generatoren (30) | Listen-/Dict-Comprehension, `key=`, `lambda`, Iterator, `yield` · **Spiel v3** |
| [13](../m13-pythonic/l01-decorators/l01-decorators-thx.md) | Pythonic Code | 4 | 13.1 Decorators (25)<br>13.2 Context Manager (20)<br>13.3 Pattern Matching (30) | `@decorator`, `functools`, `with`, `__enter__`/`__exit__`, `match`/`case`, `:=` |
| [14](../m14-scripting/l01-collections-itertools/l01-collections-itertools-thx.md) | Scripting | 4 | 14.1 collections, itertools (20)<br>14.2 Kommandozeile (30)<br>14.3 Dateisystem (40) | `Counter`, `defaultdict`, `argparse`, `glob`, `Path.copy`/`move`, Trockenlauf |
| [15](../m15-system/l01-os/l01-os-thx.md) | Betriebssystem und Textwerkzeuge | 4 | 15.1 Betriebssystem (25)<br>15.2 Reguläre Ausdrücke (40)<br>15.3 Logging (25) | Umgebungsvariablen, `subprocess`, `re`, Gruppen, `logging`, Log-Level |
| [16](../m16-automation/l01-http/l01-http-thx.md) | Remote-Zugriff und Automatisierung | 4 | 16.1 HTTP-APIs (25)<br>16.2 Lokaler Server (20)<br>16.3 Automatisierungsskript (30) | `requests`, Statuscodes, Timeout, `http.server`, Log-Auswertung · **Spiel v4** |
| [17](../m17-data-formats/l01-xml-html/l01-xml-html-thx.md) | Datenformate | 5 | 17.1 XML und HTML (25)<br>17.2 Excel (25)<br>17.3 pickle (25) | `ElementTree`, BeautifulSoup, `openpyxl`, Serialisierung |
| [18](../m18-sqlite/l01-sql/l01-sql-thx.md) | SQLite | 5 | 18.1 Datenbanken und SQL (25)<br>18.2 SQLite in Python (35)<br>18.3 Abfragen (30) | Tabelle, Primärschlüssel, `sqlite3`, Platzhalter `?`, `commit`, `GROUP BY`, `JOIN` |
| [19](../m19-data-analysis/l01-multiline-regex/l01-multiline-regex-thx.md) | Datenanalyse | 5 | 19.1 Mehrzeiliges Parsen (25)<br>19.2 NumPy und pandas (35)<br>19.3 Diagramme (30) | `re.MULTILINE`/`DOTALL`, Array, DataFrame, `groupby`, Matplotlib |
| [20](../m20-final-project/l01-game-v5/l01-game-v5-thx.md) | Abschlussprojekt | 5 | 20.1 Spiel v5 fertigstellen (50)<br>20.2 Showcase und Ausblick (25) | README, Checkliste „fertig“, Präsentation, Ausblick · **Spiel v5** |

## Transferübungen (Selbstlernen)

| Nach Modul | Übung | Lösung |
| --- | --- | --- |
| 3 | [m03-exc.md](../m03-control-flow/m03-exc.md) | [m03-sol.md](../m03-control-flow/m03-sol.md) |
| 8 | [m08-exc.md](../m08-files/m08-exc.md) | [m08-sol.md](../m08-files/m08-sol.md) |
| 11 | [m11-exc.md](../m11-advanced-oop/m11-exc.md) | [m11-sol.md](../m11-advanced-oop/m11-sol.md) |
| 16 | [m16-exc.md](../m16-automation/m16-exc.md) | [m16-sol.md](../m16-automation/m16-sol.md) |
| 19 | [m19-exc.md](../m19-data-analysis/m19-exc.md) | [m19-sol.md](../m19-data-analysis/m19-sol.md) |

Jedes Modul hat einen Spickzettel (`*-cheatsheet.md`) im Modulordner.
