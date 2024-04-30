- [« main](main.md)
- [« functions](client_functions.md)

# `Student`
### `Attributes`
```python
from nz import objects
Student = objects.Student()

Student.json: dict
Student.accessToken: str
Student.refreshToken: str
Student.emailHash: str
Student.studentId: int
Student.fio: str
Student.avatar: str
Student.permissions: str
Student.error_message: str
```
#
# `Schedule`
### `Attributes`
```python
from nz import objects
Schedule = objects.Schedule()

Schedule.json: dict
Schedule.days: list #Day
Schedule.error_message: str

Schedule.days[0]: objects.Schedule.Day

Schedule.Day.json: dict
Schedule.Day.date: str
Schedule.Day.lessons: list #Lesson

Schedule.days[0]lessons[0]: objects.Schedule.Day.Lesson

Schedule.Day.Lesson.json: dict
Schedule.Day.Lesson.callId: int
Schedule.Day.Lesson.number: int
Schedule.Day.Lesson.lessonName: str
Schedule.Day.Lesson.room: str
Schedule.Day.Lesson.HometaskId: int
Schedule.Day.Lesson.Hometask_isClosed: bool
Schedule.Day.Lesson.hometask: str
Schedule.Day.Lesson.type: str
Schedule.Day.Lesson.mark: str
Schedule.Day.Lesson.comment: str
```
#
# `Hometask`
### `Attributes`
```python
from nz import objects
Hometask = objects.Hometask()

Hometask.json: dict
Hometask.hometask: str
Hometask.answer: str
Hometask.isClosed: bool
Hometask.error_message: str
Hometask.hometaskFiles: list #File
Hometask.answerFiles: list #File

Hometask.hometaskFiles[0]: objects.Hometask.File
Hometask.answerFiles[0]: objects.Hometask.File

Hometask.File.json: dict
Hometask.File.fileId: int
Hometask.File.fileName: str
Hometask.File.url: str
Hometask.File.size: str
Hometask.File.createTime: str
```
#
# `UploadHometask`
### `Attributes`
```python
from nz import objects
LessonPerformance = objects.LessonPerformance()

LessonPerformance.json: dict
LessonPerformance.missedLessons: int
LessonPerformance.lessons: list
LessonPerformance.error_message: str
```
#
# `UploadHometask`
### `Attributes`
```python
from nz import objects
UploadHometask = objects.UploadHometask()

UploadHometask.json: dict
UploadHometask.error_message: str
UploadHometask.answer: str
UploadHometask.files: list #Files

UploadHometask.files[0]: objects.UploadHometask.Files

UploadHometask.Files.json: dict
UploadHometask.Files.fileId: int
UploadHometask.Files.fileName: str
```
#
