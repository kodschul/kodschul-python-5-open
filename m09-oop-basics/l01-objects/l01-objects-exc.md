# Lab 9.1 – Übung: Das Spiel als Modell

**Dauer:** ca. 10 Minuten
**Ändert die Zahlenraten-Projektbasis?** Nein — Modell auf Papier; Lab 9.2 setzt das erste Ding (`Game`) als Klasse um.
**Arbeitsdatei:** Papier oder `playground/model.md`
**Starter:** keiner

## Vorbereitung

- Papier und Stift, oder in VS Code die Datei `playground/model.md` anlegen und den Spielablauf unten hineinkopieren.
- Grundlage ist das Spiel v2 von Tag 2. Zum Auffrischen einmal spielen: im Ordner `project/` erst `cd examples/m08-files/l03-csv`, dann `python -m guess_game`.

**Spielablauf (Stand v2):**

1. Eine Spielerin gibt ihren Namen ein und wählt eine Stufe.
2. Das Spiel zieht passend zur Stufe eine Geheimzahl aus einem Bereich (z. B. 1 bis 10) und erlaubt eine feste Zahl von Versuchen.
3. Die Spielerin gibt Tipps ab. Das Spiel prüft jeden Tipp, merkt sich die bisherigen Tipps und meldet „zu hoch“, „zu niedrig“ oder „richtig“.
4. Das Spiel ist vorbei, wenn die Zahl getroffen ist oder keine Versuche mehr übrig sind.
5. Am Ende entsteht ein Ergebnis mit Name, Stufe, Versuchen, Dauer, gewonnen ja/nein und Datum. Gewonnene Ergebnisse kommen in die Bestenliste, sortiert nach den wenigsten Versuchen.

**Vorlage:**

| Ding (Klasse) | weiß (Attribute) | kann (Methoden) |
| --- | --- | --- |
| | | |
| | | |
| | | |

## Aufgaben

1. Unterstreiche im Spielablauf alle Substantive und kreise alle Verben ein (in `model.md`: Substantive **fett**, Verben _kursiv_).
2. Wähle drei Substantive, die eine eigene Klasse verdienen, weil sie mehrere Werte und eigenes Verhalten haben. Trage sie als Einzahl in die Spalte „Ding“ ein.
3. Ergänze für jedes Ding, was es weiß (mindestens zwei Attribute) und was es kann (mindestens eine Methode, als Verb mit `()`).
4. Ordne die Funktionen aus v2 einem Ding zu oder markiere sie als reine Ein-/Ausgabe: `draw_secret`, `check_guess`, `is_guess_correct`, `is_game_over`, `ask_number`, `show_hint`, `top_five`.
5. Zeichne das Ding „Spiel“ als Klassendiagramm (Kasten mit drei Fächern: Name, Attribute, Methoden) und prüfe: Steht der Spielername beim Spieler oder beim Spiel?

## Checkpoint

- Die Tabelle enthält drei Dinge mit Namen in der Einzahl.
- Jedes Ding hat mindestens zwei Attribute und eine Methode; alle Methoden sind Tätigkeiten.
- Jede der sieben Funktionen ist einem Ding oder der Ein-/Ausgabe zugeordnet.

## Abschlusskriterien

- Ein Klassendiagramm für das Spiel mit Attributen und Methoden liegt vor (Papier oder `model.md`).

## Erweiterung

Modelliere eine Stadtbibliothek mit derselben Methode: Ausgangstext „Ein Mitglied leiht Bücher aus und gibt sie bis zu einem Rückgabedatum zurück; die Bibliothek mahnt verspätete Ausleihen.“ Fülle die Tabelle für drei Dinge.
