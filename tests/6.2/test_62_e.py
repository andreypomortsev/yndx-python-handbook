from typing import Callable, Dict

import pandas as pd
import pytest

from tests.constants import NO_CHANGE_ERROR, RETURN_TYPE_ERROR
from tests.data.test_data_62 import get_long_test_data


@pytest.mark.parametrize(
    "to_filter, lenght, filtered_series, _",
    get_long_test_data,
    ids=[i[-1] for i in get_long_test_data],
)
def test_get_long(
    decorated_function: Callable,
    to_filter: pd.Series,
    lenght: Dict[str, int],
    filtered_series: pd.Series,
    _: str,
) -> None:
    returned_series = decorated_function(to_filter, **lenght)

    assert isinstance(returned_series, pd.Series), RETURN_TYPE_ERROR
    assert returned_series.equals(filtered_series)

    # Doesn't apply when there is nothing to filter
    if not to_filter.equals(filtered_series):
        assert not filtered_series.equals(to_filter), NO_CHANGE_ERROR
