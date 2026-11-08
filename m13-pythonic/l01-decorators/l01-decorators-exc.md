# Lab 13.1 – Übung: Zeitmessung per @timed

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — `@logic.timed` misst die Dauer von `play_round`, `Game` enthält keinen Messcode mehr; die Ergebnisausgabe steht in `ui.show_result`. Lab 13.2 baut darauf auf.
**Arbeitsdatei:** `playground/guess_game/` (geändert: `logic.py`, `ui.py`, `__main__.py`)
**Starter:** `starters/m13-l01-guess_game/` mit `__main__.py`, `logic.py`, `ui.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 12.3 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m12-functional/l03-generators/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m13-l01-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.
- Die Stellen sind im Starter mit `# TODO Lab 13.1` markiert.

## Aufgaben

1. Schreibe in `logic.py` den Decorator `timed(func)`: Der Wrapper nimmt `*args, **kwargs` an, startet `time.perf_counter()`, ruft `func(*args, **kwargs)` auf, trägt die gerundete Dauer (eine Nachkommastelle) in `result.seconds` ein und gibt `result` zurück. Setze `@functools.wraps(func)` über den Wrapper und ergänze `import functools`.
2. Entferne in `Game` die Stoppuhr: die Attribute `start_time` und `seconds` in `__init__` und das Anhalten in `guess()`. `score()` übergibt als Dauer `0.0`. Ändere `save_score(self)` in `save_score(self, score)`, sodass die Methode den übergebenen `score` in die Bestenliste einträgt.
3. Verschiebe in `ui.py` die Ergebnisausgabe (Gewinnzeile oder Geheimzahl und `Bisherige Tipps`) aus `play_round` in eine neue Funktion `show_result(game, score)`; die Dauer kommt dort aus `score.seconds`. `play_round` endet mit `return game.score()`. Setze `@logic.timed` über `def play_round`.
4. Rufe in `__main__.py` direkt nach `score = ui.play_round(game)` die Funktion `ui.show_result(game, score)` auf und übergib `score` an `game.save_score(score)`.
5. Starte `python -m guess_game`, gewinne eine Runde und lies die Dauer ab. Prüfe danach im interaktiven Modus (`python` im Ordner `playground/`): `from guess_game import ui`, dann `ui.play_round.__name__`.

## Checkpoint

- Das Spiel läuft wie in Lab 12.3; die Gewinnzeile zeigt `Benötigte Versuche: … · Dauer: … s` mit echter Dauer.
- `ui.play_round.__name__` ergibt `'play_round'`, nicht `'wrapper'`.
- `logic.py` enthält `perf_counter` nur noch in `timed`.

## Abschlusskriterien

- `Game` hat kein Attribut `start_time` mehr; `play_round` trägt `@logic.timed` und enthält keinen Messcode.
- Die Bestenliste zeigt nach einem Gewinn die gemessene Dauer.

## Erweiterung

Lege `playground/retry.py` an und schreibe einen Decorator mit Parameter `retry(times)`: Der Wrapper ruft die Funktion auf; löst sie `ValueError` aus, gibt er `Fehlversuch 1 von 3: …` aus und versucht es erneut, höchstens `times`-mal. Beim letzten Fehlversuch reicht er den Fehler weiter: Ein `raise` ohne Angabe im `except`-Block löst denselben Fehler noch einmal aus. Teste mit:

```python
import random


@retry(times=3)
def roll_six():
    """Würfelt; alles außer 6 gilt als Fehler."""
    number = random.randint(1, 6)
    print("Gewürfelt:", number)
    if number != 6:
        raise ValueError("keine 6")
    return number


print("Ergebnis:", roll_six())
```

Start mehrmals mit `python retry.py`: Mal kommt die 6 rechtzeitig, mal endet das Programm nach drei Fehlversuchen mit `ValueError: keine 6`.
