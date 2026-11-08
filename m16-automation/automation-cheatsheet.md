# Cheatsheet Modul 16: Remote-Zugriff und Automatisierung

## HTTP-Anfragen mit requests (Lab 16.1)

| Befehl | Wirkung |
| --- | --- |
| `import requests` | Paket laden (steht in `requirements.txt`) |
| `requests.get(url, timeout=5)` | Daten holen, höchstens 5 Sekunden warten |
| `requests.get(url, params={"postId": 1}, timeout=5)` | hängt `?postId=1` an die Adresse an |
| `requests.get(url, headers={"Authorization": f"Bearer {key}"}, timeout=5)` | eigenen Header mitschicken, z. B. API-Schlüssel |
| `requests.post(url, json=daten, timeout=5)` | Dictionary als JSON an den Server schicken |
| `response.status_code` | Statuscode als Zahl, z. B. `200` |
| `response.raise_for_status()` | Statuscode `4xx`/`5xx` → `requests.HTTPError` |
| `response.json()` | JSON-Inhalt → Liste/Dictionary |
| `response.text` | Inhalt als Text, z. B. `"20\n"` |
| `response.headers["Content-Type"]` | ein Header der Antwort |
| `response.url` | tatsächlich abgerufene Adresse inklusive Parameter |

## Fehler im Netz abfangen

| Befehl | Wirkung |
| --- | --- |
| `except requests.RequestException as error:` | fängt alle Netzfehler auf einmal |
| `requests.ConnectionError` | kein Netz, Server aus, Adresse unbekannt |
| `requests.Timeout` | keine Antwort innerhalb von `timeout` |
| `requests.HTTPError` | von `raise_for_status()` bei `4xx`/`5xx` |
| `type(error).__name__` | Name der Fehlerklasse als Text, z. B. `"ConnectionError"` |
| im `except`: `json.load(file)` | Ersatzdaten aus lokaler Kopie lesen (Fallback) |

## Statuscodes

| Code | Bedeutung |
| --- | --- |
| `200` / `201` | OK / angelegt |
| `400` | Anfrage fehlerhaft |
| `401` / `403` | nicht angemeldet / keine Berechtigung |
| `404` | Adresse gibt es nicht |
| `429` | zu viele Anfragen, warten |
| `500` / `503` | Fehler / Überlastung beim Server |

## Umgebungsvariablen

| Befehl | Wirkung |
| --- | --- |
| `os.environ.get("API_BASE_URL", "https://…")` | Wert lesen, sonst Standardwert |
| `os.environ.get("API_KEY")` | Wert lesen, sonst `None` |
| `$env:API_BASE_URL = "http://localhost:9"` | setzen in PowerShell (nur dieses Terminal) |
| `export API_BASE_URL=http://localhost:9` | setzen in bash/zsh (nur dieses Terminal) |
| `Remove-Item Env:API_BASE_URL` / `unset API_BASE_URL` | wieder entfernen |

## Lokaler Server (Lab 16.2)

| Befehl | Wirkung |
| --- | --- |
| `python -m http.server 8000 --bind 127.0.0.1` | aktuellen Ordner auf Port 8000 freigeben, nur für den eigenen Rechner |
| `... --directory data` | anderen Ordner freigeben |
| `http://localhost:8000/` | Verzeichnisliste im Browser |
| `http://localhost:8000/highscores.json` | eine Datei über HTTP abrufen |
| `Strg+C` im Server-Terminal | Server beenden |
| zweites Terminal: **Terminal → New Terminal** | Client starten, während der Server läuft |
| `ssh name@server.example.org` | Terminal auf einem fernen Rechner (nur Einordnung) |

## Admin-Skript (Lab 16.3)

| Befehl | Wirkung |
| --- | --- |
| `parser.add_argument("folder", type=Path)` | Positionsargument, gleich als `Path` |
| `parser.add_argument("--since", type=date.fromisoformat)` | Datum `JJJJ-MM-TT`, sonst Exit-Code 2 |
| `args.folder.is_dir()` | prüft, ob der Ordner existiert |
| `sorted(args.folder.glob("game*.log"))` | passende Dateien des Ordners, sortiert |
| `date.fromisoformat("2026-11-01") < since` | Daten vergleichen |
| `Counter(liste).most_common(3)` | die drei häufigsten Werte als `(Wert, Anzahl)` |
| `logging.basicConfig(filename="log_report.log", ...)` | eigenes Protokoll des Skripts |
| `sys.exit(1)` | Ende mit Fehlercode |

## Exit-Codes

| Code / Befehl | Bedeutung |
| --- | --- |
| `0` | Erfolg (Skriptende ohne `sys.exit`) |
| `1` | Problem bei der Arbeit (`sys.exit(1)`) |
| `2` | falscher Aufruf (argparse) |
| `$LASTEXITCODE` | letzten Exit-Code anzeigen (PowerShell) |
| `echo $?` | letzten Exit-Code anzeigen (bash/zsh) |
| `crontab -e` / Aufgabenplanung (`schtasks /create`) | Skript zeitgesteuert starten (Linux/macOS / Windows) |
