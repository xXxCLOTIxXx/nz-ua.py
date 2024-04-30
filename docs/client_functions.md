[« main](main.md)

# `login`
- login to account
### `syntax`
```python
await client.login("nick", "password)
```
### `args`
```python
username: str #account nick
password: str #account password
```
### `return`
```python
objects.Student
```
---
# `logout`
- log out of your account
### `syntax`
```python
await client.logout()
```
### `return`
```python
objects.Student
```
---
# `get_schedule`
- get schedule
### `syntax`
```python
await client.get_schedule()
```
### `args`
```python
start_date: str = None #schedule start date
end_date: str = None #schedule end date
```
### `return`
```python
objects.Schedule
```
---
# `get_hometask`
- get hometask
### `syntax`
```python
await client.get_hometask(1234567)
```
### `args`
```python
hometaskId: int #id of your hometask
```
### `return`
```python
objects.Hometask
```
---
# `get_timetable`
- get timetable
### `syntax`
```python
await client.get_timetable()
```
### `args`
```python
start_date: str = None #start date
end_date: str = None #end date
```
### `return`
```python
objects.Timetable
```
---
# `get_student_performance`
- get student performance
### `syntax`
```python
await client.get_student_performance()
```
### `args`
```python
start_date: str = None #start date
end_date: str = None #end date
```
### `return`
```python
objects.StudentPerformance
```
---
# `get_subject_performance`
- get subject performance
### `syntax`
```python
await client.get_subject_performance(123546456)
```
### `args`
```python
subjectId: int #id of subject
start_date: str = None #start date
end_date: str = None #end date
```
### `return`
```python
objects.LessonPerformance
```
---
# `delete_hometask_file`
- delete hometask file
### `syntax`
```python
await client.delete_hometask_file(536464)
```
### `args`
```python
fileId: int #id of hometask file
```
### `return`
```python
dict
```
---
# `hometask_text_answer`
- upload text answer for hometask
### `syntax`
```python
await client.hometask_text_answer(hometaskId=536464, text="hello")
```
### `args`
```python
hometaskId: int #id of hometask
text: str = None #text for answer
deleteFilesIdList: list = None #list of ID files to delete
```
### `return`
```python
objects.UploadHometask
```
