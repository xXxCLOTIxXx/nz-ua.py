import asyncio

from json import dumps, loads
from .utils import exceptions, helpers
from .utils.headers import Headers
import objects

class Client(Headers):
	def __init__(self, profile: objects.Student = None):
		self.api = 'https://api-mobile.nz.ua/v1'
		self.student = profile if profile else objects.Student()
		
		Headers.__init__(self)


	async def login(self, username: str, password: str):

		data = dumps({
			"username":username,
			"password":password
		})

		response = objects.Student(await helpers.post(f"{self.api}/user/login", headers=self.headers(data=data), data=data))
		self.student = response
		return self.student

	async def logout(self):
		self.student = objects.Student()
		return self.student

	def run(self, username: str, password: str):
		async def runner():
			await self.login(username=username, password=password)

		try:
			asyncio.run(runner())
		except KeyboardInterrupt:
			return

	async def get_schedule(self, start_date: str = None, end_date: str = None):

		data = dumps({
			"start_date": start_date if start_date else helpers.get_week()['start'],
			"end_date": end_date if end_date else helpers.get_week()['end'],
			"student_id": self.student.studentId
		})

		response = objects.Schedule(await helpers.post(f"{self.api}/schedule/diary", headers=self.headers(data=data, access_token=self.student.accessToken), data=data))
		return response


	async def get_hometask(self, hometaskId: int):

		data = dumps({
			"distance_hometask_id": hometaskId,
			"student_id": self.student.studentId
		})

		response = objects.Hometask(await helpers.post(f"{self.api}/schedule/distance-hometask", headers=self.headers(data=data, access_token=self.student.accessToken), data=data))
		return response

	async def get_timetable(self, start_date: str = None, end_date: str = None):

		data = dumps({
			"start_date": start_date if start_date else helpers.get_week()['start'],
			"end_date": end_date if end_date else helpers.get_week()['end'],
			"student_id": self.student.studentId
		})

		response = objects.Timetable(await helpers.post(f"{self.api}/schedule/timetable", headers=self.headers(data=data, access_token=self.student.accessToken), data=data))
		return response

	async def get_student_performance(self, start_date: str = None, end_date: str = None):

		data = dumps({
			"start_date": start_date if start_date else helpers.get_mounth()['start'],
			"end_date": end_date if end_date else helpers.get_mounth()['end'],
			"student_id": self.student.studentId
		})

		response = objects.StudentPerformance(await helpers.post(f"{self.api}/schedule/student-performance", headers=self.headers(data=data, access_token=self.student.accessToken), data=data))
		return response


	async def get_subject_performance(self, subjectId: int, start_date: str = None, end_date: str = None):

		data = dumps({
			"start_date": start_date if start_date else helpers.get_mounth()['start'],
			"end_date": end_date if end_date else helpers.get_mounth()['end'],
			"student_id": self.student.studentId,
			"subject_id": subjectId
		})

		response = objects.SubjectsPerformance(await helpers.post(f"{self.api}/schedule/subject-grades", headers=self.headers(data=data, access_token=self.student.accessToken), data=data))
		return response


	async def delete_hometask_file(self, fileId):

		data = dumps({"file_id": fileId})
		response = await helpers.post(f"{self.api}/schedule/delete-hometask-file", headers=self.headers(data=data, access_token=self.student.accessToken), data=data)
		return response

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