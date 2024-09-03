from types import ModuleType
from typing import Callable, Optional

import pytest

from tests.constants import MEMORY_LIMIT, TEST_FILE_NAMES, TIME_LIMIT
from tests.data.test_data_35 import q_test_data
from tests.utils import assert_equal


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
@pytest.mark.parametrize(
    "file_data, expected_output, _",
    q_test_data,
    ids=[i[-1] for i in q_test_data],
)
def test_input_output(
    monkeypatch: pytest.MonkeyPatch,
    file_data: str,
    expected_output: str,
    _: str,
    make_test_files: Callable[[str, str, Optional[str]], ModuleType],
) -> None:
    file_name = TEST_FILE_NAMES["3.5"]["q"]

    wrapped_module, _ = make_test_files(file_name, file_data)

    assert_equal(
        wrapped_module,
        monkeypatch,
        None,
        expected_output,
    )
