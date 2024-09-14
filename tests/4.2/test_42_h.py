from types import FunctionType
from typing import Dict, List, Tuple

import pytest

from tests import utils
from tests.constants import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_42 import h_test_data


@pytest.mark.parametrize(
    "string, expected_output, _",
    h_test_data,
    ids=[i[-1] for i in h_test_data],
)
def test_sort_lambda(
    request: pytest.FixtureRequest,
    string: str,
    expected_output: List[str],
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
        str_lambda: str, string: str, calls: Dict[str, FunctionType]
    ) -> Tuple[int]:
        """
        Оборачиваем исполнение функции в таймер и лимит памяти
        для отслеживания превышений.

        Возвращает:
            (Tuple[int]):
            Возвращает результаты выполнения функций sorted + lambda
        """
        return sorted(string.split(), key=eval(str_lambda, calls))

    safe_calls = {"len": len}
    returned_output = solution_wrapper(solution, string, safe_calls)

    assert returned_output == expected_output
