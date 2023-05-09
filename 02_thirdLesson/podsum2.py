text = input("Wprowadź tekst: ")
result = ""
for index, char in enumerate(text):
    if index % 2 == 1:
        result += char
print("Znaki na pozycjach parzystych:", result)
