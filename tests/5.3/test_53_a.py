from types import ModuleType
from typing import Callable, Tuple

import pytest

from tests.data.test_data_53 import a_test_data
from tests.utils import assert_equal


@pytest.mark.parametrize(
    "func, expected_error, _",
    a_test_data,
    ids=[i[-1] for i in a_test_data],
)
def test_patched_point_class(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    func: Callable[..., None],
    expected_error: Exception,
    _: str,
) -> None:
    wrapped_module, _ = setup_environment
    setattr(wrapped_module, "func", func)

    assert_equal(wrapped_module, monkeypatch, None, expected_error)
