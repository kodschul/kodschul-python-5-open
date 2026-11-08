# Lab 2.4 – Übung: Spielernamen aufräumen und persönlich begrüßen

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — der Name wird bereinigt und die Begrüßung nennt ihn; Lab 3.1 baut darauf auf.
**Arbeitsdatei:** `playground/guess_game.py`
**Starter:** `starters/m02-l04-guess_game.py`

## Vorbereitung

- Eigene `playground/guess_game.py` aus Lab 2.3 weiterverwenden oder den Starter dorthin kopieren.
- Terminal im Ordner `project/`, virtuelle Umgebung aktiv.

## Aufgaben

1. Hänge in der Zeile `name = input("Name: ")` die Methoden `strip()` und `title()` an, sodass der bereinigte Name in `name` landet.
2. Entferne die Zeile „Rate eine Zahl zwischen 1 und 10.“ aus dem Banner.
3. Gib direkt nach der Namensabfrage mit einem f-String „Hallo <Name>! Rate eine Zahl zwischen 1 und 10.“ aus.
4. Starte das Spiel und gib als Namen `  aNNa ` (mit Leerzeichen davor und danach) und als Tipp `7` ein.
5. Starte erneut mit dem Namen `aNNA-lena` und beobachte die Begrüßung.

## Checkpoint

- Mit `  aNNa ` erscheint `Hallo Anna! Rate eine Zahl zwischen 1 und 10.` und später `Anna tippt 7`.
- Mit `aNNA-lena` erscheint `Hallo Anna-Lena! …`.

## Abschlusskriterien

- Der Name wird genau einmal bereinigt, direkt bei der Eingabe.
- Das Banner hat drei Zeilen, die Begrüßung mit Namen folgt nach der Eingabe.

## Erweiterung

Schreibe `playground/email_parts.py`: Lies eine E-Mail-Adresse ein, entferne Leerzeichen am Rand, schreibe sie klein und gib den Teil vor dem `@` und die Domain getrennt aus. Teste mit ` anna@Uni-Beispiel.DE `. Vergleich: `code/m02-basics/email_parts.py`.
