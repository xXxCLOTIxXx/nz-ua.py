__all__ = [
    "Hometask"
]


class Hometask:
    def __init__(self, data: dict = {}):
        self.json = data

        self.hometask = self.json.get("hometask")
        self.answer = self.json.get("answer")
        self.is_closed = self.json.get("is_closed")
        self.hometask_files = list()
        self.answer_files = list()
        self.error_message = self.json.get("error_message", "")

        for file in self.json.get("hometask_files", []):
            self.hometask_files.append(File(file))

        for file in self.json.get("answer_files", []):
            self.answer_files.append(File(file))


class File:
    def __init__(self, data: dict = {}):
        self.json = data

        self.id = self.json.get("id")
        self.name = self.json.get("name")
        self.url = self.json.get("url")
        self.size = self.json.get("size")
        self.created_at = self.json.get("created_at")
