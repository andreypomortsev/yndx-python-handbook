import os
from io import StringIO

from tests import solution_wrapper

PATH_TO_TEST_FILE = None


def setup_function():
    global PATH_TO_TEST_FILE

    current_file_name = os.path.basename(__file__)
    current_dir = os.path.basename(os.path.dirname(__file__))

    # Получаем имя тестируемого файла
    tested_file_name = current_file_name.split("_")[-1]
    PATH_TO_TEST_FILE = os.path.join(current_dir, tested_file_name)

    # Оборачиваем тестируемый файл в функцию main
    solution_wrapper.wrapper(PATH_TO_TEST_FILE)


from tests import wrapped_c # noqa: E402


def test_yndx_one(monkeypatch):
    mock_input = StringIO("2 + 2 = 4")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)
    wrapped_c.main()
    printed_output = mock_print.getvalue().strip()
    expected_output = "2 + 2 = 4\n2 + 2 = 4\n2 + 2 = 4"

    assert printed_output == expected_output


def test_yndx_two(monkeypatch):
    mock_input = StringIO("2 * 2 = 4")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)
    wrapped_c.main()
    printed_output = mock_print.getvalue().strip()
    expected_output = "2 * 2 = 4\n2 * 2 = 4\n2 * 2 = 4"

    assert printed_output == expected_output


def test_whitespace_input(monkeypatch):
    mock_input = StringIO(" ")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)
    wrapped_c.main()
    printed_output = mock_print.getvalue()
    expected_output = " \n \n \n"

    assert printed_output == expected_output


def test_print_empty_input(monkeypatch):
    mock_input = StringIO("\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)
    wrapped_c.main()
    printed_output = mock_print.getvalue().strip("\n")
    expected_output = ""

    assert printed_output == expected_output

# Удаляем временный файл
# os.remove(os.path.join("tests", "wrapped_c.py"))
