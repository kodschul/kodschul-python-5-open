# Lab 15.2 – Übung: Namensprüfung und Log-Zeilen per Regex

**Dauer:** ca. 25 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — `logic.py` bekommt `NAME_PATTERN`, `LOG_PATTERN`, `is_valid_name` und `parse_log_line`; Lab 15.3 schreibt die passenden Log-Zeilen, Lab 16.3 wertet sie mit `parse_log_line` aus.
**Arbeitsdatei:** `playground/guess_game/` (geändert: `logic.py`, `ui.py`, `__main__.py`)
**Starter:** `starters/m15-l02-guess_game/` mit `__main__.py`, `logic.py`, `ui.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 14.3 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m14-scripting/l03-filesystem/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m15-l02-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.

## Aufgaben

1. Ergänze in `logic.py` oben `import re`. Lege an der Stelle `# TODO Lab 15.2` die Konstante `NAME_PATTERN` mit dem Muster `^[A-Za-zÄÖÜäöüß]{2,20}$` an und schreibe `is_valid_name(name)`: `True`, wenn `fullmatch` einen Treffer liefert.
2. Ändere `ask_name()` in `ui.py`: Eine `while`-Schleife mit `:=` fragt `Name: `, bis `logic.is_valid_name(...)` gilt, und meldet sonst `Der Name braucht 2 bis 20 Buchstaben, z. B. Anna.` Zurück kommt der Name mit `.title()`.
3. Lehne in `parse_args()` (`__main__.py`) ein ungültiges `--name` mit `parser.error("--name braucht 2 bis 20 Buchstaben, z. B. Anna.")` ab. Ein fehlendes `--name` (`None`) bleibt erlaubt.
4. Kopiere `LOG_PATTERN` samt Kommentar aus der Theorie (Abschnitt „Im Spiel“) unter `NAME_PATTERN`. Schreibe `parse_log_line(line)`: `search` auf die Zeile ohne Leerraum am Rand; kein Treffer → `None`, sonst `groupdict()`.
5. Teste: Starte `python -m guess_game` und gib als Namen nacheinander `A`, `Anna1`, `Anna-Lena` und `jürgen` ein. Starte danach `python -m guess_game --name Anna1 --level schwer`. Prüfe zuletzt im interaktiven Modus (`python`, dann `from guess_game import logic`) `logic.parse_log_line(...)` mit diesen zwei Zeilen:

   ```text
   2026-11-08 15:30:12 INFO guess_game: Gewonnen: Anna – 3 Versuche – 12,4 s · leicht
   2026-11-08 15:30:00 DEBUG guess_game.ui: Tipp 5: zu niedrig
   ```

## Checkpoint

- `A`, `Anna1` und `Anna-Lena` werden mit „Der Name braucht 2 bis 20 Buchstaben, z. B. Anna.“ abgelehnt; `jürgen` wird angenommen, das Spiel verabschiedet sich mit `Jürgen`.
- `--name Anna1` endet sofort mit `error: --name braucht 2 bis 20 Buchstaben, z. B. Anna.` (Exit-Code 2).
- Die Gewinnzeile ergibt ein Dictionary mit `date`, `result`, `name`, `tries`, `seconds`, `level`; die DEBUG-Zeile ergibt `None`.

## Abschlusskriterien

- `logic.py` enthält `import re`, beide Muster als `re.compile(r"...")` und kein `input`/`print`.

## Erweiterung

Namen wie `Zoë` und `José` sollen auch gelten. Baue in `logic.py` eine zweite Konstante `UNICODE_NAME_PATTERN` mit dem Paket `regex` (`import regex`) und dem Muster „2 bis 20 Buchstaben jeder Sprache“ (`\p{L}`), und lass `is_valid_name` sie statt `NAME_PATTERN` benutzen. Prüfe `Zoë`, `José`, `Jürgen`, `R2D2` und `A`.
