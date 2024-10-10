from types import ModuleType
from typing import Callable, Optional, Tuple

import pytest

from tests import utils
from tests.data.test_data_52 import fraction_test_data


@pytest.mark.parametrize(
    "digits, str_view, _",
    fraction_test_data["init"],
    ids=[i[-1] for i in fraction_test_data["init"]],
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
    fraction_test_data["numerator"],
    ids=[i[-1] for i in fraction_test_data["numerator"]],
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
    fraction_test_data["denominator"],
    ids=[i[-1] for i in fraction_test_data["denominator"]],
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
    fraction_test_data["reverse"],
    ids=[i[-1] for i in fraction_test_data["reverse"]],
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
    fraction_test_data["repr"],
    ids=[i[-1] for i in fraction_test_data["repr"]],
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
    fraction_test_data["neg"],
    ids=[i[-1] for i in fraction_test_data["neg"]],
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
    fraction_test_data["add"],
    ids=[i[-1] for i in fraction_test_data["add"]],
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
    fraction_test_data["add"],
    ids=[i[-1] for i in fraction_test_data["add"]],
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
    "digits, number, str_out, _",
    fraction_test_data["radd"],
    ids=[i[-1] for i in fraction_test_data["radd"]],
)
def test_fraction_class_radd(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    digits: Tuple[int | str, Optional[int | str]],
    number: int,
    str_out: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    fraction = solution_module.Fraction(*digits)

    new_fraction = number + fraction
    newest_fraction = fraction + number

    assert str(new_fraction) == str_out

    assert new_fraction.numerator() == newest_fraction.numerator()
    assert new_fraction.denominator() == newest_fraction.denominator()

    assert new_fraction is not fraction
    assert newest_fraction is not fraction
    assert new_fraction is not newest_fraction


@pytest.mark.parametrize(
    "first_digits, second_digits, str_out, _",
    fraction_test_data["sub"],
    ids=[i[-1] for i in fraction_test_data["sub"]],
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
    fraction_test_data["sub"],
    ids=[i[-1] for i in fraction_test_data["sub"]],
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
    "digits, number, str_out, _",
    fraction_test_data["rsub"],
    ids=[i[-1] for i in fraction_test_data["rsub"]],
)
def test_fraction_class_rsub(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    digits: Tuple[int | str, Optional[int | str]],
    number: int,
    str_out: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    fraction = solution_module.Fraction(*digits)

    new_fraction = number - fraction

    assert str(new_fraction) == str_out
    assert new_fraction is not fraction


@pytest.mark.parametrize(
    "first_digits, second_digits, str_out, _",
    fraction_test_data["mul"],
    ids=[i[-1] for i in fraction_test_data["mul"]],
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
    fraction_test_data["mul"],
    ids=[i[-1] for i in fraction_test_data["mul"]],
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
    "digits, number, str_out, _",
    fraction_test_data["rmul"],
    ids=[i[-1] for i in fraction_test_data["rmul"]],
)
def test_fraction_class_rmul(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    digits: Tuple[int | str, Optional[int | str]],
    number: int,
    str_out: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    fraction = solution_module.Fraction(*digits)

    new_fraction = number * fraction
    newest_fraction = fraction * number

    assert str(new_fraction) == str_out

    assert new_fraction.numerator() == newest_fraction.numerator()
    assert new_fraction.denominator() == newest_fraction.denominator()

    assert new_fraction is not fraction
    assert newest_fraction is not fraction
    assert new_fraction is not newest_fraction


@pytest.mark.parametrize(
    "first_digits, second_digits, str_out, _",
    fraction_test_data["truediv"],
    ids=[i[-1] for i in fraction_test_data["truediv"]],
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
    fraction_test_data["truediv"],
    ids=[i[-1] for i in fraction_test_data["truediv"]],
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


@pytest.mark.parametrize(
    "digits, number, str_out, _",
    fraction_test_data["rtruediv"],
    ids=[i[-1] for i in fraction_test_data["rtruediv"]],
)
def test_fraction_class_rtruediv(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    digits: Tuple[int | str, Optional[int | str]],
    number: int,
    str_out: str,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    fraction = solution_module.Fraction(*digits)

    new_fraction = number / fraction

    assert str(new_fraction) == str_out
    assert new_fraction is not fraction


@pytest.mark.parametrize(
    "first_digits, second_digits, expected_result, _",
    fraction_test_data["gt"],
    ids=[i[-1] for i in fraction_test_data["gt"]],
)
def test_fraction_class_gt(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    first_digits: Tuple[int | str, Optional[int | str]],
    second_digits: Tuple[int | str, Optional[int | str]],
    expected_result: bool,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    frst_fraction = solution_module.Fraction(*first_digits)
    scnd_fraction = solution_module.Fraction(*second_digits)

    result = frst_fraction > scnd_fraction

    assert result == expected_result


@pytest.mark.parametrize(
    "first_digits, second_digits, expected_result, _",
    fraction_test_data["ge"],
    ids=[i[-1] for i in fraction_test_data["ge"]],
)
def test_fraction_class_ge(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    first_digits: Tuple[int | str, Optional[int | str]],
    second_digits: Tuple[int | str, Optional[int | str]],
    expected_result: bool,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    frst_fraction = solution_module.Fraction(*first_digits)
    scnd_fraction = solution_module.Fraction(*second_digits)

    result = frst_fraction >= scnd_fraction

    assert result == expected_result


@pytest.mark.parametrize(
    "first_digits, second_digits, expected_result, _",
    fraction_test_data["lt"],
    ids=[i[-1] for i in fraction_test_data["lt"]],
)
def test_fraction_class_lt(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    first_digits: Tuple[int | str, Optional[int | str]],
    second_digits: Tuple[int | str, Optional[int | str]],
    expected_result: bool,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    frst_fraction = solution_module.Fraction(*first_digits)
    scnd_fraction = solution_module.Fraction(*second_digits)

    result = frst_fraction < scnd_fraction

    assert result == expected_result


@pytest.mark.parametrize(
    "first_digits, second_digits, expected_result, _",
    fraction_test_data["le"],
    ids=[i[-1] for i in fraction_test_data["le"]],
)
def test_fraction_class_le(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    first_digits: Tuple[int | str, Optional[int | str]],
    second_digits: Tuple[int | str, Optional[int | str]],
    expected_result: bool,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    frst_fraction = solution_module.Fraction(*first_digits)
    scnd_fraction = solution_module.Fraction(*second_digits)

    result = frst_fraction <= scnd_fraction

    assert result == expected_result


@pytest.mark.parametrize(
    "first_digits, second_digits, expected_result, _",
    fraction_test_data["eq"],
    ids=[i[-1] for i in fraction_test_data["eq"]],
)
def test_fraction_class_eq(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    first_digits: Tuple[int | str, Optional[int | str]],
    second_digits: Tuple[int | str, Optional[int | str]],
    expected_result: bool,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    frst_fraction = solution_module.Fraction(*first_digits)
    scnd_fraction = solution_module.Fraction(*second_digits)

    result = frst_fraction == scnd_fraction

    assert result == expected_result


@pytest.mark.parametrize(
    "first_digits, second_digits, expected_result, _",
    fraction_test_data["ne"],
    ids=[i[-1] for i in fraction_test_data["ne"]],
)
def test_fraction_class_ne(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    first_digits: Tuple[int | str, Optional[int | str]],
    second_digits: Tuple[int | str, Optional[int | str]],
    expected_result: bool,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    frst_fraction = solution_module.Fraction(*first_digits)
    scnd_fraction = solution_module.Fraction(*second_digits)

    result = frst_fraction != scnd_fraction

    assert result == expected_result


def test_fraction_class_raises(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    with pytest.raises(TypeError) as info:
        fraction = solution_module.Fraction(2, 1)
        fraction += ("error",)

    assert "Неподдерживаемый тип" in str(info.value)
