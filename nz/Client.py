import asyncio
from datetime import date

from .utils.http_client import HttpClient
from . import objects


class Client:
    def __init__(
        self,
        profile: objects.Student = objects.Student(),
        headers: dict | None = None,
        base_url: str = "https://api-mobile.nz.ua",
    ) -> None:
        self.http = HttpClient(headers=headers, base_url=base_url)
        self.student = profile

    async def login(self, username: str, password: str) -> objects.Student:
        data = {"username": username, "password": password}
        self.student = objects.Student(await self.http.post("/v1/user/login", data))
        self.http.token = self.student.access_token
        return self.student

    async def close(self) -> None:
        await self.http.close()
        await asyncio.sleep(0)

    async def get_schedule(
        self,
        start_date: str | date = date.today().replace(day=1),
        end_date: str | date = date.today(),
    ) -> objects.Schedule:
        data = {"start_date": str(start_date), "end_date": str(end_date)}
        return objects.Schedule(await self.http.post("/v1/schedule/diary", data))

    async def get_hometask(self, hometask_id: int | str) -> objects.Hometask:
        data = {"distance_hometask_id": hometask_id}
        return objects.Hometask(
            await self.http.post("/v1/schedule/distance-hometask", data)
        )

    async def get_timetable(
        self,
        start_date: str | date = date.today().replace(day=1),
        end_date: str | date = date.today(),
    ) -> objects.Timetable:
        data = {"start_date": str(start_date), "end_date": str(end_date)}
        return objects.Timetable(await self.http.post("/v1/schedule/timetable", data))

    async def get_student_performance(
        self,
        start_date: str | date = date.today().replace(day=1),
        end_date: str | date = date.today(),
    ) -> objects.StudentPerformance:
        data = {"start_date": str(start_date), "end_date": str(end_date)}
        return objects.StudentPerformance(
            await self.http.post("/v1/schedule/student-performance", data)
        )

    async def get_subject_performance(
        self,
        subject_id: int,
        start_date: str | date = date.today().replace(day=1),
        end_date: str | date = date.today(),
    ) -> objects.SubjectsPerformance:
        data = {
            "start_date": str(start_date),
            "end_date": str(end_date),
            "subject_id": subject_id,
        }
        return objects.SubjectsPerformance(
            await self.http.post("/v1/schedule/subject-grades", data)
        )

    async def delete_hometask_file(self, hometask_id):
        data = {"file_id": hometask_id}
        return await self.http.post("/v1/schedule/delete-hometask-file", data)
