def roman(a: int, b: int) -> str:
    """
    Converts the given Arabic numbers to Roman numerals.

    Args:
        a (int): The first Arabic number.
        b (int): The second Arabic number.

    Returns:
        str: The Roman numeral representation of
            the sum of the two Arabic numbers.
    """
    roman_map = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }
    roman_numbers = []

    for number in [a, b, a + b]:
        temp_roman_number = ""
        for arabic, roman in roman_map.items():
            count = number // arabic
            if count:
                temp_roman_number += roman * count
                number -= arabic * count
        roman_numbers.append(temp_roman_number)

    return "{} + {} = {}".format(*roman_numbers)
