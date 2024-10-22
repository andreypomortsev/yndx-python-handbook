import pandas as pd

length_stats_test_data = [
    (
        "Мама мыла раму",
        pd.Series({"мама": 4, "мыла": 4, "раму": 4}),
        "first open test",
    ),
    (
        "Лес, опушка, странный домик. Лес, опушка и зверушка.",
        pd.Series(
            {
                "домик": 5,
                "зверушка": 8,
                "и": 1,
                "лес": 3,
                "опушка": 6,
                "странный": 8,
            }
        ),
        "second open test",
    ),
    (
        "str.maketrans(" ", " ", string.punctuation + string.digits)",
        pd.Series(
            {"stringdigits": 12, "stringpunctuation": 17, "strmaketrans": 12}
        ),
        "part of the solution",
    ),
    (
        "stylesheet.py:237: UserWarning: Workbook contains no default style, apply openpyxl's default "
        'warn("Workbook contains no default style, apply openpyxl\'s default")',
        pd.Series(
            {
                "apply": 5,
                "contains": 8,
                "default": 7,
                "no": 2,
                "openpyxls": 9,
                "style": 5,
                "stylesheetpy": 12,
                "userwarning": 11,
                "warnworkbook": 12,
                "workbook": 8,
            }
        ),
        "mix of chars, digits, and punctuation",
    ),
    (
        "stylesheet.py:237: UserWarning: Workbook contains no default style, apply openpyxl's default "
        'warn("Workbook contains no default style, apply openpyxl\'s default")\nНо это не точно',
        pd.Series(
            {
                "apply": 5,
                "contains": 8,
                "default": 7,
                "no": 2,
                "openpyxls": 9,
                "style": 5,
                "stylesheetpy": 12,
                "userwarning": 11,
                "warnworkbook": 12,
                "workbook": 8,
                "не": 2,
                "но": 2,
                "точно": 5,
                "это": 3,
            }
        ),
        "mix of chars, digits, and punctuation in two languages",
    ),
    ("", pd.Series({}, dtype="int64"), "empty string"),
]

length_stats_test_data_2 = [
    (
        "Мама мыла раму",
        (
            pd.Series({}, dtype="int64"),
            pd.Series({"мама": 4, "мыла": 4, "раму": 4}),
        ),
        "first open test",
    ),
    (
        "Лес, опушка, странный домик. Лес, опушка и зверушка.",
        (
            pd.Series(
                {
                    "домик": 5,
                    "и": 1,
                    "лес": 3,
                }
            ),
            pd.Series(
                {
                    "зверушка": 8,
                    "опушка": 6,
                    "странный": 8,
                }
            ),
        ),
        "second open test",
    ),
    (
        "str.maketrans(" ", " ", string.punctuation + string.digits)",
        (
            pd.Series({"stringpunctuation": 17}),
            pd.Series({"stringdigits": 12, "strmaketrans": 12}),
        ),
        "some code",
    ),
    (
        "stylesheet.py:237: UserWarning: Workbook contains no default style, apply openpyxl's default "
        'warn("Workbook contains no default style, apply openpyxl\'s default")',
        (
            pd.Series(
                {
                    "apply": 5,
                    "default": 7,
                    "openpyxls": 9,
                    "style": 5,
                    "userwarning": 11,
                }
            ),
            pd.Series(
                {
                    "contains": 8,
                    "no": 2,
                    "stylesheetpy": 12,
                    "warnworkbook": 12,
                    "workbook": 8,
                }
            ),
        ),
        "mix of chars, digits, and punctuation",
    ),
    (
        "stylesheet.py:237: UserWarning: Workbook contains no "
        "default style, apply openpyxl's default warn(\"Workbook "
        "contains no default style, apply openpyxl's default\")\nНо это не точно",
        (
            pd.Series(
                {
                    "apply": 5,
                    "default": 7,
                    "openpyxls": 9,
                    "style": 5,
                    "userwarning": 11,
                    "точно": 5,
                    "это": 3,
                }
            ),
            pd.Series(
                {
                    "contains": 8,
                    "no": 2,
                    "stylesheetpy": 12,
                    "warnworkbook": 12,
                    "workbook": 8,
                    "не": 2,
                    "но": 2,
                }
            ),
        ),
        "mix of chars, digits, and punctuation in two languages",
    ),
    (
        "stylesheet.py:237: UserWarning: Workbook contains no "
        "default style, apply openpyxl's default warn(\"Workbook "
        "contains no default style, apply openpyxl's default\")\nНо это не точно "
        * 10**3,
        (
            pd.Series(
                {
                    "apply": 5,
                    "default": 7,
                    "openpyxls": 9,
                    "style": 5,
                    "userwarning": 11,
                    "точно": 5,
                    "это": 3,
                }
            ),
            pd.Series(
                {
                    "contains": 8,
                    "no": 2,
                    "stylesheetpy": 12,
                    "warnworkbook": 12,
                    "workbook": 8,
                    "не": 2,
                    "но": 2,
                }
            ),
        ),
        "long string",
    ),
    (
        "",
        (pd.Series({}, dtype="int64"), pd.Series({}, dtype="int64")),
        "empty string",
    ),
]

cheque_test_data = [
    (
        pd.Series({"bread": 37, "milk": 58, "soda": 99, "cream": 72}),
        {"soda": 3, "milk": 2, "cream": 1},
        pd.DataFrame(
            {
                "product": {0: "cream", 1: "milk", 2: "soda"},
                "price": {0: 72, 1: 58, 2: 99},
                "number": {0: 1, 1: 2, 2: 3},
                "cost": {0: 72, 1: 116, 2: 297},
            }
        ),
        pd.DataFrame(
            {
                "product": {0: "cream", 1: "milk", 2: "soda"},
                "price": {0: 72, 1: 58, 2: 99},
                "number": {0: 1, 1: 2, 2: 3},
                "cost": {0: 72.0, 1: 116.0, 2: 148.5},
            }
        ),
        "first open test",
    ),
    (
        pd.Series({"beer": 37, "milk": 58, "soda": 99, "cream": 72}),
        {"beer": 2},
        pd.DataFrame(
            {
                "product": {0: "beer"},
                "price": {0: 37},
                "number": {0: 2},
                "cost": {0: 74},
            }
        ),
        pd.DataFrame(
            {
                "product": {0: "beer"},
                "price": {0: 37},
                "number": {0: 2},
                "cost": {0: 74.0},
            }
        ),
        "only beer",
    ),
    (
        pd.Series({"beer": 19.92}),
        {"beer": 6, "soda": 3, "milk": 2, "cream": 1},
        pd.DataFrame(
            {
                "product": {0: "beer"},
                "price": {0: 19.92},
                "number": {0: 6},
                "cost": {0: 119.52000000000001},
            }
        ),
        pd.DataFrame(
            {
                "product": {0: "beer"},
                "price": {0: 19.92},
                "number": {0: 6},
                "cost": {0: 59.760000000000005},
            }
        ),
        "only beer in store",
    ),
    (
        pd.Series(
            {
                "bread": 3.79,
                "milk": 5.89,
                "soda": 9.99,
                "cream": 10.72,
                "tea": 0.99,
            }
        ),
        {"soda": 213, "milk": 322, "cream": 221, "tea": 0.3},
        pd.DataFrame(
            {
                "product": {0: "cream", 1: "milk", 2: "soda", 3: "tea"},
                "price": {0: 10.72, 1: 5.89, 2: 9.99, 3: 0.99},
                "number": {0: 221.0, 1: 322.0, 2: 213.0, 3: 0.3},
                "cost": {
                    0: 2369.1200000000003,
                    1: 1896.58,
                    2: 2127.87,
                    3: 0.297,
                },
            }
        ),
        pd.DataFrame(
            {
                "product": {0: "cream", 1: "milk", 2: "soda", 3: "tea"},
                "price": {0: 10.72, 1: 5.89, 2: 9.99, 3: 0.99},
                "number": {0: 221.0, 1: 322.0, 2: 213.0, 3: 0.3},
                "cost": {
                    0: 1184.5600000000002,
                    1: 948.29,
                    2: 1063.935,
                    3: 0.297,
                },
            }
        ),
        "a lot of products",
    ),
]

get_long_test_data = [
    (
        pd.Series({"мир": 3, "питон": 5, "привет": 6, "яндекс": 6}),
        {},
        pd.Series({"питон": 5, "привет": 6, "яндекс": 6}),
        "first open test",
    ),
    (
        pd.Series({"мир": 3, "питон": 5, "привет": 6, "яндекс": 6}),
        {"min_length": 6},
        pd.Series({"привет": 6, "яндекс": 6}),
        "second open test",
    ),
    (
        pd.Series({"мир": 13, "питон": 25, "привет": 26, "яндекс": 63}),
        {"min_length": 6},
        pd.Series({"мир": 13, "питон": 25, "привет": 26, "яндекс": 63}),
        "all more than the limit",
    ),
    (
        pd.Series({"мир": 13, "питон": 25, "привет": 26, "яндекс": 63}),
        {"min_length": 64},
        pd.Series({}, dtype="int64"),
        "none more than the limit",
    ),
]
