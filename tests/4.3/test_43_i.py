from io import StringIO
from types import ModuleType
from typing import Tuple

import pytest
from _pytest.monkeypatch import MonkeyPatch

from tests.data.test_data_43 import i_test_data


@pytest.mark.parametrize(
    "iterable, n, expected_output, _",
    i_test_data,
    ids=[i[-1] for i in i_test_data],
)
def test_cycle(
    monkeypatch: MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    iterable: int,
    n: str,
    expected_output: str,
    _: str,
) -> None:
    module, _ = setup_environment

    mock_print = StringIO()
    monkeypatch.setattr("sys.stdout", mock_print)

    print(*(x for _, x in zip(range(n), module.cycle(iterable))))
    printed_output = mock_print.getvalue()

    assert printed_output == expected_output
