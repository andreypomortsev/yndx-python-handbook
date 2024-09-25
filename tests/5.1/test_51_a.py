from types import ModuleType
from typing import Callable

import pytest

from tests import utils
from tests.data.test_data_51 import point_init_test_data


@pytest.mark.parametrize(
    "x, y, _",
    point_init_test_data,
    ids=[i[-1] for i in point_init_test_data],
)
def test_point_class(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    x: int | float,
    y: int | float,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)
    point = solution_module.Point(x, y)

    assert point.x == x
    assert point.y == y
