from typing import Any, List, Optional, Set, Tuple, Union
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
    sleep_time: Optional[float],
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
    time_waster: pytest.fixture, sleep_time: Optional[float], _: str
) -> None:
    wrapped_waste_time = utils.time_limit(TIME_LIMIT)(time_waster)

    with pytest.raises(TimeLimitExceeded) as exc_info:
        wrapped_waste_time(sleep_time)

    assert str(exc_info.value) == "Execution exceeded the limit of 1 second."


def test_memory_limit_with_args_passes() -> None:
    @utils.memory_limit(MEMORY_LIMIT)
    def low_ram(n: int) -> List[int]:
        return list(range(n))

    assert list(range(10)) == low_ram(10)


def test_memory_limit_with_args_fails() -> None:
    quarter_ram_limit = MEMORY_LIMIT // 4

    @utils.memory_limit(quarter_ram_limit)
    def high_ram(n: int) -> List[int]:
        long_string = ""
        multiplier = n**2
        for _ in range(20):
            long_string += "a" * multiplier

    with pytest.raises(MemoryLimitExceeded) as exc_info:
        high_ram(1000)

    assert "Использовано:" in str(exc_info.value)
    assert f"лимит {quarter_ram_limit} MB" in str(exc_info.value)


def test_memory_limit_no_args_passes() -> None:
    @utils.memory_limit(MEMORY_LIMIT)
    def low_ram() -> List[int]:
        return list(range(10))

    assert list(range(10)) == low_ram()


def test_memory_limit_no_args_fails() -> None:
    quarter_ram_limit = MEMORY_LIMIT // 4

    @utils.memory_limit(quarter_ram_limit)
    def high_ram() -> None:
        long_string = ""
        multiplier = 10**6
        for _ in range(20):
            long_string += "a" * multiplier

    with pytest.raises(MemoryLimitExceeded) as exc_info:
        high_ram()

    assert "Использовано:" in str(exc_info.value)
    assert f"лимит {quarter_ram_limit} MB" in str(exc_info.value)


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
    initial_paths: Optional[List[str]],
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


@pytest.mark.parametrize(
    "number, expected_calls, expected_return, _",
    test_data.function_calls,
    ids=[i[-1] for i in test_data.function_calls],
)
def test_count_function_calls(
    number: Optional[int],
    expected_calls: int,
    expected_return: Optional[int],
    _: str,
) -> None:
    @utils.count_function_calls
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        return n * factorial(n - 1)

    if isinstance(number, int):
        assert factorial(number) == expected_return

    assert factorial.call_count == expected_calls

    # Checking reset
    factorial.call_count = 0
    assert factorial.call_count == 0
