import warnings
from io import StringIO
from types import ModuleType
from typing import Dict, List, Tuple, TypeVar
from unittest.mock import Mock

import pytest

from tests.constants import JSON_ERROR, TIMEOUT_WARNING, WRONG_URL_ERROR
from tests.data.test_data_63 import h_test_data

T = TypeVar("T")


@pytest.mark.parametrize(
    "user_input_tuple, expected_json, _",
    h_test_data,
    ids=[i[-1] for i in h_test_data],
)
def test_post_user(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    user_input_tuple: Tuple[str],
    expected_json: List[Dict[str, T]],
    _: str,
) -> None:
    wrapped_module, _ = setup_environment

    user_input = "\n".join(user_input_tuple)

    mock_input = StringIO(user_input)
    monkeypatch.setattr("sys.stdin", mock_input)

    ip_port = user_input_tuple[0]

    def mock_post(*args, **kwargs) -> Mock:
        # Mark that the function was called
        mock_post.called = True

        if "timeout" not in kwargs:
            warnings.warn(TIMEOUT_WARNING, UserWarning)

        assert ip_port in args[0], WRONG_URL_ERROR
        assert kwargs["json"] == expected_json, JSON_ERROR

    setattr(mock_post, "called", False)
    monkeypatch.setattr("requests.post", mock_post)
    wrapped_module.main()

    assert mock_post.called, "Expected requests.post to be called"
