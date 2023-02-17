import aiohttp
from . import exceptions, objects
from json import loads

async def post(url: str, headers, data = None):
	async with aiohttp.ClientSession() as session:
		async with session.post(url, headers=headers, data=data) as response:
			return exceptions.CheckException(await response.text()) if response.status != 200 else loads(await response.text())