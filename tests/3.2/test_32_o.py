from types import ModuleType
from typing import Tuple

import pytest

from tests.data.test_data_32 import o_test_data
from tests.utils import assert_equal


@pytest.mark.parametrize(
    "mock_input_text, expected_output, _",
    o_test_data,
    ids=[i[-1] for i in o_test_data],
)
def test_input_output(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    mock_input_text: str,
    expected_output: str,
    _: str,
) -> None:
    wrapped_module, _ = setup_environment
    assert_equal(
        wrapped_module,
        monkeypatch,
        mock_input_text,
        expected_output + "\n",
    )
