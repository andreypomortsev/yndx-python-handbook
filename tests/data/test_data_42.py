from tests.data.test_data_41 import d_test_data as d_test_data_41

a_test_data = [
    ((3,), [0, 0, 0], "first open test"),
    ((5, 1), [1, 1, 1, 1, 1], "second open test"),
    ((1, 5), [5], "single value"),
    ((5, 5), [5, 5, 5, 5, 5], "double value"),
    ((1,), [0], "one default value"),
    ((1, 290293843), [290293843], "one and big value"),
]

b_test_data = [
    ((3,), [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "first open test"),
    (((4, 2), 1), [[1, 1, 1, 1], [1, 1, 1, 1]], "second open test"),
    (
        (5, 1),
        [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ],
        "five ones",
    ),
    (((3, 1), 9), [[9, 9, 9]], "one row matrix"),
    (((1, 3), 9), [[9], [9], [9]], "one column matrix"),
    (((1, 1), 9), [[9]], "one value nine"),
    (((1, 1),), [[0]], "one value default"),
    (((1, 1), 0), [[0]], "zero value"),
    (((1, 1), 1), [[1]], "one value one"),
    (((1, 1), 290293843), [[290293843]], "one and big value"),
]

c_test_data = [
    ((3,), 3, "first open test"),
    ((36, 48, 156, 100500), 12, "second open test"),
    ((3, 5, 7, 9, 17, 33), 1, "gcd of small primes"),
    ((2, 290293843, 290293847, 290293849), 1, "gcd of big primes"),
    ((290293843,), 290293843, "one big prime"),
    ((2,) * 10**5, 2, "a lot equal of numbers"),
    (tuple(range(198)), 1, "a lot of increasing numbers"),
    (tuple(range(0, 1298, 2)), 2, "a lot of even increasing numbers"),
    (tuple(range(1, 9297, 3)), 1, "a lot of odd increasing numbers"),
]

d_test_data = [
    ((1, "en"), "January", "first open test"),
    ((7,), "Июль", "second open test"),
    ((1,), "Январь", "Jan"),
    ((2,), "Февраль", "Feb"),
    ((3,), "Март", "Mar"),
    ((4,), "Апрель", "Apr"),
    ((5,), "Май", "May"),
    ((6,), "Июнь", "Jun"),
    ((8,), "Август", "Jul"),
    ((9,), "Сентябрь", "Sep"),
    ((10,), "Октябрь", "Oct"),
    ((11,), "Ноябрь", "Nov"),
    ((12,), "Декабрь", "Dec"),
] + d_test_data_41[2:]

e_test_data = [
    ((1, 2, 3), {}, "1 2 3\n", "first open test"),
    (
        [7, 3, 1, "hello", (1, 2, 3)],
        {"sep": ", ", "end": "!"},
        "7, 3, 1, hello, (1, 2, 3)!",
        "second open test",
    ),
    (("lambda x: x",), {"sep": " ", "end": "!"}, "lambda x: x!", "lambda"),
    (
        (1, 2, 3),
        {"sep": "\nlambda x: x\n", "end": "\n!!!"},
        "1\nlambda x: x\n2\nlambda x: x\n3\n!!!",
        "integers with crazy sep",
    ),
    (
        ("lambda x: x", [9, 8, 7, 6], {"one": 1, "two": 3}),
        {},
        "lambda x: x [9, 8, 7, 6] {'one': 1, 'two': 3}\n",
        "mix of data types",
    ),
]
