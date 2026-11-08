# Lab 15.2: E-Mail-Adresse prüfen – erst ohne, dann mit regulärem Ausdruck
import re


def is_valid_email_simple(email):
    """Prüfung nur mit count, split und in (Werkzeuge aus Lab 2.4)."""
    if email.count("@") != 1:  # genau ein @
        return False
    user, domain = email.split("@")
    return user != "" and "." in domain  # etwas vor dem @, ein Punkt dahinter


# Vor dem @: Buchstaben, Ziffern, _ . + -; danach Domain-Teile mit Punkt dazwischen
EMAIL_PATTERN = re.compile(r"[\w.+-]+@[\w-]+(\.[\w-]+)+")


def is_valid_email(email):
    """Prüfung mit Muster: fullmatch = die ganze Adresse muss passen."""
    return EMAIL_PATTERN.fullmatch(email) is not None


tests = [
    "anna@uni-beispiel.de",
    "ben.meier@mail.example.org",
    "anna@.de",
    "anna@uni..de",
    "an na@uni.de",
    "anna@unide",
]

for email in tests:
    simple = is_valid_email_simple(email)
    with_regex = is_valid_email(email)
    print(f"{email}: ohne Regex {simple}, mit Regex {with_regex}")
