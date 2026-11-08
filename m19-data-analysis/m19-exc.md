# Modul 19 – Transferübung: Umsatzbericht

**Einsatz:** optional, Selbstlernen; kein eigener Zeitslot
**Dauer:** ca. 30 Minuten
**Ändert die Zahlenraten-Projektbasis?** Nein — eigenständiges Auswertungsskript, das pandas (Lab 19.2), Diagramme (Lab 19.3) und eine Excel-Ausgabe (Lab 17.2) ohne Vorlage kombiniert. Referenz für den Aufbau: Spiel v5 mit [analyze.py](../project/examples/m19-data-analysis/l02-pandas/analyze.py) und [guess_game/charts.py](../project/examples/m19-data-analysis/l03-matplotlib/guess_game/charts.py).
**Arbeitsdatei:** `playground/sales_report.py` (neu)
**Starter:** keiner, leere Datei
**Daten:** [project/data/umsatz_pro_ort.csv](../project/data/umsatz_pro_ort.csv) (20 Orte mit Region und Jahresumsatz, erfundene Zahlen)

## Ausgangslage

Eine Ladenkette hat Filialen in 20 Orten und bekommt jedes Jahr eine CSV-Datei mit den Umsätzen:

```text
Ort,Region,Umsatz
Berlin,Ost,120000
Hamburg,Nord,95000
München,Süd,135000
```

Bisher entsteht daraus von Hand in Excel eine Übersicht pro Region. Ein Skript soll das ab jetzt mit einem Befehl erledigen: Kennzahlen pro Region im Terminal, dieselbe Tabelle als Excel-Datei zum Weitergeben und ein Balkendiagramm.

Gewünschte Ausgabe (Ausschnitt):

```text
$ python playground/sales_report.py
20 Orte aus data/umsatz_pro_ort.csv, Spalten: ['Ort', 'Region', 'Umsatz']
...
Umsatz pro Region:
        Orte   Summe  Durchschnitt   Median  Anteil %
Region
Süd        6  407000       67833.0  59000.0      32.4
...
Stärkste Region: Süd
Gespeichert: umsatz_regionen.xlsx, umsatz_regionen.png
```

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `project/`.
- Neue Datei `playground/sales_report.py` anlegen. Start mit `python playground/sales_report.py`; die Ergebnisdateien entstehen im Ordner `project/`.

## Aufgaben

1. Schreibe `load_sales(path)`: Fehlt die CSV-Datei, gibt das Skript `data/umsatz_pro_ort.csv nicht gefunden. Start im Ordner project/?` aus und endet mit `sys.exit(1)`; sonst gibt es den DataFrame zurück. `main()` gibt die Zahl der Orte, die Spaltennamen (`list(sales.columns)`) und die ersten drei Zeilen aus.
2. Schreibe `region_summary(sales)`: ein DataFrame pro Region mit den Spalten `Orte`, `Summe`, `Durchschnitt` (gerundet) und `Median`, sortiert nach `Summe`, größte zuerst.
3. Ergänze in `region_summary` die Spalte `Anteil %`: Anteil der Region am Gesamtumsatz in Prozent, auf eine Nachkommastelle gerundet. Gib danach `Stärkste Region: <Name>` aus (die erste Zeile des sortierten Index, `summary.index[0]`).
4. Schreibe `save_chart(summary, path)`: Balkendiagramm „Umsatz pro Region“ mit Wert über jedem Balken, Achsenbeschriftungen und `"Agg"`-Backend, gespeichert als `umsatz_regionen.png`.
5. Speichere die Zusammenfassung mit `summary.to_excel("umsatz_regionen.xlsx")` (pandas nutzt dafür `openpyxl` aus Lab 17.2) und gib die Zeile `Gespeichert: …` aus. Öffne beide Dateien zur Kontrolle und teste den Fehlerfall, indem das Skript aus `playground/` statt aus `project/` gestartet wird.

## Checkpoint

- Die Ausgabe entspricht der gewünschten Ausgabe; die Summen der vier Regionen ergeben zusammen `1255000`, die Anteile zusammen 100 %.
- `umsatz_regionen.png` zeigt vier Balken von Süd (407000) bis West (259000).
- `umsatz_regionen.xlsx` hat die Kopfzeile `Region, Orte, Summe, Durchschnitt, Median, Anteil %` und vier Zeilen.
- Aus `playground/` gestartet: Meldung „nicht gefunden“ und Exit-Code `1`.

## Abschlusskriterien

- `python playground/sales_report.py` läuft ohne Rückfragen und erzeugt Terminal-Ausgabe, Excel-Datei und Diagramm.

## Erweiterung

Speichere zusätzlich `umsatz_top10.png`: die zehn Orte mit dem höchsten Umsatz als waagrechte Balken (`ax.barh`), der größte oben.
