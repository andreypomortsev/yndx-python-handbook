def merge_sort(numbers: list) -> list:
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    left_part = numbers[:mid]
    right_part = numbers[mid:]

    return merge(merge_sort(left_part), merge_sort(right_part))


def merge(left: list, right: list) -> list:
    merged = []
    left_index = right_index = 0
    l_length, r_length = len(left), len(right)

    while left_index < l_length and right_index < r_length:
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged
