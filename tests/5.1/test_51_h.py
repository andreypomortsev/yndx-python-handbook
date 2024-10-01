from types import ModuleType
from typing import Callable, Tuple

import pytest

from tests import utils
from tests.data.test_data_51 import checkers_move


@pytest.mark.parametrize(
    "moves, expected_board, _",
    checkers_move,
    ids=[i[-1] for i in checkers_move],
)
def test_checkers(
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    moves: Tuple[Tuple[str, str] | None],
    expected_board: float | int,
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    checkers = solution_module.Checkers()

    for move in moves:
        checkers.move(*move)

    printed_board = tuple(
        checkers.get_cell(col + row).status()
        for row in "87654321"
        for col in "ABCDEFGH"
    )

    assert printed_board == expected_board
