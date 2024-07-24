import pytest
from io import StringIO

MEMORY_LIMIT = 64  # RAM в MB
TIME_LIMIT = 1  # Временной лимит в сек


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_first_open_test(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("черешня\n2\n3\n10\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    # Преобразование в лист помогает избежать проблемы с несколькими print
    printed_output = mock_print.getvalue().rstrip().split()
    expected_output = """Чек
    черешня - 3кг - 2руб/кг
    Итого: 6руб
    Внесено: 10руб
    Сдача: 4руб""".split()

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_second_open_test(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("манго\n187\n43\n8041\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip().split()
    expected_output = """Чек
    манго - 43кг - 187руб/кг
    Итого: 8041руб
    Внесено: 8041руб
    Сдача: 0руб""".split()

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_briks_capitalized(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("Кирпичи\n187\n43\n108041\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip().split()
    expected_output = """Чек
    Кирпичи - 43кг - 187руб/кг
    Итого: 8041руб
    Внесено: 108041руб
    Сдача: 100000руб""".split()

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_zero_receipt(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("БаНаНы\n200\n0\n0\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip().split()
    expected_output = """Чек
    БаНаНы - 0кг - 200руб/кг
    Итого: 0руб
    Внесено: 0руб
    Сдача: 0руб""".split()

    assert printed_output == expected_output


@pytest.mark.memory_limit(MEMORY_LIMIT)
@pytest.mark.time_limit(TIME_LIMIT)
def test_two_words_product(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("Черная Смородина\n500\n1\n1000\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip().split()
    expected_output = """Чек
    Черная Смородина - 1кг - 500руб/кг
    Итого: 500руб
    Внесено: 1000руб
    Сдача: 500руб""".split()

    assert printed_output == expected_output
