from typing import Callable, Tuple

import numpy as np
import pandas as pd
import pytest

from tests.constants import ELEMENT_TYPE_ERROR, RETURN_TYPE_ERROR
from tests.data.test_data_62 import length_stats_test_data_2


@pytest.mark.parametrize(
    "phrase, expected_series, _",
    length_stats_test_data_2,
    ids=[i[-1] for i in length_stats_test_data_2],
)
def test_length_stats_2(
    decorated_function: Callable,
    phrase: str,
    expected_series: Tuple[pd.Series, pd.Series],
    _: str,
) -> None:
    returned_series = decorated_function(phrase)

    for returned, expected in zip(returned_series, expected_series):
        assert isinstance(returned, pd.Series), RETURN_TYPE_ERROR
        assert np.issubdtype(returned.dtype, np.integer), ELEMENT_TYPE_ERROR
        assert returned.equals(expected)
