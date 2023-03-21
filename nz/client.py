import asyncio
from datetime import date

from .utils.http_client import HttpClient
from .utils.exceptions import (
    IncorrectNickname,
    IncorrectPassword,
    HometaskNotFound,
    HometaskFileNotFound,
    UnknownError,
)
from . import objects


class Client:
    def __init__(self, token: str | None = None, **http_options) -> None:
        self._http = HttpClient(token, **http_options)

    async def login(self, username: str, password: str) -> objects.Student:
        data = {"username": username, "password": password}
        response: dict = await self._http.post("/v1/user/login", data)
        match response.get("error_message"):
            case "":
                student = objects.Student(response)
                self._http.token = student.access_token
                return student
            case "Користувач не знайдений.":
                raise IncorrectNickname
            case "Введено невірний логін або пароль.":
                raise IncorrectPassword
            case _:
                raise UnknownError(response)

    async def get_schedule(
        self,
        start_date: str | date = date.today().replace(day=1),
        end_date: str | date = date.today(),
    ) -> objects.Schedule:
        data = {"start_date": str(start_date), "end_date": str(end_date)}
        response: dict = await self._http.post("/v1/schedule/diary", data)
        match response.get("error_message"):
            case "":
                return objects.Schedule(response)
            case _:
                raise UnknownError(response)

    async def get_timetable(
        self,
        start_date: str | date = date.today().replace(day=1),
        end_date: str | date = date.today(),
    ) -> objects.Timetable:
        data = {"start_date": str(start_date), "end_date": str(end_date)}
        response: dict = await self._http.post("/v1/schedule/timetable", data)
        match response.get("error_message"):
            case "":
                return objects.Timetable(response)
            case _:
                raise UnknownError(response)

    async def get_student_performance(
        self,
        start_date: str | date = date.today().replace(day=1),
        end_date: str | date = date.today(),
    ) -> objects.StudentPerformance:
        data = {"start_date": str(start_date), "end_date": str(end_date)}
        response: dict = await self._http.post("/v1/schedule/student-performance", data)
        match response.get("error_message"):
            case "":
                return objects.StudentPerformance(response)
            case _:
                raise UnknownError(response)

    async def get_subject_performance(
        self,
        subject_id: int | str,
        start_date: str | date = date.today().replace(day=1),
        end_date: str | date = date.today(),
    ) -> objects.SubjectsPerformance:
        if subject_id in (0, "0") or not isinstance(subject_id, (int, str)):
            raise ValueError("Id must be a number or a string. Id cannot be 0")
        data = {
            "start_date": str(start_date),
            "end_date": str(end_date),
            "subject_id": subject_id,
        }
        response: dict = await self._http.post("/v1/schedule/subject-grades", data)
        match response.get("error_message"):
            case "":
                return objects.SubjectsPerformance(response)
            case _:
                raise UnknownError(response)

    async def get_hometask(self, hometask_id: int | str) -> objects.Hometask:
        if hometask_id in (0, "0") or not isinstance(hometask_id, (int, str)):
            raise ValueError("Id must be a number or a string. Id cannot be 0")
        data = {"distance_hometask_id": hometask_id}
        response: dict = await self._http.post("/v1/schedule/distance-hometask", data)
        match response.get("error_message"):
            case "":
                return objects.Hometask(response)
            case "Завдання не знайдене":
                raise HometaskNotFound
            case _:
                raise UnknownError(response)

    async def delete_hometask_file(self, hometask_id: int | str) -> None:
        if hometask_id in (0, "0") or not isinstance(hometask_id, (int, str)):
            raise ValueError("Id must be a number or a string. Id cannot be 0")
        data = {"file_id": hometask_id}
        response: dict = await self._http.post(
            "/v1/schedule/delete-hometask-file", data
        )
        match response.get("status"):
            case "success":
                return
            case 404:
                raise HometaskFileNotFound
            case _:
                raise UnknownError(response)

    def __del__(self) -> None:
        asyncio.run(self._http.close())