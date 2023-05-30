import re

def get_card_type(card_number):
    visa_pattern = r"^4[0-9]{12}(?:[0-9]{3})?$"
    mastercard_pattern = r"^5[1-5][0-9]{14}$"
    amex_pattern = r"^3[47][0-9]{13}$"

    if re.match(visa_pattern, card_number):
        return "Visa"
    elif re.match(mastercard_pattern, card_number):
        return "Mastercard"
    elif re.match(amex_pattern, card_number):
        return "American Express"
    else:
        return "Nieznany"

def classify_cards(filename):
    with open(filename) as file:
        cards = file.readlines()

    visa_file = open("visa.txt", "w")
    mastercard_file = open("mastercard.txt", "w")
    amex_file = open("americanexpress.txt", "w")
    unknown_file = open("unknown.txt", "w")

    for card in cards:
        card_number = card.strip()
        card_type = get_card_type(card_number)

        if card_type == "Visa":
            visa_file.write(card)
        elif card_type == "Mastercard":
            mastercard_file.write(card)
        elif card_type == "American Express":
            amex_file.write(card)
        else:
            unknown_file.write(card)

    visa_file.close()
    mastercard_file.close()
    amex_file.close()
    unknown_file.close()

filename = "credit_cards.txt"
with open(filename, "w") as file:
    file.write("4111111111111111\n")
    file.write("5555555555554444\n")
    file.write("378282246310005\n")
    file.write("1234567890123456\n")

classify_cards(filename)
