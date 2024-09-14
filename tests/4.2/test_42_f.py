from types import ModuleType
from typing import Callable, Dict, Tuple

import pytest

from tests import utils
from tests.conftest import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_42 import f_test_data


@pytest.mark.parametrize(
    "in_stock_values, args, expected_outputs, _",
    f_test_data,
    ids=[i[-1] for i in f_test_data],
)
def test_order(
    request: pytest.FixtureRequest,
    load_module: Callable[[str], ModuleType],
    in_stock_values: Dict[str, int],
    args: Tuple[Tuple[str]],
    expected_outputs: Tuple[Tuple[str]],
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    setattr(solution_module, "in_stock", in_stock_values)

    decorated_func = utils.memory_limit(MEMORY_LIMIT)(solution_module.order)
    decorated_func = utils.time_limit(TIME_LIMIT)(decorated_func)

    for arg, expected_output in zip(args, expected_outputs):
        returned_output = decorated_func(*arg)
        assert returned_output == expected_output
