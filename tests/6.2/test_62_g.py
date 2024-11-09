from typing import Callable

import pandas as pd
import pytest

from tests.constants import NO_CHANGE_ERROR, RETURN_TYPE_ERROR
from tests.data.test_data_62 import filter_test_data


@pytest.mark.parametrize(
    "df_to_filter, unused_df, expected_return_nwb, unused_df_2, unused_str",
    filter_test_data,
    ids=[i[-1] for i in filter_test_data],
)
def test_need_to_work_better(
    decorated_function: Callable,
    df_to_filter: pd.DataFrame,
    unused_df: pd.DataFrame,  # Excpected return of the F solution 6.2
    expected_return_nwb: pd.DataFrame,
    unused_df_2: pd.DataFrame,  # Excpected return of the H solution 6.2
    unused_str: str,  # A test name
) -> None:
    equal = df_to_filter.equals(expected_return_nwb)
    returned = decorated_function(df_to_filter)

    assert isinstance(returned, pd.DataFrame), RETURN_TYPE_ERROR
    assert returned.equals(expected_return_nwb)

    if not equal:
        assert not df_to_filter.equals(expected_return_nwb), NO_CHANGE_ERROR
