def merge(left: tuple, right: tuple) -> tuple:
    """
    Объединяет два отсортированных списка в один отсортированный кортеж.

    Аргументы:
        left (tuple): Отсортированный кортеж.
        right (tuple): Отсортированный кортеж.

    Возвращает:
        tuple: Объединенный отсортированный кортеж.
    """
    merged = []
    left_index = right_index = 0

    # Сравниваем элементы left и right
    while left_index < len(left) and right_index < len(right):

        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1

        else:
            merged.append(right[right_index])
            right_index += 1

    # Добавляем оставшиеся элементы
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return tuple(merged)
