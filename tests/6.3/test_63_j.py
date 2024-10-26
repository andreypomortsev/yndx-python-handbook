import warnings
from io import StringIO
from types import ModuleType
from typing import Tuple, TypeVar

import pytest

from tests.constants import TIMEOUT_WARNING, WRONG_URL_ERROR
from tests.data.test_data_63 import j_test_data

T = TypeVar("T")


@pytest.mark.parametrize(
    "user_input_tuple, _",
    j_test_data,
    ids=[i[-1] for i in j_test_data],
)
def test_delete_user(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    user_input_tuple: Tuple[str],
    _: str,
) -> None:
    wrapped_module, _ = setup_environment

    user_input = "\n".join(user_input_tuple)

    mock_input = StringIO(user_input)
    monkeypatch.setattr("sys.stdin", mock_input)

    ip_port = user_input_tuple[0]
    user_id = user_input_tuple[1]

    def mock_delete(*args, **kwargs) -> None:
        # Mark that the function was called
        mock_delete.called = True

        if "timeout" not in kwargs:
            warnings.warn(TIMEOUT_WARNING, UserWarning)

        assert ip_port in args[0], WRONG_URL_ERROR
        assert args[0].endswith(f"/users/{user_id}"), WRONG_URL_ERROR

    setattr(mock_delete, "called", False)
    monkeypatch.setattr("requests.delete", mock_delete)
    wrapped_module.main()

    assert mock_delete.called, "Expected requests.delete to be called"
