names = input("Wprowadź imiona, oddzielone przecinkiem lub białym znakiem: ")
name_list = names.split(",")
for name in name_list:
    name = name.strip()
    print(f"Witaj, {name}!")
