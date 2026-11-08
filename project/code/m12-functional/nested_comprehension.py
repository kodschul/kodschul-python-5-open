# Verschachtelte Comprehensions: wann sie helfen, wann eine Schleife lesbarer ist

courses = {
    "Mathe": [2.0, 1.3, 2.7],
    "Python": [1.0, 1.7],
    "Statistik": [3.3, 2.3, 4.0],
}

# Liste von Listen zu einer Liste: zwei for in einer Comprehension
all_grades = [grade for grades in courses.values() for grade in grades]
print("Alle Noten:", all_grades)

# Comprehension im Wert: Kurs -> Noten besser als 2,5
good = {course: [g for g in grades if g < 2.5] for course, grades in courses.items()}
print("Gute Noten:", good)

# Zu viel in einer Zeile: richtig, aber schwer zu lesen
report = {c: round(sum(g) / len(g), 1) for c, g in courses.items() if len(g) > 2}
print("Schnitt (Einzeiler):", report)

# Dasselbe als Schleife: länger, aber jeder Schritt hat einen Namen
report = {}
for course, grades in courses.items():
    if len(grades) > 2:  # nur Kurse mit mindestens drei Noten
        average = round(sum(grades) / len(grades), 1)
        report[course] = average
print("Schnitt (Schleife):  ", report)
