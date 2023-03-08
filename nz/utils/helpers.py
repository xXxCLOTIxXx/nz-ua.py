import aiohttp
from . import exceptions
from json import loads
from datetime import datetime, date

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

def get_week():
	dt = str(datetime.today()).split(' ')[0].split('-')
	year = int(dt[0])
	mounth = int(dt[1])
	day = int(dt[2])
	weekDay = date(year, mounth, day).isocalendar()[2]

	#start 
	startDay = day-weekDay
	startMounth = mounth
	startYear = year
	if startDay <=0:
		startMounth=startMounth-1
		if startMounth <=0:
			startYear=startYear-1
			startMounth=12
		md = mounth_days.get(startMounth)
		startDay = md - abs(startDay)


	if startDay <10:
		startDay = f'0{startDay}'
	if startMounth <10:
		startMounth = f'0{startMounth}'

	#end
	leftDays = 7 - weekDay
	endDay = day+leftDays
	endMounth = mounth
	endYear = year
	if endDay > mounth_days.get(endMounth):
		endDay = endDay - mounth_days.get(endMounth)
		endMounth=endMounth+1
		if endMounth > 12:
			endYear=endYear+1
			endMounth=1


	if endDay <10:
		endDay = f'0{endDay}'
	if endMounth <10:
		endMounth = f'0{endMounth}'

	return {'start': f'{startYear}-{startMounth}-{startDay}', 'end': f'{endYear}-{endMounth}-{endDay}'}
