import random
import itertools

def find_longest_sequence(string):
    max_sequence = ""
    max_length = 0

    for char, group in itertools.groupby(string):
        sequence = "".join(group)
        length = len(sequence)
        if length > max_length:
            max_sequence = sequence
            max_length = length

    return max_sequence, max_length

def generate_test_case(characters):
    sequence = random.choice(characters) * random.randint(2, 10)
    return sequence

def main():
    characters = input("Podaj znaki oddzielone spacją: ").split()
    test_case = generate_test_case(characters)
    print("Wygenerowany ciąg:", test_case)

    longest_sequence, length = find_longest_sequence(test_case)
    print("Najdłuższa sekwencja:", longest_sequence)
    print("Długość sekwencji:", length)

if __name__ == "__main__":
    main()
