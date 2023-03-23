from pydantic import BaseModel, HttpUrl
import datetime

__all__ = ("Hometask", )


class File(BaseModel):
    id: int
    name: str
    url: HttpUrl
    size: int
    created_at: datetime.datetime


class Hometask(BaseModel):
    answer: str | None  # TODO: Убрать html код
    hometask: str  # TODO: Убрать html код
    is_closed: bool
    answer_files: tuple[File, ...] = tuple()
    hometask_files: tuple[File, ...] = tuple()
