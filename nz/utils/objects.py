#thanks for improving objects.py -> https://github.com/GoldMasterPro

__all__ = ['Student', 'Schedule', 'Hometask', 'Timetable', 'StudentPerformance', 'LessonPerformance']


class Student:
	def __init__(self, data: dict = {}):
		self.json = data
		self.access_token = self.json.get('access_token', None)
		self.refresh_token = self.json.get('refresh_token', None)
		self.email_hash = self.json.get('email_hash', None)
		self.student_id = self.json.get('student_id', None)
		self.fio = self.json.get('FIO', None)
		self.avatar = self.json.get('avatar', None)
		self.permissions = self.json.get('permissions', None)
		self.error_message = self.json.get('error_message', None)


class Schedule:
	def __init__(self, data: dict = {}):
		self.json = data
		self.days = []
		self.error_message = self.json.get('error_message', None)
		for date in self.json.get('dates', []):
			self.days.append(self.Day(date))


	class Day:
		def __init__(self, data: dict = {}):
			self.json = data
			self.date = self.json.get('date', None)
			self.lessons = []
			for call in self.json.get('calls', []):
				self.lessons.append(self.Lesson(call))
			self.schoolSubjects = self.lessons # Обратная совместимость


		class Lesson:
			def __init__(self, data: dict = {}):
				self.json = data
				self.callId = self.json.get('call_id', None)
				self.number = self.json.get('call_number', None)

				subjects = self.json.get('subjects', [])
				subject = subjects[0] if subjects else {}

				self.subject_name = subject.get('subject_name', None)
				self.room = subject.get('room', None)
				self.distance_hometask_id = subject.get('distance_hometask_id', None)
				self.distance_hometask_is_closed = subject.get('distance_hometask_is_closed', None)
				self.hometask: list = subject.get('hometask', None)

				lesson = subject.get('lesson', [])
				lesson = lesson[0] if lesson else {}

				self.type = lesson.get('type', None)
				self.mark = lesson.get('mark', None)
				self.comment = lesson.get('comment', None)


class Hometask:
	def __init__(self, data: dict = {}):
		self.json = data
		self.hometask = self.json.get('hometask', None)
		self.answer = self.json.get('answer', None)
		self.answer_files = self.json.get('answer_files', None)
		self.is_closed = self.json.get('is_closed', None)
		self.error_message = self.json.get('error_message', None)


#new objects
class Timetable:
	def __init__(self, data: dict = {}):
		self.json = data
		#TODO THIS




class StudentPerformance:
	def __init__(self, data: dict = {}):
		self.json = data

		missed = self.json.get('missed', None)

		self.missedDays = missed.get('days', None)
		self.missedLessons = missed.get('lessons', None)
		self.error_message = self.json.get('error_message', None)
		self.subjects = list()
		for subject in self.json.get('subjects', []):
			self.subjects.append(self.Subjects(subject))

	class Subjects:
		def __init__(self, data: dict = {}):
			self.subjectId = data.get('subject_id', None)
			self.subjectName = data.get('subject_name', None)
			self.marks = data.get('marks', [])




class LessonPerformance:
	def __init__(self, data: dict = {}):
		self.json = data
		#TODO THIS