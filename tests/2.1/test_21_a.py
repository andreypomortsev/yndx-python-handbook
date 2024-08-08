import pytest

from io import StringIO

MEMORY_LIMIT = 64  # RAM в MB
TIME_LIMIT = 1  # Временной лимит в сек


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


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_second_open_test(setup_environment):
    _, path_to_test_file = setup_environment

    with open(path_to_test_file, encoding="UTF-8") as file:
        line = file.readline().strip()
        expected_outputs = {
            'print("Привет, Яндекс!")',
            "print('Привет, Яндекс!')",
            'print("Привет, Яндекс!")\n',
            "print('Привет, Яндекс!')\n",
        }
        assert line in expected_outputs
