import pytest
from io import StringIO

MEMORY_LIMIT = 64  # RAM в MB
TIME_LIMIT = 1  # Временной лимит в сек


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_first_open_test(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("2\n2\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = "2"

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_second_open_test(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("10\n10\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = "50"

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_only_child(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("1\n1\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = "0"

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_long_week_with_one_child(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("10080\n1\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = "5040"

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_long_week_with_children(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("10080\n80")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = "403200"

    assert printed_output == expected_output
