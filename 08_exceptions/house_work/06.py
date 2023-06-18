def obsluga_bledow():
    try:
        with open("plik_nieistniejacy.txt", "r") as file:
            zawartosc = file.read()
            print("Zawartość pliku:", zawartosc)

    except FileNotFoundError:
        print("Błąd: Plik nie istnieje.")

    try:
        with open("plik_do_odczytu_w_trybie_w.txt", "w") as file:
            zawartosc = file.read()
            print("Zawartość pliku:", zawartosc)

    except IOError:
        print("Błąd: Nie można odczytać pliku otwartego w trybie 'w'.")

    try:
        with open("plik_juz_istniejacy.txt", "x") as file:
            file.write("Przykładowa zawartość.")
            print("Plik został utworzony.")

    except FileExistsError:
        print("Błąd: Plik już istnieje.")

    except PermissionError:
        print("Błąd: Brak uprawnień do utworzenia pliku.")

    except Exception as e:
        print("Wystąpił nieoczekiwany błąd:", str(e))


obsluga_bledow()
