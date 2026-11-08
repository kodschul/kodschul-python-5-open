# Python-Setup-Cheatsheet

Schnellreferenz für Modul 1 (Python, VS Code, virtuelle Umgebung). Alle Befehle im Terminal von VS Code im Ordner `project/`.

## Python prüfen

| Befehl | Wirkung |
| --- | --- |
| `python --version` | Version anzeigen (Windows; überall nach dem Aktivieren der venv) |
| `py -V:3.14 --version` / `py list` | Version anzeigen / installierte Versionen auflisten (Windows, Python Install Manager) |
| `python3 --version` | Version anzeigen (macOS, Linux vor dem Aktivieren) |
| `python3.14 --version` | gezielt Python 3.14 prüfen, wenn mehrere Versionen installiert sind |

## Virtuelle Umgebung

| Befehl | Wirkung |
| --- | --- |
| `python -m venv .venv` | venv anlegen (Windows) |
| `py -V:3.14 -m venv .venv` | venv mit Python 3.14 anlegen (Windows, Python Install Manager) |
| `python3 -m venv .venv` | venv anlegen (macOS, Linux) |
| `python3.14 -m venv .venv` | venv anlegen, wenn `python3` ein älteres System-Python ist |
| `.venv\Scripts\Activate.ps1` | venv aktivieren (Windows, PowerShell) |
| `source .venv/bin/activate` | venv aktivieren (macOS, Linux) |
| `(.venv)` vor der Eingabezeile | venv ist aktiv |
| `deactivate` | venv verlassen |
| `.venv` löschen und neu anlegen | Reparatur bei kaputter Umgebung |

## Pakete

| Befehl | Wirkung |
| --- | --- |
| `pip install -r requirements.txt` | alle Kurspakete in die aktive venv installieren |
| `pip list` | installierte Pakete anzeigen |
| `pip install --no-index --find-links <ordner> -r requirements.txt` | offline aus einem Ordner mit Paketdateien installieren |

## Python ausführen

| Befehl | Wirkung |
| --- | --- |
| `python` | interaktiven Modus (REPL) starten, Eingabezeile `>>>` |
| `exit` | interaktiven Modus beenden |
| `python playground/hello.py` | Skriptdatei ausführen |
| `python -c "import this"` | eine einzelne Zeile ausführen, hier: Zen of Python |

## VS Code

| Aktion | Weg |
| --- | --- |
| Projekt öffnen | **File → Open Folder…** → `project/` |
| Terminal öffnen | **Terminal → New Terminal**, ``Ctrl+` `` (US-Tastatur) bzw. `Strg+Ö` (deutsche Tastatur) |
| Befehlspalette | `Strg+Shift+P` (macOS `Cmd+Shift+P`) |
| Interpreter wählen | Befehlspalette → **Python: Select Interpreter** → `.venv` |
| Datei ausführen | Run-Knopf ▷ oben rechts im Editor |
| gewählter Interpreter | Statusleiste unten rechts, z. B. `3.14.x ('.venv': venv)` |

## Kurs-Repo `project/`

| Ordner / Datei | Inhalt |
| --- | --- |
| `code/` | kurze Beispiele je Modul |
| `examples/` | fertiger Spielstand je Lab |
| `starters/` | Startdatei je Übung |
| `playground/` | eigener Arbeitsbereich |
| `data/` | Beispieldateien |
| `requirements.txt` | alle Kurspakete mit fester Version |

## Windows-Sonderfall

| Befehl | Wirkung |
| --- | --- |
| `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` | erlaubt lokale PowerShell-Skripte wie `Activate.ps1` (einmal, ohne Adminrechte) |
| `Get-ExecutionPolicy -List` | aktuelle Einstellung anzeigen |
