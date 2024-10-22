from types import ModuleType
from typing import Callable

import numpy as np
import pandas as pd
import pytest

from tests import utils
from tests.constants import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_62 import length_stats_test_data


@pytest.mark.parametrize(
    "phrase, expected_series, _",
    length_stats_test_data,
    ids=[i[-1] for i in length_stats_test_data],
)
def test_length_stats(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    phrase: str,
    expected_series: pd.Series,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution = load_module(file_path)

    decorated_func = utils.memory_limit(MEMORY_LIMIT)(solution.length_stats)
    decorated_func = utils.time_limit(TIME_LIMIT)(decorated_func)

    returned_series = decorated_func(phrase)

    assert isinstance(returned_series, pd.Series)

    type_err = "The function should return a pd.Series of integer elements"
    assert np.issubdtype(returned_series.dtype, np.integer), type_err

    assert returned_series.equals(expected_series)
