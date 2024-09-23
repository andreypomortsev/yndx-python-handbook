from typing import Any, List, Set, Tuple, Union
from unittest import mock

import pytest

from tests.data import test_data_utils as test_data

from . import utils
from .constants import MEMORY_LIMIT, TIME_LIMIT
from .errors import MemoryLimitExceeded, TimeLimitExceeded


@pytest.mark.parametrize(
    "sleep_time, _",
    test_data.time_limit_data_pas,
    ids=[i[-1] for i in test_data.time_limit_data_pas],
)
def test_time_limit_passes(
    time_spender: pytest.fixture,
    sleep_time: Union[None, float],
    _: str,
) -> None:
    wrapped_spend_time = utils.time_limit(TIME_LIMIT)(time_spender)

    assert wrapped_spend_time(sleep_time) is None


@pytest.mark.parametrize(
    "sleep_time, _",
    test_data.time_limit_data_fail,
    ids=[i[-1] for i in test_data.time_limit_data_fail],
)
def test_time_limit_fails(
    time_waster: pytest.fixture, sleep_time: Union[None, float], _: str
) -> None:
    wrapped_waste_time = utils.time_limit(TIME_LIMIT)(time_waster)

    with pytest.raises(TimeLimitExceeded) as exc_info:
        wrapped_waste_time(sleep_time)

    assert str(exc_info.value) == "Тест занял больше лимита в 1 сек."


def test_memory_limit_with_args_passes() -> None:
    @utils.memory_limit(MEMORY_LIMIT)
    def low_ram(n: int) -> List[int]:
        return list(range(n))

    assert list(range(10)) == low_ram(10)


def test_memory_limit_with_args_fails() -> None:
    memory_limit = 1

    @utils.memory_limit(memory_limit)
    def high_ram(n: int) -> List[int]:
        long_string = ""
        for i in range(n):
            for j in range(n):
                long_string += f"{i}" + f"{j}"
        return long_string

    with pytest.raises(MemoryLimitExceeded) as exc_info:
        high_ram(1000)

    assert "Использовано:" in str(exc_info.value)
    assert f"лимит {memory_limit} MB" in str(exc_info.value)


def test_memory_limit_no_args_passes() -> None:
    @utils.memory_limit(MEMORY_LIMIT)
    def low_ram() -> List[int]:
        return list(range(10))

    assert list(range(10)) == low_ram()


def test_memory_limit_no_args_fails() -> None:
    memory_limit = 4

    @utils.memory_limit(memory_limit)
    def high_ram() -> List[int]:
        long_string = ""
        n = 1000
        for i in range(n):
            for j in range(n):
                long_string += f"{i}" + f"{j}"
        return long_string

    with pytest.raises(MemoryLimitExceeded) as exc_info:
        high_ram()

    assert "Использовано:" in str(exc_info.value)
    assert f"лимит {memory_limit} MB" in str(exc_info.value)


@pytest.mark.parametrize(
    "inpt, outpt, _",
    test_data.generate_error_msg_data,
    ids=[i[-1] for i in test_data.generate_error_msg_data],
)
def test_generate_error_msg(
    inpt: Any,
    outpt: Any,
    _: str,
) -> None:
    printed_output = utils.generate_error_msg(inpt, outpt)
    expected_output = f"\nExpected output:\n{outpt}\n\nPrinted output:\n{inpt}"
    assert printed_output == expected_output


@pytest.mark.parametrize(
    "printed, expected, _",
    test_data.compare_output_data_pas,
    ids=[i[-1] for i in test_data.compare_output_data_pas],
)
def test_compare_output_passes(
    printed: str,
    expected: Union[str, Set[str], Tuple[str], List[str], str],
    _: str,
) -> None:
    result = utils.compare_output(printed, expected)
    assert result is None


@pytest.mark.parametrize(
    "user_input, expected_output, _",
    test_data.assert_equal_data,
    ids=[i[-1] for i in test_data.assert_equal_data],
)
def test_assert_equal(
    monkeypatch: pytest.MonkeyPatch,
    user_input: str,
    expected_output: Union[str, Set[str], Tuple[str], List[str]],
    _: str,
) -> None:
    mock_module = mock.MagicMock()

    mock_module.main.side_effect = lambda: print(f"Hello, {input()}!")

    utils.assert_equal(mock_module, monkeypatch, user_input, expected_output)


@pytest.mark.parametrize(
    "file_path, expected_output, _",
    test_data.get_tested_file_details_data,
    ids=[i[-1] for i in test_data.get_tested_file_details_data],
)
def test_get_tested_file_details(
    file_path: str,
    expected_output: Tuple[str],
    _: str,
) -> None:
    mock_request = mock.MagicMock()

    mock_request.module.__file__ = file_path
    result = utils.get_tested_file_details(mock_request)

    assert result == expected_output


@pytest.mark.parametrize(
    "initial_paths, new_paths, expected_paths, _",
    test_data.add_file_to_cleanup_data,
    ids=[i[-1] for i in test_data.add_file_to_cleanup_data],
)
def test_add_file_to_cleanup(
    monkeypatch: pytest.MonkeyPatch,
    initial_paths: Union[List[str], None],
    new_paths: List[str],
    expected_paths: List[str],
    _: str,
) -> None:
    mock_request = mock.MagicMock()

    monkeypatch.setattr(mock_request.config, "temp_file_paths", initial_paths)

    for path in new_paths:
        utils.add_file_to_cleanup(mock_request, path)

    result = mock_request.config.temp_file_paths

    assert result == expected_paths


def test_count_function_calls_zero_calls() -> None:
    @utils.count_function_calls
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        return n * factorial(n - 1)

    assert factorial.call_count == 0


def test_count_function_calls_one_call() -> None:
    @utils.count_function_calls
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        return n * factorial(n - 1)

    result = factorial(0)

    assert result == 1
    assert factorial.call_count == 1


def test_count_function_calls_six_call() -> None:
    @utils.count_function_calls
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        return n * factorial(n - 1)

    result = factorial(5)

    assert result == 120
    assert factorial.call_count == 6


def test_count_function_calls_reset() -> None:
    @utils.count_function_calls
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        return n * factorial(n - 1)

    factorial(3)
    assert factorial.call_count == 4

    factorial.call_count = 0
    assert factorial.call_count == 0
