import random
import string

def get_word(category):
    words = {
        "zwierzeta": ["kot", "pies", "kon", "krowa"],
        "owoce": ["jablko", "banan", "wisnia", "gruszka"],
        "kolory": ["czerwony", "zielony", "niebieski", "zolty"]
    }

    return random.choice(words[category])

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    print(displayed_word)

def play_game():
    categories = ["zwierzeta", "owoce", "kolory"]

    category = input("Wybierz kategorię (dostępne kategorie: zwierzeta, owoce, kolory): ").lower()

    if category not in categories:
        print("Nieprawidłowa kategoria.")
        return

    word = get_word(category)
    guessed_letters = set()

    attempts = 6

    print("Zaczynamy grę Wisielec!")
    print("Masz 6 prób, aby odgadnąć hasło.")

    while attempts > 0:
        print()
        display_word(word, guessed_letters)

        guess = input("Zgadnij literę: ").lower()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Nieprawidłowa litera.")
            continue

        if guess in guessed_letters:
            print("Ta litera już została zgadnięta.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print(f"Nie ma takiej litery. Pozostało {attempts} prób.")

        if set(word) == guessed_letters:
            print("Gratulacje! Odgadłeś hasło!")
            break

    if attempts == 0:
        print("Przegrałeś. Hasło to:", word)

play_game()
