from json import dumps, loads
from .utils import exceptions, helpers
from .utils.http_client import HttpClient
from . import objects

class Client:
	def __init__(
		self,
		profile: objects.Student = objects.Student(),
		headers: dict | None = None,
		base_url: str = "https://api-mobile.nz.ua"
	) -> None:
		self.http = HttpClient(headers=headers, base_url=base_url)
		self.student = profile

	async def login(self, username: str, password: str) -> objects.Student:
		data = {"username": username, "password": password}
		self.student = objects.Student(await self.http.post("/v1/user/login", data))
		self.http.token = self.student.access_token
		return self.student

	async def logout(self):
		self.student = objects.Student()
		return self.student

	async def close(self):
		await self.http.close()

	async def get_schedule(self, start_date: str = None, end_date: str = None):
		data = {
			"start_date": start_date if start_date else helpers.get_week()["start"],
			"end_date": end_date if end_date else helpers.get_week()["end"],
			"student_id": self.student.student_id
		}
		return objects.Schedule(await self.http.post("/v1/schedule/diary", data))

	async def get_hometask(self, hometaskId: int):
		data = {
			"distance_hometask_id": hometaskId,
			"student_id": self.student.student_id
		}
		return objects.Hometask(await self.http.post("v1/schedule/distance-hometask", data))

	async def get_timetable(self, start_date: str = None, end_date: str = None):
		data = {
			"start_date": start_date if start_date else helpers.get_week()['start'],
			"end_date": end_date if end_date else helpers.get_week()['end'],
			"student_id": self.student.student_id
		}
		return objects.Timetable(await self.http.post("v1/schedule/timetable", data))

	async def get_student_performance(self, start_date: str = None, end_date: str = None):
		data = {
			"start_date": start_date if start_date else helpers.get_mounth()['start'],
			"end_date": end_date if end_date else helpers.get_mounth()['end'],
			"student_id": self.student.student_id
		}
		return objects.StudentPerformance(await self.http.post("v1/schedule/student-performance", data))

	async def get_subject_performance(self, subjectId: int, start_date: str = None, end_date: str = None):
		data = {
			"start_date": start_date if start_date else helpers.get_mounth()['start'],
			"end_date": end_date if end_date else helpers.get_mounth()['end'],
			"student_id": self.student.student_id,
			"subject_id": subjectId
		}
		return objects.SubjectsPerformance(await self.http.post("v1/schedule/subject-grades", data))

	async def delete_hometask_file(self, fileId):
		data = {"file_id": fileId}
		return await self.http.post("v1/schedule/delete-hometask-file", data)

	async def load_hometask(self, hometaskId: int, text: str = None, file = None):
		pass
		#TODO IT
		"""
		return objects.LoadHometask(
			await helpers.post(
				f"{self.api}/schedule/delete-hometask-file", headers=self.headers(access_token=self.student.accessToken)
				)
			)

		"""