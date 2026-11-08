# Lab 15.3: Die fünf Log-Level mit basicConfig – Ausgabe im Terminal
import logging

logging.basicConfig(
    level=logging.INFO,  # ab INFO aufwärts; DEBUG wird verworfen
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    datefmt="%H:%M:%S",  # nur die Uhrzeit
)
logger = logging.getLogger("grades")  # Name erscheint in jeder Zeile

logger.debug("Noten gelesen: [1.7, 2.3, 6.0]")  # erscheint nicht (unter INFO)
logger.info("Programm gestartet")
logger.warning("Note 6.0 liegt außerhalb von 1.0 bis 5.0 und wird ignoriert")
logger.error("Datei grades.csv nicht gefunden")
logger.critical("Kein Speicherplatz frei, Programm bricht ab")
