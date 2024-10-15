from tests.data.test_data_41 import j_test_data as merge


def get_value_error() -> None:
    """
    A test function for the problem A 5.3

    Raises: ValueError
    """
    x = int("Hello, world!")


def get_type_error() -> None:
    """
    A test function for the problem A 5.3

    Raises: TypeError
    """
    x = "2" + 2


def get_system_error() -> None:
    """
    A test function for the problem A 5.3

    Raises: SystemError
    """
    raise SystemError


def get_no_errors() -> None:
    """
    A test function for the problem A 5.3

    Does nothing
    """
    return


a_test_data = [
    (get_value_error, "ValueError\n", "first open test"),
    (get_type_error, "TypeError\n", "second open test"),
    (get_system_error, "SystemError\n", "system error"),
    (get_no_errors, "No Exceptions\n", "no errors"),
]


def get_sum(a, b) -> int | float | str:
    """
    A test function for the problem B 5.3

    Returns: sum of two args
    """
    return a + b


def get_prod(a, b) -> int | float | str:
    """
    A test function for the problem B 5.3

    Returns: product of two args
    """
    return a * b


def get_sub(a, b) -> int | float:
    """
    A test function for the problem B 5.3

    Returns: subtraction of two args
    """
    a, b = float(a), float(b)
    return a - b


def get_pow(a, b) -> int | float:
    """
    A test function for the problem B 5.3

    Returns: power of two args
    """
    return a**b


def get_div(a, b) -> int | float:
    """
    A test function for the problem B 5.3

    Returns: division of two args
    """
    a, b = float(a), float(b)
    return a / (b + 1e9)


b_test_data = [
    (get_sum, "first open test"),
    (get_prod, "second open test"),
    (get_sub, "sub"),
    (get_pow, "pow"),
    (get_div, "div"),
]


def concat_str(a, b, c) -> str:
    """
    A test function for the problem C 5.3

    Returns: string of three args
    """
    return "".join(map(str, (a, b, c)))


def get_set(a, b) -> set:
    """
    A test function for the problem C 5.3

    Returns: set of unique elements from two args
    """
    return set(a) ^ set(b)


def get_repr(*args) -> bool:
    """
    A test function for the problem C 5.3

    Returns: string representation of args
    """
    return all(isinstance(repr(arg), str) for arg in args)


def get_str(*args) -> bool:
    """
    A test function for the problem C 5.3

    Returns: string representation of args
    """
    return all(isinstance(str(arg), str) for arg in args)


c_test_data = [
    (concat_str, "first open test"),
    (get_set, "second open test"),
    (get_repr, "repr"),
    (get_str, "str"),
]

d_test_data = {
    "Errors": (
        (("3", 2.5), TypeError, "first open test"),
        ((1, 22313.5), TypeError, "big float"),
        ((122313123132.0, 22313), TypeError, "another big float"),
        (("4", 22313), TypeError, "string and int"),
        ((0.0, "0"), TypeError, "zero as float and string"),
        ((0.0001, 0), TypeError, "float and zero as int"),
        (("0.0", "0"), TypeError, "zeros as strings"),
        ((1, 4), ValueError, "odd first arg"),
        ((12, 47), ValueError, "odd second arg"),
        ((2193121, 130393494351), ValueError, "odd both args"),
        ((-(10**7), 2), ValueError, "big negative num"),
        ((10**5, -2), ValueError, "small negative num"),
        ((-2, -4), ValueError, "both negative nums"),
    ),
    "Values": (
        ((2, 4), 6, "six"),
        ((10**9 + 2, 4), 10**9 + 6, "big int"),
        ((0, 0), 0, "zeros"),
        ((0, -0), 0, "zero minus zero"),
        ((14, 0), 14, "second zero"),
        ((0, 10004), 10004, "first zero"),
        ((8, 482382412012912), 482382412012920, "small + big ints"),
    ),
}

e_test_data = {
    "Errors": (
        ((35, (1, 2, 3)), StopIteration, "first open test"),
        (((1, 2, 3), -21), StopIteration, "not iterable"),
        ((0, -21), StopIteration, "not iterables"),
        (([3, 2, 1], [2.0, 1.1, 100000]), TypeError, "type error"),
        (
            ([-3.3, -2, -1], [-2, -1, 99999999]),
            TypeError,
            "type error negative nums",
        ),
        (
            ([3.3, -2.2, -1.123], [-2.123124, -6643.2312341, 100000]),
            TypeError,
            "type error one int",
        ),
        (([3, 2, 1], range(10)), ValueError, "second open test"),
        ((range(1), (21, 2311, 0)), ValueError, "range and tuple"),
        (([-3, -2, 1], [2, -11, 100000]), ValueError, "one unsorted"),
        (([-3.1, -2.22, -1.9], [-2.01, -2.009, -2.011]), ValueError, "negative numbers"),
    ),
    "Values": merge,  # The same test data as for the problem J 4.1
}
