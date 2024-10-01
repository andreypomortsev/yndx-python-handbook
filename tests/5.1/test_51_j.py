from types import ModuleType
from typing import Callable, Iterable

import pytest

from tests import utils
from tests.data.test_data_51 import queue_test_data


@pytest.mark.parametrize(
    "iterable, _",
    queue_test_data,
    ids=[i[-1] for i in queue_test_data],
)
def test_stack(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    iterable: Iterable,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    stack = solution_module.Stack()

    assert hasattr(stack, "push")
    assert hasattr(stack, "pop")
    assert hasattr(stack, "is_empty")
    assert stack.is_empty() is True

    for item in iterable:
        stack.push(item)

    counter = len(iterable) - 1

    while not stack.is_empty():
        assert stack.pop() == iterable[counter]
        counter -= 1
