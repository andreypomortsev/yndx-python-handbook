from types import ModuleType
from typing import Callable, Tuple

import pandas as pd
import pytest

from tests import utils
from tests.constants import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_62 import j_test_data


@pytest.mark.parametrize(
    "input_data, expected_return_from_values, unused_tuple, unused_str",
    j_test_data,
    ids=[i[-1] for i in j_test_data],
)
def test_values(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    input_data: Tuple[Callable[[int | float], float], float, float, float],
    expected_return_from_values: pd.Series,
    unused_tuple: Tuple[float, float],  # Min and max expected returns
    unused_str: str,  # A test name
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution = load_module(file_path)

    # Decorate the values function to monitor memory and time usage
    decorated_func = utils.memory_limit(MEMORY_LIMIT)(solution.values)
    decorated_func = utils.time_limit(TIME_LIMIT)(decorated_func)

    returned_series = decorated_func(*input_data)

    assert isinstance(returned_series, pd.Series)
    assert returned_series.equals(expected_return_from_values)


@pytest.mark.parametrize(
    "input_data, unused_series, min_max, unused_str",
    j_test_data,
    ids=[i[-1] for i in j_test_data],
)
def test_min_max_extremums(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    input_data: Tuple[Callable[[int | float], float], float, float, float],
    unused_series: pd.Series,  # The value function expected returns
    min_max: Tuple[float, float],
    unused_str: str,  # A test name
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution = load_module(file_path)

    returned_values = solution.values(*input_data)

    # Decorate the min_extremum to monitor memory and time usage
    decorated_min_extr = utils.memory_limit(MEMORY_LIMIT)(
        solution.min_extremum
    )
    decorated_min_extr = utils.time_limit(TIME_LIMIT)(decorated_min_extr)
    returned_minimum = decorated_min_extr(returned_values)

    # Decorate the max_extremum to monitor memory and time usage
    decorated_max_extr = utils.memory_limit(MEMORY_LIMIT)(
        solution.max_extremum
    )
    decorated_max_extr = utils.time_limit(TIME_LIMIT)(decorated_max_extr)
    returned_maximum = decorated_max_extr(returned_values)

    assert min_max[0] == returned_minimum, "Minimum value is incorrect"
    assert min_max[1] == returned_maximum, "Maximum value is incorrect"
