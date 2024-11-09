from typing import Callable

import numpy as np
import pandas as pd
import pytest

from tests.constants import ELEMENT_TYPE_ERROR, RETURN_TYPE_ERROR
from tests.data.test_data_62 import length_stats_test_data


@pytest.mark.parametrize(
    "phrase, expected_series, _",
    length_stats_test_data,
    ids=[i[-1] for i in length_stats_test_data],
)
def test_length_stats(
    decorated_function: Callable,
    phrase: str,
    expected_series: pd.Series,
    _: str,
) -> None:
    returned_series = decorated_function(phrase)

    assert isinstance(returned_series, pd.Series), RETURN_TYPE_ERROR
    assert np.issubdtype(returned_series.dtype, np.integer), ELEMENT_TYPE_ERROR
    assert returned_series.equals(expected_series)
