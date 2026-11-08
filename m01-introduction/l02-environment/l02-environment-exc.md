# Lab 1.2 – Übung: Arbeitsumgebung einrichten

**Dauer:** ca. 20 Minuten
**Ändert die Zahlenraten-Projektbasis?** Nein — die Übung richtet `project/` mit `.venv` ein; das Spiel beginnt in Lab 2.1.
**Arbeitsdatei:** `playground/hello.py` (liegt im Kurs-Repo bereit)

## Vorbereitung

- Python 3.14 und VS Code mit den Erweiterungen „Python“ und „Ruff“ sind installiert ([00-setup-and-installation.md](../../00-setup-and-installation.md)).
- Das Kurs-Repo liegt als ZIP-Datei vor: auf der GitHub-Seite des Kurs-Repos über **Code → Download ZIP** geladen (ohne git).
- Shell: Terminal in VS Code, unter Windows PowerShell, unter macOS und Linux zsh oder bash.

## Aufgaben

1. Entpacke das ZIP in einen Ordner im eigenen Benutzerverzeichnis (nicht in OneDrive, Dropbox o. Ä.). Öffne in VS Code über **File → Open Folder…** den Ordner `project/` und danach das Terminal über **Terminal → New Terminal**.
2. Lege die virtuelle Umgebung `.venv` an und aktiviere sie mit der Zeile für das eigene System (Tabelle „Virtuelle Umgebung“ in der Theorie). Prüfe mit `python --version`. Zeigt `python3 --version` unter macOS oder Linux eine ältere Version als 3.14, lege die venv mit `python3.14 -m venv .venv` an.
3. Installiere alle Kurspakete mit `pip install -r requirements.txt`.
4. Starte den interaktiven Modus mit `python`. Gib `2 + 3` ein, danach `print("Hallo")`, und beende mit `exit`.
5. Wähle in VS Code über die Befehlspalette (`Strg+Shift+P`, macOS `Cmd+Shift+P`) → **Python: Select Interpreter** die `.venv` und starte im Terminal `python playground/hello.py`.

## Checkpoint

- Vor der Eingabezeile steht `(.venv)`; `python --version` zeigt `Python 3.14.x`.
- `pip install` endet mit `Successfully installed …`.
- Der interaktive Modus zeigt nach `2 + 3` die Zahl `5` und nach `print("Hallo")` den Text `Hallo`.

## Abschlusskriterien

- Das Terminal zeigt nach `python playground/hello.py` die Zeile `Hallo`.
- Die Statusleiste von VS Code unten rechts zeigt `.venv` als Interpreter.

## Erweiterung

Gib im interaktiven Modus `import this` ein und finde den Leitsatz „Readability counts.“ aus Lab 1.1.

## Fallback

- `Activate.ps1 cannot be loaded …` (Windows): einmal `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` ausführen, dann erneut aktivieren.
- Kein Internetzugang zu `pypi.org`: Aufgabe 3 überspringen; Aufgaben 4 und 5 und alle Labs bis Modul 5 brauchen keine Zusatzpakete. Offline-Installation: [00-setup-and-installation.md](../../00-setup-and-installation.md), Abschnitt „Fallbacks“.
