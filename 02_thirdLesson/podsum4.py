import random
def get_user_choice():
    while True:
        choice = input("Wybierz kamień (k), papier (p) lub nożyce (n): ")
        if choice in ['k', 'p', 'n']:
            return choice
        elif choice.lower() == 'koniec':
            return 'koniec'
        else:
            print("Błędny wybór. Spróbuj ponownie.")
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Remis!"
    elif (user_choice == 'k' and computer_choice == 'n') or (user_choice == 'p' and computer_choice == 'k') or (user_choice == 'n' and computer_choice == 'p'):
        return "Wygrałeś!"
    else:
        return "Komputer wygrał!"
def play_game(num_rounds):
    user_wins = 0
    computer_wins = 0

    for _ in range(num_rounds):
        user_choice = get_user_choice()
        if user_choice == 'koniec':
            print("Koniec gry.")
            break

        computer_choice = random.choice(['k', 'p', 'n'])
        print("Komputer wybrał:", computer_choice)

        if user_choice != 'koniec':
            round_result = determine_winner(user_choice, computer_choice)
            print(round_result)
            if round_result == "Wygrałeś!":
                user_wins += 1
            elif round_result == "Komputer wygrał!":
                computer_wins += 1
    print("Wynik końcowy:")
    print("Użytkownik:", user_wins)
    print("Komputer:", computer_wins)
num_rounds = int(input("Podaj liczbę rund: "))
play_game(num_rounds)
