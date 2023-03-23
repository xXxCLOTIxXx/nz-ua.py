from pydantic import BaseModel, Field

__all__ = ("StudentPerformance", )


class Subject(BaseModel):
    id: int = Field(alias="subject_id")
    name: str = Field(alias="subject_name")
    marks: tuple[str, ...] = tuple()


class StudentPerformance(BaseModel):
    missed_days: int
    missed_lessons: int
    subjects: tuple[Subject, ...] = tuple()

    def __init__(self, **data) -> None:
        missed = data.get("missed", {})
        data.update(
            {
                "missed_days": missed.get("days", 0),
                "missed_lessons": missed.get("lessons", 0),
            }
        )
        super().__init__(**data)
