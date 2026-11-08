# Lab 16.2 – Übung: Bestenliste über HTTP

**Dauer:** ca. 12 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — neben dem Paket entsteht `fetch_scores.py`; das Paket `guess_game/` bleibt unverändert. Lab 16.3 legt daneben `log_report.py` an.
**Arbeitsdatei:** `playground/fetch_scores.py` (neu, neben `playground/guess_game/`)
**Starter:** keiner; `fetch_scores.py` entsteht neu, das Spiel bleibt auf dem Stand nach Lab 15.3

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 15.3 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen und `examples/m15-system/l03-logging/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren.
- Fehlt `playground/highscores.json` oder ist die Liste leer, zwei Runden spielen: `python -m guess_game --name Anna --level leicht --player computer`, die Frage `Bestenliste nach …` mit Enter bestätigen, `Nochmal spielen?` erst mit `j`, dann mit `n` beantworten.

## Aufgaben

1. Starte im Terminal (Terminal 1, Ordner `playground/`) den Server mit `python -m http.server 8000 --bind 127.0.0.1`. Öffne im Browser `http://localhost:8000/highscores.json` und danach `http://localhost:8000/`.
2. Öffne ein zweites Terminal (**Terminal → New Terminal**), aktiviere dort `.venv` und wechsle mit `cd playground` in den Spielordner.
3. Lege `playground/fetch_scores.py` an: Konstante `URL = "http://localhost:8000/highscores.json"`, Funktion `main()` mit `requests.get(URL, timeout=5)` und `raise_for_status()`. Bei `requests.RequestException` gibt das Skript `Bestenliste nicht erreichbar: <Fehler>` aus und endet mit `sys.exit(1)`. Unten im Skript startet `if __name__ == "__main__":` die Funktion `main()`.
4. Ergänze in `main()`: Die Einträge nach `"tries"` sortieren (`sorted` mit `key=lambda`), die ersten drei als `1. Anna · Versuche: 3 · schwer` ausgeben, davor eine Zeile `Top 3 von <URL> (<n> Einträge)`. Starte in Terminal 2 `python fetch_scores.py` und beobachte dabei Terminal 1.
5. Beende den Server in Terminal 1 mit `Strg+C`, starte `python fetch_scores.py` erneut und zeige danach den Exit-Code an (PowerShell: `$LASTEXITCODE`, macOS/Linux: `echo $?`).

## Checkpoint

- Der Browser zeigt den Inhalt von `highscores.json`; `http://localhost:8000/` listet alle Dateien des Spielordners.
- `python fetch_scores.py` zeigt `Top 3 von http://localhost:8000/highscores.json (…)` und höchstens drei Zeilen, die beste zuerst.
- Terminal 1 zeigt pro Abruf eine Zeile `"GET /highscores.json HTTP/1.1" 200 -`.
- Ohne Server: `Bestenliste nicht erreichbar: … Connection refused …` (Windows: `[WinError 10061]`), Exit-Code `1`, kein Traceback.

## Abschlusskriterien

- `playground/fetch_scores.py` liest die Bestenliste ausschließlich über HTTP (kein `open`), mit `timeout=`, `raise_for_status()` und Exit-Code 1 im Fehlerfall.

## Erweiterung

Lege mit `python -m guess_game --backup` ein Backup an (Lab 14.3) und starte den Server danach mit `python -m http.server 8000 --bind 127.0.0.1 --directory backups`. Öffne `http://localhost:8000/` und folge den Links bis zu einer gesicherten `highscores.json`. Ändere `URL` in `fetch_scores.py` auf diese Datei und starte das Skript.
