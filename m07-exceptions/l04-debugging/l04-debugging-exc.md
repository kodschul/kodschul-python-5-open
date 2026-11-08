# Lab 7.4 – Übung: Zwei versteckte Fehler finden

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Nein — die fehlerhafte Version ersetzt das eigene Spiel nur für diese Übung; nach dem Beheben entspricht sie dem Stand nach Lab 7.3.
**Arbeitsdatei:** `playground/guess_game/ui.py`
**Starter:** `starters/m07-l04-guess_game/` mit `ui.py` (Stand nach Lab 7.3 mit zwei Logikfehlern)

## Vorbereitung

- In VS Code ist der Ordner `project/` geöffnet, `.venv` ist als Interpreter gewählt (Statusleiste unten rechts).
- Benenne den eigenen Ordner `playground/guess_game/` im Explorer in `guess_game_7_3` um (F2), damit er erhalten bleibt.
- Kopiere `examples/m07-exceptions/l03-raise/guess_game/` nach `playground/` (Rechtsklick → **Copy**, Rechtsklick auf `playground/` → **Paste**). Kopiere danach `starters/m07-l04-guess_game/ui.py` nach `playground/guess_game/` und ersetze die vorhandene Datei.

## Aufgaben

1. Öffne die Ansicht **Run and Debug** (Strg+Shift+D), wähle oben „Spiel debuggen (python -m guess_game)“ und starte mit F5. Spiele eine Runde auf Stufe `leicht` mit den Tipps `500`, `5`, `5`, `8` und weiteren Zahlen bis zum Ende. Notiere die zwei Stellen, an denen die Ausgabe nicht zu den Spielregeln passt (ungültige Tipps kosten keinen Versuch; „Zu hoch.“ nur bei zu großem Tipp). Beende mit Shift+F5.
2. Setze in `playground/guess_game/ui.py` einen Haltepunkt auf die Zeile `guess = ask_number("Tipp: ")` in `play_round` und starte erneut mit F5. Trage unter **Watch** den Ausdruck `max_tries - tries` ein.
3. Drücke Step Over (F10), tippe im Terminal `500` und Enter, und gehe dann mit F10 Zeile für Zeile weiter. Beobachte `tries` unter Variables: Finde die Zeile, nach der `tries` steigt, obwohl der Tipp ungültig ist. Behebe den Fehler, speichere (Strg+S) und starte neu (Restart).
4. Tippe einen gültigen Tipp und gehe mit Step Over bis zur Zeile `show_hint(guess, secret)`. Prüfe in der Debug Console `guess > secret`. Springe mit Step Into (F11) in `show_hint` und finde die Zeile, die den falschen Hinweis wählt. Behebe den Fehler.
5. Entferne den Haltepunkt, starte erneut und spiele die Runde aus Aufgabe 1 noch einmal. Notiere zu jedem Fehler die Zeile und die Ursache in einem Satz.

## Checkpoint

- Nach `500` und einem doppelten Tipp bleibt `max_tries - tries` unverändert; nach dem ersten gültigen Fehltipp steht `Verbleibende Versuche: 4`.
- Ein Tipp unter der Geheimzahl ergibt „Zu niedrig.“ (blau), über der Geheimzahl „Zu hoch.“ (rot).
- Zwei Sätze beschreiben die beiden Ursachen.

## Abschlusskriterien

- `playground/guess_game/ui.py` enthält beide Korrekturen; das Spiel verhält sich wie der Stand nach Lab 7.3.
- Zu beiden Fehlern sind Zeile und Ursache notiert.

## Erweiterung

Debugge `code/m07-exceptions/bank_withdraw.py` mit der Konfiguration „Aktuelle Datei debuggen“: Setze einen bedingten Haltepunkt (Rechtsklick links neben die Zeile → **Add Conditional Breakpoint…**) auf die Zeile `balance = withdraw(balance, amount)` mit der Bedingung `amount < 0`. Prüfe mit Step Into, in welcher Zeile von `withdraw` die Funktion verlassen wird, und beobachte, dass `balance` danach unverändert bleibt.
