class MemoryLimitExceeded(Exception):
    """Exception raised when the memory usage exceeds the defined limit."""

    pass


class TimeLimitExceeded(Exception):
    """Exception raised when the execution time exceeds the allowed limit."""

    pass
