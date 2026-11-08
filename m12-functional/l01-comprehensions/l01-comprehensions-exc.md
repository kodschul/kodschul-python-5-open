# Lab 12.1 – Übung: Statistik der Bestenliste

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — am Spielende erscheint eine Statistik der Bestenliste (Gewinner, Versuche pro Spieler, Durchschnitt pro Stufe); Lab 12.2 baut darauf auf.
**Arbeitsdatei:** `playground/guess_game/` (geändert: `logic.py`, `ui.py`, `__main__.py`)
**Starter:** `starters/m12-l01-guess_game/` mit `__main__.py`, `logic.py`, `ui.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 11.3 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m11-advanced-oop/l03-abstraction/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m12-l01-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.
- Für eine aussagekräftige Statistik: eine vorhandene `playground/highscores.json` umbenennen (z. B. `highscores_eigen.json`) und `data/highscores_sample.json` als `playground/highscores.json` hineinkopieren. Sie enthält sechs Gewinne von Anna, Ben, Jürgen und dem Computer.

## Aufgaben

1. Schreibe in `logic.py` an der Stelle `# TODO Lab 12.1` die Funktion `average(numbers)`: Sie gibt den Durchschnitt der Zahlenliste zurück, gerundet auf eine Nachkommastelle.
2. Beginne darunter die Funktion `statistics(scores)`. Bilde mit einer Set-Comprehension `winners`: die Namen aller Scores, jeder Name nur einmal.
3. Bilde mit einer Dict-Comprehension `tries_per_player`: Schlüssel ist jeder Name aus `winners`, Wert die Liste der Versuche aller Scores mit diesem Namen (Listen-Comprehension mit `if` im Wert).
4. Bilde `levels` (Set der gespielten Stufen) und `average_per_level` (Stufe → `average` der Versuche dieser Stufe). Gib ein Dictionary mit den Schlüsseln `"winners"`, `"tries_per_player"` und `"average_per_level"` zurück. Prüfe im Ordner `playground/`:

   ```bash
   python -c "from guess_game import logic, storage; print(logic.statistics(storage.Scoreboard().scores))"
   ```

5. Übernimm die Ausgabefunktion unten in `ui.py` (Stelle `# TODO Lab 12.1`) und rufe in `__main__.py` vor `ui.show_goodbye(...)` `ui.show_statistics(logic.statistics(scoreboard.scores))` auf. Spiele eine Runde, gewinne sie und beende mit `n`.

```python
def show_statistics(stats):
    """Zeigt Gewinner, Versuche pro Spieler und Durchschnitt pro Stufe."""
    print("\nStatistik der Bestenliste")
    if not stats["winners"]:
        print("Noch keine Einträge.")
        return
    print("Gewinner:", sorted(stats["winners"]))  # sorted: feste Reihenfolge
    print("Versuche pro Spieler:")
    for name in sorted(stats["tries_per_player"]):
        print(f"  {name}: {stats['tries_per_player'][name]}")
    print("Durchschnitt pro Stufe:")
    for level in sorted(stats["average_per_level"]):
        value = str(stats["average_per_level"][level]).replace(".", ",")
        print(f"  {level}: {value} Versuche")
```

## Checkpoint

- Der `python -c`-Befehl gibt ein Dictionary mit drei Schlüsseln aus; `winners` ist ein Set mit vier Namen.
- Nach `Nochmal spielen? (j/n): n` erscheint `Statistik der Bestenliste` mit `Gewinner: ['Anna', 'Ben', 'Computer', 'Jürgen']` (plus eigener Name, falls neu).
- Der eigene Gewinn steht unter `Versuche pro Spieler` und verändert den Durchschnitt der gespielten Stufe.
- Mit leerer Bestenliste (Datei `highscores.json` umbenannt, Runde verloren) erscheint `Noch keine Einträge.`

## Abschlusskriterien

- `logic.statistics` enthält je zwei Set-, Dict- und Listen-Comprehensions und keine `append`-Schleife.
- Das Spiel zeigt am Ende die Statistik und danach wie bisher `Versuche pro Runde` und den Abschied.

## Erweiterung

Lege `playground/shop.py` an mit `names = [" Mango", "apfel ", "MANGO", "Birne"]` und `prices = {"mango": 1.99, "apfel": 0.45, "birne": 0.89}`. Bilde per Comprehension (a) ein Set der Namen ohne Leerzeichen in Kleinbuchstaben und (b) ein Dictionary Name → Preis mit 10 % Rabatt (auf 2 Stellen gerundet), nur für Preise über 0,50 €. Start im Ordner `playground/` mit `python shop.py`.
