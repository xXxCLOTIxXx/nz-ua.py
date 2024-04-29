#some types of variables may not match (I no longer remember what type of some keys)

__all__ = ['Student', 'Schedule', 'Hometask', 'Timetable', 'StudentPerformance', 'LessonPerformance', 'UploadHometask']


class Student:
	__slots__ = (
			"json", "accessToken", "refreshToken", "emailHash", "studentId",
			"fio", "avatar", "permissions", "error_message"
		)

	def __init__(self, data: dict = {}):
		self.json: dict = data
		self.accessToken: str = self.json.get('access_token')
		self.refreshToken: str = self.json.get('refresh_token')
		self.emailHash: str = self.json.get('email_hash')
		self.studentId: int = self.json.get('student_id')
		self.fio: str = self.json.get('FIO')
		self.avatar: str = self.json.get('avatar')
		self.permissions: str = self.json.get('permissions')
		self.error_message: str = self.json.get('error_message')


class Schedule:
	__slots__ = (
			"json", "days", "error_message"
		)
	def __init__(self, data: dict = {}):
		self.json: dict = data
		self.days: list = list()
		self.error_message: str = self.json.get('error_message')
		for date in self.json.get('dates', []):
			self.days.append(self.Day(date))


	class Day:
		__slots__ = (
				"json", "date", "lessons"
			)
		def __init__(self, data: dict = {}):
			self.json: dict = data
			self.date: str = self.json.get('date')
			self.lessons: list = list()
			for call in self.json.get('calls', []):
				self.lessons.append(self.Lesson(call))


		class Lesson:
			__slots__ = (
					"json", "callId", "number", "lessonName",
					"room", "HometaskId", "Hometask_isClosed",
					"hometask", "type", "mark", "comment"

			)
			def __init__(self, data: dict = {}):
				self.json: dict = data
				self.callId: str = self.json.get('call_id')
				self.number: int = self.json.get('call_number')

				subjects: list = self.json.get('subjects', [])
				subject: dict = subjects[0] if subjects else {}

				self.lessonName: str = subject.get('subject_name')
				self.room: str = subject.get('room')
				self.HometaskId: int = subject.get('distance_hometask_id')
				self.Hometask_isClosed: bool = subject.get('distance_hometask_is_closed')
				self.hometask: list = subject.get('hometask')

				lesson = subject.get('lesson', [])
				lesson = lesson[0] if lesson else {}

				self.type: str = lesson.get('type')
				self.mark: str = lesson.get('mark')
				self.comment: str = lesson.get('comment')


class Hometask:
	__slots__ = (
		"json", "hometask", "answer", "answerFiles"
		"isClosed", "error_message", "hometaskFiles"
	)
	def __init__(self, data: dict = {}):
		self.json: dict = data
		self.hometask: str = self.json.get('hometask')
		self.answer: str = self.json.get('answer')
		self.isClosed: bool = self.json.get('is_closed')
		self.error_message: str = self.json.get('error_message')
		self.hometaskFiles: list = list()
		self.answerFiles: list = list()

		for file in self.json.get('hometask_files', []):
			self.hometaskFiles.append(self.File(file))

		for file in self.json.get('answer_files', []):
			self.answerFiles.append(self.File(file))


	class File:
		__slots__ = (
			"json", "fileId", "fileName", "url"
			"size", "createTime"
		)
		def __init__(self, data: dict = {}):
			self.json: dict = data
			self.fileId: int = self.json.get('id')
			self.fileName: str = self.json.get('name')
			self.url: str = self.json.get('url')
			self.size: str = self.json.get('size')
			self.createTime: str = self.json.get('created_at')




class Timetable:
	__slots__ = (
		"json", "dates", "error_message"
	)

	def __init__(self, data: dict = {}):
		self.json: dict = data
		self.error_message: str = self.json.get('error_message')
		self.dates: list = list()
		for date in self.json.get('dates', []):
			self.dates.append(self.Dates(date))

	class Dates:
		__slots__ = (
			"json", "date", "lessons"
		)

		def __init__(self, data: dict = {}):
			self.json: dict = data
			self.date: str = self.json.get('date')
			self.lessons: list = list()

			for lesson in self.json.get('calls', []):
				self.lessons.append(self.Lesson(lesson))

		class Lesson:
			__slots__ = (
				"json", "lessonId", "lessonNumber",
				"lessonStrat", "lessonEnd", "subjects"
			)
			def __init__(self, data: dict = {}):
				self.json: dict = data
				self.lessonId: int = self.json.get('call_id')
				self.lessonNumber: int = self.json.get('call_number')
				self.lessonStrat: str = self.json.get('time_start')
				self.lessonEnd: str = self.json.get('time_end')
				self.subjects: list = list()
				for subject in self.json.get('subjects', []):
					self.subjects.append(self.Subjects(subject))

			class Subjects:
				__slots__ = (
					"json", "lessonName", "room",
					"teacherId", "teacherName"
				)
				def __init__(self, data: dict = {}):
					self.json: dict = data
					teacher: dict = self.json.get('teacher', {})

					self.lessonName: str = self.json.get('subject_name')
					self.room: str  = self.json.get('room')
					self.teacherId: int = teacher.get('id')
					self.teacherName: str = teacher.get('name')


class StudentPerformance:
	__slots__ = (
		"json", "missedDays", "missedLessons", "error_message",
		"subjects"
	)

	def __init__(self, data: dict = {}):
		self.json: dict = data

		missed: dict = self.json.get('missed', {})

		self.missedDays: int = missed.get('days')
		self.missedLessons: int = missed.get('lessons')
		self.error_message: str = self.json.get('error_message')
		self.subjects: list = list()
		for subject in self.json.get('subjects', []):
			self.subjects.append(self.Subjects(subject))

	class Subjects:
		__slots__ = (
			"json", "subjectId", "subjectName", "marks"
		)
		def __init__(self, data: dict = {}):
			self.json: dict = data
			self.subjectId: int = data.get('subject_id')
			self.subjectName: str = data.get('subject_name')
			self.marks: list = data.get('marks', [])


class LessonPerformance:
	__slots__ = (
		"json", "missedLessons", "lessons", "error_message"
	)

	def __init__(self, data: dict = {}):
		self.json: dict = data
		self.missedLessons: int = self.json.get('number_missed_lessons')
		self.lessons: list = self.json.get('lessons')
		self.error_message: str = self.json.get('error_message')

class UploadHometask:
	__slots__ = (
		"json", "error_message", "answer", "files"
	)

	def __init__(self, data: dict = {}):
		self.json: dict = data
		self.error_message: str = self.json.get('error_message')
		self.answer: str = self.json.get('answer')
		self.files: list = list()
		for file in self.json.get('answer_files', []):
			self.files.append(self.Files(file))

	class Files:
		__slots__ = (
			"json", "fileId", "fileName"
		)

		def __init__(self, data: dict = {}):
			self.json: dict = data
			self.fileId: int = self.json.get('id')
			self.fileName: str =self.json.get('name')