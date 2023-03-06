from json import loads


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


def callException(data: str):
    try:
        if data.find("Enable JavaScript and cookies to continue") != -1:
            raise Unauthorized(data)
        json = loads(data)
        code = json["error_message"]
    except Exception:
        raise UnknownError(data)
    if code in errors:
        raise errors[code](code)
    else:
        raise UnknownError(data)
