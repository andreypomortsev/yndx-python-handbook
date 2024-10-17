import string
from hashlib import sha256
from typing import Callable


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(
    p_word: str,
    min_length: int = 8,
    possible_chars: str = None,
    at_least_one: Callable[[str], bool] = str.isdigit,
) -> str:
    if not isinstance(p_word, str):
        raise TypeError

    if not possible_chars:
        possible_chars = set(string.ascii_letters + string.digits)

    if len(p_word) < min_length:
        raise MinLengthError

    if not all(map(lambda x: x in possible_chars, p_word)):
        raise PossibleCharError

    if not any(map(at_least_one, p_word)):
        raise NeedCharError

    return sha256(p_word.encode("utf-8")).hexdigest()
