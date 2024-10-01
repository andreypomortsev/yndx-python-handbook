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
def test_queue(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    iterable: Iterable,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    queue = solution_module.Queue()

    assert hasattr(queue, "push")
    assert hasattr(queue, "pop")
    assert hasattr(queue, "is_empty")
    assert queue.is_empty() is True

    for item in iterable:
        queue.push(item)

    counter = 0

    while not queue.is_empty():
        assert queue.pop() == iterable[counter]
        counter += 1
