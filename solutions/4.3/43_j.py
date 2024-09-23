def make_linear(iterable):
    answer = []

    for i in iterable:
        if isinstance(i, list):
            answer.extend(make_linear(i))
        else:
            answer.append(i)

    return answer
