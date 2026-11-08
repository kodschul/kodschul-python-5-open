# Posts einer Test-API laden und pro Benutzer zählen
# Ohne Netz liest das Skript die Kopie data/posts.json.
# Start im Ordner project/: python code/m16-automation/posts_by_user.py

import json
import os
from pathlib import Path

import requests

BASE_URL = os.environ.get("API_BASE_URL", "https://jsonplaceholder.typicode.com")
LOCAL_COPY = Path("data") / "posts.json"  # Ersatz, wenn die API nicht antwortet


def load_posts():
    """Holt die Posts von der API; bei Netzproblemen aus der lokalen Datei."""
    try:
        response = requests.get(f"{BASE_URL}/posts", timeout=5)
        response.raise_for_status()  # 404, 500 ... -> Fehler
        print(f"Quelle: {BASE_URL}/posts")
        return response.json()  # JSON-Text -> Liste von Dictionaries
    except requests.RequestException as error:  # offline, Zeitüberschreitung ...
        print(f"API nicht erreichbar ({type(error).__name__}), nutze {LOCAL_COPY}")
        with open(LOCAL_COPY, encoding="utf-8") as file:
            return json.load(file)


posts = load_posts()
print(f"{len(posts)} Posts geladen")

counts = {}  # Benutzer-ID -> Anzahl Posts
for post in posts:
    user_id = post["userId"]
    counts[user_id] = counts.get(user_id, 0) + 1

for user_id in sorted(counts):
    print(f"Benutzer {user_id}: {counts[user_id]} Posts")
