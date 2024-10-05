from types import ModuleType
from typing import Callable, Tuple

import pytest

from tests import utils
from tests.data.test_data_51 import point_init


@pytest.mark.parametrize(
    "coordinates, _",
    point_init,
    ids=[i[-1] for i in point_init],
)
def test_point_class(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    coordinates: Tuple[int | float, int | float],
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)
    x, y = coordinates
    point = solution_module.Point(x, y)

    assert point.x == x
    assert point.y == y
