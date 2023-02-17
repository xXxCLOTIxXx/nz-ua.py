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


errors = {
	'Введено невірний логін або пароль.': IncorrectPassword,
	'Користувач не знайдений.': IncorrectNickname,
	0:Unauthorized,
}

def CheckException(data):
	try:
		data = loads(data)
		try:code = data['code']
		except KeyError:
			code = data['error_message']
	except:
		raise UnknownError(data)
	if code in errors: raise errors[code](data)
	else:raise UnknownError(data)