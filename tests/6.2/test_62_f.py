from types import ModuleType
from typing import Callable

import pandas as pd
import pytest

from tests import utils
from tests.constants import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_62 import filter_test_data


@pytest.mark.parametrize(
    "df_to_filter, expected_return_best, unused_df, unused_df_2, unused_str",
    filter_test_data,
    ids=[i[-1] for i in filter_test_data],
)
def test_best(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    df_to_filter: pd.DataFrame,
    expected_return_best: pd.DataFrame,
    unused_df: pd.DataFrame,  # Excpected return of the G solution 6.2
    unused_df_2: pd.DataFrame,  # Excpected return of the H solution 6.2
    unused_str: str,  # A test name
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution = load_module(file_path)

    decorated_func = utils.memory_limit(MEMORY_LIMIT)(solution.best)
    decorated_func = utils.time_limit(TIME_LIMIT)(decorated_func)

    equal = df_to_filter.equals(expected_return_best)
    returned = decorated_func(df_to_filter)

    assert isinstance(returned, pd.DataFrame)
    assert returned.equals(expected_return_best)

    if not equal:
        err_msg = "The function should not modify the input DataFrame."
        assert not df_to_filter.equals(expected_return_best), err_msg
