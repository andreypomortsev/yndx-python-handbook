def cycle(iterable):
    index = 0
    while True:
        yield iterable[index]
        index += 1
        if index == len(iterable):
            index = 0
