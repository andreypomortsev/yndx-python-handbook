from types import ModuleType
from typing import Callable, Dict

import pandas as pd
import pytest

from tests import utils
from tests.constants import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_62 import cheque_test_data


@pytest.mark.parametrize(
    "prices, products, expected_df, unused_df, unused_str",
    cheque_test_data,
    ids=[i[-1] for i in cheque_test_data],
)
def test_cheque(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    prices: pd.Series,
    products: Dict[str, int],
    expected_df: pd.DataFrame,
    unused_df: pd.DataFrame,  # Df for the D problem
    unused_str: str,  # A name of the test
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution = load_module(file_path)

    decorated_func = utils.memory_limit(MEMORY_LIMIT)(solution.cheque)
    decorated_func = utils.time_limit(TIME_LIMIT)(decorated_func)

    returned_series = decorated_func(prices, **products)

    assert isinstance(returned_series, pd.DataFrame)
    assert returned_series.equals(expected_df)
