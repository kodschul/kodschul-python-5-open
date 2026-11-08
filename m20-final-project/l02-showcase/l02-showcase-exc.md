# Lab 20.2 – Übung: Showcase und Ausblick

**Dauer:** ca. 15 Minuten (im Kurs danach je 2 Minuten Vorstellung in der Runde)
**Ändert die Zahlenraten-Projektbasis?** Nein — nur `playground/README.md` bekommt oben einen Pitch; der Code bleibt Spiel v5.

## Vorbereitung

- Das eigene Spiel v5 mit Wahlaufgabe aus Lab 20.1 liegt in `playground/` (ohne eigenen Stand: [examples/m20-final-project/l01-game-v5/](../../project/examples/m20-final-project/l01-game-v5/) und eine Referenzlösung aus `code/m20-final-project/`).
- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/`.
- Die Tabelle „Wohin nach dem Kurs?“ aus der Theorie liegt offen.

## Aufgaben

1. Schreibe ganz oben in `playground/README.md` den 5-Zeilen-Pitch der eigenen Erweiterung: Titel, **Problem**, **Lösung**, **Start** (genau ein Befehl), **Gelernt**.
2. Bereite die Live-Demo vor: Befehl aus der Zeile **Start** fertig ins Terminal tippen (noch nicht ausführen), Schrift vergrößern, einen Code-Ausschnitt von höchstens zehn Zeilen in VS Code öffnen.
3. Probe mit Timer: Stelle die Erweiterung laut in der Reihenfolge Problem → Demo → Code → Gelernt vor und stoppe die Zeit. Kürze, bis es unter 2 Minuten bleibt.
4. Wähle aus der Tabelle „Wohin nach dem Kurs?“ eine Richtung und ergänze unter dem Pitch eine Zeile **Nächster Schritt:** mit Richtung, Link und einer konkreten ersten Aufgabe am eigenen Spiel.
5. Zeige die Erweiterung in 2 Minuten (im Kurs in der Runde; allein als Bildschirmaufnahme oder laut mit Timer).

## Checkpoint

- `README.md` beginnt mit fünf Zeilen: Titel, Problem, Lösung, Start, Gelernt.
- Der Befehl aus **Start** läuft beim Kopieren im Ordner `playground/` ohne Änderung.
- Die Probe dauert höchstens 2 Minuten.

## Abschlusskriterien

- Pitch und **Nächster Schritt** stehen in der README.
- Die Vorstellung zeigt das Programm live, nicht nur Folien oder Code.

## Erweiterung

Setze den ersten Schritt der gewählten Richtung sofort um, z. B. für pytest: `pip install pytest`, `test_logic.py` aus der Theorie neben `guess_game/` anlegen, `pytest -v` ausführen und einen vierten Test für `ComputerPlayer` ergänzen (nach `start_round(1, 100)` tippt er `50`).
