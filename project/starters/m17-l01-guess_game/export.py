# Export: Bestenliste als Datei zum Weitergeben, hier als HTML-Seite
# Zahlenraten – Starter für Lab 17.1 (Stand nach Lab 16.3)
# Vorbereitet: Seitenkopf, Tabellenkopf und Schreiben der Datei

import html  # html.escape für die Namen
from datetime import datetime
from pathlib import Path

HTML_FILE = Path("highscores.html")  # entsteht im aktuellen Ordner

# Aussehen der Tabelle (CSS); steht als fester Text in der Seite
STYLE = (
    "body { font-family: sans-serif; margin: 2em; }"
    " table { border-collapse: collapse; }"
    " th, td { border: 1px solid #999; padding: 4px 12px; text-align: left; }"
    " th { background: #eee; }"
)


def export_html(scores, path=HTML_FILE):
    """Schreibt die Bestenliste als HTML-Tabelle in path und gibt path zurück."""
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
    # TODO Lab 17.1: pro Score eine Tabellenzeile anhängen:
    #   <tr><td>Platz</td><td>Name</td><td>Stufe</td><td>Versuche</td>
    #   <td>Dauer</td><td>Punkte</td><td>Datum</td></tr>
    #   Name mit html.escape(...); Platz zählen wie in ui.show_highscores
    # TODO Lab 17.1: leere Liste -> <tr><td colspan="7">Noch keine Einträge.</td></tr>
    lines.append("</table>")
    lines.append("</body>")
    lines.append("</html>")
    with open(path, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")  # eine HTML-Zeile pro Textzeile
    return path
