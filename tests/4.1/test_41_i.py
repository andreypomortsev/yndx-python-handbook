from typing import Callable

import pytest

from tests import utils
from tests.data.test_data_41 import i_test_data


@pytest.mark.parametrize(
    "arg, expected_output, _",
    i_test_data,
    ids=[i[-1] for i in i_test_data],
)
def test_is_prime(
    decorated_function: Callable,
    arg: int,
    expected_output: int,
    _: str,
) -> None:
    returned_output = decorated_function(arg)

    assert returned_output == expected_output


@pytest.mark.xfail(reason="Слишком большие числа на входе.")
def test_is_prime_time_overload(
    decorated_function: Callable,
):
    """
    Проверяет, что функция вызывает TimeLimitExceeded при использовании слишком
    больших чисел.

    Аргументы:
        decorated_function (Callable): Декорированная функция для тестирования.
    """
    a = 2305843009213693951
    with pytest.raises(utils.TimeLimitExceeded):
        decorated_function(a)
