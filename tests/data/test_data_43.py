a_test_data = [
    ((1, 2, 3), 6, "first open test"),
    ((7, 1, 3, 2, 10), 23, "second open test"),
    ((-7, -1, -3, -2, -10), -23, "negative numbers"),
    ((-7, -1, -3, -2, -10, 7, 1, 3, 2, 10), 0, "mixed numbers to zero"),
    ((-7, -1, -3, -2, 10, 7, 1, 3, 2, 10), 20, "mixed numbers to positive"),
    (
        (-7, -1, -33, -2, -10, 7, 1, 33, 2, -10),
        -20,
        "mixed numbers to negative",
    ),
    (
        (
            -70000000,
            -10000000,
            -30000000,
            -20000000,
            -100000000,
            70000000,
            10000000,
            30000000,
            20000000,
            100000000,
        ),
        0,
        "big mixed numbers to zero",
    ),
    ((0, 0, 0, 0, 0, 0, 0, 0, 0, 10), 10, "zeros and ten"),
    ((0, 0, 0, 0, 0, 1, 0, 0, 0, 0), 1, "zeros-one-zeros"),
]

b_test_data = [
    (123, 6, "first open test"),
    (7321346, 26, "second open test"),
    (7, 7, "one number"),
    (0, 0, "zero"),
    (100000000, 1, "average number"),
    (12345678910111213141516171819, 100, "big number"),
    (
        1000000000000000000000000000000000000000000000000000000000000000,
        1,
        "huge number",
    ),
]

c_test_data = [
    ((3, 2, 1), "((3) * x + 2) * x + 1", "first open test"),
    ((3, 1, 5, 3), "(((3) * x + 1) * x + 5) * x + 3", "second open test"),
    (
        (1, 2, 3, 4, 5, 6, 0),
        "((((((1) * x + 2) * x + 3) * x + 4) * x + 5) * x + 6) * x + 0",
        "seven digits",
    ),
    ((100,), "100", "one number test"),
    ((100, 200), "(100) * x + 200", "two digits"),
    ((0.2, 0.1, 0.3), "((0.2) * x + 0.1) * x + 0.3", "floats"),
]

test_data_d_a_plus_b = [
    ((3, 5), "Результат функции: 8\n", "first open test 1"),
    ((7, 9), "Результат функции: 16\n", "first open test 2"),
    ((0, 0), "Результат функции: 0\n", "zeros"),
    ((10**9, 1), "Результат функции: 1000000001\n", "big number"),
]

test_data_d_get_letters = [
    (("Hello, world!",), "Результат функции: dehlorw\n", "second open test 1"),
    (
        ("Декораторы это круто =)",),
        "Результат функции: адекортуыэ\n",
        "second open test 2",
    ),
    ((" ",), "Результат функции: \n", "whitespace"),
    (("Very interesting!",), "Результат функции: eginrstvy\n", "mixed"),
]

test_data_d_get_sum_of_ords = [
    (
        ("Hello, world!",),
        "Результат функции: 1161\n",
        "like second open test 1",
    ),
    (
        ("Декораторы это круто =)",),
        "Результат функции: 19724\n",
        "like second open test 2",
    ),
    ((" ",), "Результат функции: 32\n", "whitespace"),
    (("Very interesting!",), "Результат функции: 1683\n", "mixed"),
]

test_data_e_a_plus_b = [
    ((3, 5), {"method": "accumulate"}, None, "first open test 1"),
    ((7, 9), {}, None, "first open test 2"),
    ((-3, 5), {"method": "drop"}, [8, 16, 2], "first open test 3"),
    ((1, -7), {}, None, "first open test 4"),
    ((10, 35), {"method": "drop"}, [-6, 45], "first open test 5"),
]

test_data_e_get_letters = [
    (("Hello, world!",), {}, None, "second open test 1"),
    (
        ("Декораторы это круто =)",),
        {},
        None,
        "second open test 2",
    ),
    (
        ("Ехали медведи на велосипеде",),
        {"method": "drop"},
        ["dehlorw", "адекортуыэ", "авдеилмнопсх"],
        "second open test 3",
    ),
]

test_data_e_get_sum_of_ords = [
    (
        ("Hello, world!",),
        {"method": "accumulate"},
        None,
        "like second open test 1",
    ),
    (
        ("Декораторы это круто =)",),
        {"method": "drop"},
        [1161, 19724],
        "like second open test 2",
    ),
    ((" ",), {}, None, "whitespace"),
    (("Very interesting!",), {"method": "drop"}, [32, 1683], "mixed"),
]
