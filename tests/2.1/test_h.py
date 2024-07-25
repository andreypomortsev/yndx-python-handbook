import pytest
from io import StringIO

MEMORY_LIMIT = 64  # RAM в MB
TIME_LIMIT = 1  # Временной лимит в сек


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_first_open_test(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("2\nКупи слона!\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = """Я больше никогда не буду писать "Купи слона!"!
Я больше никогда не буду писать "Купи слона!"!"""

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_second_open_test(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("3\nПопка дурак!\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = """Я больше никогда не буду писать "Попка дурак!"!
Я больше никогда не буду писать "Попка дурак!"!
Я больше никогда не буду писать "Попка дурак!"!"""

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_single_quote(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("1\nLet's Rock!")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = """Я больше никогда не буду писать "Let's Rock!"!"""

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_double_quote(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO('1\n"\n')
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = 'Я больше никогда не буду писать """!'

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_single_quotes(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("3\nIt's movin'")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = """Я больше никогда не буду писать "It's movin'"!
Я больше никогда не буду писать "It's movin'"!
Я больше никогда не буду писать "It's movin'"!"""

    assert printed_output == expected_output
