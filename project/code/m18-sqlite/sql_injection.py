# SQL-Injection: warum nie f-Strings in SQL, sondern immer ?-Platzhalter
# Start im Ordner project/: python code/m18-sqlite/sql_injection.py

import sqlite3

connection = sqlite3.connect(":memory:")  # Datenbank nur im Arbeitsspeicher
connection.execute("CREATE TABLE scores (name TEXT, tries INTEGER)")
connection.executemany(
    "INSERT INTO scores VALUES (?, ?)", [("Anna", 3), ("Ben", 5), ("Cem", 4)]
)

# Eingabe einer Angreiferin statt eines Namens
name = "x' OR '1'='1"

print("1) f-String (unsicher):")
sql = f"SELECT * FROM scores WHERE name = '{name}'"
print("   SQL:", sql)  # das ' in der Eingabe beendet den Text, OR wird zu SQL
print("   Treffer:", connection.execute(sql).fetchall())  # alle Zeilen!

print("2) Platzhalter ? (sicher):")
rows = connection.execute("SELECT * FROM scores WHERE name = ?", (name,)).fetchall()
print("   Treffer:", rows)  # sucht nach genau diesem Text -> nichts

print("3) gefährlicher Name, mit ? gespeichert:")
evil = "Anna'); DROP TABLE scores;--"
connection.execute("INSERT INTO scores VALUES (?, ?)", (evil, 7))
print("   gespeichert:", connection.execute("SELECT name FROM scores").fetchall()[-1])
count = connection.execute("SELECT COUNT(*) FROM scores").fetchone()[0]
print("   Tabelle scores gibt es noch:", count, "Zeilen")

connection.close()
