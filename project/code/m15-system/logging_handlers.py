# Lab 15.3: Ein Logger, zwei Handler – alles in eine Datei, nur Probleme ins Terminal
import logging

logger = logging.getLogger("grades")
logger.setLevel(logging.DEBUG)  # der Logger selbst lässt alles durch

file_handler = logging.FileHandler("grades.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)  # Datei: alles ab DEBUG

console_handler = logging.StreamHandler()  # Terminal
console_handler.setLevel(logging.WARNING)  # Terminal: nur WARNING und höher

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(name)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def average(grades):
    """Durchschnitt einer Notenliste."""
    logger.debug(f"Berechne Durchschnitt aus {grades}")
    return sum(grades) / len(grades)


for grades in [[1.7, 2.3, 1.0], []]:
    try:
        result = average(grades)
        logger.info(f"Durchschnitt: {result:.2f}")
    except ZeroDivisionError:  # leere Liste: Division durch 0
        logger.exception("Durchschnitt ohne Noten nicht möglich")  # mit Traceback

print("Fertig. Alle Details stehen in grades.log.")
