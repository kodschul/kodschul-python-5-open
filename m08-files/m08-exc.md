# Modul 8 – Transferübung: Lagerbericht aus Excel-CSV

**Einsatz:** optional, Selbstlernen; kein eigener Zeitslot
**Dauer:** ca. 30 Minuten
**Ändert die Zahlenraten-Projektbasis?** Nein — eigenständiges kleines Programm, das Funktionen (Modul 5), Module (Modul 6), Fehlerbehandlung (Modul 7) und Dateien (Modul 8) ohne Vorlage kombiniert. Referenz für den Aufbau: Spiel v2 in [project/examples/m08-files/l03-csv/guess_game/](../project/examples/m08-files/l03-csv/guess_game/).
**Arbeitsdatei:** `playground/inventory_report.py` (neu)
**Starter:** keiner, leere Datei
**Daten:** [project/data/inventory.csv](../project/data/inventory.csv) (Excel-Export: `;`, Dezimalkomma, UTF-8 mit BOM)

## Ausgangslage

Ein Lager exportiert seinen Bestand aus Excel als CSV. Ein Programm fasst pro Kategorie die Anzahl der Produkte und den Lagerwert (Preis × Bestand) zusammen, listet Produkte mit weniger als 10 Stück zum Nachbestellen und speichert den Bericht als JSON, damit ein anderes Programm ihn weiterverarbeiten kann.

Gewünschte Ausgabe:

```text
CSV-Datei (Enter = data/inventory.csv):
Elektronik · Produkte: 3 · Lagerwert: 90859.76
Zubehör · Produkte: 2 · Lagerwert: 13528.33
Möbel · Produkte: 3 · Lagerwert: 12423.45
Nachbestellen: ['Gaming-Maus', 'Bürostuhl Ergo']
Bericht gespeichert in playground/inventory_report.json
```

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `project/` (aus `playground/` mit `cd ..` zurück). Start mit `python playground/inventory_report.py`.
- Neue Datei `playground/inventory_report.py` anlegen.

## Aufgaben

1. Schreibe `to_number(text)` (wandelt `"1299,99"` in `1299.99` um) und `load_inventory(path)` (liest die CSV mit `csv.DictReader`, `delimiter=";"`, `encoding="utf-8-sig"`, `newline=""` und gibt alle Zeilen als Liste zurück). Teste mit `print(len(...))` und der ersten Zeile.
2. Schreibe `summarize(products)`: ein Dictionary Kategorie → `{"Produkte": n, "Lagerwert": summe}`. Der Lagerwert eines Produkts ist Preis × Lagerbestand; runde die Summe auf zwei Stellen.
3. Schreibe `low_stock(products, limit=10)`: gibt die Namen aller Produkte mit einem Bestand unter `limit` als Liste zurück.
4. Schreibe `save_report(report)` (JSON mit `indent=2` und `ensure_ascii=False` nach `playground/inventory_report.json`) und `main()`: Bericht `{"Kategorien": …, "Nachbestellen": …}` bauen, wie oben ausgeben, speichern. Starte `main()` unter `if __name__ == "__main__":`.
5. Mache das Programm robust: `main()` fragt nach dem Dateinamen (Enter = `data/inventory.csv`) und meldet eine fehlende Datei ohne Absturz. Kopiere `data/inventory.csv` nach `playground/inventory_test.csv`, ersetze dort den Preis der Gaming-Maus durch `unbekannt` und sorge dafür, dass `summarize` diese Zeile mit `Zeile übersprungen: Gaming-Maus` auslässt.

## Checkpoint

- Ohne Eingabe erscheint die gewünschte Ausgabe; `playground/inventory_report.json` ist eingerückt und zeigt Umlaute.
- Eingabe `data/lager.csv` ergibt `Datei data/lager.csv nicht gefunden.` und kein Traceback.
- Mit `playground/inventory_test.csv` meldet das Programm die übersprungene Zeile, Zubehör zählt nur noch 1 Produkt.

## Abschlusskriterien

- Das Programm besteht aus Funktionen mit je einer Aufgabe, liest CSV mit `csv.DictReader` und schreibt JSON mit `json.dump`.
- `FileNotFoundError` und `ValueError` werden gezielt abgefangen.

## Erweiterung

Zerlege das Programm in ein kleines Paket wie das Spiel: `playground/inventory/` mit `storage.py` (Lesen und Schreiben), `report.py` (`summarize`, `low_stock`) und `__main__.py` (`main`). Start im Ordner `playground/` mit `python -m inventory`; der Pfad zu den Daten lautet dann `Path("..") / "data" / "inventory.csv"`.
