max(
    a * b
    for a, b in [
        (min(numbers), min([x for x in numbers if x != min(numbers)])),
        (max(numbers), max([x for x in numbers if x != max(numbers)])),
    ]
)
