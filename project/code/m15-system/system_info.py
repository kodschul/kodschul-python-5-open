# Lab 15.1: Systembericht – Angaben über den eigenen Rechner für eine Support-Anfrage
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

print("Systembericht")
print("=" * 40)

# 1. Betriebssystem und Python
print(f"Betriebssystem: {platform.system()} {platform.release()}")  # z. B. Windows 11
print(f"sys.platform:   {sys.platform}")  # win32, darwin (macOS) oder linux
print(f"Python-Version: {platform.python_version()}")
print(f"Arbeitsordner:  {Path(os.getcwd()).name}")  # nur der letzte Ordnername

# 2. Freier Speicherplatz auf dem Laufwerk des Arbeitsordners
usage = shutil.disk_usage(".")  # Werte in Byte
free_gb = f"{usage.free / 10**9:.1f}".replace(".", ",")  # 1 GB = 10**9 Byte
total_gb = f"{usage.total / 10**9:.1f}".replace(".", ",")
print(f"Speicher frei:  {free_gb} GB von {total_gb} GB")

# 3. Umgebungsvariable lesen: PATH gibt es auf jedem System
folders = os.environ["PATH"].split(os.pathsep)  # Trenner: ; unter Windows, sonst :
print(f"PATH:           {len(folders)} Ordner")

# 4. Ein anderes Programm starten: Python selbst, das gibt es überall
result = subprocess.run(
    [sys.executable, "--version"],  # Liste: Programm, dann jedes Argument einzeln
    capture_output=True,  # Ausgabe auffangen statt direkt anzeigen
    text=True,  # Ausgabe als Text (str) statt als Bytes
    check=True,  # Rückgabecode ungleich 0 -> CalledProcessError
)
print(f"Befehl:         python --version -> {result.stdout.strip()}")
print(f"Rückgabecode:   {result.returncode}")  # 0 = erfolgreich
