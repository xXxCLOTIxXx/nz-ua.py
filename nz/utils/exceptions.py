__all__ = [
    "UnknownError",
    "IncorrectPassword",
    "IncorrectNickname",
    "Unauthorized",
    "callException",
]


class UnknownError(Exception):
    pass


class IncorrectPassword(Exception):
    pass


class IncorrectNickname(Exception):
    pass


class Unauthorized(Exception):
    pass


errors = {
    "Введено невірний логін або пароль.": IncorrectPassword,
    "Користувач не знайдений.": IncorrectNickname,
    0: Unauthorized,
}


def callException(json: dict):
    try:
        code = json["error_message"]
    except Exception:
        raise UnknownError(json)
    if code in errors:
        raise errors[code](code)
    else:
        raise UnknownError(json)
