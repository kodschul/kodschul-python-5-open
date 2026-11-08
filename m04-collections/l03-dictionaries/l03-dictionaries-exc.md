# Lab 4.3 – Übung: Dictionaries

**Dauer:** ca. 20 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — drei Schwierigkeitsstufen aus einem Dictionary; das Ergebnis ist Spiel v1, die Basis für Tag 2.

**Arbeitsdatei:** `playground/guess_game.py`
**Starter:** `starters/m04-l03-guess_game.py`

## Vorbereitung

- Das eigene Spiel aus Lab 4.2 liegt in `playground/guess_game.py`. Ohne eigenen Stand: Inhalt von `starters/m04-l03-guess_game.py` komplett nach `playground/guess_game.py` kopieren.
- Die Stellen zum Ändern sind im Starter mit `# TODO Lab 4.3` markiert.

## Aufgaben

1. Ersetze `MAX_TRIES`, `NUMBER_RANGE` und die Zeile `low, high = NUMBER_RANGE` durch ein Dictionary `LEVELS` mit den Stufen `"leicht": (1, 10, 5)`, `"mittel": (1, 50, 7)` und `"schwer": (1, 100, 7)` (kleinste Zahl, größte Zahl, Versuche).
2. Frage zu Beginn jeder Runde die Stufe mit `input("Stufe (leicht/mittel/schwer): ")` ab und vereinheitliche die Eingabe mit `.strip().lower()`.
3. Frage erneut, solange die Eingabe kein Schlüssel von `LEVELS` ist, und gib dabei „Diese Stufe gibt es nicht.“ aus.
4. Entpacke die Werte der gewählten Stufe in `low, high, max_tries` und verwende `max_tries` überall, wo bisher `MAX_TRIES` stand. Nenne die Stufe in der Begrüßung der Runde.
5. Starte das Spiel, tippe zuerst eine Stufe, die es nicht gibt, und spiele dann je eine Runde auf „leicht“, „mittel“ und „schwer“.

## Checkpoint

- Eine unbekannte Stufe wie `extrem` führt zur Meldung „Diese Stufe gibt es nicht.“ und zu einer neuen Abfrage, nicht zu einem Absturz.
- „leicht“ nennt den Bereich 1 bis 10 und erlaubt 5 Versuche, „mittel“ 1 bis 50 mit 7, „schwer“ 1 bis 100 mit 7.
- Doppelte Tipps und `Bisherige Tipps:` funktionieren weiter wie in Lab 4.2.

## Abschlusskriterien

- Spiel v1 läuft: Name, Stufenwahl, Hinweise, begrenzte Versuche, doppelte Tipps erkannt, Liste der Tipps, mehrere Runden.

## Erweiterung

Berechne nach einem Treffer Punkte je Stufe: Lege ein zweites Dictionary `POINTS` mit Punkten pro übrigem Versuch an (z. B. leicht 10, mittel 20, schwer 30) und gib nach „Richtig“ die Punkte aus: Punkte der Stufe mal (Versuche der Stufe − gebrauchte Versuche + 1).
