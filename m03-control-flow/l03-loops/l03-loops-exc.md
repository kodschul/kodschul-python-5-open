# Lab 3.3 – Übung: Drei Versuche

**Dauer:** ca. 18 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — das Spiel fragt bis zu dreimal und endet beim Treffer; Lab 3.4 baut darauf auf.
**Arbeitsdatei:** `playground/guess_game.py`
**Starter:** `starters/m03-l03-guess_game.py`

## Vorbereitung

- Terminal im Ordner `project/`, `.venv` aktiv.
- Das eigene Spiel aus Lab 3.2 liegt in `playground/guess_game.py`. Ohne eigenen Stand: Inhalt von `starters/m03-l03-guess_game.py` nach `playground/guess_game.py` kopieren.

## Aufgaben

1. Lege unter der Geheimzahl die Variable `tries_left = 3` an.
2. Setze die Zeile mit `input("Tipp: ")` und die ganze `if`-Kette in eine Schleife `while tries_left > 0:` (alles darunter um 4 Leerzeichen einrücken: markieren, dann `Tab`). Ziehe direkt nach der Eingabe einen Versuch ab.
3. Stelle die Prüfung auf Treffer an den Anfang der Kette und beende die Schleife dort mit `break`.
4. Ergänze nach der Kette, noch in der Schleife: Sind Versuche übrig, gibt das Spiel `Verbleibende Versuche: <n>` aus, sonst `Keine Versuche mehr. Die Zahl war <Geheimzahl>.`.
5. Teste zwei Fälle: einmal so lange raten, bis ein Treffer kommt, einmal dreimal danebentippen. Bleibt ein Spiel hängen, beende es mit `Strg+C`.

## Checkpoint

- Das Spiel fragt höchstens dreimal nach einem Tipp und endet.
- Nach einem Fehltipp erscheint `Verbleibende Versuche: 2` bzw. `Verbleibende Versuche: 1`.
- Ein Treffer beendet das Spiel sofort, ohne weitere Frage.
- Nach drei Fehltipps nennt das Spiel die Geheimzahl.

## Abschlusskriterien

- `playground/guess_game.py` enthält eine `while`-Schleife mit dem Zähler `tries_left`, ein `break` beim Treffer und die Meldung nach dem letzten Versuch.

## Erweiterung

Ändere den Weihnachtsbaum aus der Theorie in `playground/tree.py` so ab, dass die Höhe nicht fest im Code steht, sondern mit `Höhe: ` abgefragt wird. Teste mit `4` und mit `8`.
