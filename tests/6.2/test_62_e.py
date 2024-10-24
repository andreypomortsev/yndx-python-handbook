from types import ModuleType
from typing import Callable, Dict

import pandas as pd
import pytest

from tests import utils
from tests.constants import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_62 import get_long_test_data


@pytest.mark.parametrize(
    "to_filter, lenght, filtered_series, _",
    get_long_test_data,
    ids=[i[-1] for i in get_long_test_data],
)
def test_get_long(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    to_filter: pd.Series,
    lenght: Dict[str, int],
    filtered_series: pd.Series,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution = load_module(file_path)

    decorated_func = utils.memory_limit(MEMORY_LIMIT)(solution.get_long)
    decorated_func = utils.time_limit(TIME_LIMIT)(decorated_func)

    returned_series = decorated_func(to_filter, **lenght)

    assert isinstance(returned_series, pd.Series)
    assert returned_series.equals(filtered_series)

    # Don't apply when there is nothing to filter
    if not to_filter.equals(filtered_series):
        err_msg = "The function should not modify the input series."
        assert not filtered_series.equals(to_filter), err_msg
