from aiohttp import ClientSession, ClientConnectorError

from .errors import (
    ServiceUnavailable,
    ConnectionTimedOut,
    Unauthorized,
    InternalServerError,
    UnknownError,
)


class HttpClient:
    def __init__(
        self,
        /,
        token: str | None = None,
        headers: dict = {},
        base_url: str | None = None,
    ) -> None:
        self.headers: dict = {
            "Content-Type": "application/json",
            "User-Agent": "IRC RESTClient",
            "Accept-Charset": "utf-8, *;q=0.8",
            "Host": "api-mobile.nz.ua",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
        }
        self.base_url = base_url or "https://api-mobile.nz.ua"
        self.headers.update(headers)
        self.token = token
        self._client_session = None

    @property
    def token(self):
        self.headers.get("Authorization")

    @token.setter
    def token(self, token):
        if token is not None:
            self.headers.update({"Authorization": f"Bearer {token}"})

    @property
    def _session(self):
        if not self._client_session:
            self._client_session = ClientSession(self.base_url)
        return self._client_session

    async def post(self, url: str, data: dict | None = None):
        try:
            async with self._session.post(
                url, headers=self.headers, json=data
            ) as response:
                match response.status:
                    case 200:
                        return await response.json()
                    case 401:
                        raise Unauthorized
                    case 500:
                        json: dict = await response.json()
                        if json.get("name") == "Internal Server Error":
                            raise InternalServerError
                        return json
                    case 503:
                        raise ServiceUnavailable
                    case 522:
                        raise ConnectionTimedOut
                    case _:
                        raise UnknownError(await response.text())
        except ClientConnectorError as error:
            if error.errno == 22:
                raise ConnectionTimedOut
            raise error

    async def close(self):
        if self._session:
            await self._session.close()
