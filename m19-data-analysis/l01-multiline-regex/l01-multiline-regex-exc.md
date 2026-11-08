# Lab 19.1 – Übung: Spiel-Log importieren

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — neben dem Paket entsteht `import_log.py`; `game.db` bekommt die Tabelle `log_rounds`. Das Paket `guess_game/` bleibt unverändert, Lab 19.2 baut nicht darauf auf.
**Arbeitsdatei:** `playground/import_log.py` (neben `playground/guess_game/`)
**Starter:** `starters/m19-l01-import_log.py` (Gerüst); das Spiel bleibt auf dem Stand nach Lab 18.3

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel liegt in `playground/guess_game/` (Stand Lab 18.3). Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen und `examples/m18-sqlite/l03-queries/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren.
- `starters/m19-l01-import_log.py` nach `playground/` kopieren und in `import_log.py` umbenennen.

## Aufgaben

1. Spiele zwei Sitzungen, damit `game.log` passende Runden enthält: `python -m guess_game --level schwer --name Anna --player mensch` (erste Runde zu Ende spielen, Enter bei der Bestenliste, mit `j` weiter, in der zweiten Runde nach zwei Tipps `quit`), dann `python -m guess_game --level leicht --name Ben --player computer` (Enter bei der Bestenliste, dann `n`). Öffne `game.log` und suche die „Neue Runde“-Zeile der `quit`-Runde.
2. Starte `python import_log.py`. Das Gerüst meldet noch `0 Runden gefunden`.
3. Ersetze den Platzhalter `ROUND_PATTERN` durch ein Muster mit `re.MULTILINE | re.VERBOSE`: Anfangszeile mit den Gruppen `started` (Datum und Uhrzeit) und `level`, danach die Gruppe `body` mit beliebig vielen, aber so wenigen DEBUG-Zeilen wie möglich, zum Schluss die Ergebniszeile mit `result` (`Gewonnen|Verloren`), `name`, `tries` und `seconds`. Vorlage für die Zeilen ist der Kommentarblock über dem Muster.
4. Fülle `parse_rounds(text)`: Wandle jeden Treffer von `ROUND_PATTERN.finditer(text)` mit `groupdict()` in ein Dictionary um, ersetze `body` durch `guesses` (Tipps mit `GUESS_PATTERN.findall`, verbunden mit `" ".join`), mache `tries` zur Zahl, `seconds` zur Kommazahl (`"0,0"` → `0.0`) und ersetze `result` durch `won` (`True`/`False`).
5. Starte `python import_log.py` zweimal hintereinander und prüfe die Tabelle mit `python -m sqlite3 game.db "SELECT * FROM log_rounds"`.

## Checkpoint

- Nach Aufgabe 2: `game.log: 0 Runden gefunden, davon 0 gewonnen`.
- Nach Aufgabe 5: Die Zahl der gefundenen Runden ist die Zahl der „Neue Runde“-Zeilen minus der `quit`-Runde; jede Zeile zeigt Startzeit, Name, Stufe, Ergebnis und Tipps.
- Die Computer-Runde erscheint mit dem Namen `Computer` und den Tipps des Computers.
- `SELECT * FROM log_rounds` zeigt genau so viele Zeilen wie das Skript meldet, auch nach dem zweiten Lauf (keine Duplikate).

## Abschlusskriterien

- `playground/import_log.py` enthält kein `TODO` mehr.
- Die `quit`-Runde fehlt in `log_rounds`, und keine Runde hat eine falsche Stufe oder einen falschen Namen.

## Erweiterung

Schreibe ein eigenes Skript `playground/contacts.py`, das [data/addresses.txt](../../project/data/addresses.txt) (aus `playground/` gesehen: `../data/addresses.txt`) in Blöcke zerlegt und nur die Kontakte **mit** Telefonnummer ausgibt, je Zeile `Anna Beispiel: 030 1234567`.
