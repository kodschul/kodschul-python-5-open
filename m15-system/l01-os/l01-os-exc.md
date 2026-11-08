# Lab 15.1 – Übung: Systembericht

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Nein — eigenständiges Skript; das Spiel bleibt auf dem Stand von Lab 14.3.
**Arbeitsdatei:** `playground/system_info.py` (neu)
**Starter:** keiner

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `project/`.
- Lege die leere Datei `playground/system_info.py` an.

## Aufgaben

1. Importiere `os`, `platform`, `shutil`, `subprocess` und `sys`. Gib die Überschrift `Systembericht` aus, darunter Betriebssystem mit Version (`platform.system()`, `platform.release()`), `sys.platform` und die Python-Version.
2. Ermittle mit `shutil.disk_usage(".")` den freien und den gesamten Speicherplatz und gib beide in GB mit einer Nachkommastelle und Komma aus, z. B. `Speicher frei:  4,2 GB von 245,1 GB`.
3. Lies die Umgebungsvariable `PATH` mit `os.environ`, zerlege sie mit `os.pathsep` und gib die Anzahl der Ordner aus.
4. Starte mit `subprocess.run` den Befehl `[sys.executable, "--version"]` mit `capture_output=True`, `text=True` und `check=True`. Gib die aufgefangene Ausgabe (ohne Zeilenumbruch am Ende) und den Rückgabecode aus.
5. Starte den Bericht mit `python playground/system_info.py`. Setze danach im selben Terminal die Umgebungsvariable `DEMO_TOKEN` auf `abc12345` (Befehl je System in der Theorie) und starte `python code/m15-system/env_vars.py` vor und nach dem Setzen.

## Checkpoint

- Der Bericht zeigt Betriebssystem, `sys.platform` (`win32`, `darwin` oder `linux`), Python-Version, Speicher in GB mit Komma, Anzahl der `PATH`-Ordner, `Python 3.14.…` und Rückgabecode `0`.
- `env_vars.py` meldet erst „DEMO_TOKEN ist nicht gesetzt.“, nach dem Setzen „DEMO_TOKEN ist gesetzt (8 Zeichen).“; der Wert selbst erscheint nicht.

## Abschlusskriterien

- `system_info.py` läuft ohne Fehler und enthält kein `shell=True`.

## Erweiterung

Ergänze den Bericht um eine Zeile, die den eigenen Rechner einmal mit `ping` anspricht (`127.0.0.1`): Option `-n 1` unter Windows, sonst `-c 1`, Befehl als Liste, `capture_output=True`, `timeout=10`. Gib `ping: erreichbar` aus, wenn der Rückgabecode 0 ist, sonst `ping: nicht erreichbar`; fehlt `ping`, fängt `except FileNotFoundError` das ab.
