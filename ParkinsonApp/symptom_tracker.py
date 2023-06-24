import random

class SymptomTracker:
    def __init__(self):
        self.symptoms = []

    def track_symptom(self):
        """Śledź objaw, sugerując go i zapisując."""
        symptom = self._suggest_symptom()
        self.symptoms.append(symptom)
        print("Symptom tracked:", symptom)

    def view_symptoms(self):
        """Wyświetl śledzone objawy."""
        print("Tracked symptoms:")
        for symptom in self.symptoms:
            print(symptom)

    def _suggest_symptom(self):
        """Zasugeruj użytkownikowi objaw i umożliw mu wprowadzenie własnego objawu."""
        suggested_symptoms = ["Tremors", "Rigidity", "Bradykinesia", "Postural instability"]
        print("Suggested symptoms:")
        for index, symptom in enumerate(suggested_symptoms, start=1):
            print(f"{index}. {symptom}")
        choice = input("Enter the number of the symptom you are experiencing or enter your own symptom: ")
        if choice.isdigit() and 1 <= int(choice) <= len(suggested_symptoms):
            return suggested_symptoms[int(choice) - 1]
        else:
            return input("Enter your own symptom: ")
