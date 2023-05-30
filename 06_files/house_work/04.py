import random

def get_content():
    filename = "quotes.txt"
    with open(filename) as file:
        content = file.readlines()

    return content


def show(quote):
    txt, author = quote.split(" - ")
    print("Cytat dnia:")
    print()
    width = 70
    print("*" * width)
    print(txt.center(width))
    print(author.strip().center(width))
    print("*" * width)


def main():
    quotes = get_content()

    num_quotes = 3
    random_quotes = random.sample(quotes, num_quotes)
    for quote in random_quotes:
        show(quote)
        print()

main()
