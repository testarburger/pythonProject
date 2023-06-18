class Kolejka:
    def __init__(self, elementy=[]):
        self.kolejka = elementy

    def wyswietl(self):
        print("Kolejka:", self.kolejka)

    def czy_pusta(self):
        return len(self.kolejka) == 0

    def put(self, element):
        self.kolejka.append(element)
        print("Dodano element do kolejki:", element)

    def get(self):
        if not self.czy_pusta():
            element = self.kolejka.pop(0)
            print("Pobrano element z kolejki:", element)
            return element
        else:
            print("Kolejka jest pusta.")
            return None


# Przykład użycia
kolejka = Kolejka([1, 2, 3, 4, 5])

kolejka.wyswietl()  # Wyświetlenie kolejki: [1, 2, 3, 4, 5]
print("Czy kolejka jest pusta?", kolejka.czy_pusta())  # Czy kolejka jest pusta? False

kolejka.put(6)  # Dodano element do kolejki: 6

element = kolejka.get()  # Pobrano element z kolejki: 1
print("Pobrany element:", element)  # Pobrany element: 1

kolejka.wyswietl()  # Wyświetlenie kolejki: [2, 3, 4, 5, 6]
