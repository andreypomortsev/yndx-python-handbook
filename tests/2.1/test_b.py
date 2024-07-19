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


from tests import wrapped_b


def test_print_input_ann(monkeypatch):
    mock_input = StringIO("Ann")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)
    wrapped_b.main()
    printed_output = mock_print.getvalue().strip()
    expected_output = "Как Вас зовут?\nПривет, Ann"

    assert printed_output == expected_output


def test_print_input_bob(monkeypatch):
    mock_input = StringIO("Bob")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)
    wrapped_b.main()
    printed_output = mock_print.getvalue().strip()
    expected_output = "Как Вас зовут?\nПривет, Bob"

    assert printed_output == expected_output


def test_print_input_bob_lower(monkeypatch):
    mock_input = StringIO("bob")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)
    wrapped_b.main()
    printed_output = mock_print.getvalue().strip()
    expected_output = "Как Вас зовут?\nПривет, bob"

    assert printed_output == expected_output


def test_print_empty_input(monkeypatch):
    mock_input = StringIO("\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)
    wrapped_b.main()
    printed_output = mock_print.getvalue().strip("\n")
    expected_output = "Как Вас зовут?\nПривет, "

    assert printed_output == expected_output


def test_print_whitespace_input(monkeypatch):
    mock_input = StringIO("   ")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)
    wrapped_b.main()
    printed_output = mock_print.getvalue().strip("\n")
    expected_output = "Как Вас зовут?\nПривет,    "

    assert printed_output == expected_output


def test_code_statement():
    with open(PATH_TO_TEST_FILE, encoding="UTF-8") as file:
        lines = file.readlines()
        line = "".join(lines)
        expected_output = {
            'print("Как Вас зовут?")\nprint(f"Привет, {input()}")',
            "print('Как Вас зовут?')\nprint(f'Привет, {input()}')",
            'print("Как Вас зовут?")\nprint(f"Привет, {input()}")\n',
            "print('Как Вас зовут?')\nprint(f'Привет, {input()}')\n",
        }
        assert line in expected_output


# Удаляем временный файл
# os.remove(os.path.join("tests", "wrapped_b.py"))
