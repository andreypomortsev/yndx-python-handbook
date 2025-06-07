import os

time_limit_data_pas = [
    (None, "passes w/o arg"),
    (0.1, "passes for 10 ms"),
    (0, "passes for 0"),
    (0.91, "passes for 91 ms"),
    (0.49, "passes for 49 ms"),
]

time_limit_data_fail = [
    (None, "fails w/o arg"),
    (1.3, "fails with 130 ms"),
    (1.1, "fails with 110 ms"),
    (2.0, "fails with 2 s"),
]

get_mocked_print = [
    (
        "World\n",
        "Hello, World!\n",
        lambda: print(f"Hello, {input()}!"),
        "Hello, World!",
    ),
    ("\n", "Hello, !\n", lambda: print(f"Hello, {input()}!"), "empty input"),
    ("2\n", "4\n", lambda: print(int(input()) * 2), "double input"),
    (
        "Some text\n",
        "Some\ntext\n",
        lambda: print(*input().split(), sep="\n"),
        "split into lines",
    ),
    (
        "Set Set test test test\n",
        "Set\ntest\n",
        lambda: print(*sorted(set(input().split())), sep="\n"),
        "unique words",
    ),
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
