def flames_game():
    name1 = input("Podaj imię pierwszej osoby: ")
    name2 = input("Podaj imię drugiej osoby: ")

    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    for char in name1:
        if char in name2:
            name2 = name2.replace(char, "", 1)
            name1 = name1.replace(char, "", 1)

    count = len(name1) + len(name2)

    flames = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Sibling"]

    while len(flames) > 1:
        index = (count % len(flames) - 1)
        if index >= 0:
            right = flames[index + 1:]
            left = flames[:index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]

    relationship = flames[0]
    print(f"\nPrawdziwy związek między {name1.capitalize()} i {name2.capitalize()}: {relationship}")


flames_game()
