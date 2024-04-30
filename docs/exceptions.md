[« main](main.md)
## Using:

```python
import nz
import asyncio
client = nz.Client()

async def main():
	try:
		info = await client.login('user_name', 'password')
		print(info.json)
	except nz.exceptions.IncorrectPassword:
		print("password error")


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(loop.create_task(main()))

```

## All types of exceptions
```python
from nz import exceptions
exceptions.UnknownError
exceptions.IncorrectPassword
exceptions.IncorrectNickname
exceptions.Unauthorized
exceptions.InternalServerError
exceptions.NotFoundError
exceptions.HometaskNotFoundError
```
