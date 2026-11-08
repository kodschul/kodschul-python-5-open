# **kwargs: beliebig viele Werte nach Name, gesammelt in einem Dictionary


def make_profile(name, **details):
    """Baut ein Profil aus dem Namen und beliebigen weiteren Angaben."""
    print("details ist", details)  # ein Dictionary aus allen Schlüsselwörtern
    profile = {"name": name}
    for key, value in details.items():
        profile[key] = value
    return profile


anna = make_profile("Anna", study="Informatik", semester=3)
ben = make_profile("Ben", city="Köln")
print(anna)
print(ben)
