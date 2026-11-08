# Lab 6.3 – Übung: Dauer und Datum jeder Runde

**Dauer:** ca. 18 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — jede Runde zeigt ihre Startzeit und am Ende die Dauer; `play_round` gibt ein Ergebnis-Dictionary zurück, das Modul 8 speichert.
**Arbeitsdatei:** `playground/guess_game/ui.py` und `playground/guess_game/__main__.py`
**Starter:** `starters/m06-l03-guess_game/` mit `__main__.py`, `ui.py`

## Vorbereitung

- Terminal im Ordner `project/playground/` (`cd playground`), `.venv` aktiv.
- Das eigene Paket aus Lab 6.2 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m06-modules/l02-pypi/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m06-l03-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.

## Aufgaben

1. Importiere in `ui.py` ganz oben die Module `time` und `datetime` (aus dem Modul `datetime`, also `from datetime import datetime`). Schreibe über `play_round` die Funktion `format_seconds(seconds)`, die eine Zahl wie `12.4321` als Text `"12,4"` zurückgibt (eine Nachkommastelle, Komma statt Punkt).
2. Lege in `play_round` vor der Begrüßung `won = False` und `started = datetime.now()` an. Gib nach der Begrüßung `Start: 08.11.2026, 14:05 Uhr` mit dem aktuellen Datum aus und starte danach die Stoppuhr mit `start = time.perf_counter()`.
3. Ersetze beim Treffer die grüne Gewinnzeile durch `won = True` (das `break` bleibt). Halte nach der Schleife die Stoppuhr an: `seconds = round(time.perf_counter() - start, 1)`. Ist `won` wahr, gibt das Spiel grün aus: `Richtig, Anna! Benötigte Versuche: 3 · Dauer: 12,4 s`.
4. Gib am Ende von `play_round` statt `tries` ein Dictionary mit den Schlüsseln `"name"`, `"level"`, `"tries"`, `"seconds"`, `"won"` und `"date"` zurück; `"date"` ist das Startdatum im ISO-Format (`"2026-11-08"`). Passe `main()` in `__main__.py` an: `result = ui.play_round(...)`, gesammelt wird `result["tries"]`.
5. Starte mit `python -m guess_game` und spiele eine gewonnene und eine verlorene Runde.

## Checkpoint

- Jede Runde zeigt unter der Begrüßung `Start: <Datum>, <Uhrzeit> Uhr`.
- Eine gewonnene Runde endet mit der grünen Zeile `Richtig, <Name>! Benötigte Versuche: <n> · Dauer: <Sekunden> s`, die Dauer mit Komma und genau einer Nachkommastelle.
- Eine verlorene Runde zeigt keine Dauer, aber wie bisher „Keine Versuche mehr. Die Zahl war …“.
- Am Ende steht weiterhin `Versuche pro Runde: [...]`.

## Abschlusskriterien

- `play_round` misst mit `time.perf_counter()`, formatiert mit `format_seconds` und gibt ein Dictionary mit sechs Schlüsseln zurück; `main()` liest daraus `result["tries"]`.

## Erweiterung

Schreibe `playground/age_in_days.py`: Das Programm fragt den Geburtstag (`TT.MM.JJJJ`) ab und gibt aus, an welchem Wochentag (deutsch) die Geburt war, seit wie vielen Tagen die Person lebt und an welchem Datum sie 10.000 Tage alt wird. Start im Ordner `playground/`: `python age_in_days.py`.
