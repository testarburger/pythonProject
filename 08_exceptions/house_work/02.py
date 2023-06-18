try:
    krotka = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    print("Krotka przed modyfikacją:", krotka)

    index = int(input("Podaj indeks: "))
    value = input("Podaj wartość: ")

    krotka = krotka[:index] + (value,) + krotka[index + 1:]

    print("Krotka po modyfikacji:", krotka)

except IndexError:
    print("Błąd: Podany indeks jest poza zakresem krotki.")
except Exception as e:
    print("Wystąpił nieoczekiwany błąd:", str(e))
