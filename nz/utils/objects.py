#thanks for improving objects.py -> https://github.com/GoldMasterPro

__all__ = ['Student', 'Schedule', 'Hometask', 'Timetable', 'StudentPerformance', 'LessonPerformance', 'LoadHometask']


class Student:
	def __init__(self, data: dict = {}):
		self.json = data
		self.accessToken = self.json.get('access_token', None)
		self.refreshToken = self.json.get('refresh_token', None)
		self.emailHash = self.json.get('email_hash', None)
		self.studentId = self.json.get('student_id', None)
		self.fio = self.json.get('FIO', None)
		self.avatar = self.json.get('avatar', None)
		self.permissions = self.json.get('permissions', None)
		self.error_message = self.json.get('error_message', None)


class Schedule:
	def __init__(self, data: dict = {}):
		self.json = data
		self.days = list()
		self.error_message = self.json.get('error_message', None)
		for date in self.json.get('dates', []):
			self.days.append(self.Day(date))


	class Day:
		def __init__(self, data: dict = {}):
			self.json = data
			self.date = self.json.get('date', None)
			self.lessons = list()
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

				self.lessonName = subject.get('subject_name', None)
				self.room = subject.get('room', None)
				self.HometaskId = subject.get('distance_hometask_id', None)
				self.Hometask_isClosed = subject.get('distance_hometask_is_closed', None)
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
		self.isClosed = self.json.get('is_closed', None)
		self.error_message = self.json.get('error_message', None)
		self.hometaskFiles = list()
		self.answerFiles = list()

		for file in self.json.get('hometask_files', []):
			self.hometaskFiles.append(self.File(file))

		for file in self.json.get('answer_files', []):
			self.answerFiles.append(self.File(file))


	class File:
		def __init__(self, data: dict = {}):
			self.json = data
			self.fileId = self.json.get('id', None)
			self.fileName = self.json.get('name', None)
			self.url = self.json.get('url', None)
			self.size = self.json.get('size', None)
			self.createTime = self.json.get('created_at', None)



#new objects
class Timetable:
	def __init__(self, data: dict = {}):
		self.json = data
		self.error_message = self.json.get('error_message', None)
		self.dates = list()
		for date in self.json.get('dates', []):
			self.dates.append(self.Dates(date))

	class Dates:
		def __init__(self, data: dict = {}):
			self.json = data
			self.date = self.json.get('date', None)
			self.lessons = list()

			for lesson in self.json.get('calls', []):
				self.lessons.append(self.Lesson(lesson))

		class Lesson:
			def __init__(self, data: dict = {}):
				self.json = data
				self.lessonId = self.json.get('call_id', None)
				self.lessonNumber = self.json.get('call_number', None)
				self.lessonStrat = self.json.get('time_start', None)
				self.lessonEnd = self.json.get('time_end', None)
				self.subjects = list()
				for subject in self.json.get('subjects', []):
					self.subjects.append(self.Subjects(subject))

			class Subjects:
				def __init__(self, data: dict = {}):
					self.json = data
					teacher = self.json.get('teacher', {})

					self.lessonName = self.json.get('subject_name', None)
					self.room  =self.json.get('room', None)
					self.teacherId = teacher.get('id', None)
					self.teacherName = teacher.get('name', None)







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
		self.missedLessons = self.json.get('number_missed_lessons', None)
		self.lessons = self.json.get('lessons', None)
		self.error_message = self.json.get('error_message', None)

class LoadHometask:
	def __init__(self, data: dict = {}):
		self.json = data
		self.error_message = self.json.get('error_message', None)
		self.answer = self.json.get('answer', None)
		self.files = list()
		for file in self.json.get('answer_files', []):
			self.files.append(Files(file))

	class Files:
		def __init__(self, data: dict = {}):
			self.json = data
			self.fileId = self.json.get('id', None)
			self.fileName =self.json.get('name', None)