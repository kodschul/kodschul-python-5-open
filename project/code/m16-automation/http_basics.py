# HTTP-Grundlagen mit requests: Anfrage senden, Antwort lesen, Fehler abfangen
# Start im Ordner project/: python code/m16-automation/http_basics.py

import os

import requests

# Adresse der API aus einer Umgebungsvariable, sonst die öffentliche Test-API
BASE_URL = os.environ.get("API_BASE_URL", "https://jsonplaceholder.typicode.com")

# 1. GET: einen Post abrufen
response = requests.get(f"{BASE_URL}/posts/1", timeout=5)  # höchstens 5 s warten
print("Statuscode:", response.status_code)  # 200 = OK
print("Inhaltstyp:", response.headers["Content-Type"])  # ein Antwort-Header
post = response.json()  # JSON-Text -> Dictionary
print("Titel:", post["title"])

# 2. Parameter: requests hängt ?postId=1 an die Adresse an
response = requests.get(f"{BASE_URL}/comments", params={"postId": 1}, timeout=5)
print("Adresse:", response.url)
print("Kommentare zu Post 1:", len(response.json()))

# 3. POST: Daten an den Server schicken (die Test-API speichert nichts)
new_post = {"title": "Lerngruppe", "body": "Treffen Montag 18 Uhr", "userId": 1}
response = requests.post(f"{BASE_URL}/posts", json=new_post, timeout=5)
print("POST-Statuscode:", response.status_code, "· neue id:", response.json()["id"])

# 4. Fehler: Post 999 gibt es nicht -> Statuscode 404
try:
    response = requests.get(f"{BASE_URL}/posts/999", timeout=5)
    response.raise_for_status()  # 4xx oder 5xx -> requests.HTTPError
except requests.RequestException as error:  # auch: kein Netz, Zeitüberschreitung
    print("Fehler:", error)
