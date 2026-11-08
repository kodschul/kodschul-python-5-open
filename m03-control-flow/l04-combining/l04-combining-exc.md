# Lab 3.4 – Übung: Mehrere Runden und Fehlersuche

**Dauer:** ca. 13 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — das Spiel zählt die Versuche und lässt sich mehrmals hintereinander spielen (Basis für Spiel v1); Lab 4.1 baut darauf auf.
**Arbeitsdatei:** `playground/guess_game.py` (Erweiterung: `playground/guess1.py`)
**Starter:** `starters/m03-l04-guess_game.py`

## Vorbereitung

- Terminal im Ordner `project/`, `.venv` aktiv.
- Das eigene Spiel aus Lab 3.3 liegt in `playground/guess_game.py`. Ohne eigenen Stand: Inhalt von `starters/m03-l04-guess_game.py` nach `playground/guess_game.py` kopieren.
- Ablaufdiagramm „Zahlenraten mit mehreren Runden“ aus der Theorie zur Hand haben.

## Aufgaben

1. Lege oben die Konstante `MAX_TRIES = 3` an und stelle den Zähler auf Hochzählen um: `tries = 0` statt `tries_left = 3`, je Tipp `tries += 1`, Schleife `while tries < MAX_TRIES:`. Passe danach die Meldungen an: Die Prüfung nach dem Tipp lautet `if tries < MAX_TRIES:`, die Restversuche rechnet der Ausdruck `MAX_TRIES - tries` aus (`Verbleibende Versuche: {MAX_TRIES - tries}`), und der Treffer meldet zusätzlich `Benötigte Versuche: {tries}.`.
2. Lege um die Runde eine äußere Schleife `while play_again == "j":` (vorher `play_again = "j"`). Geheimzahl und `tries = 0` gehören an den Anfang der äußeren Schleife; die Namensabfrage bleibt davor.
3. Frage am Ende jeder Runde `Nochmal spielen? (j/n): ` und speichere die Antwort bereinigt (`strip`, `lower`) in `play_again`. Nach der äußeren Schleife verabschiedet sich das Spiel mit `Danke fürs Spielen, <Name>!`.
4. Spiele zwei Runden hintereinander: eine mit Treffer, eine ohne. Beende mit `n`.

## Checkpoint

- Jede Runde zieht eine neue Geheimzahl und erlaubt wieder drei Tipps.
- Ein Treffer meldet die Zahl der benötigten Versuche, ein Fehltipp die verbleibenden Versuche.
- `j` startet eine neue Runde, `n` beendet das Spiel mit der Verabschiedung.

## Abschlusskriterien

- `playground/guess_game.py` enthält `MAX_TRIES`, eine äußere und eine innere `while`-Schleife; `tries_left` kommt nicht mehr vor.

## Erweiterung

Kopiere `code/m03-control-flow/guess1.py` nach `playground/guess1.py`, starte `python playground/guess1.py` und tippe mehrmals eine zu hohe Zahl. Beschreibe das Symptom, finde die falsch eingerückte Zeile und korrigiere sie. Danach läuft `tries -= 1` bei jedem Fehltipp, und das Programm endet nach drei Fehltipps.
