from typing import Callable

import pandas as pd
import pytest

from tests.constants import NO_CHANGE_ERROR, RETURN_TYPE_ERROR
from tests.data.test_data_62 import filter_test_data


@pytest.mark.parametrize(
    "df_to_filter, expected_return_best, unused_df, unused_df_2, unused_str",
    filter_test_data,
    ids=[i[-1] for i in filter_test_data],
)
def test_best(
    decorated_function: Callable,
    df_to_filter: pd.DataFrame,
    expected_return_best: pd.DataFrame,
    unused_df: pd.DataFrame,  # Excpected return of the G solution 6.2
    unused_df_2: pd.DataFrame,  # Excpected return of the H solution 6.2
    unused_str: str,  # A test name
) -> None:
    equal = df_to_filter.equals(expected_return_best)
    returned = decorated_function(df_to_filter)

    assert isinstance(returned, pd.DataFrame), RETURN_TYPE_ERROR
    assert returned.equals(expected_return_best)

    if not equal:
        assert not df_to_filter.equals(expected_return_best), NO_CHANGE_ERROR
