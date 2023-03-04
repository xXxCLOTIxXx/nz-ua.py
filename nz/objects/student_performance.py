__all__ = [
    "StudentPerformance"
]


class StudentPerformance:
    def __init__(self, data: dict = {}):
        self.json = data

        missed = self.json.get("missed", {})

        self.missed_days = missed.get("days")
        self.missed_lessons = missed.get("lessons")
        self.subjects = list()
        self.error_message = self.json.get("error_message", "")

        for subject in self.json.get("subjects", []):
            self.subjects.append(Subject(subject))


class Subject:
    def __init__(self, data: dict = {}):
        self.json = data

        self.id = self.json.get("subject_id")
        self.name = self.json.get("subject_name")
        self.marks = self.json.get("marks", tuple())
