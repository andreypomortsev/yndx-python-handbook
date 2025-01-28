class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError

    # We can use regex for this, but let's do it manually
    for char in name:
        char_index = ord(char.lower())
        if not (
            48 <= char_index <= 57  # 0-9
            or 97 <= char_index <= 122  # a-z
            or char_index == 95  # _
        ):
            raise BadCharacterError

    if name[0].isdigit():
        raise StartsWithDigitError

    return name
