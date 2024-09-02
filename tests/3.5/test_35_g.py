from types import ModuleType
from typing import Callable, Optional, Set, Union

import pytest

from tests.constants import MEMORY_LIMIT, TIME_LIMIT
from tests.data.test_data_35 import g_test_data
from tests.utils import assert_equal


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
@pytest.mark.parametrize(
    "file_name, mock_input_text, expected_output, _",  # _ - название теста
    g_test_data,
    ids=[i[3] for i in g_test_data],  # Считываем названия тестов
)
def test_input_output(
    monkeypatch: pytest.MonkeyPatch,
    file_name: str,
    mock_input_text: str,
    expected_output: Union[Set[str], str],
    _: str,
    make_test_files: Callable[[str, str, Optional[str]], ModuleType],
) -> None:

    wrapped_module, _ = make_test_files(file_name, mock_input_text)

    assert_equal(
        wrapped_module,
        monkeypatch,
        file_name,
        expected_output,
    )
