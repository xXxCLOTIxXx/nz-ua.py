__all__ = ["LoadHometask"]


class LoadHometask:
    def __init__(self, data: dict = {}):
        self.json = data

        self.answer = self.json.get("answer", None)
        self.files = list()
        self.error_message = self.json.get("error_message", "")

        for file in self.json.get("answer_files", []):
            self.files.append(File(file))


class File:
    def __init__(self, data: dict = {}):
        self.json = data
        self.id = self.json.get("id", None)
        self.name = self.json.get("name", None)
