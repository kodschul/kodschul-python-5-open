# Lab 2.4: E-Mail-Adresse zerlegen

email = input("E-Mail: ").strip().lower()

at = email.find("@")  # Position des @ (Index)
user = email[:at]  # alles vor dem @
domain = email[at + 1 :]  # alles nach dem @

print(f"Name:   {user}")
print(f"Domain: {domain}")
print("Endet auf .de:", domain.endswith(".de"))
