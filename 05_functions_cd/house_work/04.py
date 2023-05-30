def love_calculator():
    name1 = input("Podaj imię pierwszej osoby: ")
    name2 = input("Podaj imię drugiej osoby: ")

    combined_names = name1.lower() + name2.lower()
    letters = list(combined_names + "love")

    letter_count = {}
    for letter in letters:
        letter_count[letter] = letter_count.get(letter, 0) + 1

    numbers = list(letter_count.values())
    while len(numbers) > 2:
        reduced_numbers = [numbers[0] + numbers[-1]]
        numbers = reduced_numbers

    percentage = int(''.join(map(str, numbers)))

    print(f"\nWartość procentowa dopasowania pary: {percentage}%")

love_calculator()
