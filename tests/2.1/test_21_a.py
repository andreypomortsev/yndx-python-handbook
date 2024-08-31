from io import StringIO

import pytest

from tests.constants import MEMORY_LIMIT, TIME_LIMIT


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_first_open_test(setup_environment, monkeypatch):
    wrapped_module, _ = setup_environment

    mock_print = StringIO()
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue()
    expected_output = "Привет, Яндекс!\n"

    assert printed_output == expected_output
