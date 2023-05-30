import random

def get_word(category):
    filename = f"{category}.txt"
    with open(filename) as file:
        words = file.readlines()
    return random.choice(words).strip()

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    print(displayed_word)

def play_game():
    categories = ["zwierzeta", "owoce", "kolory"]  # Dodaj więcej kategorii, jeśli chcesz

    category = input("Wybierz kategorię (dostępne kategorie: zwierzeta, owoce, kolory): ")
    category = category.lower()

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

        guess = input("Zgadnij literę: ")
        guess = guess.lower()

        if len(guess) != 1 or not guess.isalpha():
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
