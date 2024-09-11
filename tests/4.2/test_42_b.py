from typing import Callable, Tuple, Union

import pytest

from tests.data.test_data_42 import b_test_data


@pytest.mark.parametrize(
    "args, expected_output, _",
    b_test_data,
    ids=[i[-1] for i in b_test_data],
)
def test_make_matrix(
    decorated_function: Callable,
    args: Tuple[Union[Tuple[int], int]],
    expected_output: Tuple[int],
    _: str,
) -> None:
    returned_output = decorated_function(*args)

    assert returned_output == expected_output

    returned_output[0][0] = "c"
    expected_output[0][0] = "c"
    
    error_msg = "Все строки матрицы являются одним и тем же списком."
    
    assert returned_output == expected_output, error_msg
