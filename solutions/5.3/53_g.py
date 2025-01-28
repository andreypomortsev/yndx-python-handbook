class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError

    for char in name:
        char_index = ord(char)
        # Compare with the ASCII table is fastest way to check
        # if a character is Cyrillic
        if not (1040 <= char_index <= 1105 or char_index == 1025):
            raise CyrillicError

    if name != name.capitalize():
        raise CapitalError

    return name
