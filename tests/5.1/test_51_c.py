from io import StringIO
from types import ModuleType
from typing import Callable

import pytest
from pytest import MonkeyPatch

from tests import utils


def test_red_button_first_open_test(
    monkeypatch: MonkeyPatch,
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
) -> None:
    REPEATS = 5
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    first_button = solution_module.RedButton()
    second_button = solution_module.RedButton()

    assert first_button.count() == 0
    assert second_button.count() == 0

    mock_print = StringIO()
    monkeypatch.setattr("sys.stdout", mock_print)

    for time in range(REPEATS):
        if time % 2 == 0:
            second_button.click()
        else:
            first_button.click()

    printed_output = mock_print.getvalue()
    excepted_output = "Тревога!\n" * REPEATS

    assert printed_output == excepted_output
    assert (first_button.count(), second_button.count()) == (2, 3)
