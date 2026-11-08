# Export: Bestenliste als Datei zum Weitergeben, als HTML-Seite oder Excel-Datei

import html
from datetime import datetime
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font

HTML_FILE = Path("highscores.html")  # entsteht im aktuellen Ordner
EXCEL_FILE = Path("highscores.xlsx")

# Spalte im Excel-Blatt -> Breite (ungefähr in Zeichen)
COLUMN_WIDTHS = {"A": 8, "B": 14, "C": 10, "D": 10, "E": 10, "F": 8, "G": 12}

# Aussehen der Tabelle (CSS); steht als fester Text in der Seite
STYLE = (
    "body { font-family: sans-serif; margin: 2em; }"
    " table { border-collapse: collapse; }"
    " th, td { border: 1px solid #999; padding: 4px 12px; text-align: left; }"
    " th { background: #eee; }"
)


def export_html(scores, charts=None, path=HTML_FILE):
    """Schreibt die Bestenliste als HTML-Tabelle in path und gibt path zurück.

    charts: [(Bilddatei, Titel), ...] aus charts.save_charts, darunter als Bilder.
    """
    now = datetime.now().strftime("%d.%m.%Y, %H:%M")
    lines = [
        "<!DOCTYPE html>",
        '<html lang="de">',
        "<head>",
        '<meta charset="utf-8">',
        "<title>Bestenliste Zahlenraten</title>",
        f"<style>{STYLE}</style>",
        "</head>",
        "<body>",
        "<h1>Bestenliste Zahlenraten</h1>",
        f"<p>Stand: {now} Uhr</p>",
        "<table>",
        "<tr><th>Platz</th><th>Name</th><th>Stufe</th><th>Versuche</th>"
        "<th>Dauer (s)</th><th>Punkte</th><th>Datum</th></tr>",
    ]
    place = 1
    for score in scores:
        name = html.escape(score.name)  # < > & im Namen als Text, nicht als HTML
        seconds = f"{score.seconds:.1f}".replace(".", ",")
        lines.append(
            f"<tr><td>{place}</td><td>{name}</td><td>{score.level}</td>"
            f"<td>{score.tries}</td><td>{seconds}</td><td>{score.points()}</td>"
            f"<td>{score.date}</td></tr>"
        )
        place += 1
    if not scores:
        lines.append('<tr><td colspan="7">Noch keine Einträge.</td></tr>')
    lines.append("</table>")
    if charts:  # Statistik mit Diagrammen; die PNG-Dateien liegen daneben
        lines.append("<h2>Statistik</h2>")
        for chart, title in charts:
            lines.append(f'<p><img src="{chart}" alt="{title}"></p>')
    lines.append("</body>")
    lines.append("</html>")
    with open(path, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")  # eine HTML-Zeile pro Textzeile
    return path


def export_excel(scores, path=EXCEL_FILE):
    """Schreibt die Bestenliste als Excel-Tabelle in path und gibt path zurück."""
    workbook = Workbook()  # neue, leere Arbeitsmappe mit einem Blatt
    sheet = workbook.active  # das erste Blatt
    sheet.title = "Bestenliste"
    sheet.append(["Platz", "Name", "Stufe", "Versuche", "Dauer (s)", "Punkte", "Datum"])
    for cell in sheet[1]:  # Zeile 1 = Kopfzeile
        cell.font = Font(bold=True)
    place = 1
    for score in scores:
        # Zahlen bleiben Zahlen: Excel kann damit rechnen und sortieren
        row = [
            place,
            score.name,
            score.level,
            score.tries,
            score.seconds,
            score.points(),
            score.date,
        ]
        sheet.append(row)  # hängt eine Zeile unter der letzten an
        place += 1
    for column, width in COLUMN_WIDTHS.items():
        sheet.column_dimensions[column].width = width
    workbook.save(path)  # erst jetzt entsteht die Datei
    return path
