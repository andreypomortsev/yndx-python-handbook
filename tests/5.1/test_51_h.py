from types import FunctionType, ModuleType
from typing import Callable, Tuple

import pytest

from tests import utils
from tests.data.test_data_51 import checkers_move


def test_checkers_init(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution = load_module(file_path)

    init_err = "You should implement the __init__ method"
    assert isinstance(solution.Checkers.__init__, FunctionType), init_err
    assert isinstance(solution.Cell.__init__, FunctionType), init_err

    checkers = solution.Checkers()
    cell = checkers.get_cell("A1")

    for attr in ("move", "get_cell"):
        checkers_msg = f"Expected class Checkers to have attribute {attr}"
        assert hasattr(checkers, attr), checkers_msg
    
    assert hasattr(cell, "status")
    
    assert isinstance(checkers, solution.Checkers)
    assert isinstance(cell, solution.Cell)


@pytest.mark.parametrize(
    "moves, expected_board, _",
    checkers_move,
    ids=[i[-1] for i in checkers_move],
)
def test_checkers_moves(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    moves: Tuple[Tuple[str, str] | None],
    expected_board: float | int,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution = load_module(file_path)

    checkers = solution.Checkers()

    for move in moves:
        checkers.move(*move)

    printed_board = tuple(
        checkers.get_cell(col + row).status()
        for row in "87654321"
        for col in "ABCDEFGH"
    )

    assert printed_board == expected_board
