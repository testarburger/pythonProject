def oblicz_srednia():
    liczby = input("Podaj liczby oddzielone przecinkami: ")
    liczby = liczby.split(",")

    suma = 0
    ilosc_liczb = 0

    for liczba in liczby:
        try:
            liczba = float(liczba)
            suma += liczba
            ilosc_liczb += 1
        except ValueError:
            print("Błąd: Nieprawidłowy format liczby:", liczba)

    if ilosc_liczb > 0:
        srednia = suma / ilosc_liczb
        print("Średnia arytmetyczna:", srednia)
    else:
        print("Brak poprawnych liczb do obliczenia średniej.")


oblicz_srednia()
