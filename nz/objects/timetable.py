from pydantic import BaseModel, Field
import datetime

__all__ = ("Timetable", )


class Teacher(BaseModel):
    id: int
    name: str


class Subject(BaseModel):
    name: str = Field(alias="subject_name")
    room: str
    teacher: Teacher


class Lesson(BaseModel):
    id: int | None = Field(alias="call_id")
    number: int | None = Field(alias="call_number")
    start: datetime.time = Field(alias="time_start")
    end: datetime.time = Field(alias="time_end")
    subjects: tuple[Subject, ...] = tuple()


class Day(BaseModel):
    date: datetime.date
    lessons: tuple[Lesson, ...] = Field(alias="calls")


class Timetable(BaseModel):
    days: tuple[Day, ...] = Field(alias="dates")

    def __len__(self) -> int:
        return len(self.days)
