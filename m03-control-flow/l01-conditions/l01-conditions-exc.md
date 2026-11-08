# Lab 3.1 – Übung: Tipp bewerten

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — das Spiel antwortet mit „Zu hoch.“, „Zu niedrig.“ oder „Richtig, Anna!“; Lab 3.2 baut darauf auf.
**Arbeitsdatei:** `playground/guess_game.py`
**Starter:** `starters/m03-l01-guess_game.py`

## Vorbereitung

- VS Code ist im Kurs-Repo geöffnet, das Terminal steht im Ordner `project/`, `.venv` ist aktiv.
- Das eigene Spiel aus Lab 2.4 liegt in `playground/guess_game.py`. Ohne eigenen Stand: Inhalt von `starters/m03-l01-guess_game.py` nach `playground/guess_game.py` kopieren.

## Aufgaben

1. Öffne `playground/guess_game.py` und suche die Zeile `print("Treffer:", guess == secret)`. Lösche sie.
2. Ergänze an ihrer Stelle eine `if`-Prüfung: Ist der Tipp größer als die Geheimzahl, gibt das Spiel `Zu hoch.` aus.
3. Ergänze einen `elif`-Zweig für `Zu niedrig.` und einen `else`-Zweig, der mit f-String `Richtig, <Name>!` ausgibt.
4. Starte das Spiel dreimal mit `python playground/guess_game.py` und tippe eine zu hohe, eine zu niedrige und die richtige Zahl (die Geheimzahl steht oben in der Datei).
5. Tippe einmal die Grenzwerte `1` und `10` und prüfe, dass jeweils genau eine Zeile Bewertung erscheint.

## Checkpoint

- Ein zu hoher Tipp zeigt `Zu hoch.`, ein zu niedriger `Zu niedrig.`.
- Der richtige Tipp zeigt `Richtig, Anna!` mit dem eingegebenen Namen.
- Jeder Start gibt genau eine Bewertungszeile aus.

## Abschlusskriterien

- `playground/guess_game.py` enthält eine Kette aus `if`, `elif` und `else`.
- Die Zeile mit `Treffer: True/False` ist entfernt.

## Erweiterung

Schreibe nach dem Muster des Rabatt-Checks einen Kinoticket-Rechner in `playground/ticket.py`: Alter, „Studierend? (j/n)“ und „Kinotag? (j/n)“ abfragen; Kinder unter 12 Jahren zahlen 6 €, am Kinotag zahlen alle anderen 7 €, Studierende unter 30 Jahren 8 €, sonst 12 €. Gib `Preis: <n> €` aus und teste mit Alter 22, studierend, kein Kinotag.
