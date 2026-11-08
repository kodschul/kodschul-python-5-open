# Lab 15.1: Programme starten mit subprocess – Rückgabecode und Fehler auswerten
import subprocess
import sys

# Ein Befehl, der klappt: Rückgabecode 0, Ausgabe in result.stdout
result = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
print(f"1) Rückgabecode {result.returncode}, Ausgabe: {result.stdout.strip()}")

# Ein Befehl, der scheitert: Python beendet sich mit Code 3 (wie sys.exit(3))
result = subprocess.run([sys.executable, "-c", "import sys; sys.exit(3)"])
print(f"2) Rückgabecode {result.returncode}")
if result.returncode != 0:
    print("   Befehl ist fehlgeschlagen.")

# Mit check=True wird ein Code ungleich 0 zur Exception
try:
    subprocess.run([sys.executable, "-c", "import sys; sys.exit(3)"], check=True)
except subprocess.CalledProcessError as error:
    print(f"3) CalledProcessError: Rückgabecode {error.returncode}")

# Ein Programm, das es nicht gibt
try:
    subprocess.run(["gibt-es-nicht"])
except FileNotFoundError:
    print("4) FileNotFoundError: Programm nicht gefunden")

# Variante mit Plattform-Prüfung: ping heißt überall gleich, die Option nicht
count_option = "-n" if sys.platform == "win32" else "-c"  # Windows: -n, sonst -c
command = ["ping", count_option, "1", "127.0.0.1"]  # 127.0.0.1 = eigener Rechner
print(f"5) Befehl als Liste: {command}")
try:
    result = subprocess.run(command, capture_output=True, text=True, timeout=10)
    print(f"   Rückgabecode {result.returncode}")
except FileNotFoundError:
    print("   ping ist auf diesem Rechner nicht installiert.")
