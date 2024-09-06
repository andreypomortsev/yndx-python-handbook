from typing import Callable, Tuple

import pytest

from tests import utils
from tests.data.test_data_41 import j_test_data


@pytest.mark.parametrize(
    "args, expected_output, _",
    j_test_data,
    ids=[i[-1] for i in j_test_data],
)
def test_input_output(
    decorated_function: Callable,
    args: Tuple[Tuple[int]],
    expected_output: Tuple[int],
    _: str,
) -> None:
    returned_output = decorated_function(*args)

    assert returned_output == expected_output


@pytest.mark.slow
@pytest.mark.xfail(reason="Слишком большие числа на входе.")
def test_memory_overload(
    decorated_function: Callable,
):
    """
    Проверяет, что функция вызывает MemoryLimitExceeded при использовании
    слишком больших чисел.

    Аргументы:
        decorated_function (Callable): Декорированная функция для тестирования.
    """
    first = tuple(range(10**6))

    with pytest.raises(utils.MemoryLimitExceeded):
        decorated_function(first, first)

    del first
