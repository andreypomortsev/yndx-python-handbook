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

f_test_data = [
    ([3, 2, 1], [1, 2, 3], "first open test"),
    ([3, 1, 5, 3], [1, 3, 3, 5], "second open test"),
    ([100, 200, 400, 600, 101], [100, 101, 200, 400, 600], "odd length"),
    ([13], [13], "one number"),
    ([6, 7, 8, 9, 10], [6, 7, 8, 9, 10], "already sorted"),
    ([10, 9, 8, 7, 6], [6, 7, 8, 9, 10], "reverse sorted"),
]

test_data_g_a_plus_b = [
    (
        (3, 5.2),
        "Обнаружены различные типы данных\nFail\n",
        "first open test 1",
    ),
    (
        (7, "9"),
        "Обнаружены различные типы данных\nFail\n",
        "first open test 2",
    ),
    ((-3, 5), "2\n", "first open test 3"),
]

test_data_g_combine_text = [
    (("Hello,", "world!"), "Hello, world!\n", "first open test 1"),
    (
        (2, "+", 2, "=", 4),
        "Обнаружены различные типы данных\nFail\n",
        "first open test 2",
    ),
    (
        ("Список из 30", 0, "можно получить так", [0] * 30),
        "Обнаружены различные типы данных\nFail\n",
        "first open test 3",
    ),
]

test_data_g_get_sum_of_ords = [
    (("Hello, world!",), "1161\n", "hello world"),
    (
        ("Декораторы это круто =)", True),
        "Обнаружены различные типы данных\nFail\n",
        "different types",
    ),
    ((" ", 123.1), "Обнаружены различные типы данных\nFail\n", "whitespace"),
    (
        ("Very interesting!", 12 + 13j),
        "Обнаружены различные типы данных\nFail\n",
        "complex",
    ),
]

h_test_data = [
    (5, " ", "0 1 1 2 3\n", "first open test"),
    (10, ", ", "0, 1, 1, 2, 3, 5, 8, 13, 21, 34\n", "second open test"),
    (6, "", "011235\n", "no separation"),
    (1, " ", "0\n", "one"),
    (2, "\t", "0\t1\n", "two"),
    (3, "\n", "0\n1\n1\n", "three"),
    (0, "\n", "\n", "zero -> None"),
]

i_test_data = [
    ([1, 2, 3], 5, "1 2 3 1 2\n", "first open test"),
    ([1, 2, 3, 4], 15, "1 2 3 4 1 2 3 4 1 2 3 4 1 2 3\n", "second open test"),
    ("iterable", 8, "i t e r a b l e\n", "string"),
    (
        (
            "Who",
            "loves",
            23,
            4 + 7j,
        ),
        7,
        "Who loves 23 (4+7j) Who loves 23\n",
        "mixed types",
    ),
    (
        (
            "Who",
            "loves",
            23,
            4 + 7j,
        ),
        1,
        "Who\n",
        "short mixed types",
    ),
    (range(5), 5, "0 1 2 3 4\n", "range"),
    (range(-5, 0, 1), 5, "-5 -4 -3 -2 -1\n", "negative range"),
    (range(-5, 0, 1), 3, "-5 -4 -3\n", "negative range short"),
    (range(-3, 0, 1), 6, "-3 -2 -1 -3 -2 -1\n", "long negative range"),
]

j_test_data = [
    ([1, 2, [3]], [1, 2, 3], "first open test"),
    ([1, [2, [3, 4]], 5, 6], [1, 2, 3, 4, 5, 6], "second open test"),
    ([[[[[[[1]]]]]]], [1], "deep"),
    (
        [[3, 2], [[[[5], 6]], 12], 31, [[[21], 3]]],
        [3, 2, 5, 6, 12, 31, 21, 3],
        "everything and between",
    ),
    ([1], [1], "one element"),
    ([[[[[[[[], 2], 1]]]]]], [2, 1], "with empty list"),
]
