from types import ModuleType
from typing import Callable, Dict

import pandas as pd
import pytest

from tests import utils
from tests.constants import (MEMORY_LIMIT, NO_CHANGE_ERROR, RETURN_TYPE_ERROR,
                             TIME_LIMIT)
from tests.data.test_data_62 import cheque_test_data


@pytest.mark.parametrize(
    "prices, products, expected_cheque, expected_discount, _",
    cheque_test_data,
    ids=[i[-1] for i in cheque_test_data],
)
def test_cheque_discount(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    decorated_function: Callable,
    prices: pd.Series,
    products: Dict[str, int],
    expected_cheque: pd.DataFrame,
    expected_discount: pd.DataFrame,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution = load_module(file_path)

    decorated_func = utils.memory_limit(MEMORY_LIMIT)(solution.cheque)
    decorated_func = utils.time_limit(TIME_LIMIT)(decorated_func)

    cheque_df = decorated_func(prices, **products)

    assert isinstance(cheque_df, pd.DataFrame), RETURN_TYPE_ERROR
    assert cheque_df.equals(expected_cheque)

    returned_df = decorated_function(cheque_df)

    assert isinstance(returned_df, pd.DataFrame), RETURN_TYPE_ERROR
    assert returned_df.equals(expected_discount)

    # Check that the cheque function didn't change the cheque_df
    assert cheque_df.equals(expected_cheque), NO_CHANGE_ERROR
