patched_point_init = [
    (tuple(), "first open test 5,2"),
    ((2, -7), "ints"),
    ((0.213, -13.7), "floats"),
    (((0.2, -0.7),), "tuple of floats"),
    (((2, -7),), "tuple of ints"),
]

patched_point_str_repr = [
    (((2, -7),), "(2, -7)", "PatchedPoint(2, -7)", "second open test 1"),
    ((7, 9), "(7, 9)", "PatchedPoint(7, 9)", "second open test 2"),
    (
        ((0.07, 0.09),),
        "(0.07, 0.09)",
        "PatchedPoint(0.07, 0.09)",
        "tuple of floats",
    ),
    ((7.21, 9.02), "(7.21, 9.02)", "PatchedPoint(7.21, 9.02)", "floats"),
    (tuple(), "(0, 0)", "PatchedPoint(0, 0)", "w/o coordinates"),
    ((0, 0), "(0, 0)", "PatchedPoint(0, 0)", "zero coordinates"),
    (((0, 0),), "(0, 0)", "PatchedPoint(0, 0)", "seros in tuple"),
]

patched_point_add = [
    (tuple(), (2, -3), "first open test"),
    ((-2, 3), (2, -3), "zero point"),
    (((0.012, 3212),), (0, 0), "zero difference with tuple of mixed"),
    (tuple(), (0, 0), "zero difference w/o coordinates"),
    ((121, 989), (0, 0), "zero difference with ints"),
]
