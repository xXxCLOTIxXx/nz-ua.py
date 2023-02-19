from json import dumps, loads
from .utils import exceptions, helpers, objects
from .utils.headers import Headers

from aiofiles.threadpool.binary import AsyncBufferedReader

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


	async def get_schedule(self, start_date: str = "2023-02-13", end_date: str = "2023-02-19"):

		data = dumps({
			"start_date": start_date,
			"end_date": end_date,
			"student_id": self.student.student_id
		})

		response = objects.Schedule(await helpers.post(f"{self.api}/schedule/diary", headers=self.headers(data=data, access_token=self.student.access_token), data=data))
		return response


	async def get_hometask(self, hometask_id: int):
		data = dumps({
			"distance_hometask_id": hometask_id,
			"student_id": self.student.student_id
		})

		response = objects.Hometask(await helpers.post(f"{self.api}/schedule/distance-hometask", headers=self.headers(data=data, access_token=self.student.access_token), data=data))
		return response

	async def get_timetable(self, start_date: str = "2023-02-13", end_date: str = "2023-02-19"):
		#TODO: objects for this 
		data = dumps({
			"start_date": start_date,
			"end_date": end_date,
			"student_id": self.student.student_id
		})

		response = await helpers.post(f"{self.api}/schedule/diary", headers=self.headers(data=data, access_token=self.student.access_token), data=data)
		return response

	async def get_student_performance(self, start_date: str = "2023-02-13", end_date: str = "2023-02-19"):
		#TODO: objects for this 

		data = dumps({
			"start_date": start_date,
			"end_date": end_date,
			"student_id": self.student.student_id
		})

		response = await helpers.post(f"{self.api}/schedule/student-performance", headers=self.headers(data=data, access_token=self.student.access_token), data=data)
		return response


	async def get_subject_performance(self, subject_id: int, start_date: str = "2023-02-13", end_date: str = "2023-02-19"):
		#TODO: objects for this 

		data = dumps({
			"start_date": start_date,
			"end_date": end_date,
			"student_id": self.student.student_id,
			"subject_id": subject_id
		})

		response = await helpers.post(f"{self.api}/schedule/subject-grades", headers=self.headers(data=data, access_token=self.student.access_token), data=data)
		return response


	async def delete_hometask_file(self, file_id):
		#TODO: objects for this 

		data = dumps({"file_id": file_id})
		response = await helpers.post(f"{self.api}/schedule/delete-hometask-file", headers=self.headers(data=data, access_token=self.student.access_token), data=data)
		return response

	async def load_hometask_file(self, file: AsyncBufferedReader):
		#TODO THIS
		pass