class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        print(f"Jestem {self.imie} {self.nazwisko}")

# Tworzenie obiektu klasy Osoba
osoba1 = Osoba("Jan", "Kowalski")

# Wywołanie metody przedstaw_sie na obiekcie
osoba1.przedstaw_sie()
