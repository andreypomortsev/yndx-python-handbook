from types import ModuleType
from typing import Callable, Tuple, Union

import pytest

from tests import utils
from tests.constants import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_42 import g_test_data


@pytest.mark.parametrize(
    "results, expected_outputs, _",
    g_test_data,
    ids=[i[-1] for i in g_test_data],
)
def test_enter_results_get_sum_average(
    request: pytest.FixtureRequest,
    load_module: Callable[[str], ModuleType],
    results: Tuple[Tuple[Union[int, float]]],
    expected_outputs: Tuple[Tuple[Union[int, float]]],
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution = load_module(file_path)

    @utils.memory_limit(MEMORY_LIMIT)
    @utils.time_limit(TIME_LIMIT)
    def solution_wrapper(
        result: Tuple[Union[int, float]]
    ) -> Tuple[Union[int, float]]:
        """
        Оборачиваем исполнение функции в таймер и лимит памяти
        для отслеживания превышений.

        Возвращает:
            get_sum, get_average (Tuple[Union[int, float]]):
            Возвращает результаты выполнения функций get_sum и get_average
        """
        solution.enter_results(*result)
        return solution.get_sum(), solution.get_average()

    for result, expected_output in zip(results, expected_outputs):
        expected_get_sum, expected_get_average = expected_output

        returned_get_sum, returned_get_average = solution_wrapper(result)

        assert returned_get_sum == expected_get_sum
        assert returned_get_average == expected_get_average
