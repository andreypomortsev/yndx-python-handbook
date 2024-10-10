from types import ModuleType
from typing import Callable, Optional, Tuple

import pytest

from tests import utils
from tests.data.test_data_52 import fraction_test_data


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
    "digits, str_view, _",
    fraction_test_data["reverse_h"],
    ids=[i[-1] for i in fraction_test_data["reverse_h"]],
)
def test_fraction_class_reverse(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    digits: Tuple[int | str, Optional[int | str]],
    str_view: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    fraction = solution_module.Fraction(*digits)
    reversed_fraction = fraction.reverse()

    assert str(reversed_fraction) == str_view
    assert reversed_fraction is not fraction


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


@pytest.mark.parametrize(
    "first_digits, second_digits, str_out, _",
    fraction_test_data["add_h"],
    ids=[i[-1] for i in fraction_test_data["add_h"]],
)
def test_fraction_class_add(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    first_digits: Tuple[int | str, Optional[int | str]],
    second_digits: Tuple[int | str, Optional[int | str]],
    str_out: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    frst_fraction = solution_module.Fraction(*first_digits)
    scnd_fraction = solution_module.Fraction(*second_digits)

    sum_fraction = frst_fraction + scnd_fraction

    assert str(sum_fraction) == str_out
    assert sum_fraction is not frst_fraction
    assert sum_fraction is not scnd_fraction


@pytest.mark.parametrize(
    "first_digits, second_digits, str_out, _",
    fraction_test_data["add_h"],
    ids=[i[-1] for i in fraction_test_data["add_h"]],
)
def test_fraction_class_iadd(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    first_digits: Tuple[int | str, Optional[int | str]],
    second_digits: Tuple[int | str, Optional[int | str]],
    str_out: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    frst_fraction = solution_module.Fraction(*first_digits)
    scnd_fraction = solution_module.Fraction(*second_digits)

    old_first_fraction = frst_fraction
    frst_fraction += scnd_fraction

    assert str(frst_fraction) == str_out
    assert old_first_fraction is frst_fraction
    assert frst_fraction is not scnd_fraction


@pytest.mark.parametrize(
    "first_digits, second_digits, str_out, _",
    fraction_test_data["sub_h"],
    ids=[i[-1] for i in fraction_test_data["sub_h"]],
)
def test_fraction_class_sub(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    first_digits: Tuple[int | str, Optional[int | str]],
    second_digits: Tuple[int | str, Optional[int | str]],
    str_out: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    frst_fraction = solution_module.Fraction(*first_digits)
    scnd_fraction = solution_module.Fraction(*second_digits)

    sum_fraction = frst_fraction - scnd_fraction

    assert str(sum_fraction) == str_out
    assert sum_fraction is not frst_fraction
    assert sum_fraction is not scnd_fraction


@pytest.mark.parametrize(
    "first_digits, second_digits, str_out, _",
    fraction_test_data["sub_h"],
    ids=[i[-1] for i in fraction_test_data["sub_h"]],
)
def test_fraction_class_isub(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    first_digits: Tuple[int | str, Optional[int | str]],
    second_digits: Tuple[int | str, Optional[int | str]],
    str_out: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    frst_fraction = solution_module.Fraction(*first_digits)
    scnd_fraction = solution_module.Fraction(*second_digits)

    old_first_fraction = frst_fraction
    frst_fraction -= scnd_fraction

    assert str(frst_fraction) == str_out
    assert old_first_fraction is frst_fraction
    assert frst_fraction is not scnd_fraction


@pytest.mark.parametrize(
    "first_digits, second_digits, str_out, _",
    fraction_test_data["mul_h"],
    ids=[i[-1] for i in fraction_test_data["mul_h"]],
)
def test_fraction_class_mul(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    first_digits: Tuple[int | str, Optional[int | str]],
    second_digits: Tuple[int | str, Optional[int | str]],
    str_out: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    frst_fraction = solution_module.Fraction(*first_digits)
    scnd_fraction = solution_module.Fraction(*second_digits)

    sum_fraction = frst_fraction * scnd_fraction

    assert str(sum_fraction) == str_out
    assert sum_fraction is not frst_fraction
    assert sum_fraction is not scnd_fraction


@pytest.mark.parametrize(
    "first_digits, second_digits, str_out, _",
    fraction_test_data["mul_h"],
    ids=[i[-1] for i in fraction_test_data["mul_h"]],
)
def test_fraction_class_imul(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    first_digits: Tuple[int | str, Optional[int | str]],
    second_digits: Tuple[int | str, Optional[int | str]],
    str_out: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    frst_fraction = solution_module.Fraction(*first_digits)
    scnd_fraction = solution_module.Fraction(*second_digits)

    old_first_fraction = frst_fraction
    frst_fraction *= scnd_fraction

    assert str(frst_fraction) == str_out
    assert old_first_fraction is frst_fraction
    assert frst_fraction is not scnd_fraction


@pytest.mark.parametrize(
    "first_digits, second_digits, str_out, _",
    fraction_test_data["truediv_h"],
    ids=[i[-1] for i in fraction_test_data["truediv_h"]],
)
def test_fraction_class_truediv(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    first_digits: Tuple[int | str, Optional[int | str]],
    second_digits: Tuple[int | str, Optional[int | str]],
    str_out: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    frst_fraction = solution_module.Fraction(*first_digits)
    scnd_fraction = solution_module.Fraction(*second_digits)

    sum_fraction = frst_fraction / scnd_fraction

    assert str(sum_fraction) == str_out
    assert sum_fraction is not frst_fraction
    assert sum_fraction is not scnd_fraction


@pytest.mark.parametrize(
    "first_digits, second_digits, str_out, _",
    fraction_test_data["truediv_h"],
    ids=[i[-1] for i in fraction_test_data["truediv_h"]],
)
def test_fraction_class_itruediv(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    first_digits: Tuple[int | str, Optional[int | str]],
    second_digits: Tuple[int | str, Optional[int | str]],
    str_out: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    frst_fraction = solution_module.Fraction(*first_digits)
    scnd_fraction = solution_module.Fraction(*second_digits)

    old_first_fraction = frst_fraction
    frst_fraction /= scnd_fraction

    assert str(frst_fraction) == str_out
    assert old_first_fraction is frst_fraction
    assert frst_fraction is not scnd_fraction
