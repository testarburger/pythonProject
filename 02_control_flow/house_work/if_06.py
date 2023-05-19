import random
programm_number = random.randint(1, 100)
guess = int(input("Zgadnij liczbę od 1 do 100: "))
if guess == programm_number:
    print("Great! You are win!")
else:
    print("Sorry, you are lost, number of programmist is :", programm_number)
