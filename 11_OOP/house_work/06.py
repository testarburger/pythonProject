class Kraj:
    def __init__(self, nazwa, powierzchnia, ludnosc, jezyk_urzedowy, stolica):
        self.nazwa = nazwa
        self.powierzchnia = powierzchnia
        self.ludnosc = ludnosc
        self.jezyk_urzedowy = jezyk_urzedowy
        self.stolica = stolica

    def __str__(self):
        return f"Nazwa: {self.nazwa}, Powierzchnia: {self.powierzchnia}, Ludność: {self.ludnosc}, Język urzędowy: {self.jezyk_urzedowy}, Stolica: {self.stolica}"


kraj1 = Kraj("Polska", 312696, 38000000, "polski", "Warszawa")
kraj2 = Kraj("Niemcy", 357022, 83000000, "niemiecki", "Berlin")
kraj3 = Kraj("Francja", 551695, 67000000, "francuski", "Paryż")

kraje = [kraj1, kraj2, kraj3]

for kraj in kraje:
    print(kraj)
