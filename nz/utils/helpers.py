import aiohttp
from . import exceptions, objects
from json import loads
from datetime import datetime

mounth_days = {
	1: 31,
	2: 28,
	3: 31,
	4: 30,
	5: 31,
	6: 30,
	7: 31,
	8: 31,
	9: 30,
	10: 31,
	11: 30,
	12: 31,
}


def get_mounth():
	start = str(datetime.today().replace(day=1)).split(' ')[0]
	mounth_now = start.split('-')[1]
	end =  str(datetime.today().replace(day=mounth_days[int(mounth_now)])).split(' ')[0]
	return {'start': start, 'end': end}


async def post(url: str, headers, data = None):
	async with aiohttp.ClientSession() as session:
		async with session.post(url, headers=headers, data=data) as response:
			return exceptions.CheckException(await response.text()) if response.status != 200 else loads(await response.text())