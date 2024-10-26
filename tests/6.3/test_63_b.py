import warnings
from io import StringIO
from itertools import cycle
from types import ModuleType
from typing import Generator, Tuple
from unittest.mock import Mock

import pytest

from tests.constants import TIMEOUT_WARNING, WRONG_URL_ERROR
from tests.data.test_data_63 import b_test_data


@pytest.mark.parametrize(
    "url, server_responses, expected_output, _",
    b_test_data,
    ids=[i[-1] for i in b_test_data],
)
def test_get_sum_from_server(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    url: str,
    server_responses: Generator[None, None, int],
    expected_output: str,
    _: str,
) -> None:
    wrapped_module, _ = setup_environment

    mock_input = StringIO(url)
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.ok = mock_response.status_code < 400

    # Make an infinte cycle of the server responces
    responce_cycle = cycle(server_responses)

    def mock_get(*args, **kwargs) -> Mock:
        if "timeout" not in kwargs:
            warnings.warn(TIMEOUT_WARNING, UserWarning)

        assert url in args[0], WRONG_URL_ERROR

        mock_response.text = next(responce_cycle)
        return mock_response

    monkeypatch.setattr("requests.get", mock_get)

    wrapped_module.main()

    printed_output = mock_print.getvalue().strip()
    assert printed_output == expected_output
