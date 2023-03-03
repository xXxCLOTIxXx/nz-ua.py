__all__ = [
    "SubjectsPerformance"
]


class SubjectsPerformance:
    def __init__(self, data: dict = {}):
        self.json = data

        self.missed_lessons = self.json.get("number_missed_lessons")
        self.lessons = list()
        self.error_message = self.json.get("error_message", "")

        for lesson in self.json.get("lessons", []):
            self.lessons.append(Lesson(lesson))


class Lesson:
    def __init__(self, data: dict = {}):
        self.json = data

        self.id = self.json.get("lesson_id")
        self.subject = self.json.get("subject")
        self.date = self.json.get("lesson_date")
        self.type = self.json.get("lesson_type")
        self.mark = self.json.get("mark")
        self.comment = self.json.get("comment")
