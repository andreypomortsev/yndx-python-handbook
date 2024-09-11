def to_string(*data, sep: str = " ", end: str = "\n") -> str:
    n = len(data)
    result = []

    for i in range(n):
        element = str(data[i])

        if i == n - 1:
            sep = end

        result.append(element)
        result.append(sep)

    return "".join(result)
