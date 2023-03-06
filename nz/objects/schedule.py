__all__ = ["Schedule"]


class Schedule:
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

        lesson = subject.get("lesson", [])
        lesson = lesson[0] if lesson else {}

        self.id = self.json.get("call_id")
        self.number = self.json.get("call_number")
        self.name = subject.get("subject_name")
        self.room = subject.get("room")
        self.hometask_id = subject.get("distance_hometask_id")
        self.hometask_is_closed = subject.get("distance_hometask_is_closed")
        self.hometask: list = subject.get("hometask")
        self.type = lesson.get("type")
        self.mark = lesson.get("mark")
        self.comment = lesson.get("comment")
