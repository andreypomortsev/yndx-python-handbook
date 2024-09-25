point_init_test_data = [
    (3, 5, "first open test"),
    (2, -7, "second open test"),
    (0.2, -0.7, "floats"),
    (0, 1, "zero one"),
    (1, 0, "one zero"),
    (1000000000000, 99999999999999999, "big numbers"),
    (0.000000000001, 0.0000000000000009, "small numbers"),
]

point_move_test_data = [
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

rectangle_perimeter_test_data = [
    (((3.2, -4.3), (7.52, 3.14)), 23.52, "first open test"),
    (((-3.2, -4.3), (-7.52, -3.14)), 10.96, "negative points"),
    (((1, 2), (3, 4)), 8, "positive points"),
    (((0.01, 0.02), (0.03, 0.04)), 0.08, "small rectangle"),
    (((5.0291, 6.78321), (6.49559, 3.59558)), 9.31, "tricky round"),
]

rectangle_area_test_data = [
    (((7.52, -4.3), (3.2, 3.14)), 32.14, "second open test"),
    (((-3.2, -4.3), (-7.52, -3.14)), 5.01, "negative points"),
    (((0, -4.3), (-7.52, -3.14)), 8.72, "negative points and zero"),
    (((0.01, 0.02), (0.03, 0.04)), 0.00, "small rectangle"),
    (((0.1, 0.2), (0.3, 0.4)), 0.04, "a bit bigger rectangle"),
    (((5.0291, 6.78321), (6.49559, 3.59558)), 4.67, "tricky round"),
]
