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

h_test_data = [
    ({"string": "Российская Федерация"}, "РФ", "first open test"),
    ({"string": "открытое акционерное общество"}, "ОАО", "second open test"),
    ({"string": "bring Your own Booze"}, "BYOB", "english"),
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

l_test_data = [
    ({"numbers": {1, 2, 3, 4, 5}}, 20, "first open test"),
    ({"numbers": {2, 4, 5, 7, -10, -8, 10, -9, -1}}, 90, "second open test"),
    ({"numbers": {-5, -3, -1}}, 15, "all negative values"),
    (
        {"numbers": {-1000, -100, 0, 100, 1000}},
        100000,
        "symmetric large extremes",
    ),
    ({"numbers": {-2, 0, 3}}, 0, "product involving zero"),
    ({"numbers": {1, 2}}, 2, "only two values"),
    ({"numbers": {-1, 1}}, -1, "two values, one negative"),
    (
        {"numbers": {-10, -9, -8, 9, 10}},
        90,
        "balanced negatives and positives",
    ),
    (
        {"numbers": {-1_000_000_000, 1, 2, 3, 999_999_999}},
        2_999_999_997,
        "extreme int boundaries",
    ),
    ({"numbers": {-5, -2, 2, 3}}, 10, "positive or negative pair gives max"),
    (
        {"numbers": set(range(1_000))},
        997002,
        "stress test – large range to reject O(n²) solutions",
    ),
]

m_test_data = [
    ({"data": {"a": [1, 2, 3], "b": [2, 3, 4, 5]}}, "a", "first open test"),
    (
        {"data": {"a": [100], "b": [20, 5], "c": [7, 15, 3]}},
        "b",
        "second open test",
    ),
    (
        {"data": {"x": [5], "y": [5]}},
        "x",
        "equal sums, choose lexicographically first key",
    ),
    ({"data": {"z": [1], "a": [1], "m": [1]}}, "a", "3-way tie, first by key"),
    ({"data": {"a": [], "b": [0]}}, "a", "empty list vs zero"),
    (
        {"data": {"a": [-1, -2], "b": [-3]}},
        "a",
        "negative values, smaller sum wins",
    ),
    ({"data": {"a": [1.5, 2.5], "b": [4.0]}}, "a", "float values, equal sum"),
    (
        {"data": {"aaa": [1, 2], "aa": [3]}},
        "aa",
        "same sum, shorter key doesn't win unless lexicographically first",
    ),
    ({"data": {"b": [1, 2], "a": [3]}}, "a", "same sum, 'a' comes before 'b'"),
    (
        {"data": {"c": [10], "b": [1, 9], "a": [5, 5]}},
        "a",
        "3-way tie again, lex sort decides",
    ),
    (
        {"data": {"a": [1_000_000], "b": [1], "c": [2] * 1_000}},
        "b",
        "check large dataset and small winner",
    ),
]

n_test_data = [
    (
        {"data": {"a": [1, 2, 1], "b": [2, 3, 2, 5, 1]}},
        {"a", "b"},
        "first open test",
    ),
    (
        {"data": {"a": [1, 2, 3], "b": [5, 2, 5], "c": [7, 15, 3]}},
        {"b"},
        "second open test",
    ),
    (
        {"data": {"x": [], "y": [1], "z": [2, 2]}},
        {"z"},
        "empty and one-element lists",
    ),
    (
        {"data": {"a": [1, 2, 3], "b": [4, 5, 6]}},
        set(),
        "all values are unique",
    ),
    (
        {"data": {"m": [0, -1, -2, -1], "n": [-3, -4, -5]}},
        {"m"},
        "negative values with one duplicate",
    ),
    (
        {"data": {"k": [2**31 - 1, 0, 2**31 - 1]}},
        {"k"},
        "duplicate at int upper boundary",
    ),
    (
        {"data": {"p": [1] * 1000, "q": list(range(1000))}},
        {"p"},
        "large list with all duplicates vs large unique",
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

s_test_data = [
    ({"numbers": {1, 2, 3, 4, 5}}, {2, 3, 5}, "first open test"),
    (
        {"numbers": set(range(11, 50, 2))},
        {11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47},
        "second open test",
    ),
    (
        {"numbers": set(range(0, 20))},
        {2, 3, 5, 7, 11, 13, 17, 19},
        "small range with mixed numbers",
    ),
    ({"numbers": {0, 1}}, set(), "zero and one are not primes"),
    (
        {"numbers": {2, 3, 5, 7, 11, 13, 17, 19, 23}},
        {2, 3, 5, 7, 11, 13, 17, 19, 23},
        "all primes only",
    ),
    ({"numbers": {4, 6, 8, 9, 10, 12}}, set(), "all non-primes"),
    ({"numbers": {997, 998, 999, 1000}}, {997}, "upper-bound edge near 1000"),
    ({"numbers": {999_999_937}}, {999_999_937}, "your solution is too slow"),
]

t_test_data = [
    (
        {"text": "ехали медведи на велосипеде"},
        {("велосипеде", "ехали"), ("велосипеде", "медведи")},
        "first open test",
    ),
    (
        {"text": "а за ними кот задом наперед"},
        set(),
        "second open test – no pair shares more than 2 letters",
    ),
    (
        {"text": "мама рама тама сама"},
        set(),
        "repeated syllables, many overlaps",
    ),
    (
        {"text": "abcde bcdef cdefg defgh"},
        {
            ("abcde", "bcdef"),
            ("abcde", "cdefg"),
            ("bcdef", "cdefg"),
            ("bcdef", "defgh"),
            ("cdefg", "defgh"),
        },
        "cascading overlap across words",
    ),
    ({"text": "x y z"}, set(), "short words with no shared letters"),
    (
        {"text": "123abc abc321 a1b2c3"},
        {
            ("123abc", "a1b2c3"),
            ("123abc", "abc321"),
            ("a1b2c3", "abc321"),
        },
        "numeric+alphabetic mix with overlapping characters",
    ),
]
