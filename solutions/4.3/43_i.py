def cycle(iterable):
    index = 0
    length = len(iterable)

    while True:
        yield iterable[index]
        index += 1
        if index == length:
            index = 0
