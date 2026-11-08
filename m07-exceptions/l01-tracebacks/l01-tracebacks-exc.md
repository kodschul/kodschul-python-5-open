# Lab 7.1 – Übung: Fehlertabelle

**Dauer:** ca. 10 Minuten
**Ändert die Zahlenraten-Projektbasis?** Nein — die Skripte werden nur gestartet und gelesen, nicht repariert.
**Dateien:** `code/m07-exceptions/broken_1_name.py` bis `broken_5_key.py`, eigenes Spiel in `playground/guess_game/`

## Vorbereitung

- Terminal in VS Code im Ordner `project/`, `.venv` aktiv.
- Lege die Datei `playground/fehlertabelle.md` an und kopiere diese leere Tabelle hinein (oder übertrage sie auf Papier):

```text
| Skript | Fehlertyp | Zeile | Ursache in einem Satz |
| --- | --- | --- | --- |
| broken_1_name.py | | | |
| broken_2_type.py | | | |
| broken_3_value.py | | | |
| broken_4_index.py | | | |
| broken_5_key.py | | | |
| Spiel, Eingabe „sieben“ | | | |
```

## Aufgaben

1. Starte `python code/m07-exceptions/broken_1_name.py`. Lies den Traceback von unten: Trage Fehlertyp, Zeilennummer und Ursache in die Tabelle ein. Öffne erst danach die Datei und prüfe die Zeile.
2. Verfahre genauso mit `broken_2_type.py`, `broken_3_value.py` und `broken_5_key.py`.
3. Starte `broken_4_index.py`. Der Traceback hat zwei Stationen: Trage die Zeile ein, in der das Programm abbricht, und notiere zusätzlich, welche Zeile die Funktion aufgerufen hat.
4. Starte das eigene Spiel (`cd playground`, dann `python -m guess_game`) und tippe bei der ersten Frage nach einem Tipp `sieben`. Trage Datei, Zeile und Funktion der eigenen Abbruchstelle ein. Ohne eigenen Spielstand: Kopiere den Ordner `examples/m06-modules/l03-datetime/guess_game/` nach `playground/`.
5. Markiere in der Tabelle, welche der sechs Fehler Programmierfehler sind und welcher durch eine Eingabe von außen entsteht.

## Checkpoint

- Jede Zeile der Tabelle hat einen Fehlertyp, eine Zeilennummer und eine Ursache.
- Zu `broken_4_index.py` stehen zwei Zeilennummern (Abbruch und Aufruf).
- Beim Spiel zeigt die unterste eigene Datei auf `ui.py`, Funktion `play_round`.

## Abschlusskriterien

- `playground/fehlertabelle.md` (oder das Papier) enthält alle sechs Zeilen ausgefüllt.

## Erweiterung

Kopiere die fünf kaputten Skripte nach `playground/` und repariere jedes so, dass es ohne Fehler läuft. Für `broken_3_value.py`: Der Text `"4,99"` soll bleiben, die Umwandlung soll trotzdem klappen (Hinweis: `replace` aus Lab 2.4).
