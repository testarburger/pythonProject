def oblicz_srednia():
    try:
        liczby = input("Podaj liczby oddzielone przecinkami: ")

        liczby = liczby.split(",")

        liczby = [float(num) for num in liczby]

        srednia = sum(liczby) / len(liczby)

        print("Średnia arytmetyczna:", srednia)

    except ValueError as e:
        with open("bledy.txt", "a") as file:
            file.write("Błąd: Nieprawidłowy format liczby. " + str(e) + "\n")

    except Exception as e:
        with open("bledy.txt", "a") as file:
            file.write("Wystąpił nieoczekiwany błąd: " + str(e) + "\n")


oblicz_srednia()
