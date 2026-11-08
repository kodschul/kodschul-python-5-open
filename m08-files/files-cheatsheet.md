# Dateien-Cheatsheet

Schnellreferenz für Modul 8 (Textdateien, JSON, CSV). Alle Beispiele setzen `from pathlib import Path` voraus.

## Pfade (pathlib)

| Syntax | Wirkung |
| --- | --- |
| `Path("data") / "names.txt"` | Pfad zusammensetzen, auf allen Systemen gleich |
| `Path("..") / "data"` | eine Ordnerebene höher |
| `Path.cwd()` | aktueller Ordner (dort, wo das Terminal steht) |
| `pfad.absolute()` | vollständiger Pfad ab dem Laufwerk |
| `pfad.exists()` | `True`, wenn Datei oder Ordner existiert |
| `pfad.name` | nur der Dateiname |
| `pfad.read_text(encoding="utf-8")` | ganze Datei als String |
| `pfad.write_text(text, encoding="utf-8")` | ganze Datei schreiben (ersetzt den Inhalt) |
| `os.path.join("data", "x.txt")` | ältere Schreibweise, steht in älterem Code |

## Textdateien mit open()

| Syntax | Wirkung |
| --- | --- |
| `with open(pfad, encoding="utf-8") as file:` | lesen (Modus `"r"` ist Standard); Datei wird nach dem Block geschlossen |
| `with open(pfad, "w", encoding="utf-8") as file:` | neu schreiben, vorhandener Inhalt wird gelöscht |
| `with open(pfad, "a", encoding="utf-8") as file:` | ans Ende anhängen; fehlende Datei wird angelegt |
| `file.write("Text\n")` | Text schreiben; `\n` für den Zeilenumbruch selbst setzen |
| `file.read()` | ganzer Inhalt als String |
| `file.readlines()` | Liste aller Zeilen (mit `\n`) |
| `for line in file:` | Zeile für Zeile lesen |
| `line.strip()` | Zeilenumbruch und Leerzeichen am Rand entfernen |
| `except FileNotFoundError:` | fehlende Datei beim Lesen abfangen |

## JSON

| Syntax | Wirkung |
| --- | --- |
| `import json` | Modul laden |
| `json.dump(daten, file, indent=2, ensure_ascii=False)` | Liste/Dictionary lesbar in eine Datei schreiben (Modus `"w"`) |
| `daten = json.load(file)` | aus einer Datei lesen |
| `text = json.dumps(daten)` | in einen JSON-String verwandeln |
| `daten = json.loads(text)` | aus einem JSON-String lesen |
| `True` / `False` / `None` | werden zu `true` / `false` / `null` |
| Tupel | wird zur Liste |
| Set, `datetime` | `TypeError`; vorher in Liste bzw. String umwandeln |
| `json.JSONDecodeError` | Datei ist leer oder kein gültiges JSON |

## Sortieren mit key=

| Syntax | Wirkung |
| --- | --- |
| `def get_tries(score): return score["tries"]` | Sortierschlüssel als benannte Funktion |
| `sorted(scores, key=get_tries)` | aufsteigend nach dem Rückgabewert; Funktion **ohne** `()` übergeben |
| `sorted(scores, key=get_tries, reverse=True)` | absteigend |
| `sorted(scores, key=get_tries)[:5]` | die ersten fünf |

## CSV

| Syntax | Wirkung |
| --- | --- |
| `import csv` | Modul laden |
| `open(pfad, encoding="utf-8", newline="")` | CSV immer mit `newline=""` öffnen |
| `csv.reader(file)` | jede Zeile als Liste von Strings |
| `csv.writer(file).writerow(["a", 1])` | eine Zeile aus einer Liste schreiben; setzt Anführungszeichen selbst |
| `csv.DictReader(file)` | jede Zeile als Dictionary, Schlüssel aus der Kopfzeile |
| `csv.DictWriter(file, fieldnames=spalten)` | Zeilen aus Dictionaries schreiben |
| `writer.writeheader()` | Kopfzeile schreiben (nur bei neuer Datei) |
| `writer.writerow(zeile)` | eine Zeile schreiben |
| `delimiter=";"` | Trennzeichen Semikolon (deutsches Excel) |
| `encoding="utf-8-sig"` | UTF-8 mit BOM: Excel zeigt Umlaute richtig; beim Lesen wird die BOM übersprungen |
| `float("1299,99".replace(",", "."))` | Dezimalkomma in Zahl umwandeln |
| `f"{zahl:.2f}".replace(".", ",")` | Zahl mit zwei Stellen und Komma für Excel |

## JSON oder CSV?

| Frage | Format |
| --- | --- |
| Verschachtelte Daten, Typen sollen erhalten bleiben | JSON |
| Austausch mit Web-Diensten und anderen Programmen | JSON |
| Flache Tabelle, eine Zeile pro Datensatz | CSV |
| Öffnen in Excel, LibreOffice, Numbers | CSV |
| Zeile anhängen, ohne die Datei neu zu schreiben | CSV (Modus `"a"`) |

## Typische Fehler

| Symptom | Lösung |
| --- | --- |
| `FileNotFoundError` bei relativem Pfad | Terminal-Ordner prüfen (`Path.cwd()`) |
| Datei leer nach dem Schreiben | `"a"` statt `"w"` zum Ergänzen |
| Umlaute als `Ã¼` | `encoding="utf-8"` beim Schreiben und Lesen |
| Excel zeigt alles in Spalte A | `delimiter=";"` |
| `KeyError` beim ersten Spaltennamen | `encoding="utf-8-sig"` |
| Leerzeilen in CSV (Windows) | `newline=""` |
