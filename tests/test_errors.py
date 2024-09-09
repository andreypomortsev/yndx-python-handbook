import pytest

from .errors import MemoryLimitExceeded, TimeLimitExceeded


def test_memory_limit_exceeded():
    with pytest.raises(MemoryLimitExceeded) as exc_info:
        raise MemoryLimitExceeded("Memory limit exceeded.")
    assert str(exc_info.value) == "Memory limit exceeded."


def test_time_limit_exceeded():
    with pytest.raises(TimeLimitExceeded) as exc_info:
        raise TimeLimitExceeded("Time limit exceeded.")
    assert str(exc_info.value) == "Time limit exceeded."
