from io import StringIO
from types import ModuleType
from typing import Callable, Tuple

import pytest
from pytest import MonkeyPatch

from tests import utils
from tests.data.test_data_51 import d_test_data


@pytest.mark.parametrize(
    "name_grade, all_hours, excepted_outputs, _",
    d_test_data,
    ids=[i[-1] for i in d_test_data],
)
def test_programmer(
    monkeypatch: MonkeyPatch,
    load_module: Callable[[str], ModuleType],
    request: pytest.FixtureRequest,
    name_grade: Tuple[str],
    all_hours: Tuple[int],
    excepted_outputs: Tuple[str],
    _: str,
) -> None:
    file_path, _ = utils.get_tested_file_details(request)
    solution_module = load_module(file_path)

    mock_print = StringIO()
    monkeypatch.setattr("sys.stdout", mock_print)

    programmer = solution_module.Programmer(*name_grade)

    programmer.work(all_hours[0])
    assert programmer.info() == excepted_outputs[0]

    for hours, excepted_output in zip(all_hours[1:], excepted_outputs[1:]):
        programmer.rise()
        programmer.work(hours)
        assert programmer.info() == excepted_output
