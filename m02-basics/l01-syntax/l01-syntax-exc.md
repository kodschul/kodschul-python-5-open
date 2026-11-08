# Lab 2.1 – Übung: Begrüßungsbanner für das Zahlenraten

**Dauer:** ca. 12 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — `playground/guess_game.py` entsteht und zeigt das Banner; Lab 2.2 baut darauf auf.
**Arbeitsdatei:** `playground/guess_game.py`
**Starter:** `starters/m02-l01-guess_game.py`

## Vorbereitung

- Der Kursordner ist in VS Code geöffnet, das Terminal steht im Ordner `project/`, die virtuelle Umgebung ist aktiv (`(.venv)` vor der Eingabezeile, Lab 1.2).
- Optional: Format on save für Ruff ist eingeschaltet (Abschnitt „Vertiefung“ in der Theorie).

## Aufgaben

1. Lege die Datei `playground/guess_game.py` an: Klicke im Explorer links auf den Ordner `playground`, dann oben auf das Symbol **New File…** (Blatt mit Plus, siehe Bild) und tippe `guess_game.py`. Öffne danach `starters/m02-l01-guess_game.py`, markiere alles (`Strg+A`, macOS `Cmd+A`), kopiere es (`Strg+C`, macOS `Cmd+C`), füge es in `playground/guess_game.py` ein (`Strg+V`, macOS `Cmd+V`) und speichere (`Strg+S`, macOS `Cmd+S`).

   <img src="https://code.visualstudio.com/assets/docs/python/tutorial/toolbar-new-file.png" alt="VS Code Explorer mit rot markiertem Symbol New File und einer neu angelegten Datei hello.py" width="720" />

   _Quelle: VS Code Docs, „Python in VS Code tutorial“ (https://code.visualstudio.com/docs/python/python-tutorial), CC BY 4.0, abgerufen am 08.11.2026. Im Kurs heißt die neue Datei `guess_game.py` im Ordner `playground`._
2. Ersetze die `TODO`-Zeile durch vier `print`-Anweisungen: eine Linie aus 40 Gleichheitszeichen, den Titel „Zahlenraten“, den Satz „Rate eine Zahl zwischen 1 und 10.“ und noch einmal die Linie.
3. Starte das Spiel mit `python playground/guess_game.py` und vergleiche die Ausgabe mit dem Bild „Begrüßungsbanner“ in der Theorie.
4. Rücke die Zeile mit `"Zahlenraten"` um zwei Leerzeichen ein, starte erneut und notiere Zeilennummer und Fehlerart aus der Meldung. Entferne die Einrückung danach wieder.
5. Lösche in derselben Zeile die schließende Klammer `)`, starte und lies die letzte Zeile der Meldung. Setze die Klammer wieder ein und starte, bis das Banner wieder erscheint.

## Checkpoint

- Das Terminal zeigt vier Zeilen: Linie, „Zahlenraten“, „Rate eine Zahl zwischen 1 und 10.“, Linie.
- Aufgabe 4 endet mit `IndentationError: unexpected indent`, Aufgabe 5 mit `SyntaxError: '(' was never closed`.

## Abschlusskriterien

- `playground/guess_game.py` läuft ohne Fehlermeldung und gibt das Banner aus.
- Die Datei beginnt mit einem Kommentar; keine Zeile ist eingerückt.

## Erweiterung

Schreibe eine eigene Visitenkarte als `playground/business_card.py`: Rahmenlinie, Name, Studienfach, E-Mail und ein Datum, das mit `sep="."` aus drei Werten entsteht. Nutze für eine Zeile `end=" "`, damit die nächste Ausgabe in derselben Zeile weitergeht. Vergleich: `code/m02-basics/business_card.py`.
