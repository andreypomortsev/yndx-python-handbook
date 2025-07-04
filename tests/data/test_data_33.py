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
    (
        {"a": 0, "b": -3},
        [0, 1, 4, 9],
        "ascending from zero to negative (invalid case forced by range logic)",
    ),
    ({"a": -3, "b": 0}, [9, 4, 1, 0], "descending from negative to zero"),
]

c_test_data = [
    ({"a": 1, "b": 5, "d": 2}, [2, 4], "first open test"),
    (
        {"a": -9, "b": 15, "d": 3},
        [-9, -6, -3, 0, 3, 6, 9, 12, 15],
        "second open test",
    ),
    ({"a": 5, "b": 7, "d": 4}, [], "no multiples in range"),
    ({"a": 6, "b": 6, "d": 3}, [6], "single number divisible"),
    ({"a": 5, "b": 5, "d": 3}, [], "single number not divisible"),
    (
        {"a": 1, "b": 10**7, "d": 10**7},
        [10_000_000],
        "large input stress test",
    ),
    ({"a": 0, "b": 3, "d": 1}, [0, 1, 2, 3], "from zero with step 1"),
    ({"a": 0, "b": 6, "d": 2}, [0, 2, 4, 6], "from zero with even step"),
    ({"a": 0, "b": -5, "d": 2}, [], "zero to negative returns empty"),
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

f_test_data = [
    ({"sentence": "Мама мыла раму"}, [4, 4, 4], "first open test"),
    (
        {"sentence": "Ехали медведи на велосипеде"},
        [5, 7, 2, 10],
        "second open test",
    ),
]

g_test_data = [
    (
        {
            "text": "33 коровы,\n"
            + "33 коровы,\n"
            + "33 коровы -\n"
            + "Свежая строка.\n"
            + "33 коровы,\n"
            + "Стих родился новый,\n"
            + "Как стакан парного молока.\n"
            + "Стих родился новый,\n"
            + "Как стакан парного молока.\n"
        },
        "33333333",
        "first open test - poem with repeated numbers",
    ),
    (
        {"text": "2 + 2 = 4"},
        "224",
        "second open test - simple arithmetic line",
    ),
    (
        {"text": "No numbers here!"},
        "",
        "no digits present",
    ),
    (
        {"text": "Room 101, Sector 7G, Unit 42"},
        "101742",
        "multiple digit clusters with punctuation",
    ),
    (
        {"text": "\n\t123\nabc456\n!@#789"},
        "123456789",
        "digits across newlines and mixed content",
    ),
    (
        {"text": "٠١٢٣٤٥٦٧٨٩"},  # Arabic digits
        "٠١٢٣٤٥٦٧٨٩",
        "non-ASCII digits (Arabic numerals)",
    ),
    (
        {
            "text": "１ that's the mood １２３４５"
        },  # full-width digits (used in CJK)
        "１１２３４５",
        "full-width unicode digits (CJK-style)",
    ),
]

j_test_data = [
    (
        {"words": "Ехали медведи на велосипеде"},
        ["Ехали", "медведи", "велосипеде"],
        "first open test – Cyrillic with vowels > 2",
    ),
    (
        {"words": "My homework is too difficult!"},
        ["homework", "difficult!"],
        "second open test – English sentence with punctuation",
    ),
    (
        {"words": "sky fly by"},
        [],
        "short English words with 1 vowel or less each",
    ),
    (
        {"words": "В лесу родилась ёлочка"},
        ["родилась", "ёлочка"],
        "Cyrillic sentence with ё and mixed vowels",
    ),
    (
        {"words": "AEIOU and sometimes Y"},
        ["AEIOU", "sometimes"],
        "upper and lower case vowels",
    ),
    (
        {"words": "aaa aaaa a"},
        ["aaa", "aaaa"],
        "words made entirely of vowels",
    ),
    (
        {"words": "bcd fg hjklmnpqrstvwxyz"},
        [],
        "no vowels at all",
    ),
]

k_test_data = [
    (
        {"numbers": [1, 2, 1, 3, 1, 2, 2, 4, 1, 2, 5, 1, 2]},
        {3, 4, 5},
        "first open test",
    ),
    (
        {"numbers": [-8, 7, -3, -2, 5, 0, 7, -2, -8, 6, -10, 4, -9, -9, 7]},
        {0, 4, 5, 6, -10, -3},
        "second open test",
    ),
    ({"numbers": [1, 2, 3, 4, 5]}, {1, 2, 3, 4, 5}, "all unique elements"),
    ({"numbers": [1, 1, 1, 1]}, set(), "all duplicates"),
    ({"numbers": []}, set(), "empty list"),
    ({"numbers": [42]}, {42}, "single element list"),
    ({"numbers": [0, 0, 0, 0, 0]}, set(), "all zeros duplicated"),
    ({"numbers": [0, 1, 0, 1, 2]}, {2}, "only one unique among common"),
    ({"numbers": [-1, -2, -3, -1, -2, -4]}, {-3, -4}, "negative integers mix"),
    (
        {"numbers": [2**31 - 1, -(2**31), 0, 2**31 - 1]},
        {0, -(2**31)},
        "int boundaries and zero",
    ),
    (
        {"numbers": list(range(1000)) + list(range(500))},
        set(range(500, 1000)),
        "large list with half duplicates",
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
