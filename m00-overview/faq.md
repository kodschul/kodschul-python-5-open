# FAQ: Python Programmierung

## Setup

**Welche Python-Version?**

- Python 3.14; Prüfung mit `python --version` (macOS, Linux: `python3 --version`).
- 3.15 ist erschienen, aber noch nicht jede Bibliothek bietet fertige Pakete an.
- Details: [Setup](../00-setup-and-installation.md), [Neuerungen](python-updates.md)

**Unter Windows öffnet `python` den Microsoft Store. Was tun?**

- Python installieren, Terminal neu öffnen.
- Sonst App-Ausführungsaliase für `python.exe` ausschalten: [Setup](../00-setup-and-installation.md)

**macOS zeigt `Python 3.9`. Ist das falsch?**

- Das ist das System-Python von Apple.
- venv gezielt mit `python3.14 -m venv .venv` anlegen: [Lab 1.2](../m01-introduction/l02-environment/l02-environment-thx.md)

**Ist Git nötig?**

- Nein. Kurs-Repo auf GitHub über **Code → Download ZIP** laden und entpacken.

## Virtuelle Umgebung

**Woran ist eine aktive venv zu erkennen?**

- `(.venv)` steht vor der Eingabezeile.
- VS Code zeigt `.venv` unten rechts in der Statusleiste.

**PowerShell meldet `Activate.ps1 cannot be loaded`.**

- Einmal ausführen: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`
- Details: [Setup](../00-setup-and-installation.md)

**`ModuleNotFoundError: No module named 'rich'`?**

- venv ist nicht aktiv oder Pakete fehlen.
- Aktivieren, dann `pip install -r requirements.txt`: [Lab 6.2](../m06-modules/l02-pypi/l02-pypi-thx.md)

## Fehler

**Die Fehlermeldung ist lang. Wo anfangen?**

- Letzte Zeile: was? Zeile darüber: wo? Dann nach oben: wie kam es dazu?
- Details: [Lab 7.1](../m07-exceptions/l01-tracebacks/l01-tracebacks-thx.md)

**`IndentationError` – was ist falsch?**

- Einrückung passt nicht; 4 Leerzeichen pro Ebene.
- Ruff formatiert beim Speichern: [Lab 2.1](../m02-basics/l01-syntax/l01-syntax-thx.md)

**Warum ergibt `"3" + "4"` den Text `"34"`?**

- `input()` liefert immer Text; erst `int()` macht eine Zahl daraus.
- Details: [Lab 2.2](../m02-basics/l02-variables/l02-variables-thx.md)

**Das Programm läuft ohne Fehler, tut aber das Falsche.**

- Logikfehler: mit Haltepunkt und Debugger Schritt für Schritt prüfen.
- Details: [Lab 7.4](../m07-exceptions/l04-debugging/l04-debugging-thx.md)

**Das Terminal läuft voll und reagiert nicht mehr.**

- Endlosschleife: mit `Strg+C` abbrechen.
- Details: [Lab 3.3](../m03-control-flow/l03-loops/l03-loops-thx.md)

## Übungen und Projekt

**Rückstand im Spiel: Wie gelingt der Wiedereinstieg?**

- Starter aus `project/starters/` nach `playground/` kopieren.
- Jeder Starter enthält alle vorherigen Labs: [project/README.md](../project/README.md)
- Fertige Lösung: `-sol.md` des Labs und `project/examples/`.

**Früh fertig: Was nun?**

- Die generische Aufgabe aus `code/` selbst lösen.
- Erweiterungsaufgabe im `-exc.md` bearbeiten.

## Nach dem Kurs

**Wie geht es weiter?**

- Web, Testen, Typprüfung, Packaging, Data Science, Machine Learning.
- Je ein erster Schritt am eigenen Spiel: [Lab 20.2](../m20-final-project/l02-showcase/l02-showcase-thx.md)

**Lohnt sich `uv` statt `pip` und `venv`?**

- `uv` ersetzt `pip` und `venv` und ist schneller; separat zu installieren.
- Vergleich der Befehle: [Lab 6.2](../m06-modules/l02-pypi/l02-pypi-thx.md)

**Wo nachschlagen?**

- [Glossar](glossary.md), [Best Practices](best-practices.md), Spickzettel im jeweiligen Modulordner.
- Offizielle Doku: [docs.python.org](https://docs.python.org/3.14/)
