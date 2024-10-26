import warnings
from io import StringIO
from types import ModuleType
from typing import Dict, List, Tuple, TypeVar
from unittest.mock import Mock

import pytest

from tests.constants import TIMEOUT_WARNING, WRONG_URL_ERROR
from tests.data.test_data_63 import g_test_data

T = TypeVar("T")


@pytest.mark.parametrize(
    "ip_port, user_id, message, server_response, expected_output, _",
    g_test_data,
    ids=[i[-1] for i in g_test_data],
)
def test_get_user(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    ip_port: str,
    user_id: int,
    message: str,
    server_response: List[Dict[str, T]],
    expected_output: str,
    _: str,
) -> None:
    wrapped_module, _ = setup_environment

    user_input = f"{ip_port}\n{user_id}\n{message}"
    mock_input = StringIO(user_input)
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    def mock_get(*args, **kwargs) -> Mock:
        if "timeout" not in kwargs:
            warnings.warn(TIMEOUT_WARNING, UserWarning)

        assert ip_port in args[0], WRONG_URL_ERROR

        mock_response = Mock()

        try:
            mock_response.json = Mock(
                return_value=server_response[user_id - 1]
            )
            mock_response.status_code = 200
        except IndexError:
            mock_response.status_code = 404

        mock_response.ok = mock_response.status_code < 400

        return mock_response

    monkeypatch.setattr("requests.get", mock_get)

    wrapped_module.main()

    printed_output = mock_print.getvalue().strip()
    assert printed_output == expected_output
