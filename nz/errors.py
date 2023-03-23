__all__ = (
    "IncorrectNickname",
    "IncorrectPassword",

    "HometaskNotFound",
    "HometaskFileNotFound",

    "ServiceUnavailable",
    "ConnectionTimedOut",
    "Unauthorized",
    "InternalServerError",

    "UnknownError",
)


class IncorrectNickname(Exception):
    pass


class IncorrectPassword(Exception):
    pass


class HometaskFileNotFound(Exception):
    pass


class HometaskNotFound(Exception):
    pass


class ServiceUnavailable(Exception):
    def __init__(self) -> None:
        super().__init__("No server is available to handle this request.")


class ConnectionTimedOut(Exception):
    pass


class Unauthorized(Exception):
    def __init__(self) -> None:
        super().__init__("Your request was made with invalid credentials. You need to call the login method.")


class InternalServerError(Exception):
    pass


class UnknownError(Exception):
    pass
