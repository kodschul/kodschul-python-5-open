# Best Practices: Python Programmierung

## Code-Stil

| Regel | Warum |
| --- | --- |
| 4 Leerzeichen pro Ebene, Ruff formatieren lassen | Einrückung ist Syntax; einheitlicher Code liest sich schneller |
| Namen klein, mit Unterstrich, sprechend: `secret_number` | Code wird öfter gelesen als geschrieben |
| Ergebnis einer String-Methode speichern | Strings sind unveränderlich |
| `input()` immer mit `int()`/`float()` umwandeln | `input()` liefert immer Text |

## Funktionen und Module

| Regel | Warum |
| --- | --- |
| Eine Aufgabe pro Funktion: prüfen oder ausgeben | kurz, testbar, wiederverwendbar |
| Daten über Parameter und `return`, nicht `global` | Datenfluss bleibt sichtbar |
| Startcode unter `if __name__ == "__main__":` | Import startet das Programm nicht mit |
| Pakete nur in der aktiven venv, gepinnt in `requirements.txt` | Installation ist wiederholbar |

## Fehler

| Regel | Warum |
| --- | --- |
| Traceback von unten lesen: was, wo, wie | die letzte Zeile nennt den Fehler |
| Gezielt abfangen (`except ValueError`), nie nackt | sonst verschwinden auch echte Bugs |
| Falsche Werte früh mit `raise` melden | lieber laut scheitern als still falsch rechnen |
| `assert` nur für eigene Annahmen, nie für Eingaben | Eingaben brauchen echte Fehlermeldungen |

## Dateien und Daten

| Regel | Warum |
| --- | --- |
| Dateien mit `with` öffnen | schließt die Datei auch bei Fehlern |
| `encoding="utf-8"` immer angeben | gleiches Ergebnis auf jedem Rechner |
| CSV mit dem Modul `csv`, nicht `split(",")` | Anführungszeichen und Kommas im Text |
| `pickle.load` nur für eigene Dateien | fremde Pickle-Dateien können Code ausführen |
| SQL-Werte nur über Platzhalter `?` | verhindert SQL-Injection |
| Nach Änderungen `commit()` | ohne `commit()` ist nichts gespeichert |

## Klassen

| Regel | Warum |
| --- | --- |
| Daten nur über Methoden ändern | Regeln bleiben im Objekt |
| Komposition vor Vererbung („hat ein“ statt „ist ein“) | flexibler, weniger feste Abhängigkeiten |
| `@dataclass` für reine Datenklassen | spart `__init__`, `__repr__`, `__eq__` |

## Skripte und Automatisierung

| Regel | Warum |
| --- | --- |
| Trockenlauf und Test an einer Kopie | Verschieben und Löschen ist nicht umkehrbar |
| Befehle als Liste, nie `shell=True` mit fremdem Text | verhindert Shell-Injection |
| `logging` statt `print` für Protokolle | Level steuern, was erscheint |
| Jede HTTP-Anfrage mit `timeout` | Skript hängt sonst ewig |
| Schlüssel und Adressen aus Umgebungsvariablen | Geheimnisse gehören nicht in den Code |
| Regex als Raw-String `r"..."` | Backslashes bleiben, wie sie sind |
