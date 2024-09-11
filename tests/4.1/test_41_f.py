from io import StringIO
from typing import Callable, Tuple

import pytest

from tests.data.test_data_41 import f_test_data


@pytest.mark.parametrize(
    "args, expected_output, _",
    f_test_data,
    ids=[i[-1] for i in f_test_data],
)
def test_modern_print(
    monkeypatch: pytest.MonkeyPatch,
    decorated_function: Callable,
    args: Tuple[str],
    expected_output: str,
    _: str,
) -> None:

    outputs = []

    for input in args:
        # Считываем print с функции
        mock_stdout = StringIO()
        monkeypatch.setattr("sys.stdout", mock_stdout)

        decorated_function(input)
        printed = mock_stdout.getvalue()

        if printed:
            outputs.append(printed)

    printed_output = "".join(outputs)

    assert printed_output == expected_output
