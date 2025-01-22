import importlib
import json
import os
import sys
import time
from pathlib import Path
from types import ModuleType
from typing import Callable, Generator, Optional, Tuple, Union

import pytest
from _pytest.fixtures import SubRequest
from _pytest.main import Session

from . import utils
from .constants import MEMORY_LIMIT, TEST_FUNCTION_NAMES, TIME_LIMIT

# Добавить родительский каталог в системный путь
# Это позволяет импортировать модули из родительского каталога
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture(scope="module")
def wrap_answer() -> Callable[[str, str, Optional[str]], str]:
    def wrapper(file_path: str, file_name: str, args: Optional[str]) -> str:
        """
        Считывает решение из файла и оборачивает его в main функцию
        для получения информации о покрытии тестов во время тестирования.

        Аргументы:
            file_path (str): путь к файлу с решением.
            file_name (str): имя файла с решением: "43_a".

        Возвращает:
            str: путь к обернутому файлу.
        """
        with open(file_path, encoding="UTF-8") as file_in:
            script = file_in.read()

        # Добавляем отступы для обертывания в функцию
        indented_script = script.replace("\n", "\n    ").rstrip(" ")

        recursion_counter = counter_decorator = ""

        recursive = file_name.startswith("43")

        # Добавляем декоратор для подсчета вызовов декорируемой функции
        if recursive:
            recursion_counter = ", count_function_calls"
            counter_decorator = "@count_function_calls\n"

        imports = (
            "from tests.utils import time_limit,"
            f" memory_limit{recursion_counter}\n"
            "from tests.constants import TIME_LIMIT, MEMORY_LIMIT\n\n\n"
        )
        decorators = (
            f"{counter_decorator}"
            "@time_limit(TIME_LIMIT)\n"
            "@memory_limit(MEMORY_LIMIT)\n"
        )

        if recursive:
            wrapped_script = f"{imports}{decorators}" f"{script}"
        # Обертываем считанный из файла код в функцию main
        elif args:
            wrapped_script = (
                f"{imports}{decorators}def main({args}):\n"
                f"    return {indented_script}"
            )
        else:
            wrapped_script = (
                f"{imports}{decorators}def main():\n    {indented_script}"
            )

        # Создаем имя решения обернутого в функцию
        wrapped_file_name = f"wrapped_{file_name}.py"

        # Определяем папку с тестами "tests"
        current_dir = os.path.dirname(__file__)

        # Создаем путь в которуй запишем файл для оценки покрытия тестами
        path_to_save = os.path.join(current_dir, wrapped_file_name)

        with open(path_to_save, "w", encoding="UTF-8") as file_out:
            file_out.write(wrapped_script)

        # Возвращаем путь для его удаления файла после прохождения тестов
        return path_to_save

    return wrapper


@pytest.fixture(scope="module")
def setup_environment(
    request: SubRequest, wrap_answer: Callable[..., None]
) -> Generator[Tuple[ModuleType, str], None, None]:
    """
    Фикстура для настройки тестовой среды, которая оборачивает тестируемый
    файл в функцию main и динамически импортирует обернутый модуль.

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
        request (SubRequest): объект, предоставляющий информацию
            о тестовом запросе.
        wrap_answer (Callable[..., None]): функция, которая оборачивает файл
            в функцию main и возвращает путь к обернутому файлу.

    Возвращает:
        tuple: Кортеж, содержащий импортированный модуль и путь
            к обернутому тестируемому файлу.
    """
    # Получаем путь к файлу с решением и его имя
    path_to_test_file, tested_file_name = utils.get_tested_file_details(
        request
    )
    # "33_a" -> "33", "a"
    module, letter = tested_file_name.split("_")

    if module == "33":
        test_data_module_name = f"tests.data.test_data_{module}"
        test_data = importlib.import_module(test_data_module_name)

        # Получаем доступ к тестовым данным List[Tuple[Dict[Any]]]
        input_data = getattr(test_data, f"{letter}_test_data", None)

        if isinstance(input_data[0][0], dict):
            args = ", ".join(key for key in input_data[0][0])
        else:
            args = None
    else:
        args = None

    # Оборачиваем тестируемый файл в функцию main, получаем путь файла
    path_to_the_wrapped_file = wrap_answer(
        path_to_test_file, tested_file_name, args
    )

    # Динамически импортируем wrapped файл после создания
    wrapped_module_name = f"tests.wrapped_{tested_file_name}"
    try:
        wrapped_module = importlib.import_module(wrapped_module_name)
    except SyntaxError:
        pytest.exit(
            f"Syntax error in the file {tested_file_name}.py", returncode=1
        )

    # Добавляем путь к обернутому файлу в список для удаления
    utils.add_file_to_cleanup(request, path_to_the_wrapped_file)

    yield wrapped_module, path_to_the_wrapped_file


@pytest.fixture(scope="module")
def make_test_files(
    request: SubRequest,
    setup_environment: Generator[Tuple[ModuleType, str], None, None],
) -> Generator[
    Callable[[Union[Tuple[str], str], Union[Tuple[str], str]], ModuleType],
    None,
    None,
]:
    """
    Фикстура для создания тестовых файлов и добавления их в список для удаления
    после завершения тестов.

    Эта фикстура выполняет следующие действия:
    1. Создаёт тестовый файл с данными из переменной `mock_input_text`.
    2. Добавляет путь к файлу в список для удаления после завершения тестов.

    Аргументы:
        request (SubRequest): объект, дающий информацию о тестовом запросе.
        setup_environment (Generator[Tuple[ModuleType, str], None, None]):
            фикстура для настройки тестовой среды.

    Возвращает:
        Generator[
            Callable[
                [Union[Tuple[str], str],
                Union[Tuple[str], str]],
                ModuleType
            ]:
        Генератор, который возвращает функцию для создания тестовых файлов.
        Эта функция принимает имена файлов и данные для записи в файлы,
        а затем возвращает объект окружения тестирования.
    """

    def _create_test_file(
        file_names: Union[Tuple[str], str],
        mock_input_texts: Union[Tuple[str], str],
        mode: str = "w",
    ) -> ModuleType:
        """
        Создаёт тестовый файл с указанным именем и записывает в него данные из
        переменной `mock_input_texts`. Добавляет путь к файлу в список
        для удаления после завершения тестов.

        Аргументы:
            file_names (Union[Tuple[str], str]): Имена файлов
            mock_input_texts (Union[Tuple[str], str]): Данные для записи
                в файлы.
            mode (str): В каком режиме записывать файлы.

        Возвращает:
            ModuleType: Объект окружения тестирования.
        """
        if isinstance(file_names, str):
            file_names = (file_names,)
            mock_input_texts = (mock_input_texts,)

        for file_name, input_text in zip(file_names, mock_input_texts):
            if file_name.lower().endswith("json"):

                with open(file_name, mode, encoding="UTF-8") as json_file:
                    json.dump(input_text, json_file)

            else:
                if mode == "wb":
                    encoding = None
                else:
                    encoding = "UTF-8"

                with open(file_name, mode, encoding=encoding) as file:
                    file.write(input_text)

            utils.add_file_to_cleanup(request, file_name)

        return setup_environment

    yield _create_test_file


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session: Session) -> None:
    """
    Pytest hook, который запускается после завершения тестовой сессии.
    Этот хук удаляет все временные файлы, созданные во время тестирования.

    Аргументы:
        session (Session): Текущая тестовая сессия Pytest.
    """
    # Удаляем все временные файлы
    if hasattr(session.config, "temp_file_paths"):
        for temp_file_path in session.config.temp_file_paths:
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_call(item: pytest.Item) -> Generator[None, None, None]:
    """
    Pytest hook для применения ограничений по памяти и времени к тестам.

    Аргументы:
        item (pytest.Item): Тестовый элемент, к которому применяются
            ограничения.
    """
    memory_limit_marker = item.get_closest_marker("memory_limit")
    time_limit_marker = item.get_closest_marker("time_limit")

    if memory_limit_marker:
        limit_mb = memory_limit_marker.args[0]
        item.obj = utils.memory_limit(limit_mb)(item.obj)

    if time_limit_marker:
        limit_seconds = time_limit_marker.args[0]
        item.obj = utils.time_limit(limit_seconds)(item.obj)

    yield


@pytest.fixture
def temp_files(request: SubRequest) -> Callable[[str], None]:
    """
    Создает временные файлы для тестов и добавляет их в список
    на удаление после выполнения тестов.

    Фикстура позволяет добавлять пути к временным файлам, которые
    должны быть удалены после завершения тестовой сессии.

    Аргументы:
        request (SubRequest): объект, предоставляющий информацию
            о тестовом запросе.

    Возвращает:
        Callable[[str], None]: Функция, которая принимает путь к файлу
            и добавляет его в список на удаление.
    """
    files_to_cleanup = []

    def add_file(file_path: str) -> None:
        """
        Добавляет путь к файлу в список для удаления.

        Аргументы:
            file_path (str): путь к файлу, который нужно удалить.
        """
        files_to_cleanup.append(file_path)

    def cleanup() -> None:
        """
        Удаляет все файлы, добавленные в список `files_to_cleanup`.
        """
        for file_path in files_to_cleanup:
            if os.path.exists(file_path):
                os.remove(file_path)

    request.addfinalizer(cleanup)
    return add_file


@pytest.fixture
def load_module() -> Callable[[str], ModuleType]:
    """
    Загружает модуль Python из указанного файла с использованием importlib.

    Фикстура возвращает функцию, которая принимает путь к файлу,
    загружает модуль из этого файла и возвращает его.

    Аргументы:
        file_path (str): Путь к файлу модуля, который нужно загрузить.

    Возвращает:
        Callable[[str], ModuleType]: Функция, которая загружает и
            возвращает модуль.
    """

    def _load_module(file_path: str) -> ModuleType:
        file_path = Path(file_path).resolve()
        spec = importlib.util.spec_from_file_location(
            "solution", str(file_path)
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)  # Загружает и выполняет модуль

        return module

    return _load_module


@pytest.fixture
def decorated_function(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
) -> Callable:
    """
    Предоставляет декорированную функцию с ограничениями по времени и памяти.

    Аргументы:
        load_module (Callable[[str], ModuleType]): Фикстура для загрузки
            модуля.
        request (pytest.FixtureRequest): Объект запроса pytest.

    Возвращает:
        Callable: Декорированная функция с ограничениями по времени и памяти.

    Исключения:
        AttributeError: Если функция с указанным именем не найдена в модуле.
    """
    testing_file_path, file_name = utils.get_tested_file_details(request)

    solution = load_module(testing_file_path)

    # Пример: solutions/4.1/21_a.py -> solutions/4.1/
    dir_path = Path(testing_file_path).parent

    # Пример: solutions/4.1/21_a.py -> 4.1
    file_dir = dir_path.name

    # Получаем a из 41_a
    solution_letter = file_name[-1]
    function_name = TEST_FUNCTION_NAMES[file_dir][solution_letter]

    # Импортируем модуль для тестов
    solution = load_module(testing_file_path)
    func = getattr(solution, function_name, None)

    if func is None:
        raise AttributeError(f"Функция {function_name} не найдена в модуле")

    decorated_func = utils.memory_limit(MEMORY_LIMIT)(func)
    decorated_func = utils.time_limit(TIME_LIMIT)(decorated_func)

    return decorated_func


@pytest.fixture
def time_spender() -> Callable[..., None]:
    """
    Используется для теста декоратора utils.time_limit
    """

    def spend_time(sleep_time: Optional[float]) -> None:
        if sleep_time is None:
            sleep_time = 0.50
        time.sleep(sleep_time)

        return None

    return spend_time


@pytest.fixture
def time_waster() -> Callable[..., None]:
    """
    Используется для теста декоратора utils.time_limit
    """

    def waste_time(sleep_time: Optional[float]) -> None:
        if sleep_time is None:
            sleep_time = 1.05
        time.sleep(sleep_time)

        return None

    return waste_time
