import os

time_limit_data_pas = [
    (None, "passes w/o arg"),
    (0.1, "passes for 10 ms"),
    (0, "passes for 0"),
    (0.93, "passes for 93 ms"),
    (0.89, "passes for 89 ms"),
]

time_limit_data_fail = [
    (None, "fails w/o arg"),
    (1.3, "fails with 130 ms"),
    (1.07, "fails with 107 ms"),
    (11.0, "fails with 11 s"),
]

generate_error_msg_data = [
    ("string", "another string", "strings"),
    (["string"], ["another string"], "lists"),
    ([], [], "empty lists"),
    (tuple(), tuple("tuple"), "empty tuples"),
    (["list"], tuple("tuple"), "list tuple"),
    (tuple("another tuple"), ["another list"], "tuple list"),
    ([""], ["another string"], "one empty list"),
    (12, 21, "digits"),
    (12, "21", "digit string"),
    ("12", 221, "string digit"),
]

compare_output_data_pas = [
    ("right answer", "right answer", "strings test"),
    ("вдисолжеп\n", ("исолвдепж\n",), "tuple test"),
    (
        "сосна\n"
        "медведь\n"
        "белочка\n"
        "зайка\n"
        "березка\n"
        "волк\n"
        "елочка\n",
        [
            "сосна\n"
            "березка\n"
            "волк\n"
            "елочка\n"
            "медведь\n"
            "белочка\n"
            "зайка\n",
        ],
        "list test",
    ),
]

assert_equal_data = [
    ("World\n", "Hello, World!", "Hello, World!"),
    ("\n", "Hello, !", "empty input"),
]

get_tested_file_details_data = [
    (
        os.path.join("yndx-python-handbook", "tests", "2.1", "test_21_a.py"),
        (
            os.path.join(
                "",
                "yndx-python-handbook",
                "tests",
                "2.1",
                "..",
                "..",
                "solutions",
                "2.1",
                "21_a.py",
            ),
            "21_a",
        ),
        "21_a",
    ),
    (
        os.path.join("yndx-python-handbook", "tests", "3.1", "test_31_t.py"),
        (
            os.path.join(
                "",
                "yndx-python-handbook",
                "tests",
                "3.1",
                "..",
                "..",
                "solutions",
                "3.1",
                "31_t.py",
            ),
            "31_t",
        ),
        "31_t",
    ),
    (
        os.path.join("yndx-python-handbook", "tests", "4.1", "test_41_b.py"),
        (
            os.path.join(
                "",
                "yndx-python-handbook",
                "tests",
                "4.1",
                "..",
                "..",
                "solutions",
                "4.1",
                "41_b.py",
            ),
            "41_b",
        ),
        "41_b",
    ),
]

add_file_to_cleanup_data = [
    (
        None,
        ["/tests/wrapped_21_a.py"],
        ["/tests/wrapped_21_a.py"],
        "No initial paths, add one file",
    ),
    (
        [],
        ["/tests/wrapped_21_a.py"],
        ["/tests/wrapped_21_a.py"],
        "Empty initial paths, add one file",
    ),
    (
        ["/tests/wrapped_32_j.py"],
        ["/tests/wrapped_21_a.py"],
        ["/tests/wrapped_32_j.py", "/tests/wrapped_21_a.py"],
        "Existing paths, add one file",
    ),
    (
        ["/tests/wrapped_32_j.py"],
        ["/tests/wrapped_21_a.py", "/tests/random file.txt"],
        [
            "/tests/wrapped_32_j.py",
            "/tests/wrapped_21_a.py",
            "/tests/random file.txt",
        ],
        "Existing paths, add multiple files",
    ),
    (
        None,
        ["/tests/wrapped_21_a.py", "/tests/file.log", "/tests/file3.txt"],
        ["/tests/wrapped_21_a.py", "/tests/file.log", "/tests/file3.txt"],
        "No initial paths, add multiple files",
    ),
]

function_calls = [
    (None, 0, None, "zero calls"),
    (0, 1, 1, "one call"),
    (5, 6, 120, "six call"),
]
