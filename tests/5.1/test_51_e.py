from types import ModuleType
from typing import Callable, Tuple

import pytest

from tests import utils
from tests.data.test_data_51 import (rectangle_area_test_data,
                                     rectangle_perimeter_test_data)


@pytest.mark.parametrize(
    "points, expected_perimeter, _",
    rectangle_perimeter_test_data,
    ids=[i[-1] for i in rectangle_perimeter_test_data],
)
def test_rectangle_perimeter_test(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    points: Tuple[
        Tuple[float | int, float | int], Tuple[float | int, float | int]
    ],
    expected_perimeter: float | int,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    rect = solution_module.Rectangle(*points)

    assert rect.perimeter() == expected_perimeter


@pytest.mark.parametrize(
    "points, expected_area, _",
    rectangle_area_test_data,
    ids=[i[-1] for i in rectangle_area_test_data],
)
def test_rectangle_area_test(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    points: Tuple[
        Tuple[float | int, float | int], Tuple[float | int, float | int]
    ],
    expected_area: float | int,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    rect = solution_module.Rectangle(*points)

    assert rect.area() == expected_area
