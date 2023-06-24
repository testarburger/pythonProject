import random

class ExerciseProgram:
    def __init__(self):
        self.exercises = []

    def add_exercise(self):
        # Dodaj ćwiczenie do programu, sugerując je i zapisując.
        exercise = self._suggest_exercise()
        self.exercises.append(exercise)
        print("Exercise added:", exercise)

    def do_exercises(self):
        # Wykonaj ćwiczenia w programie.
        print("Doing exercises:")
        for exercise in self.exercises:
            print("Performing exercise:", exercise)

    def _suggest_exercise(self):
        # Zasugeruj użytkownikowi ćwiczenie i umożliw mu wprowadzenie własnego ćwiczenia.
        suggested_exercises = ["Walking", "Stretching", "Yoga", "Tai Chi"]
        print("Suggested exercises:")
        for index, exercise in enumerate(suggested_exercises, start=1):
            print(f"{index}. {exercise}")
        choice = input("Enter the number of the exercise you want to add or enter your own exercise: ")
        if choice.isdigit() and 1 <= int(choice) <= len(suggested_exercises):
            return suggested_exercises[int(choice) - 1]
        else:
            return input("Enter your own exercise: ")
