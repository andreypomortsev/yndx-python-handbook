import warnings
from io import StringIO
from types import ModuleType
from typing import Tuple
from unittest.mock import Mock

import pytest

from tests.constants import TEST_URLS, TIMEOUT_WARNING, WRONG_URL_ERROR
from tests.data.test_data_63 import a_test_data


@pytest.mark.parametrize(
    "expected_output, _",
    a_test_data,
    ids=[i[-1] for i in a_test_data],
)
def test_localhost(
    monkeypatch: pytest.MonkeyPatch,
    setup_environment: Tuple[ModuleType, str],
    expected_output: str,
    _: str,
) -> None:
    wrapped_module, _ = setup_environment

    mock_print = StringIO()
    monkeypatch.setattr("sys.stdout", mock_print)

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = expected_output

    def mock_get(*args, **kwargs) -> Mock:
        assert args[0] == TEST_URLS["6.3"]["a"], WRONG_URL_ERROR

        if "timeout" not in kwargs:
            warnings.warn(TIMEOUT_WARNING, UserWarning)

        return mock_response

    monkeypatch.setattr("requests.get", mock_get)

    wrapped_module.main()

    printed_output = mock_print.getvalue().strip()
    assert printed_output == expected_output
