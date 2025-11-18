def fragments(numbers: list) -> list:
    answer = []
    start = 0
    length = len(numbers)

    for i in range(1, length):
        if numbers[i - 1] >= numbers[i]:
            answer.append(numbers[start:i])
            start = i

    if start < length:
        answer.append(numbers[start:])

    return answer
