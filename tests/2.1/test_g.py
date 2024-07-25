import pytest
from io import StringIO

MEMORY_LIMIT = 64  # RAM в MB
TIME_LIMIT = 1  # Временной лимит в сек


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_first_open_test(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("1\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = "Купи слона!"

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_second_open_test(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("3\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = "Купи слона!\nКупи слона!\nКупи слона!"

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_zero_repeats(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("0\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = ""

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_five_repeats(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("5\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = "Купи слона!\nКупи слона!\nКупи слона!\n\
Купи слона!\nКупи слона!"

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_hundred_elephants(monkeypatch, setup_environment, elephants):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("21\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = elephants

    assert printed_output == expected_output
