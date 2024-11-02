from types import ModuleType
from typing import List, Tuple

import pytest

from tests.data.test_data_43 import f_test_data


@pytest.mark.parametrize(
    "unsorted_list, expected_output, _",
    f_test_data,
    ids=[data[-1] for data in f_test_data],
)
def test_merge_sort(
    setup_environment: Tuple[ModuleType, str],
    unsorted_list: List[int],
    expected_output: List[int],
    _: str,
) -> None:
    wrapped_module, _ = setup_environment

    returned_output = wrapped_module.merge_sort(unsorted_list)
    error_msg = (
        "Функция `merge_sort` должна быть реализована при помощи рекурсии."
    )
    try:
        assert (
            wrapped_module.merge_sort.call_count >= len(unsorted_list) // 2
        ), error_msg
        assert returned_output == expected_output

    finally:
        # Сбрасываем счетчик вызова функции, независимо от результата теста
        wrapped_module.merge_sort.call_count = 0
