

class Student:
	def __init__(self, data = None):
		self.json = data
		try:self.access_token = self.json['access_token']
		except:self.access_token = None
		try:self.refresh_token = self.json['refresh_token']
		except:self.refresh_token = None
		try:self.email_hash = self.json['email_hash']
		except:self.email_hash = None
		try:self.student_id = self.json['student_id']
		except:self.student_id = None
		try:self.fio = self.json['FIO']
		except:self.fio = None
		try:self.avatar = self.json['avatar']
		except:self.avatar = None
		try:self.permissions = self.json['permissions']
		except:self.permissions = None
		try:self.error_message = self.json['error_message']
		except:self.error_message = None



class Schedule:
	def __init__(self, data = None):
		self.json = data
		self.days = []
		try:self.error_message = self.json['error_message']
		except:self.error_message = None
		try:
			for dt in self.json['dates']:
				self.days.append(self.Day(dt))
		except:
			pass


	class Day:
		def __init__(self, data):
			self.json = data
			try:self.date = self.json['date']
			except:self.date = None
			self.schoolSubjects = []
			try:
				for schoolSubject in self.json['calls']:
					self.schoolSubjects.append(self.SchoolSubject(schoolSubject))
			except:
				pass


		class SchoolSubject:
			def __init__(self, data):
				self.json = data
				try:self.subjects = self.json['subjects']
				except:self.subjects = None
				try:self.subject_name = self.subjects[0]['subject_name']
				except:self.subject_name = None
				try:self.room = self.subjects[0]['room']
				except:self.room = None
				try:self.call_id = self.json['call_id']
				except:self.call_id = None
				try:self.number = self.json['call_number']
				except:self.number = None
				try:self.hometask = self.subjects[0]['hometask']
				except:self.hometask = None
				try:self.distance_hometask_id = self.subjects[0]['distance_hometask_id']
				except:self.distance_hometask_id = None
				try:self.distance_hometask_is_closed = self.subjects[0]['distance_hometask_is_closed']
				except:self.distance_hometask_is_closed = None



class Hometask:
	def __init__(self, data):
		self.json = data
		try:self.hometask = self.json['hometask']
		except:self.hometask = None
		try:self.answer = self.json['answer']
		except:self.answer = None
		try:self.answer_files = self.json['answer_files']
		except:self.answer_files = None
		try:self.is_closed = self.json['is_closed']
		except:self.is_closed = None
		try:self.error_message = self.json['error_message']
		except:self.error_message = None
