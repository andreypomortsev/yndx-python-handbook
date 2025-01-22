import string

from tests.data.test_data_41 import j_test_data as merge


def get_value_error() -> None:
    """
    A test function for the problem A 5.3

    Raises: ValueError
    """
    x = int("Hello, world!")


def get_type_error() -> None:
    """
    A test function for the problem A 5.3

    Raises: TypeError
    """
    x = "2" + 2


def get_system_error() -> None:
    """
    A test function for the problem A 5.3

    Raises: SystemError
    """
    raise SystemError


def get_no_errors() -> None:
    """
    A test function for the problem A 5.3

    Does nothing
    """
    return


a_test_data = [
    (get_value_error, "ValueError\n", "first open test"),
    (get_type_error, "TypeError\n", "second open test"),
    (get_system_error, "SystemError\n", "system error"),
    (get_no_errors, "No Exceptions\n", "no errors"),
]


def get_sum(a, b) -> int | float | str:
    """
    A test function for the problem B 5.3

    Returns: sum of two args
    """
    return a + b


def get_prod(a, b) -> int | float | str:
    """
    A test function for the problem B 5.3

    Returns: product of two args
    """
    return a * b


def get_sub(a, b) -> int | float:
    """
    A test function for the problem B 5.3

    Returns: subtraction of two args
    """
    a, b = float(a), float(b)
    return a - b


def get_pow(a, b) -> int | float:
    """
    A test function for the problem B 5.3

    Returns: power of two args
    """
    return a**b


def get_div(a, b) -> int | float:
    """
    A test function for the problem B 5.3

    Returns: division of two args
    """
    a, b = float(a), float(b)
    return a / (b + 1e9)


b_test_data = [
    (get_sum, "first open test"),
    (get_prod, "second open test"),
    (get_sub, "sub"),
    (get_pow, "pow"),
    (get_div, "div"),
]


def concat_str(a, b, c) -> str:
    """
    A test function for the problem C 5.3

    Returns: string of three args
    """
    return "".join(map(str, (a, b, c)))


def get_set(a, b) -> set:
    """
    A test function for the problem C 5.3

    Returns: set of unique elements from two args
    """
    return set(a) ^ set(b)


def get_repr(*args) -> bool:
    """
    A test function for the problem C 5.3

    Returns: string representation of args
    """
    return all(isinstance(repr(arg), str) for arg in args)


def get_str(*args) -> bool:
    """
    A test function for the problem C 5.3

    Returns: string representation of args
    """
    return all(isinstance(str(arg), str) for arg in args)


c_test_data = [
    (concat_str, "first open test"),
    (get_set, "second open test"),
    (get_repr, "repr"),
    (get_str, "str"),
]

d_test_data = {
    "Errors": (
        (("3", 2.5), TypeError, "first open test"),
        ((1, 22313.5), TypeError, "big float"),
        ((122313123132.0, 22313), TypeError, "another big float"),
        (("4", 22313), TypeError, "string and int"),
        ((0.0, "0"), TypeError, "zero as float and string"),
        ((0.0001, 0), TypeError, "float and zero as int"),
        (("0.0", "0"), TypeError, "zeros as strings"),
        ((1, 4), ValueError, "odd first arg"),
        ((12, 47), ValueError, "odd second arg"),
        ((2193121, 130393494351), ValueError, "odd both args"),
        ((-(10**7), 2), ValueError, "big negative num"),
        ((10**5, -2), ValueError, "small negative num"),
        ((-2, -4), ValueError, "both negative nums"),
    ),
    "Values": (
        ((2, 4), 6, "six"),
        ((10**9 + 2, 4), 10**9 + 6, "big int"),
        ((0, 0), 0, "zeros"),
        ((0, -0), 0, "zero minus zero"),
        ((14, 0), 14, "second zero"),
        ((0, 10004), 10004, "first zero"),
        ((8, 482382412012912), 482382412012920, "small + big ints"),
    ),
}

e_test_data = {
    "Errors": (
        ((35, (1, 2, 3)), StopIteration, "first open test"),
        (((1, 2, 3), -21), StopIteration, "not iterable"),
        ((0, -21), StopIteration, "not iterables"),
        (([3, 2, 1], [2.0, 1.1, 100000]), TypeError, "type error"),
        (
            ([-3.3, -2, -1], [-2, -1, 99999999]),
            TypeError,
            "type error negative nums",
        ),
        (
            ([3.3, -2.2, -1.123], [-2.123124, -6643.2312341, 100000]),
            TypeError,
            "type error one int",
        ),
        (([3, 2, 1], range(10)), ValueError, "second open test"),
        ((range(1), (21, 2311, 0)), ValueError, "range and tuple"),
        (([-3, -2, 1], [2, -11, 100000]), ValueError, "one unsorted"),
        (
            ([-3.1, -2.22, -1.9], [-2.01, -2.009, -2.011]),
            ValueError,
            "negative numbers",
        ),
    ),
    "Values": merge,  # The same test data as for the problem J 4.1
}

f_test_data = {
    "Errors": (
        ((0, 0, 1), "NoSolutionsError", "first open test"),
        ((0, 0, 0), "InfiniteSolutionsError", "inf solutions with zeros"),
        ((1020, 1, 310), "NoSolutionsError", "no solutions"),
        ((-0.321, -2.4, -7.3), "NoSolutionsError", "neg floats"),
        ((23130.9, 2.21344, 7.365744), "NoSolutionsError", "pos floats"),
        (
            (-110.009, 3.21344, -6.346544),
            "NoSolutionsError",
            "neg/pos/neg floats",
        ),
        (("math.sqrt(2)", 0, 310), "TypeError", "a - str"),
        ((1022, "math.sqrt(2)", 310), "TypeError", "b - str"),
        ((1022, -12.312, "math.sqrt(2)"), "TypeError", "c - str"),
        ((None, 0, 310), "TypeError", "a - None"),
        ((1022, None, 310), "TypeError", "b - None"),
        ((1022, -12.312, None), "TypeError", "c - None"),
        ((lambda _: None, 0, 310), "TypeError", "a - lambda"),
        ((122, lambda _: None, 310), "TypeError", "b - lambda"),
        ((1023, -12.312, lambda _: None), "TypeError", "c - lambda"),
    ),
    "Values": (
        ((1, 2, 1), (-1.0, -1.0), "second open test"),
        ((3.5, -2.4, -7.3), (-1.14, 1.83), "mix of floats"),
        ((0, -2.4, -7.3), (-3.04,), "simple equation neg floats"),
        ((0, 2.21344, 7.365744), (-3.33,), "simple equation pos floats"),
        ((0, -32.21344, 7.365744), (0.23,), "simple equation neg/pos floats"),
        ((0, 3.21344, -6.346544), (1.98,), "simple equation pos/neg floats"),
        ((0, -24, -73), (-3.04,), "simple equation neg ints"),
        ((0, 221344, 7365744), (-33.28,), "simple equation pos ints"),
        ((0, -3221344, 7365744), (2.29,), "simple equation neg/pos ints"),
        ((0, 321344, -6346544), (19.75,), "simple equation pos/neg ints"),
        ((-3.0, -32.21344, 7.365744), (-10.96, 0.22), "neg/neg/pos floats"),
        ((-31.03, 179.2184, -7.365744), (0.04, 5.73), "neg/pos/neg floats"),
        ((31.03, -79.2184, -7.365744), (-0.09, 2.64), "pos/neg/neg floats"),
        ((-3.0, 179.2184, 7.365744), (-0.04, 59.78), "neg/pos/pos floats"),
        ((0.009, 3.21344, -6.346544), (-359.01, 1.96), "pos/pos/neg floats"),
    ),
}

g_test_data = {
    "Errors": (
        ("user", "CyrillicError", "first open test"),
        ("Sub89P13", "CyrillicError", "cyrillic err"),
        ("12334", "CyrillicError", "cyrillic err num"),
        ("ИваноВ!", "CyrillicError", "cyrillic err !"),
        ("Иванов?", "CyrillicError", "cyrillic err ?"),
        ("иванов", "CapitalError", "second open test"),
        ("ИвановИванов", "CapitalError", "upper letter in the mid"),
        ("ИваноВ", "CapitalError", "upper letter at the end"),
        ("ПЕТРОВ", "CapitalError", "upper"),
        ("гуглеР", "CapitalError", "only last is upper"),
        ("КаМеЛкЕйС", "CapitalError", "camelcase"),
        (1, "TypeError", "int"),
        (1212.1, "TypeError", "float"),
        (lambda _: None, "TypeError", "callable"),
        (Exception, "TypeError", "exception"),
    ),
    "Values": (
        ("Иванов", "Иванов", "Ivanov"),
        ("Игнат", "Игнат", "Ignat"),
        ("А", "А", "short name"),
    ),
}

h_test_data = {
    "Errors": (
        ("$user_45$", "BadCharacterError", "first open test"),
        ("!@#", "BadCharacterError", "special chars"),
        ("45_user", "StartsWithDigitError", "second open test"),
        ("45_user@", "BadCharacterError", "order of errors"),
        ("05213422", "StartsWithDigitError", "digits"),
        (("45_user@",), "TypeError", "tuple"),
        (1, "TypeError", "int"),
        (1212.1, "TypeError", "float"),
        (lambda _: None, "TypeError", "callable"),
        (Exception, "TypeError", "exception"),
    ),
    "Values": (
        ("Ruser_45", "Ruser_45", "capital underscore nums"),
        ("true99USER_", "true99USER_", "mix of everythin"),
        ("trueuser", "trueuser", "only lowercase"),
        ("IMBAGOD", "IMBAGOD", "only uppercase"),
        ("I690021394", "I690021394", "mainly digits uppercase letter"),
        ("k690021394", "k690021394", "mainly digits lowercase letter"),
        ("Sub89P13", "Sub89P13", "myself"),
        ("_user45", "_user45", "starts with underscore"),
    ),
}

i_test_data = {
    "Errors": (
        (
            {
                "last_name": "Иванов",
                "first_name": "Иван",
                "username": "ivanych45",
                "password": "1223456",
            },
            "KeyError",
            "second open test",
        ),
        (
            {
                "first_name": "Иван",
                "last_name": "Иванов",
                "username": "ivanych45",
            },
            "KeyError",
            "wrong order of args",
        ),
        (
            {
                "username": "ivanych45",
                "first_name": "Иван",
                "last_name": "Иванов",
            },
            "KeyError",
            "wrong order of args 2",
        ),
        (
            {
                "last_name": "Иванов",
                "first_name": "Иван",
            },
            "KeyError",
            "two args of three",
        ),
        (
            {
                "last_name": "Иванов",
                "username": "ivanych45",
            },
            "KeyError",
            "another two args of three",
        ),
        (
            {
                "username": "ivanych45",
                "first_name": "Иван",
            },
            "KeyError",
            "last two args of three",
        ),
        (
            {
                "username": "ivanych45",
                "password": "s0me_trickY",
                "first_name": "Иван",
                "last_name": "Иванов",
            },
            "KeyError",
            "extra arg",
        ),
        (
            {
                "last_name": 1,
                "first_name": "Иван",
                "username": "ivanych45",
            },
            "TypeError",
            "last name int",
        ),
        (
            {
                "last_name": "Иванов",
                "first_name": 3.14,
                "username": "ivanych45",
            },
            "TypeError",
            "first name float",
        ),
        (
            {
                "last_name": "Иванов",
                "first_name": "Олег",
                "username": 0.07,
            },
            "TypeError",
            "username float",
        ),
        (
            {
                "last_name": "Иванов",
                "first_name": "Олег",
                "username": "0.07",
            },
            "BadCharacterError",
            "username with dot",
        ),
        (
            {
                "last_name": "Иванов",
                "first_name": "Олег",
                "username": "gringo-",
            },
            "BadCharacterError",
            "username with hyphen",
        ),
        (
            {
                "last_name": "Иванов",
                "first_name": "Олег",
                "username": "",
            },
            "BadCharacterError",
            "empty username",
        ),
        (
            {
                "last_name": "Иванов",
                "first_name": "Олег",
                "username": "59_gringo",
            },
            "StartsWithDigitError",
            "username starts with a digit",
        ),
        (
            {
                "last_name": "Иванов",
                "first_name": "Олег",
                "username": "007",
            },
            "StartsWithDigitError",
            "username from digits",
        ),
        (
            {
                "last_name": "Иванов",
                "first_name": "Олег",
                "username": "google_hero!",
            },
            "BadCharacterError",
            "username with !",
        ),
        (
            {
                "last_name": "Iванов",
                "first_name": "Иван",
                "username": "sergeich69",
            },
            "CyrillicError",
            "non cyrillic symbol in last name",
        ),
        (
            {
                "last_name": "Ивановs",
                "first_name": "Иван",
                "username": "sergeich69",
            },
            "CyrillicError",
            "non cyrillic symbol in last name at the end",
        ),
        (
            {
                "last_name": "Иванов",
                "first_name": "Sergey",
                "username": "sergeich69",
            },
            "CyrillicError",
            "english first name",
        ),
        (
            {
                "last_name": "Иванов",
                "first_name": "Сeргей",
                "username": "sergeich69",
            },
            "CyrillicError",
            "english e in first name",
        ),
        (
            {
                "last_name": "иванов",
                "first_name": "Сергей",
                "username": "sergeich69",
            },
            "CapitalError",
            "lowercase last name",
        ),
        (
            {
                "last_name": "ИВанов",
                "first_name": "Сергей",
                "username": "sergeich69",
            },
            "CapitalError",
            "extra uppercase letter in last name",
        ),
        (
            {
                "last_name": "ИваноВ",
                "first_name": "Сергей",
                "username": "sergeich69",
            },
            "CapitalError",
            "another extra uppercase letter in last name",
        ),
        (
            {
                "last_name": "Иванов",
                "first_name": "СЕргей",
                "username": "sergeich69",
            },
            "CapitalError",
            "extra uppercase letter in first name",
        ),
        (
            {
                "last_name": "Иванов",
                "first_name": "СергеЙ",
                "username": "sergeich69",
            },
            "CapitalError",
            "another extra uppercase letter in first name",
        ),
    ),
    "Values": (
        (
            {
                "last_name": "Иванов",
                "first_name": "Иван",
                "username": "ivanych45",
            },
            {
                "last_name": "Иванов",
                "first_name": "Иван",
                "username": "ivanych45",
            },
            "first open test",
        ),
        (
            {
                "last_name": "Р",
                "first_name": "Иван",
                "username": "ivanych_45",
            },
            {
                "last_name": "Р",
                "first_name": "Иван",
                "username": "ivanych_45",
            },
            "one letter last name",
        ),
        (
            {
                "last_name": "Рогоз",
                "first_name": "Д",
                "username": "moron_45",
            },
            {
                "last_name": "Рогоз",
                "first_name": "Д",
                "username": "moron_45",
            },
            "one letter first name",
        ),
        (
            {
                "last_name": "Рогоз",
                "first_name": "Д",
                "username": "Y",
            },
            {
                "last_name": "Рогоз",
                "first_name": "Д",
                "username": "Y",
            },
            "one letter username",
        ),
    ),
}

j_test_data = {
    "Errors": (
        (
            "$uNri$e_777",
            {
                "min_length": 6,
                "at_least_one": lambda char: char in "!@#$%^&*()_",
            },
            "PossibleCharError",
            "second open test",
        ),
        (
            12345,
            {
                "min_length": 6,
                "at_least_one": lambda char: char in "!@#$%^&*()_",
            },
            "TypeError",
            "wrong password data type - int",
        ),
        (
            ("12345",),
            {
                "min_length": 6,
                "at_least_one": lambda char: char in "!@#$%^&*()_",
            },
            "TypeError",
            "wrong password data type - tuple",
        ),
        (
            lambda _: "Yawn",
            {
                "min_length": 6,
                "at_least_one": lambda char: char in "!@#$%^&*()_",
            },
            "TypeError",
            "wrong password data type - callable",
        ),
        (
            12.345,
            {
                "min_length": 6,
                "at_least_one": lambda char: char in "!@#$%^&*()_",
            },
            "TypeError",
            "wrong password data type - float",
        ),
        (
            "$uNr1$e_1n_HelL",
            {
                "min_length": 16,
            },
            "MinLengthError",
            "min length test more than default",
        ),
        (
            "HelL_n0",
            {},
            "MinLengthError",
            "min length test default",
        ),
        (
            "12345",
            {
                "min_length": 6,
            },
            "MinLengthError",
            "min length test less than default",
        ),
        (
            "$uNri$e_777",
            {
                "possible_chars": set(string.ascii_letters),
            },
            "PossibleCharError",
            "possible_chars: only English letters",
        ),
        (
            "$uNri$e_777",
            {
                "possible_chars": set(string.digits),
            },
            "PossibleCharError",
            "possible_chars: only digits",
        ),
        (
            "uNrie777",
            {
                "at_least_one": lambda x: x in string.punctuation,
                "possible_chars": set(
                    string.ascii_letters + string.punctuation + string.digits
                ),
            },
            "NeedCharError",
            "need char: punctuation",
        ),
        (
            "OLDSCAREDPUSSY",
            {
                "at_least_one": lambda x: x.islower(),
            },
            "NeedCharError",
            "need char: lowercase",
        ),
        (
            "UrInatoR",
            {},
            "NeedCharError",
            "need char: by default",
        ),
        (
            "!He11:@1.ye$2345" * 10**6,
            {
                "min_length": 10,
                "possible_chars": set(
                    string.ascii_letters + string.punctuation + string.digits
                ),
            },
            "TimeLimitExceeded",
            "strong password which catches TL",
        ),
    ),
    "Values": (
        (
            "Hello12345",
            {},
            "67698a29126e52a6921ca061082783ede0e9085c45163c3658a2b0a82c8f95a1",
            "first open test",
        ),
        (
            "He11:O12345",
            {
                "min_length": 11,
                "at_least_one": lambda x: x in string.punctuation,
                "possible_chars": list(
                    string.ascii_letters + string.punctuation + string.digits
                ),
            },
            "dcac082b965e5961b4f1c77bd923fc115f28883ef17d34e3c072efaf2b8a8954",
            "changed default kwargs",
        ),
        (
            "!He11:@1.ye$2345",
            {
                "min_length": 10,
                "possible_chars": list(
                    string.ascii_letters + string.punctuation + string.digits
                ),
            },
            "c6a59bcdda2f600d5c94ce9e7e9027a25c1f21c811a00118229aad0c1ae1d230",
            "strong password",
        ),
    ),
}
