def validate_input(*args) -> None:
    for arg in args:
        try:
            _ = iter(arg)
        except Exception:
            raise StopIteration

    d_type = type(args[0][0])
    type_error = value_error = False

    for arg in args:
        if not all(map(lambda x: isinstance(x, d_type), arg)):
            type_error = True
        if list(arg) != sorted(arg):
            value_error = True

    if type_error:
        raise TypeError
    if value_error:
        raise ValueError


def merge(left: tuple, right: tuple) -> list:
    validate_input(left, right)

    sorted_list = []
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
