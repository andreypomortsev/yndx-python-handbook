from types import ModuleType
from typing import Tuple

import pytest

from tests.data.test_data_61 import b_test_data
from tests.utils import get_mocked_print


@pytest.mark.parametrize(
    "stream_of_numbers, expected_output, _",
    b_test_data,
    ids=[i[-1] for i in b_test_data],
)
def test_streaming_gcd(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    stream_of_numbers: str,
    expected_output: str,
    _: str,
) -> None:
    wrapped_module, _ = setup_environment
    printed_output = get_mocked_print(
        wrapped_module,
        monkeypatch,
        stream_of_numbers,
    )
    assert printed_output == expected_output
