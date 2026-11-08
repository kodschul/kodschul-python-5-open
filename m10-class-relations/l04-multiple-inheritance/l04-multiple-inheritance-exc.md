# Lab 10.4 – Übung: Mehrfachvererbung und Mixins

**Dauer:** ca. 8 Minuten
**Ändert die Zahlenraten-Projektbasis?** Nein — die Übung arbeitet mit einer eigenen Datei; das Spiel bleibt auf dem Stand von Lab 10.3.
**Arbeitsdatei:** `playground/mro_quiz.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Kopiere `code/m10-class-relations/mro_quiz.py` per **Copy**/**Paste** nach `playground/`.
- Noch **nicht** starten: Erst vorhersagen, dann prüfen.

## Aufgaben

1. Öffne `playground/mro_quiz.py` und lies nur „Teil 1: die Klassen“. Zeichne auf Papier das Vererbungsdiagramm von `Device`, `Phone`, `Camera` und `Smartphone`.
2. Sage für `Smartphone`, `CameraPhone` und `LoggingSmartphone` die MRO voraus (alle Klassennamen in Suchreihenfolge, bis `object`) und welchen Text `info()` jeweils liefert. Trage beides in die Tabelle unten ein.
3. Starte `python mro_quiz.py` und vergleiche die Ausgabe mit der Tabelle. Markiere jede falsche Vorhersage und notiere, welche MRO-Regel sie erklärt.
4. Ergänze am Ende von Teil 1 die Klasse `class Broken(Device, Phone):` mit `pass` als Körper. Sage voraus, was beim Start passiert, und starte erneut.
5. Entferne `Broken` wieder und vertausche in `Smartphone` die Basisklassen zu `(Camera, Phone)`. Sage die neue Ausgabe von `Smartphone().info()` voraus und prüfe sie.

| Klasse | vorhergesagte MRO | vorhergesagtes `info()` | stimmt? |
| --- | --- | --- | --- |
| `Smartphone` | | | |
| `CameraPhone` | | | |
| `LoggingSmartphone` | | | |

## Checkpoint

- Die Tabelle ist ausgefüllt, jede Zeile ist mit der Ausgabe von `mro_quiz.py` verglichen.
- Für `Broken` erscheint ein `TypeError`, bevor irgendetwas ausgegeben wird.

## Abschlusskriterien

- Für jede der drei Klassen ist begründet, warum `info()` genau diesen Text liefert.
- Die Regeln „Kind vor Eltern“ und „links vor rechts“ sind an einem eigenen Beispiel geprüft.

## Erweiterung

Lege `playground/notify.py` an: Ein `EmailMixin` mit `send_email(text)` (druckt `E-Mail an <self.email>: <text>`) und ein `SmsMixin` mit `send_sms(text)` (druckt `SMS an <self.phone>: <text>`). Eine Klasse `Customer` mit `name`, `email` und `phone` erbt beide Mixins und hat eine Methode `remind()`, die beide Kanäle nutzt. Gib zum Schluss `Customer.mro()` aus.
