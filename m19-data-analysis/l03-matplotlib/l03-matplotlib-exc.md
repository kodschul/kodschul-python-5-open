# Lab 19.3 – Übung: Statistikseite mit Diagrammen

**Dauer:** ca. 18 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — neues Modul `guess_game/charts.py`; `export.py`, `ui.py` und `__main__.py` binden die Diagramme in `--export html` ein. Das ist der Stand für Lab 20.1 (Spiel v5).
**Arbeitsdatei:** `playground/guess_game/charts.py` (neu), dazu `export.py`, `ui.py`, `__main__.py`
**Starter:** keiner; `charts.py` entsteht neu, Ausgangspunkt ist der Spielstand nach Lab 19.2

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/`.
- Ohne eigenen Spielstand: Ordner `playground/guess_game/` löschen oder umbenennen und `examples/m19-data-analysis/l02-pandas/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren.
- `game.db` enthält gewonnene Runden auf mindestens zwei Stufen (wie in Lab 19.2).

## Aufgaben

1. Lege `guess_game/charts.py` an: Imports (`sqlite3`, `Path`, `matplotlib.pyplot as plt`, `pandas as pd`, `MaxNLocator` aus `matplotlib.ticker`, `storage` aus `guess_game`), direkt danach `plt.switch_backend("Agg")`, die Konstanten `TRIES_CHART = Path("chart_tries.png")`, `WIN_RATE_CHART = Path("chart_win_rate.png")`, zwei Titel und das Dictionary `COLORS` mit einer Farbe pro Stufe. Übernimm `load_rounds` aus `analyze.py` mit `path=storage.DB_FILE`.
2. Schreibe `save_win_rate_chart(rounds, path=WIN_RATE_CHART)`: Gewinnquote pro Stufe in Prozent als Balken, Wert über jedem Balken (`bar_label` mit `fmt="%.0f %%"`), Titel, Achsenbeschriftungen, y-Achse von 0 bis 110; speichern, schließen, `path` zurückgeben.
3. Schreibe `save_tries_chart(rounds, path=TRIES_CHART)`: nur gewonnene Runden, eine Datenreihe `tries` pro Stufe (Stufen sortiert), Histogramm mit einem Balken pro Versuchszahl (`bins=range(1, rounds["tries"].max() + 2)`, `align="left"`), Farben aus `COLORS` (unbekannte Stufe grau), Legende „Stufe“, nur ganze Zahlen auf der y-Achse.
4. Schreibe `save_charts(rounds)`: Ohne gewonnene Runde gibt es `[]` zurück, sonst `[(Datei, Titel), (Datei, Titel)]` für beide Diagramme. Ergänze am Ende `if __name__ == "__main__":`, das beide speichert und je eine Zeile `Diagramm gespeichert: chart_tries.png (Versuche bis zum Gewinn)` ausgibt. Starte `python -m guess_game.charts` und öffne beide PNG-Dateien in VS Code.
5. Binde die Diagramme in den HTML-Export ein: `export_html(scores, charts=None, path=HTML_FILE)` hängt bei Diagrammen `<h2>Statistik</h2>` und je ein `<p><img src="…" alt="…"></p>` an; `run_export` in `__main__.py` ruft für HTML `charts.save_charts(charts.load_rounds())` auf und gibt die Liste weiter; `ui.show_export(path, count, images)` meldet jedes Diagramm. Starte `python -m guess_game --export html` und öffne `highscores.html` im Browser.

## Checkpoint

- `python -m guess_game.charts` meldet zwei gespeicherte Diagramme; beide PNG-Dateien liegen in `playground/` und sind 700 × 400 Pixel groß.
- Die Balken der Gewinnquote stimmen mit „Gewinnquote %“ aus `analyze.py` überein.
- `--export html` meldet `Bestenliste exportiert: highscores.html (n Einträge)` und zwei Zeilen `Diagramm: …`; die Seite zeigt unter der Tabelle „Statistik“ mit beiden Bildern.
- `--export excel` läuft unverändert, ohne Diagramme.

## Abschlusskriterien

- `highscores.html` zeigt Bestenliste und zwei Diagramme; ohne gewonnene Runde entsteht die Seite ohne Statistik-Abschnitt.

## Erweiterung

Schreibe `playground/growth.py`: Lies [data/population.csv](../../project/data/population.csv) (aus `playground/` gesehen: `../data/population.csv`), berechne pro Stadtteil den Zuwachs 2015 → 2025 als neue Spalte und speichere ihn als sortiertes Balkendiagramm `growth.png` mit einem Titel, der die Aussage nennt.
