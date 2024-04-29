

class Headers:
	
	def headers(self, data = None, access_token: str = None, contentType: str = 'application/json') -> dict:

		headers = {
		'Content-Type': contentType,
		'User-Agent': 'IRC RESTClient',
		'Accept-Charset': 'utf-8, *;q=0.8',
		'Host': 'api-mobile.nz.ua',
		'Connection': 'Keep-Alive',
		'Accept-Encoding': 'gzip',
		}

		if data:headers['Content-Length'] = str(len(data))
		if access_token: headers['Authorization'] = f'Bearer {access_token}'


		return headers