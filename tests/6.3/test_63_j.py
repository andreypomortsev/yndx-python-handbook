import warnings
from io import StringIO
from types import ModuleType
from typing import Dict, Tuple, TypeVar
from unittest.mock import Mock

import pytest

from tests.constants import TIMEOUT_WARNING, WRONG_URL_ERROR
from tests.data.test_data_63 import f_test_data

T = TypeVar("T")


@pytest.mark.parametrize(
    "url, paths, server_responses, expected_output, _",
    f_test_data,
    ids=[i[-1] for i in f_test_data],
)
def test_get_value(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    url: str,
    paths: Tuple[str],
    server_responses: Dict[str, T],
    expected_output: str,
    _: str,
) -> None:
    wrapped_module, _ = setup_environment

    mock_input = StringIO(f"{url}
{paths}")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    mock_response = Mock()
    mock_response.status_code = 200

    def mock_get(*args, **kwargs) -> str:
        assert url in args[0], WRONG_URL_ERROR

        if "timeout" not in kwargs:
            warnings.warn(TIMEOUT_WARNING, UserWarning)

        _, path = args[0].split(url, 1)
        mock_response.json = Mock(return_value=server_responses[path])

        return mock_response

    monkeypatch.setattr("requests.get", mock_get)

    wrapped_module.main()

    printed_output = mock_print.getvalue().strip()
    assert printed_output == expected_output

