# Erstes externes Paket: rich (von PyPI, steht in requirements.txt)

from rich.console import Console
from rich.table import Table

console = Console()  # Ausgabe-Werkzeug von rich

console.print("Fehler beim Speichern.", style="bold red")
console.print("Alles gespeichert.", style="green")
console.print("Markup geht auch: [yellow]gelb[/yellow] und [bold]fett[/bold].")

table = Table(title="Stundenplan Montag")  # Tabelle anlegen
table.add_column("Zeit")
table.add_column("Fach")
table.add_row("08:00", "Mathematik")
table.add_row("10:00", "Programmieren")
console.print(table)
