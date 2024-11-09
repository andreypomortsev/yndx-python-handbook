from typing import Callable, Dict

import pandas as pd
import pytest

from tests.constants import RETURN_TYPE_ERROR
from tests.data.test_data_62 import cheque_test_data


@pytest.mark.parametrize(
    "prices, products, expected_df, unused_df, unused_str",
    cheque_test_data,
    ids=[i[-1] for i in cheque_test_data],
)
def test_cheque(
    decorated_function: Callable,
    prices: pd.Series,
    products: Dict[str, int],
    expected_df: pd.DataFrame,
    unused_df: pd.DataFrame,  # Df for the D problem
    unused_str: str,  # A name of the test
) -> None:
    returned_series = decorated_function(prices, **products)

    assert isinstance(returned_series, pd.DataFrame), RETURN_TYPE_ERROR
    assert returned_series.equals(expected_df)
