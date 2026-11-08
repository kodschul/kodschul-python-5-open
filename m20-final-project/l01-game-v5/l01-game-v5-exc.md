# Lab 20.1 – Übung: Spiel v5 fertigstellen

**Dauer:** ca. 45 Minuten (zu zweit; Checkpoint nach 25 Minuten)
**Ändert die Zahlenraten-Projektbasis?** Ja — neben dem Paket entstehen `README.md` und `requirements.txt`, dazu eine Wahlaufgabe. Das ist Spiel v5, der Endstand des Kurses.
**Arbeitsdatei:** `playground/` mit `guess_game/`, neu `README.md` und `requirements.txt`
**Starter:** keiner; Ausgangspunkt ist der Spielstand nach Lab 19.3

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel liegt in `playground/guess_game/` (Stand Lab 19.3). Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen und `examples/m19-data-analysis/l03-matplotlib/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren.
- Fehlen Skripte neben dem Paket (`log_report.py`, `analyze.py`, …), liegen sie fertig in `examples/m19-data-analysis/l03-matplotlib/`.
- Vorlage zum Vergleichen: [README von v5](../../project/examples/m20-final-project/l01-game-v5/README.md).

## Wenn Labs ausgelassen wurden

| Ausgelassen | Pflicht dann | Wahlaufgabe |
| --- | --- | --- |
| 19.3 Diagramme | `--export html` erzeugt die Tabelle ohne Diagramme; das reicht für die Pflicht. Mit dem Starter sind die Diagramme trotzdem dabei. | alle möglich |
| 17.1 XML/HTML | Eigener Stand hat kein `--export`: mit dem Starter arbeiten, der Export ist dort fertig. | alle möglich |
| 16.3 Log-Bericht | unverändert | „Wochenbericht“ nur mit `log_report.py` aus `examples/m16-automation/l03-report/`; sonst eine andere wählen |

## Aufgaben

1. Spiele mit `python -m guess_game --name Anna --player mensch --level leicht` eine Runde bis zum Gewinn und beende mit `n`. Prüfe danach mit `python -m sqlite3 game.db "SELECT name, level, tries, won FROM rounds"`, dass die Runde in der Datenbank steht.
2. Exportiere mit `python -m guess_game --export html` und öffne `playground/highscores.html` im Browser (Doppelklick im Datei-Explorer bzw. Finder).
3. Lege `playground/requirements.txt` mit den Paketen an, die das Spiel importiert (Versionen aus `project/requirements.txt`), und `playground/README.md` mit den Abschnitten Titel und Kurzbeschreibung, Voraussetzungen, Installation, Spielen, Werkzeuge. Kopiere danach jeden Befehl aus der README ins Terminal und prüfe, dass er läuft.
4. Wähle eine Wahlaufgabe aus der Tabelle unten, setze sie um und prüfe ihr Akzeptanzkriterium. Ergänze in der README eine Zeile, wie die Erweiterung startet.
5. Hole die Tabelle „Was ich mit Python automatisieren will“ aus [Lab 1.1](../../m01-introduction/l01-overview/l01-overview-exc.md) hervor (ohne Tabelle: drei wiederkehrende Aufgaben notieren). Ergänze die Spalte „Werkzeuge aus Modul“ und trage zu jeder Idee die Module und Labs ein, die die Werkzeuge liefern. Markiere die Idee, die sich jetzt als erstes eigenes Skript umsetzen ließe, und notiere dafür in drei Zeilen: Eingabe, Verarbeitung, Ausgabe.

## Wahlaufgaben

| Wahlaufgabe | Spezifikation | Akzeptanzkriterium | Werkzeuge |
| --- | --- | --- | --- |
| Zwei-Personen-Modus | Neues Skript `two_players.py` neben dem Paket: fragt zwei Namen, jede Person rät eine Runde auf derselben Stufe (`--level`), danach steht fest, wer gewonnen hat (Gewinn vor Verlust, dann weniger Versuche). | `python two_players.py --level leicht` zeigt am Ende z. B. `Ben gewinnt: 2 zu 3 Versuchen.`; `statistik` im Spiel zählt beide Runden mit. | Lab 9.2, 11.1 (`<` bei `Score`), 14.2, 18.2 |
| Zeitlimit je Tipp | Ein Tipp nach mehr als 15 Sekunden wird nicht kommentiert: Meldung `Zu langsam (18,2 s): kein Hinweis.`, der Versuch zählt trotzdem. | Ein absichtlich langsamer Tipp zeigt die Meldung, `Verbleibende Versuche` sinkt um 1, schnelle Tipps verhalten sich wie bisher. | Lab 6.3/13.1 (`time.perf_counter`), 13.3 |
| Eigene Stufe per CLI | Optionen `--low`, `--high`, `--tries` legen für einen Lauf eine Stufe `eigene` an (als Skript `custom_level.py` neben dem Paket oder als Optionen in `__main__.py`). `--low` muss kleiner als `--high` sein. | `--high 1000 --tries 10` zeigt `Rate eine Zahl zwischen 1 und 1000.`; `--low 50 --high 10` endet mit argparse-Fehler und Exit-Code 2. | Lab 4.3, 14.2 |
| Wochenbericht | `log_report.py` (Lab 16.3) wertet das Log des eigenen Spiels aus. | `python log_report.py . --since <Datum vor 7 Tagen>` zeigt die eigenen Runden, `report.txt` enthält denselben Bericht. | Lab 15.2, 16.3 |
| Skript aus der Wandliste | Ein eigenes Skript für eine Idee aus Aufgabe 5, nach dem Muster aus Lab 16.3: Argumente, Dateien finden, auswerten, Bericht, Exit-Code. | Läuft ohne Rückfragen, endet mit `0` bei Erfolg und `1`, wenn nichts gefunden wurde; `--help` erklärt die Optionen. | Lab 14.2, 14.3, 16.3 |

## Checkpoint

- Nach 25 Minuten: `python -m guess_game` startet, `game.db` enthält mindestens eine Runde, `--export html` meldet `Bestenliste exportiert: highscores.html`.
- `highscores.html` zeigt die Bestenliste und (mit Stand 19.3) die zwei Diagramme.
- Jeder Befehl in `README.md` läuft beim Kopieren ohne Änderung.

## Abschlusskriterien

- Pflicht erfüllt: Spiel v5 läuft mit `python -m guess_game`, speichert in SQLite, exportiert HTML mit Diagramm, README mit Startbefehlen und `requirements.txt` liegen neben dem Paket.
- Eine Wahlaufgabe erfüllt ihr Akzeptanzkriterium.
- Die Wandliste hat zu jeder Idee mindestens ein Modul.

## Erweiterung

Teste die README wie eine fremde Person: Kopiere `guess_game/`, `README.md` und `requirements.txt` in einen neuen, leeren Ordner außerhalb von `project/`, öffne dort ein neues Terminal und befolge nur die README (neue venv, Installation, Start). Was fehlt, kommt in die README. Zu zweit: README tauschen und das Spiel der anderen Person nur mit deren README starten.
