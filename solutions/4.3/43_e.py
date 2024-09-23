def result_accumulator(func):
    def wrapper(*args, method: str = "accumulate", **kwargs):
        if not hasattr(wrapper, "results"):
            wrapper.results = []

        wrapper.results.append(func(*args, **kwargs))

        if method == "drop":
            accumulated_results = wrapper.results[:]
            wrapper.results.clear()
            return accumulated_results
        return None

    return wrapper
