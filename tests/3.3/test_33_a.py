from types import ModuleType
from typing import Dict, List, Set, Tuple, Union

import pytest

from tests.constants import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_33 import a_test_data

OUTPUT_TYPES = Union[
    str,
    List[Tuple[str, int]],
    List[int],
    List[List[int]],
    Set[int],
    Dict[str, Union[int, List[int]]],
]


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
@pytest.mark.parametrize(
    "input_data, expected_output, _",  # _ - название теста
    a_test_data,
    ids=[i[2] for i in a_test_data],  # Считываем названия тестов
)
def test_input_output(
    setup_environment: Tuple[ModuleType, str],
    input_data: Dict[str, Union[str, int, List[int]]],
    expected_output: OUTPUT_TYPES,
    _: str,
) -> None:

    variable_values = [value for value in input_data.values()]
    wrapped_module, _ = setup_environment

    returned_output = wrapped_module.main(*variable_values)

    assert returned_output == expected_output
