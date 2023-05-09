import random
def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Witaj w grze Ciepło-Zimno!")
    print("Komputer wylosował liczbę z zakresu od 1 do 100.")
    print("Spróbuj zgadnąć, jaką liczbę wylosował komputer.")
    while attempts < 6:
        guess = int(input("Podaj swoją liczbę: "))
        attempts += 1
        if guess == secret_number:
            print("Brawo! Zgadłeś liczbę!")
            return
        if guess < secret_number:
            print("Za niska liczba!")
        else:
            print("Za wysoka liczba!")
    print("Niestety, skończyły się próby.")
    print("Komputer wygrał! Wylosowana liczba to:", secret_number)
play_game()
