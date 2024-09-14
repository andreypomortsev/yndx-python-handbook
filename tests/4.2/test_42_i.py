from types import FunctionType
from typing import Dict, Tuple

import pytest

from tests import utils
from tests.constants import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_42 import i_test_data


@pytest.mark.parametrize(
    "input, expected_output, _",
    i_test_data,
    ids=[i[-1] for i in i_test_data],
)
def test_filter_lambda(
    request: pytest.FixtureRequest,
    input: Tuple[int],
    expected_output: Tuple[str],
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)

    with open(file_path, "r", encoding="UTF-8") as solution_file:
        lines = solution_file.readlines()
        solution = "".join(lines)

    if not solution.startswith("lambda"):
        raise SyntaxError("Compilation error (CE)")

    @utils.memory_limit(MEMORY_LIMIT)
    @utils.time_limit(TIME_LIMIT)
    def solution_wrapper(
        str_lambda: str, input: Tuple[int], calls: Dict[str, FunctionType]
    ) -> Tuple[int]:
        """
        Оборачиваем исполнение функции в таймер и лимит памяти
        для отслеживания превышений.

        Возвращает:
            (Tuple[int]):
            Возвращает результаты выполнения функций filter + lambda
        """
        return tuple(filter(eval(str_lambda, calls), input))

    safe_calls = {"sum": sum, "map": map, "str": str}
    returned_output = solution_wrapper(solution, input, safe_calls)

    assert returned_output == expected_output
