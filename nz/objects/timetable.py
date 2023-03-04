__all__ = [
    "Timetable"
]


class Timetable:
    def __init__(self, data: dict = {}):
        self.json = data

        self.days = list()
        self.error_message = self.json.get("error_message", "")

        for date in self.json.get("dates", []):
            self.days.append(Day(date))


class Day:
    def __init__(self, data: dict = {}):
        self.json = data

        self.date = self.json.get("date")
        self.lessons = list()

        for call in self.json.get("calls", []):
            self.lessons.append(Lesson(call))


class Lesson:
    def __init__(self, data: dict = {}):
        self.json = data

        subjects = self.json.get("subjects", [])
        subject = subjects[0] if subjects else {}

        teacher = subject.get("teacher", {})

        self.id = self.json.get("call_id")
        self.number = self.json.get("call_number")
        self.start = self.json.get("time_start")
        self.end = self.json.get("time_start")
        self.name = subject.get("subject_name")
        self.room = subject.get("room")
        self.teacher_id = teacher.get("id")
        self.teacher_name = teacher.get("name")
