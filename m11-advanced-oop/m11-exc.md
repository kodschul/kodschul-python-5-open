# Modul 11 – Transferübung: Stadtbibliothek

**Einsatz:** optional, Selbstlernen; kein eigener Zeitslot
**Dauer:** ca. 30 Minuten
**Ändert die Zahlenraten-Projektbasis?** Nein — eigenständiges kleines Programm, das Klassen, Vererbung, Komposition, eigene Fehler, Magic Methods, Dataclass und abstrakte Klasse aus den Modulen 9–11 ohne Vorlage kombiniert.
**Arbeitsdatei:** `playground/library.py` (neu)
**Starter:** keiner, leere Datei
**Vorbild im Spiel:** `examples/m11-advanced-oop/l03-abstraction/guess_game/` (`Player` als abstrakte Klasse, `Score` als Dataclass mit `__str__`/`__lt__`, `Scoreboard` hält eine Liste von Objekten)

## Ausgangslage

Eine Stadtbibliothek verleiht Bücher (28 Tage) und DVDs (7 Tage). Das Programm hält den Bestand, gibt ihn nach Erscheinungsjahr sortiert aus und verbucht Ausleihen. Ein unbekannter Titel löst einen eigenen Fehler aus.

Gewünschte Ausgabe:

```text
Bestand: 4 Medien
Die Verwandlung (1915) · 28 Tage
Momo (1973) · 28 Tage
Lola rennt (1998) · 7 Tage
Good Bye, Lenin! (2003) · 7 Tage
Loan(title='Momo', member='Anna', days=28)
Loan(title='Lola rennt', member='Ben', days=7)
Titel nicht im Bestand: Harry Potter
```

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `project/`.
- Neue Datei `playground/library.py` anlegen. Start mit `python playground/library.py`.

## Aufgaben

1. Schreibe die abstrakte Klasse `Medium` (erbt von `ABC`) mit `title` und `year` und der Pflichtmethode `loan_days()`. Leite `Book` (28 Tage) und `Dvd` (7 Tage) davon ab.
2. Gib `Medium` ein `__str__` für `Momo (1973) · 28 Tage` und ein `__lt__`: älter ist kleiner, bei gleichem Jahr entscheidet der Titel.
3. Schreibe die Klasse `Library` mit den Listen `media` und `loans`, der Methode `add(medium)`, `__len__` (Anzahl der Medien) und `sorted_media()` (Medien sortiert mit `sorted`).
4. Lege die Dataclass `Loan` mit den Feldern `title`, `member`, `days` an und die Fehlerklasse `MediumNotFoundError(ValueError)`. `Library.lend(title, member)` sucht das Medium, legt ein `Loan` mit dessen Leihfrist an, speichert es in `loans` und gibt es zurück; gibt es den Titel nicht, löst sie `MediumNotFoundError("Titel nicht im Bestand: …")` aus.
5. Erzeuge unten im Skript die Bibliothek mit den vier Medien aus der Ausgangslage, gib Bestand und sortierte Liste aus, leihe „Momo“ an Anna und „Lola rennt“ an Ben aus und gib beide Ausleihen aus. Fange die Ausleihe von „Harry Potter“ mit `try`/`except MediumNotFoundError` ab.

## Checkpoint

- Die Ausgabe entspricht der gewünschten Ausgabe.
- `len(library)` liefert 4, `sorted` arbeitet ohne `key=`.
- `Medium("Ohne Art", 2000)` löst `TypeError: Can't instantiate abstract class Medium …` aus.

## Abschlusskriterien

- `playground/library.py` enthält `Medium` (abstrakt), `Book`, `Dvd`, `Loan` (Dataclass), `Library`, `MediumNotFoundError`.
- Ein unbekannter Titel bricht das Programm nicht ab, sondern zeigt die Meldung.

## Erweiterung

Ergänze in `Library` eine Methode `save_loans(path)`, die alle Ausleihen per `asdict` als JSON-Liste in die Datei `path` schreibt (wie `Scoreboard.save()` im Spiel), und rufe sie mit `Path("playground/loans.json")` auf.
