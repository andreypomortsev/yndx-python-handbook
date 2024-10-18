from types import ModuleType
from typing import Tuple

import pytest

from tests.data.test_data_61 import e_test_data
from tests.utils import assert_equal


@pytest.mark.parametrize(
    "coordinates, expected_output, _",
    e_test_data,
    ids=[i[-1] for i in e_test_data],
)
def test_find_distance(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    coordinates: str,
    expected_output: str,
    _: str,
) -> None:
    wrapped_module, _ = setup_environment
    assert_equal(
        wrapped_module,
        monkeypatch,
        coordinates,
        expected_output,
    )
