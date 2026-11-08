# Lab 4.2 – Übung: Tupel und Sets

**Dauer:** ca. 12 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — fester Zahlenbereich als Tupel, doppelte Tipps werden erkannt; Lab 4.3 baut darauf auf.

**Arbeitsdatei:** `playground/guess_game.py`
**Starter:** `starters/m04-l02-guess_game.py`

## Vorbereitung

- Das eigene Spiel aus Lab 4.1 liegt in `playground/guess_game.py`. Ohne eigenen Stand: Inhalt von `starters/m04-l02-guess_game.py` komplett nach `playground/guess_game.py` kopieren.
- Die Stellen zum Ändern sind im Starter mit `# TODO Lab 4.2` markiert.

## Aufgaben

1. Lege unter `MAX_TRIES` ein Tupel `NUMBER_RANGE = (1, 10)` an und entpacke es nach der Namenseingabe in `low, high`.
2. Ersetze in `random.randint(1, 10)` und im Text „Rate eine Zahl zwischen 1 und 10“ die festen Zahlen durch `low` und `high`.
3. Lege zu Beginn jeder Runde, neben `guesses = []`, ein leeres Set `tried` an.
4. Prüfe direkt nach der Eingabe, ob der Tipp schon in `tried` steht: dann „Diese Zahl wurde schon getippt.“ ausgeben und mit `continue` neu fragen. Sonst den Tipp mit `add` ins Set aufnehmen. Der Versuchszähler und `append` folgen erst danach.
5. Starte das Spiel und tippe zweimal hintereinander dieselbe Zahl.

## Checkpoint

- Der doppelte Tipp erzeugt die Meldung „Diese Zahl wurde schon getippt.“.
- Nach dem doppelten Tipp erscheint keine neue Zeile „Verbleibende Versuche: …“; der Versuchszähler bleibt gleich.
- `Bisherige Tipps:` enthält jede Zahl nur einmal.
- Wird `NUMBER_RANGE` testweise auf `(1, 20)` geändert, nennt die Begrüßung den neuen Bereich.

## Abschlusskriterien

- Das Spiel läuft ohne Fehlermeldung, zieht für doppelte Tipps keinen Versuch ab und nutzt den Bereich aus dem Tupel.

## Erweiterung

Schreibe in `playground/emails.py` ein Skript, das aus einer Liste mit fünf E-Mail-Adressen (zwei davon doppelt, eine mit Großbuchstaben und Leerzeichen) die Anzahl verschiedener Adressen und die Adressen alphabetisch sortiert ausgibt.
