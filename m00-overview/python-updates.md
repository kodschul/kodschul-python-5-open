# Python-Neuerungen 3.12 bis 3.15

Stand: 08.11.2026 · Kursversion: Python 3.14

| Version | Erschienen |
| --- | --- |
| 3.12 | 02.10.2023 |
| 3.13 | 07.10.2024 |
| 3.14 | 07.10.2025 |
| 3.15 | 09.10.2026 |

## Was Einsteiger heute anders lernen

| Neuerung | Seit | Was es für Einsteiger bedeutet | Im Kurs |
| --- | --- | --- | --- |
| Fehlermeldung schlägt fehlenden Import vor („Did you forget to import 'sys'?“) | 3.12 | häufiger Anfängerfehler erklärt sich selbst | [Lab 7.1](../m07-exceptions/l01-tracebacks/l01-tracebacks-thx.md) |
| SQLite-Shell `python -m sqlite3` | 3.12 | SQL ausprobieren ohne Zusatzprogramm | [Lab 18.1](../m18-sqlite/l01-sql/l01-sql-thx.md) |
| Neuer interaktiver Modus: Farben, mehrzeilig bearbeiten, `exit` ohne Klammern | 3.13 | REPL ist bequemer zum Ausprobieren | [Lab 1.2](../m01-introduction/l02-environment/l02-environment-thx.md) |
| REPL färbt den Code ein | 3.14 | Tippfehler fallen sofort auf | [Lab 1.2](../m01-introduction/l02-environment/l02-environment-thx.md) |
| Farbige Tracebacks, Vorschläge („Did you mean …?“) | 3.13 | Fehlerstelle und Lösung schneller sichtbar | [Lab 7.1](../m07-exceptions/l01-tracebacks/l01-tracebacks-thx.md) |
| Vorschlag bei vertipptem Schlüsselwort (`whille` → `while`) | 3.14 | Syntaxfehler werden verständlicher | [Lab 7.1](../m07-exceptions/l01-tracebacks/l01-tracebacks-thx.md) |
| `except A, B:` ohne Klammern (PEP 758) | 3.14 | neue Schreibweise lesen können; mit `as` bleiben Klammern Pflicht | [Lab 7.2](../m07-exceptions/l02-try-except/l02-try-except-thx.md) |
| Template-Strings `t"..."` (PEP 750) | 3.14 | Ausblick; `f"..."` bleibt der Standard | [Lab 2.4](../m02-basics/l04-strings/l04-strings-thx.md) |
| `Path.copy()`, `.copy_into()`, `.move()`, `.move_into()` | 3.14 | Dateien und Ordner ohne `shutil` kopieren und verschieben | [Lab 14.3](../m14-scripting/l03-filesystem/l03-filesystem-thx.md) |
| UTF-8 als Standard-Kodierung (PEP 686) | 3.15 | Umlaute überall gleich; `encoding="utf-8"` trotzdem angeben | [Lab 8.1](../m08-files/l01-text-files/l01-text-files-thx.md) |
| Explizite Lazy Imports `lazy import json` (PEP 810) | 3.15 | Ausblick; Module laden erst bei Bedarf | [Lab 6.1](../m06-modules/l01-modules/l01-modules-thx.md) |
| Free-Threading ohne GIL offiziell unterstützt (PEP 779) | 3.14 | Ausblick: echte Parallelität, optionaler Build | [Lab 20.2](../m20-final-project/l02-showcase/l02-showcase-thx.md) |
| JIT-Compiler in den Installern für Windows und macOS (experimentell) | 3.14 | Ausblick: schneller ohne Code-Änderung | [Lab 20.2](../m20-final-project/l02-showcase/l02-showcase-thx.md) |
| `uv` (Astral): ersetzt `pip` und `venv`, deutlich schneller | 15.02.2024 | Alternative; Kurs bleibt bei `venv` + `pip` | [Lab 6.2](../m06-modules/l02-pypi/l02-pypi-thx.md) |
| Ruff: Linter und Formatter in einem (Formatter seit 24.10.2023) | 2023 | formatiert Code beim Speichern nach PEP 8 | [Lab 2.1](../m02-basics/l01-syntax/l01-syntax-thx.md) |

## Gut zu wissen

- `os.path` und `shutil` stehen in älterem Code; Hauptweg ist `pathlib`.
- `print "Hallo"` ohne Klammern ist Python 2 und veraltet.
- Annotationen werden seit 3.14 verzögert ausgewertet (PEP 649/749); für Einsteiger ohne Folgen.

## Quellen

- [What's New in Python 3.12](https://docs.python.org/3/whatsnew/3.12.html)
- [What's New in Python 3.13](https://docs.python.org/3/whatsnew/3.13.html)
- [What's New in Python 3.14](https://docs.python.org/3/whatsnew/3.14.html)
- [What's New in Python 3.15](https://docs.python.org/3/whatsnew/3.15.html)
- [PEP 686](https://peps.python.org/pep-0686/), [PEP 750](https://peps.python.org/pep-0750/), [PEP 758](https://peps.python.org/pep-0758/), [PEP 779](https://peps.python.org/pep-0779/), [PEP 810](https://peps.python.org/pep-0810/)
- [Astral-Blog: uv, Ruff Formatter](https://astral.sh/blog)

Alle Angaben abgerufen am 08.11.2026.
