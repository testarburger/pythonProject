def display_board(board):
    print("   1   2   3")
    print("A  " + board["A1"] + " | " + board["A2"] + " | " + board["A3"])
    print("B  " + board["B1"] + " | " + board["B2"] + " | " + board["B3"])
    print("C  " + board["C1"] + " | " + board["C2"] + " | " + board["C3"])


def check_win(board):
    winning_conditions = [
        ["A1", "A2", "A3"],  # Rzędy
        ["B1", "B2", "B3"],
        ["C1", "C2", "C3"],
        ["A1", "B1", "C1"],  # Kolumny
        ["A2", "B2", "C2"],
        ["A3", "B3", "C3"],
        ["A1", "B2", "C3"],  # Przekątne
        ["A3", "B2", "C1"]
    ]

    for condition in winning_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ".":
            return True

    return False


def play_game():
    board = {
        "A1": ".", "A2": ".", "A3": ".",
        "B1": ".", "B2": ".", "B3": ".",
        "C1": ".", "C2": ".", "C3": ".",
    }

    players = ["X", "O"]
    current_player = 0
    total_moves = 0

    while True:
        display_board(board)
        player_mark = players[current_player]
        position = input("Player " + player_mark + ", mark position (e.g., A1): ")

        if position not in board.keys() or board[position] != ".":
            print("Invalid move. Try again.")
            continue

        board[position] = player_mark
        total_moves += 1

        if check_win(board):
            display_board(board)
            print("Player " + player_mark + " wins!")
            break

        if total_moves == 9:
            display_board(board)
            print("Draw!")
            break

        current_player = (current_player + 1) % 2

    play_again = input("Would you like to continue? [yes/no]: ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thanks for playing!")


play_game()
