import math
from io import StringIO
from types import ModuleType
from typing import Tuple

import pytest

from tests.data.test_data_61 import e_test_data


@pytest.mark.parametrize(
    "coordinates, expected_output, _",
    e_test_data,
    ids=[i[-1] for i in e_test_data],
)
def test_find_distance(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    coordinates: str,
    expected_output: float,
    _: str,
) -> None:
    wrapped_module, _ = setup_environment

    mock_input = StringIO(coordinates)
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = float(mock_print.getvalue().rstrip())

    assert math.isclose(printed_output, expected_output, rel_tol=1e-6)
