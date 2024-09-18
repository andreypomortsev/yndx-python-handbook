from typing import Any, Callable, List, Optional


def result_accumulator(
    func: Callable[..., Any]
) -> Callable[..., Optional[List[Any]]]:
    def wrapper(
        *args: Any, method: str = "accumulate", **kwargs: Any
    ) -> Optional[List[Any]]:
        if not hasattr(wrapper, "results"):
            wrapper.results = []

        wrapper.results.append(func(*args, **kwargs))

        if method == "drop":
            accumulated_results = wrapper.results[:]
            wrapper.results.clear()
            return accumulated_results
        return None

    return wrapper
