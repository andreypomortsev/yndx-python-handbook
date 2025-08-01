from types import ModuleType
from typing import Callable, Optional

import pytest

from tests.constants import TEST_FILE_NAMES
from tests.data.test_data_35 import q_test_data
from tests.utils import get_mocked_print


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

    printed_output = get_mocked_print(
        wrapped_module,
        monkeypatch,
        None,
    )
    assert printed_output in expected_output
