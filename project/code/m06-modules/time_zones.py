# Dieselbe Uhrzeit in drei Zeitzonen (Windows ohne Zeitzonen-Daten: pip install tzdata)

from datetime import datetime
from zoneinfo import ZoneInfo

berlin = datetime.now(ZoneInfo("Europe/Berlin"))
print("Berlin:  ", berlin.strftime("%d.%m.%Y %H:%M"))

for zone in ["America/New_York", "Asia/Tokyo"]:
    there = berlin.astimezone(ZoneInfo(zone))  # gleicher Moment, andere Uhr
    print(f"{zone}:", there.strftime("%d.%m.%Y %H:%M"))
