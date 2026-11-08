# Lab 5.2 – Übung: Eine Runde als Funktion

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — eine Runde wird zur Funktion `play_round` mit Rückgabewert, `main()` sammelt die Versuche; Lab 5.3 baut darauf auf.

**Arbeitsdatei:** `playground/guess_game.py`
**Starter:** `starters/m05-l02-guess_game.py`

## Vorbereitung

- Terminal in VS Code im Ordner `project/`, `.venv` aktiv.
- Das eigene Spiel aus Lab 5.1 liegt in `playground/guess_game.py`. Ohne eigenen Stand: `starters/m05-l02-guess_game.py` öffnen, alles markieren (Strg+A / Cmd+A), kopieren und damit den Inhalt von `playground/guess_game.py` ersetzen.
- Die Stellen zum Ändern sind mit `# TODO Lab 5.2` markiert. Die Zeilen einer Runde sind schon 4 Leerzeichen eingerückt; beim Verschieben in eine Funktion passt die Einrückung deshalb meist sofort.

## Aufgaben

1. Definiere unter `is_game_over` die Funktion `ask_level()`. Verschiebe die Stufenabfrage samt Wiederholung bei unbekannter Stufe hinein und gib die gültige Stufe mit `return level` zurück.
2. Definiere `play_round(level="leicht")`. Verschiebe alle Zeilen einer Runde hinein, von `low, high, max_tries = LEVELS[level]` bis `print("Bisherige Tipps:", guesses)`, und gib am Ende `tries` zurück.
3. Definiere `main()` mit der Runden-Schleife: Lege eine leere Liste `all_tries` an. In der Schleife ruft `main` zuerst `ask_level()` auf, dann `play_round(level=level)` als Schlüsselwortargument, und hängt den Rückgabewert an `all_tries` an. Nach der Schleife gibt `main` „Versuche pro Runde:“ mit der Liste und den Abschiedsgruß aus.
4. Lass am Dateiende nur Banner und Namensabfrage stehen und rufe danach `main()` auf. `name` bleibt vorerst außerhalb der Funktionen; `play_round` und `main` lesen den Namen von dort (Umbau in Lab 5.3).
5. Teste zwei Runden. Ergänze danach testweise direkt vor `main()` die Zeile `play_round()`, starte erneut und lösche die Zeile wieder.

## Checkpoint

- Nach zwei Runden erscheint am Ende z. B. `Versuche pro Runde: [3, 5]` und `Danke fürs Spielen, Anna!`.
- Mit der Testzeile `play_round()` startet sofort eine Runde „Stufe leicht“, ohne nach der Stufe zu fragen: Der Standardwert greift.
- Unterhalb der Funktionen stehen nur noch Banner, Namensabfrage und `main()`.

## Abschlusskriterien

- `playground/guess_game.py` enthält `ask_level`, `play_round` mit `return tries` und `main`; das Spiel verhält sich wie vorher und meldet am Ende die Versuche jeder Runde.

## Erweiterung

Lege `playground/shop.py` an. Schreibe eine Funktion `order_summary(*prices)`, die zwei Werte zurückgibt: die Anzahl der Preise und ihre Summe. Entpacke das Ergebnis von `order_summary(12.5, 7.5, 3.0)` in `count` und `total` und gib `3 Artikel, 23.0 Euro` aus.
