a_test_data = [
    ({"a": 1, "b": 5}, [1, 4, 9, 16, 25], "first open test"),
    (
        {"a": -5, "b": 5},
        [25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25],
        "second open test",
    ),
    (
        {"a": -10, "b": 2},
        [100, 81, 64, 49, 36, 25, 16, 9, 4, 1, 0, 1, 4],
        "negative ten to two",
    ),
    ({"a": 0, "b": 1}, [0, 1], "zero to one"),
    ({"a": -1, "b": 0}, [1, 0], "minus one to zero"),
    ({"a": -2, "b": 0}, [4, 1, 0], "minus two to zero"),
]

b_test_data = [
    ({"a": 1, "b": 5}, [1, 4, 9, 16, 25], "first open test"),
    ({"a": 5, "b": -4}, [25, 16, 9, 4, 1, 0, 1, 4, 9, 16], "second open test"),
    ({"a": -3, "b": 2}, [9, 4, 1, 0, 1, 4], "ascending across zero"),
    ({"a": 2, "b": -3}, [4, 1, 0, 1, 4, 9], "descending across zero"),
    ({"a": -5, "b": -1}, [25, 16, 9, 4, 1], "ascending negative range"),
    ({"a": -1, "b": -5}, [1, 4, 9, 16, 25], "descending negative range"),
    ({"a": 0, "b": 3}, [0, 1, 4, 9], "ascending from zero to positive"),
    ({"a": 3, "b": 0}, [9, 4, 1, 0], "descending from positive to zero"),
    ({"a": 0, "b": -3}, [0, 1, 4, 9], "ascending from zero to negative (invalid case forced by range logic)"),
    ({"a": -3, "b": 0}, [9, 4, 1, 0], "descending from negative to zero"),
    ]

q_test_data = [
    ({"n": 3}, [[1, 2, 3], [2, 4, 6], [3, 6, 9]], "first open test"),
    (
        {"n": 4},
        [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]],
        "second open test",
    ),
    ({"n": 1}, [[1]], "one"),
    ({"n": 0}, [], "zero"),
]

f_test_data = [
    ({"sentence": "Мама мыла раму"}, [4, 4, 4], "first open test"),
    (
        {"sentence": "Ехали медведи на велосипеде"},
        [5, 7, 2, 10],
        "second open test",
    ),
]

d_test_data = [
    ({"numbers": [1, 2, 3, 4, 5]}, {1, 3, 5}, "first open test"),
    ({"numbers": [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]}, {1, 3}, "second open test"),
    ({"numbers": [2, 4, 2, 6, 12, 30, 2, 2]}, set(), "only even numbers"),
    (
        {"numbers": [1, 11, 13, 31, 15, 101]},
        {1, 11, 13, 31, 15, 101},
        "only odd numbers",
    ),
]

e_test_data = [
    ({"numbers": [1, 2, 3, 4, 5]}, {1, 4}, "first open test"),
    (
        {"numbers": [i for i in range(16, 100, 4)]},
        {16, 64, 36},
        "second open test",
    ),
    (
        {"numbers": [i for i in range(1000, 1500, 4)]},
        {1024, 1156, 1296, 1444},
        "longer test",
    ),
    (
        {"numbers": (i for i in range(1000000000, 1000500000, 4))},
        {1000077376, 1000456900, 1000203876, 1000330384},
        "big nums",
    ),
]

o_test_data = [
    (
        {"text": "Мама мыла раму!"},
        {"а": 4, "л": 1, "м": 4, "р": 1, "у": 1, "ы": 1},
        "first open test",
    ),
    (
        {
            "text": """Ехали медведи
На велосипеде.

А за ними кот
Задом наперёд."""
        },
        {
            "а": 6,
            "в": 2,
            "д": 5,
            "е": 7,
            "з": 2,
            "и": 5,
            "к": 1,
            "л": 2,
            "м": 3,
            "н": 3,
            "о": 3,
            "п": 2,
            "р": 1,
            "с": 1,
            "т": 1,
            "х": 1,
            "ё": 1,
        },
        "second open test",
    ),
]

r_test_data = [
    (
        {"numbers": {1, 2, 3, 4, 5}},
        {1: [1], 2: [1, 2], 3: [1, 3], 4: [1, 2, 4], 5: [1, 5]},
        "first open test",
    ),
    (
        {"numbers": {15, 49, 36}},
        {
            15: [1, 3, 5, 15],
            36: [1, 2, 3, 4, 6, 9, 12, 18, 36],
            49: [1, 7, 49],
        },
        "second open test",
    ),
    (
        {
            "numbers": {
                10709,
                10711,
                10723,
                10729,
                10733,
                10739,
                10753,
                10771,
                10781,
                10789,
            }
        },
        {
            10709: [1, 10709],
            10711: [1, 10711],
            10723: [1, 10723],
            10729: [1, 10729],
            10733: [1, 10733],
            10739: [1, 10739],
            10753: [1, 10753],
            10771: [1, 10771],
            10781: [1, 10781],
            10789: [1, 10789],
        },
        "big primes",
    ),
]

h_test_data = [
    ({"string": "Российская Федерация"}, "РФ", "first open test"),
    ({"string": "открытое акционерное общество"}, "ОАО", "second open test"),
    ({"string": "bring your own Booze"}, "BYOB", "english"),
]

i_test_data = [
    ({"numbers": [3, 1, 2, 3, 2, 2, 1]}, "1 - 2 - 3", "first open test"),
    (
        {"numbers": [1, 1, 3, 1, 10, 2, 4, 6, 7, 1, 2, 7]},
        "1 - 2 - 3 - 4 - 6 - 7 - 10",
        "second open test",
    ),
    (
        {"numbers": [100, 200, 300, 200, 20, 10]},
        "10 - 20 - 100 - 200 - 300",
        "hundreds",
    ),
]

p_test_data = [
    ({"rle": [("a", 2), ("b", 3), ("c", 1)]}, "aabbbc", "first open test"),
    (
        {"rle": [("1", 1), ("0", 2), ("5", 1), ("0", 2)]},
        "100500",
        "second open test",
    ),
    (
        {"rle": [("S", 1), ("O", 1), ("5", 1), ("!", 0)]},
        "SO5",
        "sos with zero value",
    ),
]
