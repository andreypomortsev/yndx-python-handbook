class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def all_cyrillic(word: str) -> bool:
    for char in word:
        char_index = ord(char)
        if not (1040 <= char_index <= 1105 or char_index == 1025):
            return False
    return True


# fmt: off
def all_chars_good(word: str) -> bool:
    if not word:
        return False

    # We can regex with pattren r"^[a-zA-Z0-9_]+$"
    # But let's do it manually
    for char in word:
        char_index = ord(char.lower())
        if not (
            48 <= char_index <= 57      # 0-9
            or 97 <= char_index <= 122  # a-z
            or char_index == 95         # _
        ):
            return False
    return True
# fmt: on


def user_validation(**details) -> dict:
    blueprint = ("last_name", "first_name", "username")

    if tuple(details.keys()) != blueprint:
        raise KeyError

    for key, value in details.items():
        if not isinstance(value, str):
            raise TypeError

        if key == "username":
            if not all_chars_good(value):
                raise BadCharacterError

            if value[0].isdigit():
                raise StartsWithDigitError

        if key in {"last_name", "first_name"}:
            if not all_cyrillic(value):
                raise CyrillicError

            if value != value.capitalize():
                raise CapitalError

    return details
