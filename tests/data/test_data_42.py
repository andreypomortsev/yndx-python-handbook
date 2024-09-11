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
