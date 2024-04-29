from json import loads

class UnknownError(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)

class IncorrectPassword(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)


class IncorrectNickname(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)

class Unauthorized(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)

class InternalServerError(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)


class NotFoundError(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)


class HometaskNotFoundError(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)


errors = {
}

status_errors = {
	500: InternalServerError,
	404: NotFoundError,
	401: Unauthorized
}

ems = {
	'введено невірний логін або пароль.': IncorrectPassword,
	'користувач не знайдений.': IncorrectNickname,
	'завдання не знайдене': HometaskNotFoundError
}

def CheckException(data):
	try:
		data = loads(data)
		code = data.get("code")
		status = data.get("status")
		em = data.get("error_message", '').lower()
	except:
		raise UnknownError(data)
	if status in status_errors: raise status_errors[status](data)
	elif code in errors: raise errors[code](data)
	elif em in ems: raise ems[em](data)
	else:raise UnknownError(data)