# Modul 3 – Transferübung: Würfeln bis zur 6

**Einsatz:** optional, Selbstlernen; kein eigener Zeitslot
**Dauer:** ca. 20 Minuten
**Ändert die Zahlenraten-Projektbasis?** Nein — eigenständiges kleines Programm, das Bedingungen, Zufall und Schleifen aus den Labs 3.1–3.4 ohne Vorlage kombiniert.
**Arbeitsdatei:** `playground/dice_until_six.py` (neu)
**Starter:** keiner, leere Datei

## Ausgangslage

Ein Würfelprogramm würfelt so lange, bis eine 6 fällt, zählt die Würfe und bewertet das Ergebnis. Vorher gibt die spielende Person eine Schätzung ab, wie viele Würfe es dauert.

Gewünschte Ausgabe (Zahlen weichen ab):

```text
Wie viele Würfe bis zur ersten 6? 4
Wurf 1: 2
Wurf 2: 3
Wurf 3: 1
Wurf 4: 6
Würfe bis zur 6: 4
Geduld gebraucht.
Schätzung 4: getroffen
```

## Vorbereitung

- Terminal im Ordner `project/`, `.venv` aktiv.
- Neue Datei `playground/dice_until_six.py` in VS Code anlegen (Explorer → Symbol **New File…**, wie in Lab 2.1).

## Aufgaben

1. Importiere `random`, würfle eine Zahl von 1 bis 6 und gib sie als `Wurf 1: <Zahl>` aus. Starte das Programm.
2. Wiederhole das Würfeln mit `while True:` und `break`, bis eine 6 fällt (Muster „Wiederholen, bis etwas eintritt“ aus Lab 3.3). Zähle die Würfe in einer Variablen `rolls` mit und gib danach `Würfe bis zur 6: <n>` aus.
3. Bewerte das Ergebnis mit `if`, `elif` und `else`: 1 Wurf → `Sofort!`, bis 3 Würfe → `Schnell.`, sonst `Geduld gebraucht.`.
4. Frage ganz am Anfang nach einer Schätzung (`Wie viele Würfe bis zur ersten 6? `) und gib am Ende mit einem Bedingungsausdruck `Schätzung <n>: getroffen` oder `Schätzung <n>: daneben` aus.
5. Setze vorübergehend `random.seed(4)` unter den `import`, starte zweimal und vergleiche die Würfe. Entferne die Zeile danach wieder.

## Checkpoint

- Das Programm endet immer mit einem Wurf `6`.
- Die gezählten Würfe stimmen mit der Zahl der Zeilen `Wurf …` überein.
- Mit `random.seed(4)` liefern beide Starts dieselbe Wurffolge.

## Abschlusskriterien

- `playground/dice_until_six.py` nutzt `import random`, eine `while`-Schleife mit Zähler, eine `if`-`elif`-`else`-Kette und einen Bedingungsausdruck.
- Ohne Seed liefert jeder Start eine andere Wurffolge.

## Erweiterung

Lege eine äußere Schleife „Nochmal würfeln? (j/n)“ um das ganze Programm, wie beim Zahlenraten in Lab 3.4.
