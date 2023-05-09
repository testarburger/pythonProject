secret_num = 5
while True:
    guess = int(input("Zgadnij liczbę od 0 do 20: "))
    if guess == secret_num:
        print("Gratulacje! Zgadłeś!")
        break
    else:
        print("Nie zgadłeś. Spróbuj ponownie.")
