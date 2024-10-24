from types import ModuleType
from typing import Callable

import pandas as pd
import pytest

from tests import utils
from tests.constants import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_62 import filter_test_data


@pytest.mark.parametrize(
    "df_to_filter, unused_df, expected_return_nwb, unused_df_2, unused_str",
    filter_test_data,
    ids=[i[-1] for i in filter_test_data],
)
def test_need_to_work_better(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    df_to_filter: pd.DataFrame,
    unused_df: pd.DataFrame,  # Excpected return of the F solution 6.2
    expected_return_nwb: pd.DataFrame,
    unused_df_2: pd.DataFrame,  # Excpected return of the H solution 6.2
    unused_str: str,  # A test name
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution = load_module(file_path)

    decorated_func = utils.memory_limit(MEMORY_LIMIT)(
        solution.need_to_work_better
    )
    decorated_func = utils.time_limit(TIME_LIMIT)(decorated_func)

    equal = df_to_filter.equals(expected_return_nwb)
    returned = decorated_func(df_to_filter)

    assert isinstance(returned, pd.DataFrame)
    assert returned.equals(expected_return_nwb)

    if not equal:
        err_msg = "The function should not modify the input DataFrame."
        assert not df_to_filter.equals(expected_return_nwb), err_msg
