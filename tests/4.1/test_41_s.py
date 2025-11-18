from typing import Callable, List, Tuple

import pytest

from tests.data.test_data_41 import s_test_data


@pytest.mark.parametrize(
    "args, _",
    s_test_data,
    ids=[i[-1] for i in s_test_data],
)
def test_swap(
    decorated_function: Callable, args: Tuple[List, List], _: str
) -> None:
    a = b = args[0].copy()
    c = d = args[1].copy()

    original_a = a.copy()
    original_c = c.copy()

    id_a = id(a)
    id_c = id(c)

    decorated_function(a, c)

    assert a == original_c
    assert c == original_a
    assert a is b
    assert c is d
    assert b == original_c
    assert d == original_a
    assert id(a) == id_a
    assert id(c) == id_c
    assert id(b) == id_a
    assert id(d) == id_c
