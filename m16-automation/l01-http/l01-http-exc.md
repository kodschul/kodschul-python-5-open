# Lab 16.1 – Übung: Posts laden und zählen

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Nein — eigenständiges Skript; das Spiel bleibt auf dem Stand von Lab 15.3. Lab 16.2 nutzt dieselben `requests`-Bausteine für die Bestenliste.
**Arbeitsdatei:** `playground/posts_by_user.py` (neu)
**Starter:** keiner, leere Datei

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `project/`. Start jeweils mit `python playground/posts_by_user.py`.
- Test-API im Browser prüfen: `https://jsonplaceholder.typicode.com/posts` zeigt eine lange JSON-Liste. Ohne Internet funktioniert die Übung trotzdem ab Aufgabe 3 mit der Kopie `data/posts.json`.

## Aufgaben

1. Lege `playground/posts_by_user.py` an. Lies die Adresse mit `os.environ.get("API_BASE_URL", "https://jsonplaceholder.typicode.com")`, lade `/posts` mit `requests.get(..., timeout=5)`, rufe `raise_for_status()` auf und gib die Anzahl als `100 Posts geladen` aus.
2. Zähle mit einem Dictionary, wie viele Posts jeder Benutzer (`"userId"`) geschrieben hat, und gib sie sortiert als `Benutzer 1: 10 Posts` aus.
3. Verschiebe das Laden in eine Funktion `load_posts()`. Fange darin `requests.RequestException` ab: Dann meldet das Skript `API nicht erreichbar, nutze data/posts.json` und liest stattdessen die Datei `data/posts.json` mit `json.load`.
4. Teste den Fallback: Setze im Terminal `API_BASE_URL` auf `http://localhost:9` (PowerShell: `$env:API_BASE_URL = "http://localhost:9"`, macOS/Linux: `export API_BASE_URL=http://localhost:9`), starte das Skript und entferne die Variable danach wieder (`Remove-Item Env:API_BASE_URL` bzw. `unset API_BASE_URL`).
5. Teste einen 404: Setze `API_BASE_URL` auf `https://jsonplaceholder.typicode.com/nichtda`, starte, beobachte die Meldung und entferne die Variable wieder.

## Checkpoint

- Mit Netz: `100 Posts geladen`, danach zehn Zeilen `Benutzer 1: 10 Posts` bis `Benutzer 10: 10 Posts`.
- Mit `http://localhost:9`: Meldung zum Fallback, danach dieselbe Auswertung aus `data/posts.json`, kein Traceback.
- Mit `/nichtda`: ebenfalls Fallback; ohne `raise_for_status()` käme stattdessen ein Fehler beim Auswerten.

## Abschlusskriterien

- `playground/posts_by_user.py` enthält `timeout=`, `raise_for_status()`, `except requests.RequestException` und liest die Adresse aus `API_BASE_URL`.
- Das Skript liefert online und offline dieselbe Auswertung.

## Erweiterung

Schreibe `playground/number_of_the_day.py` mit einer Funktion `number_of_the_day(low=1, high=100)`. Die Funktion holt eine Zahl von `https://www.random.org/integers/` mit den Parametern `num=1`, `min`, `max`, `col=1`, `base=10`, `format="plain"` und `rnd=f"date.{date.today()}"` (Lab 6.3). Die Antwort ist Text, also `int(response.text)`. Ohne Netz liefert `random.Random(date.today().toordinal()).randint(low, high)` eine Ersatzzahl: `toordinal()` macht aus dem Datum eine Tagesnummer, `random.Random(...)` ist ein Zufallsgenerator mit diesem festen Startwert; die Zahl bleibt so den ganzen Tag gleich. Ausgabe z. B. `Zahl des Tages: 20`. Höchstens eine Anfrage pro Start, damit random.org nicht unnötig belastet wird.

## Fallback

Ohne Internet: `load_posts()` mit `try`/`except` aus Aufgabe 3 gleich zu Beginn schreiben, danach Aufgabe 2. Die Auswertung kommt dann vollständig aus `data/posts.json`; Aufgabe 5 entfällt. Einschränkung: Ein echter Statuscode `200` ist so nicht zu sehen (Bild in der Theorie).
