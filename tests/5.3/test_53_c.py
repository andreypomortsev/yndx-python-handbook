from types import ModuleType
from typing import Callable, Tuple

import pytest

from tests import utils
from tests.data.test_data_51 import point_init, point_length, point_move


@pytest.mark.parametrize(
    "coordinates, _",
    patched_point_init,
    ids=[i[-1] for i in patched_point_init],
)
def test_patched_point_class(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    coordinates: Optional[Tuple[int | float, int | float]],
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    if not coordinates:
        x, y = 0, 0
    elif isinstance(coordinates[0], tuple):
        x, y = coordinates[0]
    else:
        x, y = coordinates

    point = solution_module.PatchedPoint(*coordinates)

    assert point.x == x
    assert point.y == y


@pytest.mark.parametrize(
    "x_y, x_y_move, _",
    point_move,
    ids=[i[-1] for i in point_move],
)
def test_point_move(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    x_y: Tuple[int | float],
    x_y_move: Tuple[int | float],
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    x, y = x_y
    point = solution_module.Point(x, y)

    assert (point.x, point.y) == (x, y)

    x_move, y_move = x_y_move
    point.move(x_move, y_move)

    x += x_move
    y += y_move

    assert (point.x, point.y) == (x, y)


@pytest.mark.parametrize(
    "xs_ys, expected_output, _",
    point_length,
    ids=[i[-1] for i in point_length],
)
def test_point_length(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    xs_ys: Tuple[int | float],
    expected_output: int | float,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    x_one, y_one, x_two, y_two = xs_ys
    point_one = solution_module.Point(x_one, y_one)
    point_two = solution_module.Point(x_two, y_two)

    assert (point_one.x, point_one.y) == (x_one, y_one)
    assert (point_two.x, point_two.y) == (x_two, y_two)

    assert point_one.length(point_two) == expected_output
    assert point_two.length(point_one) == expected_output

