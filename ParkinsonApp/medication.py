class Medication:
    def __init__(self):
        self.medication_schedule = {}

    def add_medication(self):
        # Kod do dodawania leków i harmonogramu ich przyjmowania
        medication_name = input("Enter the medication name: ")
        schedule = input("Enter the schedule: ")
        self.medication_schedule[medication_name] = schedule
        print("Medication added:", medication_name)

    def take_medication(self):
        # Kod do przyjmowania leku zgodnie z harmonogramem
        medication_name = input("Enter the medication name: ")
        if medication_name in self.medication_schedule:
            print("Taking medication:", medication_name)
        else:
            print("Medication not found.")
