# nz-ua.py
Unofficial library for the homework site "[nz.ua](https://nz.ua/)"

# What can this wrapper do?
Using this library you can view additional tasks, upload answers, view lessons and other site functions in the python programming language.

## How to install
- you can install the library on [pypi](https://pypi.org/project/nz-ua.python/)
- [this](https://pypi.org/project/nz-ua.py/) library is no longer updated because access to the account was lost, try this [pypi](https://pypi.org/project/nz-ua.python/)
```
pip install nz-ua.python
```
- or on the project's [github](https://github.com/xXxCLOTIxXx/nz-ua.py)
```
pip install git+https://github.com/xXxCLOTIxXx/nz-ua.py.git
```

## Quick Links
- Client ([CLICK](#client))
- Client functions ([CLICK](client_functions.md))
- Objects ([CLICK](objects.md))
- Error Handlers ([CLICK](exceptions.md))


# Client
```python
client = nz.Client()
```
## Import and use
```python
import nz
import asyncio
client = nz.Client()

async def main():
	info = await client.login('user_name', 'password')
	print(info.json)


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(loop.create_task(main()))
```

## Client args
objects.Student - class containing data after authorization.
```python
import nz
client = nz.Client(
  profile: nz.objects.Student = None
)
student_object = client.student
```

[Client functions](client_functions.md)
