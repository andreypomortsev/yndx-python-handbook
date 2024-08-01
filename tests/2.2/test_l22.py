import pytest

from io import StringIO
from tests.data.test_data_22 import l_test_data

MEMORY_LIMIT = 64  # RAM в MB
TIME_LIMIT = 1  # Временной лимит в сек


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
@pytest.mark.parametrize(
    "mock_input_text, expected_output, test_name",
    l_test_data,
    ids=[i[2] for i in l_test_data],  # Считываем названия тестов
)
def test_input_output(
    monkeypatch, setup_environment, mock_input_text, expected_output, test_name
):
    wrapped_module, _ = setup_environment

    mock_input = StringIO(mock_input_text)
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue()
    assert printed_output == expected_output
