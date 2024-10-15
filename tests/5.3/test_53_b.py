from types import ModuleType
from typing import Callable, Tuple

import pytest

from tests.data.test_data_53 import b_test_data


@pytest.mark.parametrize(
    "func, _",
    b_test_data,
    ids=[i[-1] for i in b_test_data],
)
def test_break_it(
    setup_environment: Tuple[ModuleType, str],
    func: Callable[..., None],
    _: str,
) -> None:

    wrapped_module, _ = setup_environment
    setattr(wrapped_module, "func", func)

    try:
        wrapped_module.main()
        pytest.fail("You didn't break it!")
    except Exception:
        pytest.xfail("Ура! Ошибка!")
