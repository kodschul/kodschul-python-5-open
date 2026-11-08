# Setup und Installation

Diese Anleitung bringt Python 3.14, VS Code und das Kurs-Repo auf den eigenen Laptop, in der Reihenfolge der Abschnitte. Nach jedem Schritt steht eine Prüfung. Stand aller Versionsangaben: 08.11.2026.

## Checkliste

| Werkzeug | Version | Prüfung |
| --- | --- | --- |
| Python | 3.14 (empfohlen; 3.15 ist erschienen, siehe unten) | `python --version` (Windows, Weg A), `py -V:3.14 --version` (Windows, Weg B) bzw. `python3 --version` (macOS, Linux) |
| VS Code | aktuell | Programm startet |
| VS Code-Erweiterung „Python“ (Microsoft) | aktuell | erscheint unter **Extensions → Installed** |
| VS Code-Erweiterung „Ruff“ (Astral) | aktuell | erscheint unter **Extensions → Installed** |
| Kurs-Repo | ZIP, entpackt | Ordner `project/` mit `requirements.txt` vorhanden |
| Netzzugang | `pypi.org`, `files.pythonhosted.org` | `pip install -r requirements.txt` läuft durch |
| Rechte | Installation von Programmen im eigenen Benutzerkonto | siehe „Ohne Administratorrechte“ |

**Warum Python 3.14 und nicht 3.15?** Python 3.15 ist seit 09.10.2026 verfügbar. Für eine neue Version bieten noch nicht alle Bibliotheken fertige Installationspakete an; 3.14 (aktuell 3.14.10 vom 25.10.2026) läuft mit allen Kurspaketen. Quelle: [python.org/downloads](https://www.python.org/downloads/), abgerufen am 08.11.2026.

## Shell-Regel

Alle Befehle im Kurs laufen im **Terminal von VS Code** (**Terminal → New Terminal**):

| System | Shell im VS-Code-Terminal | Aktivieren der venv |
| --- | --- | --- |
| Windows | PowerShell (Standard) | `.venv\Scripts\Activate.ps1` |
| macOS | zsh (Standard) | `source .venv/bin/activate` |
| Linux | bash (Standard) | `source .venv/bin/activate` |

Nach dem Aktivieren sind `python` und `pip` auf allen Systemen dieselben Befehle; nur die Aktivierungszeile unterscheidet sich.

## Python installieren: Windows

Stand 08.11.2026 gibt es unter Windows zwei offizielle Wege ([Using Python on Windows](https://docs.python.org/3.14/using/windows.html)):

| Weg | Was es ist | Für den Kurs |
| --- | --- | --- |
| A: Installer von python.org (`python-3.14.x-amd64.exe`) | klassischer Installer, eine Python-Version | **empfohlen**: einfach, `python` ist danach Python 3.14 |
| B: Python Install Manager (python.org oder Microsoft Store) | neuer Verwalter für mehrere Python-Versionen, Befehle `py`, `python`, `pymanager` | Alternative, auch ohne Administratorrechte |

Der klassische Installer gilt seit Python 3.14 als veraltet und wird ab Python 3.16 nicht mehr angeboten; für 3.14 ist er weiterhin offiziell verfügbar. Ebenso ist der alte `py`-Launcher durch den Install Manager ersetzt.

### Weg A: Installer von python.org

1. Auf [python.org/downloads/windows](https://www.python.org/downloads/windows/) unter „Python 3.14.x“ den **Windows installer (64-bit)** laden (ARM-Laptops: **ARM64**).
2. Installer starten. Im ersten Fenster unten den Haken bei **Add python.exe to PATH** setzen (in älteren Versionen „Add Python 3.x to PATH“, siehe Bild).
3. Den Haken darüber **entfernen**: „Use admin privileges when installing py.exe“ (in älteren Versionen „Install launcher for all users“). Ist er gesetzt, zeigt **Install Now** ein Schild-Symbol und fragt nach Administratorrechten.
4. **Install Now** wählen. Ohne den Haken aus Schritt 3 gilt die Installation nur für das eigene Benutzerkonto und braucht keine Administratorrechte.
5. VS Code und alle Terminals schließen und neu öffnen, damit sie den neuen Suchpfad (PATH) kennen.

<img src="https://docs.python.org/3.14/_images/win_installer.png" alt="Erstes Fenster des Python-Installers für Windows mit Install Now, Customize installation und dem Haken für PATH unten" width="560" />

_Installer-Fenster aus der Python-Dokumentation (zeigt Version 3.8.0 im Ausgangszustand: Launcher-Haken gesetzt, PATH-Haken nicht gesetzt; für den Kurs genau umgekehrt einstellen; Aufbau bei 3.14 gleich). Quelle: docs.python.org, „Using Python on Windows“ (https://docs.python.org/3.14/using/windows.html), PSF-Lizenz, abgerufen am 08.11.2026._

PATH ist die Liste der Ordner, in denen das Terminal nach Befehlen sucht. Ohne den Haken findet das Terminal `python` nicht.

Prüfung in einem neuen PowerShell-Terminal:

```powershell
python --version
```

Erwartet: `Python 3.14.x`.

### Weg B: Python Install Manager

1. Den **Python Install Manager** installieren: aus dem Microsoft Store (Suche „Python Install Manager“) oder über „Download using the Python install manager“ auf [python.org/downloads/windows](https://www.python.org/downloads/windows/). Beide Varianten sind laut Dokumentation identisch.
2. Im Terminal Python 3.14 installieren und prüfen:

```powershell
py install 3.14
py list
py -V:3.14 --version
```

Erwartet: `py list` führt einen Eintrag `3.14` auf, die letzte Zeile zeigt `Python 3.14.x`. Bei Weg B die Prüfung immer mit `py` statt `python --version` machen, denn `python` kann auf eine andere installierte Version zeigen.

3. Die venv im Kurs mit `py -V:3.14 -m venv .venv` anlegen (statt `python -m venv .venv`). So entsteht sie sicher mit 3.14, auch wenn später weitere Versionen installiert werden.

### Typischer Windows-Stolperstein: `python` öffnet den Microsoft Store

Windows liefert einen Platzhalter-Befehl `python`, der nur den Store öffnet. Abhilfe: Python nach Weg A oder B installieren und das Terminal neu öffnen. Hilft das nicht, unter **Einstellungen → Apps → Erweiterte App-Einstellungen → App-Ausführungsaliase** die Einträge „python.exe“ und „python3.exe“ für den App-Installer ausschalten.

## Python installieren: macOS

| Weg | Vorgehen |
| --- | --- |
| Installer von python.org (empfohlen) | auf [python.org/downloads/macos](https://www.python.org/downloads/macos/) den „macOS 64-bit universal2 installer“ für 3.14.x laden, `.pkg` öffnen, den Schritten folgen (braucht das Passwort eines Administratorkontos) |
| Homebrew (wer es schon nutzt) | `brew install python@3.14`; danach heißt der Befehl `python3.14` |

<img src="https://docs.python.org/3.14/_images/mac_installer_01_introduction.png" alt="Erstes Fenster des Python-Installers für macOS mit Introduction, Read Me, License und Continue" width="560" />

_Installer-Fenster aus der Python-Dokumentation (zeigt 3.13.0; Aufbau bei 3.14 gleich). Quelle: docs.python.org, „Using Python on macOS“ (https://docs.python.org/3.14/using/mac.html), PSF-Lizenz, abgerufen am 08.11.2026._

Nach dem Installer von python.org im Ordner `/Programme/Python 3.14/` einmal **Install Certificates.command** doppelklicken; das richtet die Zertifikate für sichere Downloads ein.

Prüfung im Terminal:

```bash
python3 --version
```

Zeigt das eine andere Version (z. B. das von Apple mitgelieferte `Python 3.9.6`), gezielt `python3.14 --version` prüfen und die venv mit `python3.14 -m venv .venv` anlegen. `python` ohne `3` gibt es unter macOS vor dem Aktivieren der venv nicht.

## Python installieren: Linux

| Distribution | Befehl |
| --- | --- |
| Ubuntu 26.04 LTS, Debian-basiert | `sudo apt install python3 python3-venv python3-pip` (Ubuntu 26.04 bringt Python 3.14 mit) |
| Fedora | `sudo dnf install python3` |
| ältere Ubuntu-Versionen ohne 3.14 | Python 3.14 aus dem „deadsnakes“-PPA: `sudo add-apt-repository ppa:deadsnakes/ppa`, dann `sudo apt install python3.14 python3.14-venv` |

Prüfung: `python3 --version` bzw. `python3.14 --version`. Das System-Python von Linux nie mit `sudo pip install` verändern; Pakete kommen immer in die venv.

## VS Code und Erweiterungen

1. VS Code von [code.visualstudio.com](https://code.visualstudio.com) installieren (Windows: „User Installer“ braucht keine Administratorrechte).
2. Links die Ansicht **Extensions** (Erweiterungen) öffnen (`Strg+Shift+X`, macOS `Cmd+Shift+X`).
3. Nach „Python“ suchen und die Erweiterung **Python** von **Microsoft** (blauer Haken) installieren. Die Erweiterung bringt den Python Debugger mit.
4. Nach „Ruff“ suchen und **Ruff** von **Astral Software** installieren. Ruff prüft und formatiert Python-Code (Lab 2.1).

<img src="https://code.visualstudio.com/assets/docs/configure/extensions/extension-marketplace/extensions-python.png" alt="VS Code Erweiterungsansicht mit Suche python und der Erweiterung Python von Microsoft" width="720" />

_Quelle: VS Code Docs, „Extension Marketplace“ (https://code.visualstudio.com/docs/configure/extensions/extension-marketplace), CC BY 4.0, abgerufen am 08.11.2026. Versionsnummer und Download-Zahlen sind heute höher._

## Kurs-Repo als ZIP

1. Auf der GitHub-Seite des Kurs-Repos **Code → Download ZIP** wählen. Git ist dafür nicht nötig.
2. ZIP in einen Ordner im eigenen Benutzerverzeichnis entpacken, z. B. `Dokumente/python-kurs/`. Nicht in OneDrive, iCloud oder Dropbox: Synchronisation und die vielen Dateien der venv vertragen sich schlecht.
3. In VS Code **File → Open Folder…** und den Ordner `project/` wählen.
4. **Terminal → New Terminal**. Das Terminal steht jetzt in `project/`.

Git ist für den Kurs nicht nötig.

## Virtuelle Umgebung und Pakete

Im Terminal von VS Code im Ordner `project/`:

| Schritt | Windows (PowerShell) | macOS, Linux |
| --- | --- | --- |
| venv anlegen | `python -m venv .venv` (Install Manager: `py -V:3.14 -m venv .venv`) | `python3 -m venv .venv` (oder `python3.14 -m venv .venv`) |
| aktivieren | `.venv\Scripts\Activate.ps1` | `source .venv/bin/activate` |
| Version prüfen | `python --version` | `python --version` |
| Pakete installieren | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Test | `python playground/hello.py` | `python playground/hello.py` |

Erwartet: `(.venv)` steht vor der Eingabezeile, `python --version` zeigt `Python 3.14.x`, `pip` endet mit `Successfully installed …`, der Test gibt `Hallo` aus.

Danach in VS Code `Strg+Shift+P` (macOS `Cmd+Shift+P`) → **Python: Select Interpreter** → Eintrag mit `.venv`. Unten rechts in der Statusleiste erscheint die venv:

<img src="https://code.visualstudio.com/assets/docs/python/shared/environment-in-status-bar.png" alt="VS Code Statusleiste mit Python-Version und ('.venv': venv)" width="560" />

_Quelle: VS Code Docs, „Python in Visual Studio Code“ (https://code.visualstudio.com/docs/languages/python), CC BY 4.0, abgerufen am 08.11.2026._

## PowerShell: Skripte erlauben (Windows)

Das Aktivieren startet das PowerShell-Skript `Activate.ps1`. Auf Windows-PCs ist das Ausführen von Skripten oft gesperrt; dann erscheint:

```text
.venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system.
```

Einmal ausführen (ohne Administratorrechte, gilt nur für das eigene Benutzerkonto):

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

| Teil | Bedeutung |
| --- | --- |
| `Set-ExecutionPolicy` | legt fest, welche PowerShell-Skripte laufen dürfen |
| `-Scope CurrentUser` | nur für das eigene Konto, nicht für den ganzen Rechner |
| `RemoteSigned` | Skripte, die auf dem eigenen Rechner entstehen (wie `Activate.ps1`), dürfen laufen; aus dem Internet geladene Skripte brauchen eine digitale Signatur |

Ist nichts eingestellt, gilt auf Windows-PCs `Restricted` (keine Skripte). Prüfen mit `Get-ExecutionPolicy -List`. Quelle: [about_Execution_Policies](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_execution_policies), abgerufen am 08.11.2026. Ist die Einstellung durch die IT gesperrt (Gruppenrichtlinie), hilft die IT-Abteilung; als Notlösung im Terminal-Menü von VS Code das Profil „Command Prompt“ wählen und mit `.venv\Scripts\activate.bat` aktivieren.

## Ohne Administratorrechte

| System | Weg |
| --- | --- |
| Windows | Weg A mit **Install Now** ohne Haken „Use admin privileges …“ (nur eigenes Konto) oder Weg B aus dem Microsoft Store; VS Code als „User Installer“ |
| macOS | Installer von python.org braucht ein Administratorkonto; ohne: Homebrew ist meist schon vorhanden oder die IT installiert Python 3.14 |
| Linux | `apt`/`dnf` brauchen `sudo`; ohne: die IT installiert `python3.14` und `python3.14-venv` |

## Prüfliste vor Kursbeginn

- [ ] `python --version` (Windows, Weg A), `py -V:3.14 --version` (Weg B) bzw. `python3 --version` oder `python3.14 --version` zeigt `Python 3.14.x`.
- [ ] VS Code startet; Erweiterungen „Python“ (Microsoft) und „Ruff“ sind installiert.
- [ ] Kurs-Repo ist entpackt; `project/` ist in VS Code geöffnet.
- [ ] `.venv` ist angelegt und aktiviert: `(.venv)` vor der Eingabezeile.
- [ ] `pip install -r requirements.txt` endet mit `Successfully installed …`.
- [ ] `python playground/hello.py` gibt `Hallo` aus.
- [ ] Statusleiste von VS Code zeigt `.venv` als Interpreter.

## Fehlerbehebung

| Symptom | Ursache | Lösung |
| --- | --- | --- |
| `python` wird nicht erkannt (Windows) | Haken „Add python.exe to PATH“ fehlte oder Terminal ist älter als die Installation | VS Code neu starten; sonst Installer erneut starten → **Modify** bzw. neu installieren mit Haken, oder Weg B mit `py` |
| `python` öffnet den Microsoft Store | Platzhalter-Befehl von Windows | Python installieren; App-Ausführungsaliase für `python.exe` ausschalten (Abschnitt Windows) |
| `zsh: command not found: python` | unter macOS heißt der Befehl vor der venv `python3` | `python3 -m venv .venv`, danach aktivieren |
| `python3 --version` zeigt 3.9 oder eine andere alte Version | das System-Python wird gefunden | `python3.14 -m venv .venv` verwenden |
| `Activate.ps1 cannot be loaded …` | PowerShell sperrt Skripte | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| `No module named venv` oder `ensurepip is not available` (Linux) | Paket für virtuelle Umgebungen fehlt | `sudo apt install python3-venv` bzw. `python3.14-venv` |
| `(.venv)` fehlt im neuen Terminal | Aktivierung gilt pro Terminal | Aktivierungszeile erneut ausführen |
| `pip install` meldet `ERROR: Could not find a version that satisfies the requirement …` | falsches Python (zu alt) aktiv oder kein Netz | `python --version` prüfen (3.14?), venv neu anlegen; Netz prüfen |
| `pip install` hängt oder meldet `SSL: CERTIFICATE_VERIFY_FAILED` | Firmennetz mit Proxy oder fehlende Zertifikate (macOS) | macOS: `Install Certificates.command` ausführen; Proxy: `pip install --proxy http://<proxy>:<port> -r requirements.txt` (Adresse von der IT) |
| `can't open file '…playground/hello.py'` | Terminal steht nicht in `project/` | in VS Code `project/` öffnen, neues Terminal |
| VS Code zeigt `.venv` nicht bei **Select Interpreter** | venv fehlt oder falscher Ordner geöffnet | `project/` öffnen; **Enter interpreter path …** → `.venv/Scripts/python.exe` (Windows) bzw. `.venv/bin/python` |
| venv verhält sich seltsam nach Verschieben des Ordners | venv speichert feste Pfade | Ordner `.venv` löschen, neu anlegen, Pakete neu installieren |

## Fallbacks

| Situation | Lösung |
| --- | --- |
| Keine Rechte für den Installer (Windows) | Python Install Manager aus dem Microsoft Store (Weg B) |
| Kein Zugang zu `pypi.org` | Offline-Installation aus einem Ordner mit Paketdateien (unten); Labs bis Modul 5 brauchen keine Zusatzpakete |
| PowerShell-Skripte gesperrt und nicht freischaltbar | Terminal-Profil „Command Prompt“ und `.venv\Scripts\activate.bat` |

### Offline-Installation

Pakete gibt es als fertige Paketdateien mit der Endung `.whl` („Wheels“). Liegt zum Kurs ein Ordner `wheels/` mit allen Paketen für das eigene Betriebssystem bereit, installiert dieser Befehl ohne Internet:

```bash
pip install --no-index --find-links wheels -r requirements.txt
```

| Teil | Bedeutung |
| --- | --- |
| `--no-index` | nicht im Internet (PyPI) suchen |
| `--find-links wheels` | Paketdateien im Ordner `wheels/` verwenden |
| `-r requirements.txt` | genau die Pakete und Versionen aus der Kursliste |

Einschränkung: Wheels passen nur zu Betriebssystem, Prozessor und Python-Version, für die sie gebaut wurden (z. B. Windows 64 Bit mit Python 3.14).
