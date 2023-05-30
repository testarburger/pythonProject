import os

def create_file(filename):
    with open(filename, "w") as file:
        file.write("Hello, World!")

def get_file_size(filename):
    file_size = os.path.getsize(filename)
    return file_size

filename = "quotes.txt"
create_file(filename)

file_size = get_file_size(filename)
print(f"Rozmiar pliku '{filename}': {file_size} bajtów")
