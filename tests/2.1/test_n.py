import pytest
from io import StringIO

MEMORY_LIMIT = 64  # RAM в MB
TIME_LIMIT = 1  # Временной лимит в сек


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_first_open_test(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("1\n2\n3\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = "5"

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_equal_with_ones(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("1\n1\n1\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = "3"

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_equal_with_tens(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("10\n10\n10\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = "21"

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_more_reds_than_blues(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("9\n3\n7\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = "17"

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_more_blues_than_reds(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("7\n3\n9\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = "17"

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_equal_with_lots_of_green(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("19\n300\n19\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = "39"

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_big_numbers(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("10_000_000_000\n3_333_333_333\n3_333_333_333\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = "13333333334"

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_zero_reds(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("0\n3\n33\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = "34"

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_zero_blues(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("31\n3\n0\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = "32"

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_all_greens(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("0\n3\n0\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = "1"

    assert printed_output == expected_output
