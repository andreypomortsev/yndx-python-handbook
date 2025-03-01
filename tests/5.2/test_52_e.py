from types import ModuleType
from typing import Callable, Optional, Tuple

import pytest

from tests import utils
from tests.data.test_data_52 import fraction_test_data


def test_first_open_test_fraction_class(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    Fraction = solution_module.Fraction

    a = Fraction(1, 3)
    b = Fraction(-2, -6)
    c = Fraction(-3, 9)
    d = Fraction(4, -12)

    test_cases = (
        (a, "1/3", "Fraction('1/3')"),
        (b, "1/3", "Fraction('1/3')"),
        (c, "-1/3", "Fraction('-1/3')"),
        (d, "-1/3", "Fraction('-1/3')"),
    )

    for fraction, str_view, repr_view in test_cases:
        assert str(fraction) == str_view
        assert repr(fraction) == repr_view


def test_second_open_test_fraction_class(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    Fraction = solution_module.Fraction

    a = Fraction("-1/2")
    b = -a

    for fracrion, expected in zip((a, b), ("-1/2", "1/2")):
        assert str(fracrion) == expected

    assert not (a is b)

    b.numerator(-b.numerator())
    a.denominator(-3)

    for fraction, str_view, expected_numerator, expected_denominator in (
        (a, "1/3", 1, 3),
        (b, "-1/2", 1, 2),
    ):
        assert str(fraction) == str_view
        assert fraction.numerator() == expected_numerator
        assert fraction.denominator() == expected_denominator


@pytest.mark.parametrize(
    "digits, str_view, _",
    fraction_test_data["init_h"],
    ids=[i[-1] for i in fraction_test_data["init_h"]],
)
def test_fraction_class_init(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    digits: Tuple[int | str, Optional[int | str]],
    str_view: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    fraction = solution_module.Fraction(*digits)

    assert str(fraction) == str_view


@pytest.mark.parametrize(
    "digits, numerator, expected_return, str_view, _",
    fraction_test_data["numerator_h"],
    ids=[i[-1] for i in fraction_test_data["numerator_h"]],
)
def test_fraction_class_numerator(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    digits: Tuple[int | str, Optional[int | str]],
    numerator: Optional[int],
    expected_return: Optional[int],
    str_view: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    fraction = solution_module.Fraction(*digits)

    assert fraction.numerator(numerator) == expected_return
    assert str(fraction) == str_view


@pytest.mark.parametrize(
    "digits, denominator, expected_return, str_view, _",
    fraction_test_data["denominator_h"],
    ids=[i[-1] for i in fraction_test_data["denominator_h"]],
)
def test_fraction_class_denominator(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    digits: Tuple[int | str, Optional[int | str]],
    denominator: Optional[int],
    expected_return: Optional[int],
    str_view: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    fraction = solution_module.Fraction(*digits)

    assert fraction.denominator(denominator) == expected_return
    assert str(fraction) == str_view


@pytest.mark.parametrize(
    "digits, expected_repr, _",
    fraction_test_data["repr_h"],
    ids=[i[-1] for i in fraction_test_data["repr_h"]],
)
def test_fraction_class_repr(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    digits: Tuple[int, Optional[int]],
    expected_repr: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    fraction = solution_module.Fraction(*digits)

    assert repr(fraction) == expected_repr


@pytest.mark.parametrize(
    "digits, str_view, _",
    fraction_test_data["neg_h"],
    ids=[i[-1] for i in fraction_test_data["neg_h"]],
)
def test_fraction_class_neg(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    digits: Tuple[int | str, Optional[int | str]],
    str_view: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    fraction = solution_module.Fraction(*digits)
    neg_fraction = -fraction

    assert str(neg_fraction) == str_view
    assert neg_fraction is not fraction
