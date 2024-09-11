from typing import Union


def month(number: Union[int, str], lang: str = "ru") -> str:
    months = {
        "1": {"en": "January", "ru": "Январь"},
        "2": {"en": "February", "ru": "Февраль"},
        "3": {"en": "March", "ru": "Март"},
        "4": {"en": "April", "ru": "Апрель"},
        "5": {"en": "May", "ru": "Май"},
        "6": {"en": "June", "ru": "Июнь"},
        "7": {"en": "July", "ru": "Июль"},
        "8": {"en": "August", "ru": "Август"},
        "9": {"en": "September", "ru": "Сентябрь"},
        "10": {"en": "October", "ru": "Октябрь"},
        "11": {"en": "November", "ru": "Ноябрь"},
        "12": {"en": "December", "ru": "Декабрь"},
    }
    return months.get(str(number), {}).get(lang, "")
