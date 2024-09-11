from io import StringIO
from typing import Callable

import pytest

from tests.data.test_data_41 import a_test_data


@pytest.mark.parametrize(
    "arg, expected_output, _",
    a_test_data,
    ids=[i[-1] for i in a_test_data],
)
def test_print_hello(
    monkeypatch: pytest.MonkeyPatch,
    decorated_function: Callable,
    arg: str,
    expected_output: str,
    _: str,
) -> None:

    # Считываем print с функции
    mock_stdout = StringIO()
    monkeypatch.setattr("sys.stdout", mock_stdout)

    decorated_function(arg)

    printed_output = mock_stdout.getvalue()

    assert printed_output == expected_output
