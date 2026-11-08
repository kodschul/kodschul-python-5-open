# Eine JSON-Datei vom eigenen lokalen Server laden
# Vorher in einem zweiten Terminal im Ordner project/:
#   python -m http.server 8000 --bind 127.0.0.1 --directory data
# Start im Ordner project/: python code/m16-automation/fetch_persons.py

import requests

URL = "http://localhost:8000/persons.json"  # localhost = dieser Rechner, Port 8000

try:
    response = requests.get(URL, timeout=5)
    response.raise_for_status()
except requests.RequestException as error:  # Server nicht gestartet?
    print(f"Server nicht erreichbar: {error}")
else:  # nur ohne Fehler: Daten auswerten
    persons = response.json()
    print(f"{len(persons)} Personen von {URL}")
    for person in persons:
        print(f"- {person['name']}, {person['age']} Jahre")
