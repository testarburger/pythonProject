from symptom_tracker import SymptomTracker
from exercise_program import ExerciseProgram
from medication import Medication
from diary import Diary
from support_group import SupportGroup
from educational_content import EducationalContent

def test_application():
    symptom_tracker = SymptomTracker()
    symptom_tracker.track_symptom()
    symptom_tracker.view_symptoms()

    exercise_program = ExerciseProgram()
    exercise_program.add_exercise()
    exercise_program.do_exercises()

    medication = Medication()
    medication.add_medication()
    medication.take_medication()

    diary = Diary()
    diary.add_entry()
    diary.view_entries()

    support_group = SupportGroup()
    support_group.join_group()
    support_group.send_message()
    support_group.leave_group()

    educational_content = EducationalContent()
    educational_content.add_article()
    educational_content.add_video()


# Testowanie uruchamiania
if __name__ == "__main__":
    test_application()
