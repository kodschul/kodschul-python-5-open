# filter: nur die Elemente behalten, für die eine Funktion True liefert

nums = range(10)
print("Zahlen:", list(nums))


def is_even(num):
    """True, wenn num ohne Rest durch 2 teilbar ist."""
    return num % 2 == 0


evens = filter(is_even, nums)  # benannte Funktion
odds = filter(lambda num: num % 2 != 0, nums)  # lambda
print("gerade:  ", list(evens))
print("ungerade:", list(odds))

# dasselbe als Listen-Comprehension mit if (Lab 12.1)
print("gerade (Comprehension):", [num for num in nums if num % 2 == 0])

persons = [
    {"name": "Fritz", "age": 18},
    {"name": "Paul", "age": 15},
    {"name": "Marie", "age": 40},
]
adults = filter(lambda person: person["age"] >= 18, persons)
print("Volljährig:", list(adults))
