point_init = [
    (3, 5, "first open test"),
    (2, -7, "second open test"),
    (0.2, -0.7, "floats"),
    (0, 1, "zero one"),
    (1, 0, "one zero"),
    (1000000000000, 99999999999999999, "big numbers"),
    (0.000000000001, 0.0000000000000009, "small numbers"),
]

point_move = [
    ((3, 5), (2, -3), "first open test"),
    ((-3, -9), (-12, -5), "negative numbers"),
    ((-3, -9), (0, 0), "negative numbers zero move"),
    ((3, 9), (0, 0), "positive number zero move"),
    ((-3.1, -1.9), (-1.2, -0.5), "float negative float"),
    ((-6.3, -2.9), (0.0, 0.0), "negative float zero move"),
    ((3.9, 6.9), (0.0, 0.0), "positive float zero move"),
]

point_length = [
    ((2, -7, 7, 9), 16.76, "second open test"),
    ((2, 7, -7, -9), 18.36, "positive negative"),
    ((-6, -5, 73, 2), 79.31, "negative positive"),
    ((-2, -7, -7, -9), 5.39, "all negatives"),
    ((0, 1, 2, 3), 2.83, "first zero"),
    ((1, 0, 2, 3), 3.16, "second zero"),
    ((2, 1, 0, 3), 2.83, "third zero"),
    ((3, 1, 2, 0), 1.41, "last zero"),
    ((3, 1, 3, 1), 0.0, "the same points"),
]

d_test_data = [
    (
        ("Васильев Иван", "Junior"),
        (750, 500, 250, 250),
        (
            "Васильев Иван 750ч. 7500тгр.",
            "Васильев Иван 1250ч. 15000тгр.",
            "Васильев Иван 1500ч. 20000тгр.",
            "Васильев Иван 1750ч. 25250тгр.",
        ),
        "first open test",
    ),
    (
        ("Some Guy", "Middle"),
        (100, 500, 250, 250),
        (
            "Some Guy 100ч. 1500тгр.",
            "Some Guy 600ч. 11500тгр.",
            "Some Guy 850ч. 16750тгр.",
            "Some Guy 1100ч. 22250тгр.",
        ),
        "Middle",
    ),
    (
        ("A Very Senior Guy", "Senior"),
        (100, 134, 321),
        (
            "A Very Senior Guy 100ч. 2000тгр.",
            "A Very Senior Guy 234ч. 4814тгр.",
            "A Very Senior Guy 555ч. 11876тгр.",
        ),
        "Senior",
    ),
    (
        ("A Very Lazy Senior Guy", "Senior"),
        (0, 0, 0, 1),
        (
            "A Very Lazy Senior Guy 0ч. 0тгр.",
            "A Very Lazy Senior Guy 0ч. 0тгр.",
            "A Very Lazy Senior Guy 0ч. 0тгр.",
            "A Very Lazy Senior Guy 1ч. 23тгр.",
        ),
        "Lazy Senior",
    ),
]

rectangle_perimeter = [
    (((3.2, -4.3), (7.52, 3.14)), 23.52, "first open test"),
    (((-3.2, -4.3), (-7.52, -3.14)), 10.96, "negative points"),
    (((1, 2), (3, 4)), 8, "positive points"),
    (((0.01, 0.02), (0.03, 0.04)), 0.08, "small rectangle"),
    (((5.0291, 6.78321), (6.49559, 3.59558)), 9.31, "tricky round"),
]

rectangle_area = [
    (((7.52, -4.3), (3.2, 3.14)), 32.14, "second open test"),
    (((-3.2, -4.3), (-7.52, -3.14)), 5.01, "negative points"),
    (((0, -4.3), (-7.52, -3.14)), 8.72, "negative points and zero"),
    (((0.01, 0.02), (0.03, 0.04)), 0.00, "small rectangle"),
    (((0.1, 0.2), (0.3, 0.4)), 0.04, "a bit bigger rectangle"),
    (((5.0291, 6.78321), (6.49559, 3.59558)), 4.67, "tricky round"),
]

rectangle_move = [
    (
        ((3.2, -4.3), (7.52, 3.14)),  # Rectangle coordinates
        ((3.2, 3.14), (4.52, -1.86)),  # Positions before/after the move
        ((4.32, 7.44), (4.32, 7.44)),  # Size before/after the move
        (1.32, -5),  # Change of coordinates for x and y
        "first open test",
    ),
    (
        ((-3.29, -4.31), (7.51, 3.19)),
        ((-3.29, 3.19), (-3.28, 3.19)),
        ((10.8, 7.5), (10.8, 7.5)),
        (0.009, 0.001),
        "slight move",
    ),
    (
        ((-3.29, -4.31), (7.51, 3.19)),
        ((-3.29, 3.19), (6.0, -27.71)),
        ((10.8, 7.5), (10.8, 7.5)),
        (9.285, -30.899),
        "a bit bigger move",
    ),
    (
        ((-3.29, -4.01), (-6.91, -0.999)),
        ((-6.91, -1), (-6.91, -1)),
        ((3.62, 3.01), (3.62, 3.01)),
        (0, -0.0),
        "zero move",
    ),
]

rectangle_resize = [
    (
        ((7.52, -4.3), (3.2, 3.14)),  # Rectangle coordinates
        ((3.2, 3.14), (3.2, 3.14)),  # Positions before/after the move
        ((4.32, 7.44), (23.5, 11.3)),  # Size before/after the move
        (23.5, 11.3),  # New width and height
        "second open test",
    ),
    (
        ((7.52, -4.3), (3.2, 3.14)),
        ((3.2, 3.14), (3.2, 3.14)),
        ((4.32, 7.44), (3.29, 3.15)),
        (3.289, 3.149),
        "small resize",
    ),
    (
        ((-7.519, -4.31), (-23.232, -1.126)),
        ((-23.23, -1.13), (-23.23, -1.13)),
        ((15.71, 3.18), (3.29, 3.15)),
        (3.289, 3.149),
        "negative points",
    ),
    (
        ((1.519, 4.315), (0.232, 1.126)),
        ((0.23, 4.32), (0.23, 4.32)),
        ((1.29, 3.19), (0.29, 0.15)),
        (0.289, 0.149),
        "positive points",
    ),
]

rectangle_turn = [
    (
        ((3.14, 2.71), (-3.14, -2.71)),  # Rectangle coordinates
        ((-3.14, 2.71), (-2.71, 3.14)),  # Positions before/after the turn
        ((6.28, 5.42), (5.42, 6.28)),  # Size before/after the turn
        1,  # A number of turns
        "first open test",
    ),
    (
        ((3.14, 2.71), (-3.14, -2.71)),
        ((-3.14, 2.71), (-2.71, 3.14)),
        ((6.28, 5.42), (5.42, 6.28)),
        3,
        "270 degrees turn",
    ),
    (
        ((13.14, 2.71), (-3.14, -2.71)),
        ((-3.14, 2.71), (2.29, 8.14)),
        ((16.28, 5.42), (5.42, 16.28)),
        5,
        "450 degrees turn",
    ),
    (
        ((3.14, 2.71), (-3.14, -2.71)),
        ((-3.14, 2.71), (-3.14, 2.71)),
        ((6.28, 5.42), (6.28, 5.42)),
        4,
        "360 degrees turn",
    ),
    (
        ((3.14, 2.71), (-3.14, -2.71)),
        ((-3.14, 2.71), (-3.14, 2.71)),
        ((6.28, 5.42), (6.28, 5.42)),
        2,
        "180 degrees turn",
    ),
]

rectangle_scale = [
    (
        ((3.14, 2.71), (-3.14, -2.71)),  # Rectangle coordinates
        ((-3.14, 2.71), (-6.28, 5.42)),  # Positions before/after the scale
        ((6.28, 5.42), (12.56, 10.84)),  # Size before/after the scale
        2.0,  # A scale factor
        "second open test",
    ),
    (
        ((3.144, 2.711), (-3.141, -2.714)),
        ((-3.14, 2.71), (-3.14, 2.71)),
        ((6.29, 5.42), (6.29, 5.42)),
        1,
        "no scale",
    ),
    (
        ((3.144, 2.711), (-3.141, -2.714)),
        ((-3.14, 2.71), (-3.55, 3.06)),
        ((6.29, 5.42), (7.1, 6.13)),
        1.13,
        "+13 percent scale",
    ),
    (
        ((3.144, 2.711), (-3.141, -2.714)),
        ((-3.14, 2.71), (-2.92, 2.52)),
        ((6.29, 5.42), (5.85, 5.05)),
        0.93,
        "-7 percent scale",
    ),
    (
        ((3.144, 2.711), (-3.141, -2.714)),
        ((-3.14, 2.71), (-2.9, 2.5)),
        ((6.29, 5.42), (5.81, 5.01)),
        0.9237,
        "-7,63 percent scale",
    ),
    (
        ((3.144, 2.711), (-3.141, -2.714)),
        ((-3.14, 2.71), (0, 0)),
        ((6.29, 5.42), (0, 0)),
        0,
        "zero it out",
    ),
]

# fmt: off
checkers_move = [
    (
        tuple(),
        (
            "X", "B", "X", "B", "X", "B", "X", "B",
            "B", "X", "B", "X", "B", "X", "B", "X",
            "X", "B", "X", "B", "X", "B", "X", "B",
            "X", "X", "X", "X", "X", "X", "X", "X",
            "X", "X", "X", "X", "X", "X", "X", "X",
            "W", "X", "W", "X", "W", "X", "W", "X",
            "X", "W", "X", "W", "X", "W", "X", "W",
            "W", "X", "W", "X", "W", "X", "W", "X",
        ),
        "first open test",
    ),
    (
        (("C3", "D4"), ("H6", "G5")),
        (
            "X", "B", "X", "B", "X", "B", "X", "B",
            "B", "X", "B", "X", "B", "X", "B", "X",
            "X", "B", "X", "B", "X", "B", "X", "X",
            "X", "X", "X", "X", "X", "X", "B", "X",
            "X", "X", "X", "W", "X", "X", "X", "X",
            "W", "X", "X", "X", "W", "X", "W", "X",
            "X", "W", "X", "W", "X", "W", "X", "W",
            "W", "X", "W", "X", "W", "X", "W", "X",
        ),
        "second open test",
    ),
    (
        (  # White moves  black moves
            ("A3", "B4"), ("B6", "A5"),
            ("C3", "D4"), ("C7", "B6"), 
            ("B2", "A3"), ("G7", "H6"),
            ("D2", "C3"), ("D6", "E5"),
            ("G3", "H4"), ("B6", "C5"),
            ("E3", "F4"), ("A7", "B6"),
            ("H2", "G3"), ("E7", "D6"),
            ("F2", "E3"), ("B8", "A7"),
            ("A1", "B2"), ("D8", "C7"),
            ("C1", "D2"), ("F8", "E7"),
            ("E1", "F2"), ("H8", "G7"),
            ("G1", "H2"),
         ),
        (
            "X", "X", "X", "X", "X", "X", "X", "X",  # 8
            "B", "X", "B", "X", "B", "X", "B", "X",  # 7
            "X", "B", "X", "B", "X", "B", "X", "B",  # 6
            "B", "X", "B", "X", "B", "X", "X", "X",  # 5
            "X", "W", "X", "W", "X", "W", "X", "W",  # 4
            "W", "X", "W", "X", "W", "X", "W", "X",  # 3
            "X", "W", "X", "W", "X", "W", "X", "W",  # 2
            "X", "X", "X", "X", "X", "X", "X", "X",  # 1
            # A   B    C    D    E    F    G    H
        ),
        "freeing up the 1st and 8th ranks",
    )
]
# fmt: on

queue_test_data = [
    (range(10), "first open test"),
    (("Hello,", "world!"), "second open test"),
    (
        [
            1,
            "Different",
            0.0,
            "types",
            True,
            {"one": 1, "two": 2},
            ("tuple!", ""),
            []
        ],
        "different data types",
    ),
]
