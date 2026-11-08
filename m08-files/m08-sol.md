# Modul 8 – Lösung Transferübung: Lagerbericht aus Excel-CSV

Vollständige Datei `playground/inventory_report.py` am Ende von Aufgabe 5.

## Aufgabe 1: to_number() und load_inventory()

```python
import csv
import json
from pathlib import Path

DEFAULT_FILE = Path("data") / "inventory.csv"
REPORT_FILE = Path("playground") / "inventory_report.json"


def to_number(text):
    """Wandelt deutschen Zahlentext wie "1299,99" in eine Kommazahl um."""
    return float(text.replace(",", "."))


def load_inventory(path):
    """Liest die CSV-Datei und gibt alle Zeilen als Liste von Dictionaries zurück."""
    with open(path, encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file, delimiter=";"))
```

Test (vorübergehend unten in der Datei):

```python
products = load_inventory(DEFAULT_FILE)
print(len(products))
print(products[0])
```

```text
8
{'Produkt': 'Laptop Pro 15', 'Kategorie': 'Elektronik', 'Preis': '1299,99', 'Lagerbestand': '24'}
```

## Aufgabe 2: summarize()

```python
def summarize(products):
    """Zählt Produkte und Lagerwert pro Kategorie; überspringt kaputte Zeilen."""
    summary = {}
    for product in products:
        try:
            value = to_number(product["Preis"]) * int(product["Lagerbestand"])
        except ValueError:
            print(f"Zeile übersprungen: {product['Produkt']}")
            continue
        category = product["Kategorie"]
        if category not in summary:
            summary[category] = {"Produkte": 0, "Lagerwert": 0}
        summary[category]["Produkte"] += 1
        summary[category]["Lagerwert"] = round(
            summary[category]["Lagerwert"] + value, 2
        )
    return summary
```

Ein verschachteltes Dictionary (Lab 4.3): außen die Kategorie, innen die beiden Kennzahlen. Das `try`/`except` gehört zu Aufgabe 5; ohne es ist der Rest identisch.

## Aufgabe 3: low_stock()

```python
def low_stock(products, limit=10):
    """Gibt die Namen aller Produkte mit weniger als limit Stück zurück."""
    names = []
    for product in products:
        if int(product["Lagerbestand"]) < limit:
            names.append(product["Produkt"])
    return names
```

`limit=10` ist ein Standardwert (Lab 5.2): `low_stock(products, limit=30)` findet mehr Produkte.

## Aufgabe 4: save_report() und main()

```python
def save_report(report):
    """Speichert den Bericht als eingerücktes JSON."""
    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2, ensure_ascii=False)
```

`playground/inventory_report.json`:

```json
{
  "Kategorien": {
    "Elektronik": {
      "Produkte": 3,
      "Lagerwert": 90859.76
    },
    "Zubehör": {
      "Produkte": 2,
      "Lagerwert": 13528.33
    },
    "Möbel": {
      "Produkte": 3,
      "Lagerwert": 12423.45
    }
  },
  "Nachbestellen": [
    "Gaming-Maus",
    "Bürostuhl Ergo"
  ]
}
```

CSV rein, JSON raus: Die Eingabe ist eine flache Tabelle für Excel, der Bericht ist verschachtelt und behält die Zahlen als Zahlen.

## Aufgabe 5: robust machen

`main()` mit Dateiabfrage und `FileNotFoundError`; `return` beendet `main()` vorzeitig (Lab 5.1). Vollständige Datei:

```python
# Lagerbericht: CSV aus Excel lesen, auswerten, Zusammenfassung als JSON speichern

import csv
import json
from pathlib import Path

DEFAULT_FILE = Path("data") / "inventory.csv"
REPORT_FILE = Path("playground") / "inventory_report.json"


def to_number(text):
    """Wandelt deutschen Zahlentext wie "1299,99" in eine Kommazahl um."""
    return float(text.replace(",", "."))


def load_inventory(path):
    """Liest die CSV-Datei und gibt alle Zeilen als Liste von Dictionaries zurück."""
    with open(path, encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file, delimiter=";"))


def summarize(products):
    """Zählt Produkte und Lagerwert pro Kategorie; überspringt kaputte Zeilen."""
    summary = {}
    for product in products:
        try:
            value = to_number(product["Preis"]) * int(product["Lagerbestand"])
        except ValueError:
            print(f"Zeile übersprungen: {product['Produkt']}")
            continue
        category = product["Kategorie"]
        if category not in summary:
            summary[category] = {"Produkte": 0, "Lagerwert": 0}
        summary[category]["Produkte"] += 1
        summary[category]["Lagerwert"] = round(
            summary[category]["Lagerwert"] + value, 2
        )
    return summary


def low_stock(products, limit=10):
    """Gibt die Namen aller Produkte mit weniger als limit Stück zurück."""
    names = []
    for product in products:
        if int(product["Lagerbestand"]) < limit:
            names.append(product["Produkt"])
    return names


def save_report(report):
    """Speichert den Bericht als eingerücktes JSON."""
    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2, ensure_ascii=False)


def main():
    """Datei abfragen, auswerten, Bericht ausgeben und speichern."""
    text = input(f"CSV-Datei (Enter = {DEFAULT_FILE}): ").strip()
    path = Path(text) if text != "" else DEFAULT_FILE
    try:
        products = load_inventory(path)
    except FileNotFoundError:
        print(f"Datei {path} nicht gefunden.")
        return
    report = {"Kategorien": summarize(products), "Nachbestellen": low_stock(products)}
    for category, data in report["Kategorien"].items():
        count = data["Produkte"]
        print(f"{category} · Produkte: {count} · Lagerwert: {data['Lagerwert']}")
    print("Nachbestellen:", report["Nachbestellen"])
    save_report(report)
    print("Bericht gespeichert in", REPORT_FILE)


if __name__ == "__main__":
    main()
```

Drei Testläufe (auf Windows erscheinen Pfade mit `\`, z. B. `data\inventory.csv`):

```text
$ python playground/inventory_report.py
CSV-Datei (Enter = data/inventory.csv):
Elektronik · Produkte: 3 · Lagerwert: 90859.76
Zubehör · Produkte: 2 · Lagerwert: 13528.33
Möbel · Produkte: 3 · Lagerwert: 12423.45
Nachbestellen: ['Gaming-Maus', 'Bürostuhl Ergo']
Bericht gespeichert in playground/inventory_report.json

$ python playground/inventory_report.py
CSV-Datei (Enter = data/inventory.csv): data/lager.csv
Datei data/lager.csv nicht gefunden.

$ python playground/inventory_report.py
CSV-Datei (Enter = data/inventory.csv): playground/inventory_test.csv
Zeile übersprungen: Gaming-Maus
Elektronik · Produkte: 3 · Lagerwert: 90859.76
Zubehör · Produkte: 1 · Lagerwert: 13049.13
Möbel · Produkte: 3 · Lagerwert: 12423.45
Nachbestellen: ['Gaming-Maus', 'Bürostuhl Ergo']
Bericht gespeichert in playground/inventory_report.json
```

Die Gaming-Maus fehlt in der Summe, steht aber weiter auf der Nachbestellliste: Der Bestand (8) ist gültig, nur der Preis nicht.

## Erweiterung

Ordner `playground/inventory/`, Start im Ordner `playground/` mit `python -m inventory`.

`__init__.py`:

```python
"""Lagerbericht als Paket: python -m inventory."""
```

`storage.py`:

```python
# Lesen und Schreiben: CSV rein, JSON raus

import csv
import json
from pathlib import Path

DEFAULT_FILE = Path("..") / "data" / "inventory.csv"  # von playground/ aus
REPORT_FILE = Path("inventory_report.json")


def load_inventory(path):
    """Liest die CSV-Datei und gibt alle Zeilen als Liste von Dictionaries zurück."""
    with open(path, encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file, delimiter=";"))


def save_report(report):
    """Speichert den Bericht als eingerücktes JSON."""
    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2, ensure_ascii=False)
```

`report.py`: die Funktionen `to_number`, `summarize` und `low_stock` unverändert aus Aufgabe 5, darüber die Kopfzeile `# Auswertung: Kategorien zusammenfassen, Nachbestellungen finden`.

`__main__.py`:

```python
# Startpunkt: python -m inventory führt diese Datei aus

from pathlib import Path

from inventory import report, storage


def main():
    """Datei abfragen, auswerten, Bericht ausgeben und speichern."""
    text = input(f"CSV-Datei (Enter = {storage.DEFAULT_FILE}): ").strip()
    path = Path(text) if text != "" else storage.DEFAULT_FILE
    try:
        products = storage.load_inventory(path)
    except FileNotFoundError:
        print(f"Datei {path} nicht gefunden.")
        return
    result = {
        "Kategorien": report.summarize(products),
        "Nachbestellen": report.low_stock(products),
    }
    for category, data in result["Kategorien"].items():
        count = data["Produkte"]
        print(f"{category} · Produkte: {count} · Lagerwert: {data['Lagerwert']}")
    print("Nachbestellen:", result["Nachbestellen"])
    storage.save_report(result)
    print("Bericht gespeichert in", storage.REPORT_FILE)


if __name__ == "__main__":
    main()
```

Das Dictionary heißt hier `result`, weil `report` schon der Name des Moduls ist. Der Bericht landet als `playground/inventory_report.json`, weil das Terminal in `playground/` steht.
