import pytest

from tests.data.test_data_24 import q_test_data
from tests.utils import assert_equal

MEMORY_LIMIT = 64  # RAM в MB
TIME_LIMIT = 1  # Временной лимит в сек


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
@pytest.mark.parametrize(
    "mock_input_text, expected_output, test_name",
    q_test_data,
    ids=[i[2] for i in q_test_data],  # Считываем названия тестов
)
def test_input_output(
    monkeypatch, setup_environment, mock_input_text, expected_output, test_name
):
    wrapped_module, _ = setup_environment
    assert_equal(
        wrapped_module,
        monkeypatch,
        mock_input_text,
        expected_output,
        isinstance(expected_output, set),
    )
