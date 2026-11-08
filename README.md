<div align="center">

<img src="https://raw.githubusercontent.com/kodschul/kodschul-python-5-open/assets/kodschul-logo.png" alt="Kodschul" width="220" />

# Python Programmierung: Grundlagen, Scripting und Automatisierung

5-Tage-Workshop · Python 3.14 · Deutsch

**Vom ersten `print` bis zur Datenbank: ein Spiel, fünf Ausbaustufen**

</div>

---

Im Workshop entsteht ein Zahlenratespiel. Es beginnt als einzelne Zeile, die ein Banner ausgibt, und wächst mit jedem Thema: Bedingungen, Schleifen und Listen machen es spielbar, Funktionen und Klassen ordnen den Code, Dateien und SQLite speichern die Bestenliste. Neben dem Spiel stehen zu jedem Thema kurze, einzeln startbare Beispiele.

**Für:** Einsteiger:innen ohne Programmiererfahrung
**Vorkenntnisse:** keine; Umgang mit Dateien und Ordnern am eigenen Rechner genügt
**Werkzeuge:** Python 3.14, VS Code mit den Erweiterungen „Python“ und „Ruff“

[Start](#start) · [Tag 1](#tag-1) · [Tag 2](#tag-2) · [Tag 3](#tag-3) · [Tag 4](#tag-4) · [Tag 5](#tag-5) · [Hilfe](#hilfe) · [Kursüberblick](m00-overview/overview.md)

## Start

1. Rechner einrichten: [Setup und Installation](00-setup-and-installation.md)
2. Ziel, Tagesablauf und Spielstufen lesen: [Kursüberblick](m00-overview/overview.md)
3. Kurs-Projekt kennenlernen: [project/README.md](project/README.md)
4. Im Terminal von VS Code im Ordner `project/` den ersten Test starten:

```bash
python playground/hello.py
```

## Tag 1

Python kennenlernen und das erste Spiel.

### Modul 1 · Python kennenlernen

Was Python ist, wo es eingesetzt wird und wie die Arbeitsumgebung aussieht.

- [1.1 Python im Überblick: Geschichte, Einsatz, Ausführung](m01-introduction/l01-overview/l01-overview-thx.md)
- [1.2 Arbeitsumgebung: Python, VS Code, venv](m01-introduction/l02-environment/l02-environment-thx.md)

<sub>Spickzettel: [Modul 1](m01-introduction/python-setup-cheatsheet.md)</sub>

### Modul 2 · Grundlagen der Sprache

Anweisungen, Variablen, Operatoren und Text; das Spiel begrüßt und fragt nach einem Tipp.

- [2.1 Syntax: Anweisungen, Kommentare, Einrückung](m02-basics/l01-syntax/l01-syntax-thx.md)
- [2.2 Variablen, Datentypen und Eingabe](m02-basics/l02-variables/l02-variables-thx.md)
- [2.3 Operatoren und Vergleiche](m02-basics/l03-operators/l03-operators-thx.md)
- [2.4 Strings verarbeiten](m02-basics/l04-strings/l04-strings-thx.md)

<sub>Spickzettel: [Modul 2](m02-basics/basics-cheatsheet.md)</sub>

### Modul 3 · Steuerung des Programmflusses

Entscheidungen, Zufall und Wiederholung; danach ist das Spiel über mehrere Runden spielbar.

- [3.1 Bedingte Anweisungen](m03-control-flow/l01-conditions/l01-conditions-thx.md)
- [3.2 Zufall und das erste Modul](m03-control-flow/l02-random/l02-random-thx.md)
- [3.3 Schleifen und Sprunganweisungen](m03-control-flow/l03-loops/l03-loops-thx.md)
- [3.4 Kontrollstrukturen kombinieren](m03-control-flow/l04-combining/l04-combining-thx.md)
- [Transferübung Modul 3 (optional)](m03-control-flow/m03-exc.md)

<sub>Spickzettel: [Modul 3](m03-control-flow/control-flow-cheatsheet.md)</sub>

### Modul 4 · Datensammlungen

Listen, Tupel, Sets und Dictionaries; am Ende steht Spiel v1 mit drei Schwierigkeitsstufen.

- [4.1 Listen](m04-collections/l01-lists/l01-lists-thx.md)
- [4.2 Tupel und Sets](m04-collections/l02-tuples-sets/l02-tuples-sets-thx.md)
- [4.3 Dictionaries](m04-collections/l03-dictionaries/l03-dictionaries-thx.md)

<sub>Spickzettel: [Modul 4](m04-collections/collections-cheatsheet.md)</sub>

## Tag 2

Funktionen, Module, Fehler und Dateien.

### Modul 5 · Eigene Funktionen

Eigene Funktionen mit Parametern und Rückgabewerten; das Spiel wird in Bausteine zerlegt.

- [5.1 Funktionen definieren und aufrufen](m05-functions/l01-basics/l01-basics-thx.md)
- [5.2 Parameter und Rückgabewerte](m05-functions/l02-parameters/l02-parameters-thx.md)
- [5.3 Laufzeitmodell: Namensräume, Aufrufstapel](m05-functions/l03-runtime/l03-runtime-thx.md)

<sub>Spickzettel: [Modul 5](m05-functions/functions-cheatsheet.md)</sub>

### Modul 6 · Module und Pakete

Code auf Dateien und Pakete verteilen, Pakete von PyPI installieren, mit Datum und Zeit rechnen.

- [6.1 Eigene Module und Pakete](m06-modules/l01-modules/l01-modules-thx.md)
- [6.2 Standardbibliothek, PyPI und pip](m06-modules/l02-pypi/l02-pypi-thx.md)
- [6.3 Datum und Zeit](m06-modules/l03-datetime/l03-datetime-thx.md)

<sub>Spickzettel: [Modul 6](m06-modules/modules-cheatsheet.md)</sub>

### Modul 7 · Fehlerbehandlung

Fehlermeldungen lesen, Fehler abfangen und auslösen, Logikfehler mit dem Debugger finden.

- [7.1 Fehlermeldungen lesen](m07-exceptions/l01-tracebacks/l01-tracebacks-thx.md)
- [7.2 Fehler abfangen](m07-exceptions/l02-try-except/l02-try-except-thx.md)
- [7.3 Fehler auslösen](m07-exceptions/l03-raise/l03-raise-thx.md)
- [7.4 Debuggen in VS Code](m07-exceptions/l04-debugging/l04-debugging-thx.md)

<sub>Spickzettel: [Modul 7](m07-exceptions/exceptions-cheatsheet.md)</sub>

### Modul 8 · Dateioperationen

Textdateien, JSON und CSV; die Bestenliste übersteht den Neustart (Spiel v2).

- [8.1 Dateien lesen und schreiben](m08-files/l01-text-files/l01-text-files-thx.md)
- [8.2 JSON](m08-files/l02-json/l02-json-thx.md)
- [8.3 CSV](m08-files/l03-csv/l03-csv-thx.md)
- [Transferübung Modul 8 (optional)](m08-files/m08-exc.md)

<sub>Spickzettel: [Modul 8](m08-files/files-cheatsheet.md)</sub>

## Tag 3

Objektorientierung und funktionale Werkzeuge.

### Modul 9 · Grundlagen der Objektorientierung

Klassen und Objekte, Kapselung und Properties; das Spiel wird zur Klasse.

- [9.1 Warum Objekte?](m09-oop-basics/l01-objects/l01-objects-thx.md)
- [9.2 Klassen, `__init__`, self, Methoden](m09-oop-basics/l02-classes/l02-classes-thx.md)
- [9.3 Kapselung und Properties](m09-oop-basics/l03-encapsulation/l03-encapsulation-thx.md)

<sub>Spickzettel: [Modul 9](m09-oop-basics/oop-cheatsheet.md)</sub>

### Modul 10 · Beziehungen zwischen Klassen

Vererbung, Polymorphie und Komposition; der Computer rät mit.

- [10.1 Vererbung](m10-class-relations/l01-inheritance/l01-inheritance-thx.md)
- [10.2 Polymorphie](m10-class-relations/l02-polymorphism/l02-polymorphism-thx.md)
- [10.3 Komposition](m10-class-relations/l03-composition/l03-composition-thx.md)
- [10.4 Mehrfachvererbung und Mixins](m10-class-relations/l04-multiple-inheritance/l04-multiple-inheritance-thx.md)

<sub>Spickzettel: [Modul 10](m10-class-relations/class-relations-cheatsheet.md)</sub>

### Modul 11 · Fortgeschrittene Objektorientierung

Magic Methods, Dataclasses und abstrakte Klassen; Code-Review von Spiel v3.

- [11.1 Magic Methods](m11-advanced-oop/l01-magic-methods/l01-magic-methods-thx.md)
- [11.2 Dataclasses](m11-advanced-oop/l02-dataclasses/l02-dataclasses-thx.md)
- [11.3 Abstrakte Klassen](m11-advanced-oop/l03-abstraction/l03-abstraction-thx.md)
- [11.4 Code-Review](m11-advanced-oop/l04-review/l04-review-thx.md)
- [Transferübung Modul 11 (optional)](m11-advanced-oop/m11-exc.md)

<sub>Spickzettel: [Modul 11](m11-advanced-oop/advanced-oop-cheatsheet.md)</sub>

### Modul 12 · Funktionale Programmierung

Comprehensions, Funktionen als Werte und Generatoren.

- [12.1 Comprehensions](m12-functional/l01-comprehensions/l01-comprehensions-thx.md)
- [12.2 lambda, map, filter](m12-functional/l02-lambda/l02-lambda-thx.md)
- [12.3 Iteratoren und Generatoren](m12-functional/l03-generators/l03-generators-thx.md)

<sub>Spickzettel: [Modul 12](m12-functional/functional-cheatsheet.md)</sub>

## Tag 4

Pythonic Code, Scripting und Automatisierung.

### Modul 13 · Pythonic Code

Decorators, Context Manager und Pattern Matching; das Spiel versteht Befehle.

- [13.1 Decorators](m13-pythonic/l01-decorators/l01-decorators-thx.md)
- [13.2 Context Manager](m13-pythonic/l02-context-managers/l02-context-managers-thx.md)
- [13.3 Pattern Matching und Walrus](m13-pythonic/l03-pattern-matching/l03-pattern-matching-thx.md)

<sub>Spickzettel: [Modul 13](m13-pythonic/pythonic-cheatsheet.md)</sub>

### Modul 14 · Scripting

collections, Kommandozeilen-Programme und Automatisierung im Dateisystem.

- [14.1 collections und itertools](m14-scripting/l01-collections-itertools/l01-collections-itertools-thx.md)
- [14.2 Kommandozeilen-Programme](m14-scripting/l02-argparse/l02-argparse-thx.md)
- [14.3 Dateisystem automatisieren](m14-scripting/l03-filesystem/l03-filesystem-thx.md)

<sub>Spickzettel: [Modul 14](m14-scripting/scripting-cheatsheet.md)</sub>

### Modul 15 · Betriebssystem und Textwerkzeuge

Betriebssystem, reguläre Ausdrücke und Logging.

- [15.1 Mit dem Betriebssystem arbeiten](m15-system/l01-os/l01-os-thx.md)
- [15.2 Reguläre Ausdrücke](m15-system/l02-regex/l02-regex-thx.md)
- [15.3 Logging](m15-system/l03-logging/l03-logging-thx.md)

<sub>Spickzettel: [Modul 15](m15-system/system-cheatsheet.md)</sub>

### Modul 16 · Remote-Zugriff und Automatisierung

HTTP-APIs, ein eigener lokaler Server und ein Auswertungsskript (Spiel v4).

- [16.1 HTTP-APIs](m16-automation/l01-http/l01-http-thx.md)
- [16.2 Eigener lokaler Server](m16-automation/l02-server/l02-server-thx.md)
- [16.3 Automatisierungsskript](m16-automation/l03-report/l03-report-thx.md)
- [Transferübung Modul 16 (optional)](m16-automation/m16-exc.md)

<sub>Spickzettel: [Modul 16](m16-automation/automation-cheatsheet.md)</sub>

## Tag 5

Datenformate, SQLite und Datenanalyse.

### Modul 17 · Datenformate

XML, HTML, Excel und pickle; die Bestenliste wird exportiert.

- [17.1 XML und HTML](m17-data-formats/l01-xml-html/l01-xml-html-thx.md)
- [17.2 Excel](m17-data-formats/l02-excel/l02-excel-thx.md)
- [17.3 Serialisierung mit pickle](m17-data-formats/l03-pickle/l03-pickle-thx.md)

<sub>Spickzettel: [Modul 17](m17-data-formats/data-formats-cheatsheet.md)</sub>

### Modul 18 · SQLite

Datenbanken und SQL; die Bestenliste zieht in SQLite um.

- [18.1 Datenbanken und SQL](m18-sqlite/l01-sql/l01-sql-thx.md)
- [18.2 SQLite in Python](m18-sqlite/l02-sqlite3/l02-sqlite3-thx.md)
- [18.3 Abfragen und Auswertungen](m18-sqlite/l03-queries/l03-queries-thx.md)

<sub>Spickzettel: [Modul 18](m18-sqlite/sqlite-cheatsheet.md)</sub>

### Modul 19 · Datenanalyse

Logs parsen, Daten mit pandas auswerten, Diagramme mit Matplotlib.

- [19.1 Mehrzeiliges Parsen](m19-data-analysis/l01-multiline-regex/l01-multiline-regex-thx.md)
- [19.2 NumPy und pandas](m19-data-analysis/l02-pandas/l02-pandas-thx.md)
- [19.3 Diagramme](m19-data-analysis/l03-matplotlib/l03-matplotlib-thx.md)
- [Transferübung Modul 19 (optional)](m19-data-analysis/m19-exc.md)

<sub>Spickzettel: [Modul 19](m19-data-analysis/data-analysis-cheatsheet.md)</sub>

### Modul 20 · Abschlussprojekt

Spiel v5 fertigstellen, präsentieren und den nächsten Lernschritt wählen.

- [20.1 Spiel v5 fertigstellen](m20-final-project/l01-game-v5/l01-game-v5-thx.md)
- [20.2 Showcase und Ausblick](m20-final-project/l02-showcase/l02-showcase-thx.md)

<sub>Spickzettel: [Modul 20](m20-final-project/final-project-cheatsheet.md)</sub>

## Hilfe

### Projektstand wiederherstellen

Das eigene Spiel wächst in `playground/` von Lab zu Lab. Fehlt ein Stand (Übung verpasst oder verbaut), hilft die Tabelle. Der fertige Stand jedes Labs liegt in [`project/examples/`](project/examples/); die Starter in [`project/starters/`](project/starters/) enthalten nur, was das jeweilige Lab ändert, mit `TODO`-Kommentaren an den Stellen.

| Labs | Wiederherstellen | Starten (Terminal im Ordner `project/`) |
| --- | --- | --- |
| 2.1 bis 5.3 | Starter-Datei `mNN-lNN-guess_game.py` nach `playground/guess_game.py` kopieren; sie enthält das ganze Spiel bis zum vorherigen Lab | `python playground/guess_game.py` |
| 6.1 | Ordner `starters/m06-l01-guess_game/` als `playground/guess_game/` kopieren (neues Paket) | `cd playground`, danach `python -m guess_game` |
| ab 6.2 | 1. Ordner `guess_game/` aus `examples/` des vorherigen Labs nach `playground/` kopieren. 2. Die Dateien aus `starters/mNN-lNN-guess_game/` hineinkopieren und die vorhandenen ersetzen. Labs ohne Starter-Ordner beginnen direkt mit dem Stand aus `examples/` | `cd playground`, danach `python -m guess_game` |

### Lösungen vergleichen

Jede Lösung (`-sol.md`) zeigt den fertigen Code und einen Beispiellauf. Der fertige Spielstand jedes Labs liegt in [`project/examples/`](project/examples/); die Startbefehle stehen in [project/README.md](project/README.md).

### Nachschlagen

[Glossar](m00-overview/glossary.md) · [FAQ](m00-overview/faq.md) · [Best Practices](m00-overview/best-practices.md) · [Themen](m00-overview/topics.md) · [Neu in Python 3.13–3.15](m00-overview/python-updates.md) · [Setup und häufige Probleme](00-setup-and-installation.md)

---

<div align="center">
<sub>© Nextise GmbH · <a href="https://www.kodschul.com">kodschul.com</a> · Kompetenz aufbauen – von der sicheren KI-Anwendung bis zur modernen IT-Basis</sub>
</div>
