def merge(*iterables) -> list:
    for iterable in iterables:
        try:
            _ = iter(iterable)
        except Exception:
            raise StopIteration

    d_type = type(iterables[0][0])

    type_error = False
    value_error = False

    for iterable in iterables:
        if not all(map(lambda x: isinstance(x, d_type), iterable)):
            type_error = True
            break
        if list(iterable) != sorted(iterable):
            value_error = True

    if type_error:
        raise TypeError
    if value_error:
        raise ValueError

    sorted_list = []
    left, right = iterables
    l_index = r_index = 0

    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            sorted_list.append(left[l_index])
            l_index += 1
        else:
            sorted_list.append(right[r_index])
            r_index += 1

    sorted_list += left[l_index:]
    sorted_list += right[r_index:]

    return sorted_list
