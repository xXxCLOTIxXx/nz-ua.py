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


def callException(json):
    try:
        code = json["error_message"]
    except (TypeError, KeyError):
        raise UnknownError(json)
    if code in errors:
        raise errors[code](json)
    else:
        raise UnknownError(json)
