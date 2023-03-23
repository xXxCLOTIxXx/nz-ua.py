from pydantic import BaseModel, Field
from typing import Literal
import datetime

__all__ = ("SubjectsPerformance", )


class Lesson(BaseModel):
    id: int = Field(alias="lesson_id")
    name: str = Field(alias="subject")
    date: datetime.date = Field(alias="lesson_date")
    type: Literal[
        "Поточна",
        "Самостійна робота",
        "Практична робота",
        "Лабораторна робота",
        "Контрольна робота",
        "Тематична",
        "Зошит"
    ] | str = Field(alias="lesson_type")
    mark: str
    comment: str | None


class SubjectsPerformance(BaseModel):
    missed_lessons: int = Field(alias="number_missed_lessons")
    lessons: tuple[Lesson, ...] = tuple()
