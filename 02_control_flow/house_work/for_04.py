liczba = int(input("Podaj liczbę : "))

if liczba > 8:
    print("Podaj liczbę pomiędzy 1 a 8:")
else:
    print(liczba, "! = ")

    silnia = 1

    for num in range(1, liczba+1):
        silnia = silnia * num
        if num == liczba:
            print(num, end="")
        else:
            print(num, "*", end="")

    print(f" = {silnia}")
    print(f"Silnia z {liczba} wynosi {silnia}")
