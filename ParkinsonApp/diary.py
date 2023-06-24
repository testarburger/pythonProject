class Diary:
    def __init__(self):
        self.entries = []

    def add_entry(self):
        # Kod do dodawania wpisu do dziennika
        entry = input("Enter an entry: ")
        self.entries.append(entry)
        print("Entry added:", entry)

    def view_entries(self):
        # Kod do przeglądania wpisów w dzienniku
        print("Diary entries:")
        for entry in self.entries:
            print(entry)
