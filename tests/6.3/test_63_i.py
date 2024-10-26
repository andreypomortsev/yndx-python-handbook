import json
import warnings
from io import StringIO
from types import ModuleType
from typing import Dict, Tuple, TypeVar

import pytest

from tests.constants import JSON_ERROR, TIMEOUT_WARNING, WRONG_URL_ERROR
from tests.data.test_data_63 import i_test_data

T = TypeVar("T")


@pytest.mark.parametrize(
    "user_input_tuple, expected_json, _",
    i_test_data,
    ids=[i[-1] for i in i_test_data],
)
def test_put_user(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    user_input_tuple: Tuple[str],
    expected_json: Dict[str, T],
    _: str,
) -> None:
    wrapped_module, _ = setup_environment

    user_input = "\n".join(user_input_tuple)

    mock_input = StringIO(user_input)
    monkeypatch.setattr("sys.stdin", mock_input)

    ip_port = user_input_tuple[0]
    user_id = user_input_tuple[1]

    def mock_put(*args, **kwargs) -> None:
        # Mark that the function was called
        mock_put.called = True

        if "timeout" not in kwargs:
            warnings.warn(TIMEOUT_WARNING, UserWarning)

        assert ip_port in args[0], WRONG_URL_ERROR
        assert args[0].endswith(f"/users/{user_id}"), WRONG_URL_ERROR
        assert kwargs["data"] == json.dumps(expected_json), JSON_ERROR

    setattr(mock_put, "called", False)
    monkeypatch.setattr("requests.put", mock_put)
    wrapped_module.main()

    assert mock_put.called, "Expected requests.put to be called"
