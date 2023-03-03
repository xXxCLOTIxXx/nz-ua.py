__all__ = [
    "Student"
]


class Student:
    def __init__(self, data: dict = {}):
        self.json = data

        self.access_token = self.json.get("access_token")
        self.refresh_token = self.json.get("refresh_token")
        self.email_hash = self.json.get("email_hash")
        self.student_id = self.json.get("student_id")
        self.fio = self.json.get("FIO")
        self.avatar = self.json.get("avatar")
        self.permissions = self.json.get("permissions")
        self.error_message = self.json.get("error_message", '')
