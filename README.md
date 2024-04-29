<body>
	<p align="center">
	    <a href="https://github.com/xXxCLOTIxXx/nz-ua.py/releases"><img src="https://img.shields.io/github/release/xXxCLOTIxXx/nz-ua.py.svg" alt="GitHub release" />
	    <a href="https://github.com/xXxCLOTIxXx/nz-ua.py/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="licence" /></a>
	    <a href="https://pypi.org/project/nz-ua.python/"><img src="https://img.shields.io/pypi/v/nz-ua.python" alt="pypi" /></a>
	    <a href="https://github.com/xXxCLOTIxXx/nz-ua.py/blob/dev/docs/main.md"><img src="https://img.shields.io/website?down_message=failing&label=docs&up_color=green&up_message=passing&url=https://github.com/xXxCLOTIxXx/nz-ua.py/blob/dev/docs/main.md" alt="docs" /></a>
	</p>
	<table align="center">
		</tr>
		<tr> <th colspan="3">More info</th> </tr>
		<tr>
			<td>
				<a href="https://t.me/DxsarzUnion"><img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" height="30px">
				 Telegram Channel</a>
			</td>
			<td>
				<a href="https://www.youtube.com/channel/UCNKEgQmAvt6dD7jeMLpte9Q"><img src="https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg" height="30px">
				 YouTube channel</a>
			</td>
			<td>
				<a href="https://discord.gg/GtpUnsHHT4"><img src="https://www.svgrepo.com/show/353655/discord-icon.svg" height="30px">
				 Discord Server</a>
			</td>
		</tr>
	</table>
<h1 align="center">nz-ua.py</h1>
<p align="center">Library for working with nz ua servers</p>
<h1 align="center">Login example</h1>

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

</body>
