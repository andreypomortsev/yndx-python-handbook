from typing import Callable, List, Optional, TypeVar

T = TypeVar("T")


def result_accumulator(
    func: Callable[..., T]
) -> Callable[..., Optional[List[T]]]:
    def wrapper(
        *args, method: str = "accumulate", **kwargs
    ) -> Optional[List[T]]:
        if not hasattr(wrapper, "results"):
            wrapper.results = []

        wrapper.results.append(func(*args, **kwargs))

        if method == "drop":
            accumulated_results = wrapper.results[:]
            wrapper.results.clear()
            return accumulated_results
        return None

    return wrapper
