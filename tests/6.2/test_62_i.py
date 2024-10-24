from io import StringIO
from types import ModuleType
from typing import Tuple

import pandas as pd
import pytest

from tests.constants import TEST_DATA_PATHS
from tests.data.test_data_62 import i_test_data


@pytest.mark.parametrize(
    "limits, expected_output, _",
    i_test_data,
    ids=[i[-1] for i in i_test_data],
)
def test_endless_sea_battle(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    limits: str,
    expected_output: str,
    _: str,
) -> None:
    wrapped_module, _ = setup_environment

    mock_input = StringIO(limits)
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    mock_data = pd.read_csv(TEST_DATA_PATHS["6.2"]["i"])
    monkeypatch.setattr("pandas.read_csv", lambda *args, **kwargs: mock_data)

    wrapped_module.main()

    printed_output = mock_print.getvalue()
    assert printed_output == expected_output
