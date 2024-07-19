import os
from io import StringIO

from tests import solution_wrapper


current_file_name = os.path.basename(__file__)
current_dir = os.path.basename(os.path.dirname(__file__))

# Получаем имя тестируемого файла
tested_file_name = current_file_name.split("_")[-1]
PATH_TO_TEST_FILE = os.path.join(current_dir, tested_file_name)

# Оборачиваем тестируемый файл в функцию main
solution_wrapper.wrapper(PATH_TO_TEST_FILE)

from tests import wrapped_a


def test_print_output(monkeypatch):
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdout", mock_print)
    wrapped_a.main()
    printed_output = mock_print.getvalue().strip()
    expected_output = "Привет, Яндекс!"

    assert printed_output == expected_output


def test_code_statement():
    with open(PATH_TO_TEST_FILE, encoding="UTF-8") as file:
        line = file.readline()
        expected_output = {
            'print("Привет, Яндекс!")',
            "print('Привет, Яндекс!')",
            'print("Привет, Яндекс!")\n',
            "print('Привет, Яндекс!')\n",
        }
        assert line in expected_output

# Удаляем временный файл
# os.remove(os.path.join("tests", "wrapped_a.py"))
