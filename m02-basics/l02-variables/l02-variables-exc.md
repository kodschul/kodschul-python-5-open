# Lab 2.2 – Übung: Name und Tipp abfragen

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — das Spiel fragt Name und Tipp ab; Lab 2.3 vergleicht den Tipp mit der Geheimzahl.
**Arbeitsdatei:** `playground/guess_game.py`
**Starter:** `starters/m02-l02-guess_game.py`

## Vorbereitung

- Wer Lab 2.1 abgeschlossen hat, arbeitet in der eigenen `playground/guess_game.py` weiter. Sonst den Inhalt des Starters nach `playground/guess_game.py` kopieren.
- Terminal im Ordner `project/`, virtuelle Umgebung aktiv.

## Aufgaben

1. Frage unter dem Banner mit `input("Name: ")` den Namen ab und speichere ihn in der Variablen `name`.
2. Frage mit `input("Tipp: ")` den Tipp ab und speichere ihn in `guess_text`.
3. Wandle `guess_text` mit `int()` in eine Zahl um und speichere sie in `guess`.
4. Gib mit einem f-String „<Name> tippt <Tipp>“ aus, starte das Spiel und gib `Anna` und `7` ein.
5. Starte erneut, gib als Tipp `sieben` ein und lies die letzte Zeile der Fehlermeldung.

## Checkpoint

- Mit den Eingaben `Anna` und `7` endet die Ausgabe mit `Anna tippt 7`.
- Mit `sieben` endet das Programm mit `ValueError: invalid literal for int() with base 10: 'sieben'`.

## Abschlusskriterien

- `name` ist ein `str`, `guess` ein `int`.
- Die Ausgabe nutzt einen f-String, kein `+` zwischen Text und Zahl.

## Erweiterung

Schreibe `playground/birth_year.py`: Frage das Alter ab, wandle es in eine Zahl um, berechne mit dem festen Jahr `2026` das Geburtsjahr und gib es mit einem f-String aus. Gib zusätzlich mit `type()` die Typen von Eingabe und umgewandelter Zahl aus. Vergleich: `code/m02-basics/birth_year.py`.
