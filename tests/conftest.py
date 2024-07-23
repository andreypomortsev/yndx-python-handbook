import os
import importlib
import pytest
import sys

from typing import Generator
from typing import Tuple
from types import ModuleType

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture(scope="module")
def wrap_answer() -> Generator:
    def wrapper(file_name: str) -> None:
        """
        Считывает решение из файла и оборачивает его в main функцию
        для получения информации о покрытии тестов во время тестирования.

        Args:
            file_name (str): имя файла с решением.

        Returns:
            str: путь к обернутому файлу.
        """
        with open(file_name, encoding="UTF-8") as file_in:
            script = file_in.read()

        letter = file_name.split(".py")[-2][-1]
        indented_script = script.replace("\n", "\n    ").rstrip(" ")
        wrapped_script = f"def main():\n    {indented_script}"  # noqa E231

        current_dir = os.path.dirname(__file__)
        wrapped_file_name = f"wrapped_{letter}.py"
        path_to_save = os.path.join(current_dir, wrapped_file_name)

        with open(path_to_save, "w", encoding="UTF-8") as file_out:
            file_out.write(wrapped_script)
        return path_to_save

    return wrapper


@pytest.fixture(scope="module")
def setup_environment(
    request, wrap_answer
) -> Generator[Tuple[ModuleType, str], None, None]:
    """
    Фикстура для настройки тестовой среды, которая оборачивает тестируемый файл
    в функцию main и динамически импортирует обернутый модуль.

    Эта фикстура выполняет следующие действия:
    1. Определяет имя текущего файла и каталог тестов.
    2. Определяет абсолютный путь к корневому каталогу исходного кода.
    3. Определяет папку с тестируемым кодом и имя тестируемого файла.
    4. Создает путь к тестируемому файлу и оборачивает его в функцию main
        с помощью `wrap_answer`, получая путь к обернутому файлу.
    5. Получает букву тестируемого файла для динамического импорта.
    6. Импортирует обернутый модуль после его создания.
    7. Добавляет путь к обернутому файлу в список временных файлов
        в конфигурации тестов для последующего удаления.

    Аргументы:
    request -- объект, предоставляющий информацию о тестовом запросе.
    wrap_answer -- функция, которая оборачивает файл в функцию main и
    возвращает путь к обернутому файлу.

    Возвращает:
    tuple: Кортеж, содержащий импортированный модуль и путь
    к тестируемому файлу.
    """
    current_file_name = os.path.basename(request.module.__file__)
    test_dir = os.path.dirname(request.module.__file__)

    # Абсолюный путь в корневой каталог
    abs_code_dir = os.path.abspath(os.path.join(test_dir, "..", ".."))

    # Название папки с тестируемым кодом
    file_dir = os.path.basename(test_dir)

    # Получаем имя тестируемого файла
    tested_file_name = current_file_name.split("_")[-1]

    # Путь к тестируемому файлу для обертывания в функцию
    path_to_test_file = os.path.join(
        abs_code_dir, "solutions", file_dir, tested_file_name
    )

    # Оборачиваем тестируемый файл в функцию main, получаем путь файла
    path_to_the_wrapped_file = wrap_answer(path_to_test_file)

    # Получаем букву тестируемого файла
    tested_file_letter = tested_file_name.split(".py")[-2][-1]

    # Динамически импортируем wrapped файл после создания
    wrapped_module_name = f"tests.wrapped_{tested_file_letter}"
    wrapped_module = importlib.import_module(wrapped_module_name)

    # Добавляем пути временных файлов
    if not hasattr(request.config, "wrapped_file_paths"):
        request.config.wrapped_file_paths = []
    request.config.wrapped_file_paths.append(path_to_the_wrapped_file)

    yield wrapped_module, path_to_test_file


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session):
    # Этот хук запускается после завершения тестирования
    # Удаляем все временные файлы
    if hasattr(session.config, "wrapped_file_paths"):
        for path_to_the_wrapped_file in session.config.wrapped_file_paths:
            if os.path.exists(path_to_the_wrapped_file):
                os.remove(path_to_the_wrapped_file)
