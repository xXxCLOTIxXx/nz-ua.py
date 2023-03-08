from aiohttp import ClientSession, ContentTypeError
from .exceptions import callException, UnknownError


class HttpClient:
    def __init__(
        self, /, headers: dict | None = None, base_url: str | None = None
    ) -> None:
        self.headers: dict = {
            "Content-Type": "application/json",
            "User-Agent": "IRC RESTClient",
            "Accept-Charset": "utf-8, *;q=0.8",
            "Host": "api-mobile.nz.ua",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
        }
        if headers:
            self.headers.update(headers)
        self.base_url = base_url
        self._session = None

    @property
    def token(self):
        self.headers.get("Authorization")

    @token.setter
    def token(self, token):
        self.headers.update({"Authorization": token})

    @property
    def session(self):
        if not self._session:
            self._session = ClientSession(self.base_url)
        return self._session

    async def close(self):
        if self._session:
            await self._session.close()

    async def post(self, url: str, data: dict | None = None):
        async with self.session.post(url, headers=self.headers, json=data) as response:
            try:
                json = await response.json()
            except ContentTypeError:
                raise UnknownError(await response.text())
            if response.status != 200:
                callException(json)
            return json
