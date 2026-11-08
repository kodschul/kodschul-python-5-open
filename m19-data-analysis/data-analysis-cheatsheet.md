# Cheatsheet Modul 19: Datenanalyse

## Mehrzeilige Texte mit Regex (Lab 19.1)

| Befehl | Wirkung |
| --- | --- |
| `Path("datei.txt").read_text(encoding="utf-8")` | ganze Datei als ein String |
| `re.MULTILINE` | `^` und `$` gelten für jede Zeile |
| `re.DOTALL` | `.` passt auch auf `\n` |
| `re.VERBOSE` | Muster über mehrere Zeilen, Kommentare mit `#`, Leerzeichen als `\ ` |
| `re.MULTILINE \| re.VERBOSE` | mehrere Flags verbinden |
| `.*` / `.*?` | so viel wie möglich (gierig) / so wenig wie möglich |
| `(?:...)` | Klammer ohne Gruppe, z. B. für `(?:...)*?` oder `(?:...)?` |
| `(?:\nTelefon: (?P<phone>.+))?` | ganze Zeile optional; fehlt sie, ist die Gruppe `None` |
| `(?:.*\ DEBUG\ .*\n)*?` | nur bestimmte Zeilen zwischen Anfang und Ende erlauben |
| `(?:\n\n\|\Z)` | Ende = Leerzeile oder Textende |
| `for match in PATTERN.finditer(text):` | ein Treffer pro Block |
| `match.groupdict()` | alle benannten Gruppen als Dictionary |
| `record.pop("body")` | Wert holen und Eintrag entfernen |
| `" ".join(["50", "75"])` | `"50 75"` |

## NumPy (Lab 19.2)

| Befehl | Wirkung |
| --- | --- |
| `import numpy as np` | Paket laden (steht in `requirements.txt`) |
| `np.array([1.99, 0.89])` | Array aus einer Liste |
| `np.arange(1_000_000)` | Array `0 … 999999`, wie `range` |
| `array * 1.19`, `array + other` | Rechnung für jeden Wert (Vektorrechnung) |
| `array.sum()`, `array.mean()`, `array.max()` | Summe, Mittelwert, Maximum |
| `np.median(array)` | Median |
| `array.dtype` | Typ aller Werte, z. B. `float64` |

## pandas: laden (Lab 19.2)

| Befehl | Wirkung |
| --- | --- |
| `import pandas as pd` | Paket laden |
| `pd.DataFrame(liste_von_dicts)` | Tabelle aus Dictionaries |
| `pd.read_csv("datei.csv")` | CSV mit Komma |
| `pd.read_csv("history.csv", sep=";", decimal=",", encoding="utf-8-sig")` | CSV des Spiels |
| `pd.read_excel("datei.xlsx")` | Excel-Datei (braucht `openpyxl`) |
| `pd.read_sql("SELECT * FROM rounds", connection)` | SQL-Ergebnis als DataFrame |
| `sqlite3.connect(":memory:")` | Datenbank nur im Arbeitsspeicher |

## pandas: ansehen, wählen, filtern

| Befehl | Wirkung |
| --- | --- |
| `print(df)`, `df.head()` | ganze Tabelle / erste fünf Zeilen |
| `len(df)`, `df.shape` | Zeilenzahl / `(Zeilen, Spalten)` |
| `df.columns`, `df.dtypes` | Spaltennamen / Typ jeder Spalte |
| `df["tries"]` | eine Spalte (Series) |
| `df["total"] = df["qty"] * df["price"]` | neue Spalte aus einer Rechnung |
| `df[df["price"] > 1]` | nur Zeilen, für die die Bedingung gilt |
| `df[(df["a"] == "x") & (df["b"] > 5)]` | zwei Bedingungen: `&` und, `\|` oder, jede in Klammern |
| `df["level"].unique()` | jeder Wert einmal |
| `df.sort_values("total", ascending=False)` | sortieren, größter Wert zuerst |
| `df["tries"].describe()` | Anzahl, Mittelwert, Streuung, Min, Quartile, Max |
| `df.index[0]` | Beschriftung der ersten Zeile |

## pandas: gruppieren und zusammenfassen

| Befehl | Wirkung |
| --- | --- |
| `df.groupby("Region")["Umsatz"].sum()` | Summe pro Gruppe |
| `.count()`, `.mean()`, `.median()`, `.max()`, `.min()` | weitere Kennzahlen pro Gruppe |
| `.agg(["count", "sum", "mean", "median"])` | mehrere Kennzahlen auf einmal |
| `groups["won"].mean() * 100` | Gewinnquote in Prozent (`won` ist 1 oder 0) |
| `.round()`, `.round(1)` | runden auf ganze Zahl / eine Nachkommastelle |
| `pd.DataFrame({"Spiele": s1, "Quote": s2})` | Series zu einer Tabelle zusammensetzen |
| `df.to_excel("datei.xlsx")` | DataFrame als Excel-Datei speichern |

## SQL oder pandas

| Aufgabe | Werkzeug |
| --- | --- |
| auswählen, filtern, begrenzen in der Datenbank | SQL (`WHERE`, `ORDER BY`, `LIMIT`) |
| Anzahl, Summe, Durchschnitt pro Gruppe | beides: `GROUP BY` / `groupby` |
| Median, Quartile, `describe` | pandas |
| CSV, Excel und Datenbank kombinieren | pandas |
| Diagramm | pandas + Matplotlib |

## Diagramme mit Matplotlib (Lab 19.3)

| Befehl | Wirkung |
| --- | --- |
| `import matplotlib.pyplot as plt` | Paket laden |
| `plt.switch_backend("Agg")` | nur Dateien, kein Fenster |
| `fig, ax = plt.subplots(figsize=(7, 4))` | Figure (Bild) und Axes (Diagramm), Größe in Zoll |
| `fig, (ax1, ax2) = plt.subplots(1, 2)` | zwei Diagramme nebeneinander |
| `ax.plot(x, y, marker="o")` | Liniendiagramm |
| `ax.bar(kategorien, werte, color="#2a78d6")` | Balkendiagramm |
| `ax.barh(kategorien, werte)` | waagrechte Balken |
| `ax.hist(werte, bins=range(1, 9), align="left")` | Histogramm, ein Balken pro ganzer Zahl |
| `ax.hist([reihe1, reihe2], label=["a", "b"])` | mehrere Reihen nebeneinander |
| `ax.bar_label(bars)`, `fmt="%.0f %%"` | Wert über jedem Balken, z. B. `75 %` |
| `ax.set_title(...)`, `ax.set_xlabel(...)`, `ax.set_ylabel(...)` | Titel und Achsen |
| `ax.set_ylim(0, 110)` | Bereich der y-Achse |
| `ax.legend(title="Stufe")` | Legende |
| `ax.tick_params(axis="x", labelrotation=30)` | Beschriftung drehen |
| `ax.yaxis.set_major_locator(MaxNLocator(integer=True))` | nur ganze Zahlen auf der y-Achse |
| `ax.axhline(0, color="gray")` | waagrechte Linie, z. B. Nulllinie |
| `fig.tight_layout()` | Abstände automatisch |
| `fig.savefig("bild.png", dpi=100)` | speichern (7 × 4 Zoll × 100 dpi = 700 × 400 Pixel) |
| `plt.close(fig)` | Speicher freigeben |
| `df.plot(x="Spalte", y=["a", "b"], kind="bar", rot=30)` | Abkürzung über pandas; Ergebnis ist ein Axes |

## Im Spiel (Spiel v5)

| Befehl | Wirkung |
| --- | --- |
| `python import_log.py` | Runden aus `game.log` in Tabelle `log_rounds` |
| `python analyze.py` | Auswertung pro Stufe und Spieler mit pandas |
| `python -m guess_game.charts` | nur die zwei Diagramme als PNG |
| `python -m guess_game --export html` | Bestenliste mit Statistik-Abschnitt und Diagrammen |
| `python -m sqlite3 game.db "SELECT * FROM log_rounds"` | importierte Runden ansehen |
