# Lab 15.3 (Vertiefung): farbige Log-Zeilen im Terminal mit RichHandler aus rich
import logging

from rich.logging import RichHandler

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",  # Zeit und Level zeigt RichHandler selbst an
    datefmt="%H:%M:%S",
    handlers=[RichHandler(show_path=False)],  # ohne Dateiname am Zeilenende
)
logger = logging.getLogger("grades")

logger.debug("Noten gelesen: [1.7, 2.3, 1.0]")
logger.info("Durchschnitt: 1.67")
logger.warning("Note 6.0 wird ignoriert")
logger.error("Datei grades.csv nicht gefunden")
