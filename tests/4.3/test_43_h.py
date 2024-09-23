from io import StringIO
from types import ModuleType
from typing import Tuple

import pytest
from _pytest.monkeypatch import MonkeyPatch

from tests.data.test_data_43 import h_test_data


@pytest.mark.parametrize(
    "number, separator, expected_output, _",
    h_test_data,
    ids=[i[-1] for i in h_test_data],
)
def test_fibonacci(
    monkeypatch: MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    number: int,
    separator: str,
    expected_output: str,
    _: str,
) -> None:
    wrapped_module, _ = setup_environment

    returned_output = wrapped_module.fibonacci(number)

    mock_print = StringIO()
    monkeypatch.setattr("sys.stdout", mock_print)

    print(*returned_output, sep=separator)
    printed_output = mock_print.getvalue()

    assert printed_output == expected_output
