from .utils import helpers, objects
from .utils.headers import Headers
from json import dumps
import os.path

class Client(Headers):
	def __init__(self, profile: objects.Student = None):
		self.api = 'https://api-mobile.nz.ua/v1'
		self.student = profile if profile else objects.Student()
		Headers.__init__(self)


	async def login(self, username: str, password: str) -> objects.Student:

		data = dumps({
			"username":username,
			"password":password
		})

		response = objects.Student(await helpers.post(f"{self.api}/user/login", headers=self.headers(data=data), data=data))
		self.student = response
		return self.student

	async def logout(self) -> objects.Student:
		self.student = objects.Student()
		return self.student


	async def get_schedule(self, start_date: str = None, end_date: str = None) -> objects.Schedule:

		data = dumps({
			"start_date": start_date if start_date else helpers.get_week()['start'],
			"end_date": end_date if end_date else helpers.get_week()['end'],
			"student_id": self.student.studentId
		})

		response = objects.Schedule(await helpers.post(f"{self.api}/schedule/diary", headers=self.headers(data=data, access_token=self.student.accessToken), data=data))
		return response


	async def get_hometask(self, hometaskId: int) -> objects.Hometask:

		data = dumps({
			"distance_hometask_id": hometaskId,
			"student_id": self.student.studentId
		})

		response = objects.Hometask(await helpers.post(f"{self.api}/schedule/distance-hometask", headers=self.headers(data=data, access_token=self.student.accessToken), data=data))
		return response

	async def get_timetable(self, start_date: str = None, end_date: str = None) -> objects.Timetable:

		data = dumps({
			"start_date": start_date if start_date else helpers.get_week()['start'],
			"end_date": end_date if end_date else helpers.get_week()['end'],
			"student_id": self.student.studentId
		})

		response = objects.Timetable(await helpers.post(f"{self.api}/schedule/timetable", headers=self.headers(data=data, access_token=self.student.accessToken), data=data))
		return response

	async def get_student_performance(self, start_date: str = None, end_date: str = None) -> objects.StudentPerformance:

		data = dumps({
			"start_date": start_date if start_date else helpers.get_mounth()['start'],
			"end_date": end_date if end_date else helpers.get_mounth()['end'],
			"student_id": self.student.studentId
		})

		response = objects.StudentPerformance(await helpers.post(f"{self.api}/schedule/student-performance", headers=self.headers(data=data, access_token=self.student.accessToken), data=data))
		return response


	async def get_subject_performance(self, subjectId: int, start_date: str = None, end_date: str = None) ->  objects.LessonPerformance:

		data = dumps({
			"start_date": start_date if start_date else helpers.get_mounth()['start'],
			"end_date": end_date if end_date else helpers.get_mounth()['end'],
			"student_id": self.student.studentId,
			"subject_id": subjectId
		})

		response = objects.LessonPerformance(await helpers.post(f"{self.api}/schedule/subject-grades", headers=self.headers(data=data, access_token=self.student.accessToken), data=data))
		return response


	async def delete_hometask_file(self, fileId: int) -> dict:

		data = dumps({"file_id": fileId})
		response = await helpers.post(f"{self.api}/schedule/delete-hometask-file", headers=self.headers(data=data, access_token=self.student.accessToken), data=data)
		return response

	async def hometask_text_answer(self, hometaskId: int, text: str = None, deleteFilesIdList: list = None) ->  objects.UploadHometask:

		data = dumps({
			"student_id": self.student.studentId,
			"hometask_id": hometaskId,
			"hometask_text": text,
			"deleteFilesIdList": deleteFilesIdList
		})
		return objects.UploadHometask(
			await helpers.post(f"{self.api}/schedule/student-answer", headers=self.headers(access_token=self.student.accessToken, data=data), data=data)
		)


	async def hometask_answer(self, hometaskId: int, file_path: str = None, text: str = None):
		#not tested (may be incorrect)

		data = FormData()
		file_name = os.path.basename(file_path)
		if file_path:
			file_name = os.path.basename(file_path)
			data.add_field('files[0]', open(file_path, 'rb'), filename=file_name)
		if text:
			data.add_field('hometask_text', hometask_text)
		if text is None and file_path is None:raise Exception("Wrong type")
		
		data.add_field('student_id', str(self.student.studentId))
		data.add_field('hometask_id', str(hometaskId))

		return objects.UploadHometask(
			await helpers.post(f"{self.api}/schedule/student-answer", headers=self.headers(access_token=self.student.accessToken, data=data), data=data)
		)

		
	



