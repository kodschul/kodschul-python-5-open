# Lab 15.1: Umgebungsvariablen lesen – Einstellungen und Geheimnisse außerhalb des Codes
import os

# os.environ verhält sich wie ein Dictionary: Name -> Text
print(f"Anzahl Umgebungsvariablen: {len(os.environ)}")

# os.getenv(name, standard): fehlt die Variable, kommt der Standardwert zurück
mode = os.getenv("APP_MODE", "normal")
print(f"APP_MODE: {mode}")

# Geheimnisse (Passwörter, API-Schlüssel) nie ausgeben, nur prüfen, ob sie da sind
token = os.getenv("DEMO_TOKEN")  # None, wenn nicht gesetzt
if token is None:
    print("DEMO_TOKEN ist nicht gesetzt.")
else:
    print(f"DEMO_TOKEN ist gesetzt ({len(token)} Zeichen).")
