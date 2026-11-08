# Lab 2.3 – Übung: Tipp mit der Geheimzahl vergleichen

**Dauer:** ca. 12 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — das Spiel kennt eine feste Geheimzahl und meldet `True` oder `False`; Lab 3.1 macht daraus „zu hoch“ / „zu niedrig“.
**Arbeitsdatei:** `playground/guess_game.py`
**Starter:** `starters/m02-l03-guess_game.py`

## Vorbereitung

- Eigene `playground/guess_game.py` aus Lab 2.2 weiterverwenden oder den Starter dorthin kopieren.
- Terminal im Ordner `project/`, virtuelle Umgebung aktiv.

## Aufgaben

1. Lege ganz oben unter dem Kopfkommentar die Variable `secret` mit dem Wert `7` an.
2. Gib am Ende mit `print` den Text „Treffer:“ und das Ergebnis von `guess == secret` aus.
3. Starte das Spiel zweimal: einmal mit dem Tipp `7`, einmal mit `5`.
4. Ergänze eine Zeile, die ausgibt, ob der Tipp im erlaubten Bereich liegt („Im Bereich:“ und `1 <= guess <= 10`). Teste mit `5` und `12`.
5. Entferne testweise `int(...)` um die Tipp-Eingabe, starte mit `7` und beobachte die Treffer-Zeile. Stelle danach den alten Stand wieder her.

## Checkpoint

- Tipp `7` ergibt `Treffer: True`, Tipp `5` ergibt `Treffer: False`.
- Tipp `12` ergibt `Im Bereich: False`.
- Ohne `int()` ergibt auch der Tipp `7` `Treffer: False`. Danach bricht das Programm in der Bereichs-Zeile mit `TypeError: '<=' not supported between instances of 'int' and 'str'` ab: Text und Zahl lassen sich nicht der Größe nach vergleichen.

## Abschlusskriterien

- `secret` steht vor dem Banner, der Vergleich nutzt `==`.
- Das Spiel läuft mit Zahlen-Eingaben ohne Fehlermeldung.

## Erweiterung

Schreibe `playground/even.py`: Lies eine Zahl ein, gib den Rest beim Teilen durch 2 aus und darunter „gerade:“ mit dem passenden Wahrheitswert. Teste mit `7` und `12`. Vergleich: `code/m02-basics/even.py`.
