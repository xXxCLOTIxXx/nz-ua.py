from pydantic import BaseModel, Field
from typing import Literal
import datetime

__all__ = ("Schedule", )


class Grade(BaseModel):
    type: Literal[
        "Поточна",
        "Самостійна робота",
        "Практична робота",
        "Лабораторна робота",
        "Контрольна робота",
        "Тематична",
        "Зошит"
    ] | str
    mark: str
    comment: str | None


class Subject(BaseModel):
    name: str = Field(alias="subject_name")
    room: str
    hometask: tuple[str, ...] = tuple()  # TODO: вынести тему в отдельное поле
    hometask_id: int | None = Field(alias="distance_hometask_id")
    hometask_is_closed: bool | None = Field(
        alias="distance_hometask_is_closed"
    )
    grades: tuple[Grade, ...] = Field(alias="lesson")


class Lesson(BaseModel):
    id: int | None = Field(alias="call_id")
    number: int | None = Field(alias="call_number")
    subjects: tuple[Subject, ...] = tuple()


class Day(BaseModel):
    date: datetime.date
    lessons: tuple[Lesson, ...] = Field(alias="calls")


class Schedule(BaseModel):
    days: tuple[Day, ...] = Field(alias="dates")

    def __len__(self) -> int:
        return len(self.days)
