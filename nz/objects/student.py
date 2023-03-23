from pydantic import BaseModel, Field, HttpUrl
import datetime

__all__ = ("Student", )


class Avatar(BaseModel):
    image: HttpUrl | None = Field(alias="image_url")
    created_at: datetime.datetime | None = Field(alias="datetime")


class Student(BaseModel):
    fio: str = Field(alias="FIO")
    id: int = Field(alias="student_id")
    avatar: Avatar
    token: str = Field(alias="access_token")
    refresh_token: str
    email_hash: str
    permissions: dict
