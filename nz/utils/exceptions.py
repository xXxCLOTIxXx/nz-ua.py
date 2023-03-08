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
    "Your request was made with invalid credentials.": Unauthorized,
}


def callException(json: dict):
    try:
        if "message" in json:
            code = json["message"]
        else:
            code = json["error_message"]
    except Exception:
        raise UnknownError(json)
    if code in errors:
        raise errors[code](code)
    else:
        raise UnknownError(json)
