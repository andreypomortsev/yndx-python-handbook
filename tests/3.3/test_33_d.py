from types import ModuleType
from typing import Dict, List, Set, Tuple, Union

import pytest

from tests.data.test_data_33 import d_test_data


@pytest.mark.parametrize(
    "input_data, expected_output, _",  # _ - название теста
    d_test_data,
    ids=[i[2] for i in d_test_data],  # Считываем названия тестов
)
def test_input_output(
    setup_environment: Tuple[ModuleType, str],
    input_data: Dict[str, Union[str, int, List[int]]],
    expected_output: Set[int],
    _: str,
) -> None:

    variable_values = [value for value in input_data.values()]
    wrapped_module, _ = setup_environment

    returned_output = wrapped_module.main(*variable_values)

    assert returned_output == expected_output
