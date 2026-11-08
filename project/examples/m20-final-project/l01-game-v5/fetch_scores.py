# Bestenliste über HTTP laden statt aus der Datei
# Vorher im selben Ordner in einem zweiten Terminal: python -m http.server 8000 --bind 127.0.0.1
# Start: python fetch_scores.py

import sys

import requests

URL = "http://localhost:8000/highscores.json"  # anderer Rechner: nur die Adresse ändern


def main():
    """Lädt die Bestenliste vom Server und zeigt die Top 3."""
    try:
        response = requests.get(URL, timeout=5)  # höchstens 5 Sekunden warten
        response.raise_for_status()  # Statuscode 404, 500 ... -> Fehler
    except requests.RequestException as error:  # kein Server, Zeitüberschreitung ...
        print(f"Bestenliste nicht erreichbar: {error}")
        sys.exit(1)
    scores = response.json()  # JSON-Text -> Liste von Dictionaries
    best = sorted(scores, key=lambda item: item["tries"])[:3]
    print(f"Top 3 von {URL} ({len(scores)} Einträge)")
    place = 1
    for item in best:
        print(f"{place}. {item['name']} · Versuche: {item['tries']} · {item['level']}")
        place += 1


if __name__ == "__main__":
    main()
