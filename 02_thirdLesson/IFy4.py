text = input("Please, give your text: ")

if len(text) > 5 and "a" in text:
    text_second = text.replace("a", "z")
    print("The text after changing letters 'a' on 'z' ", text_second)
else:
    print("The text is shorter than 5 characters or does not contain the 'a'.")
