def make_equation(*numbers) -> str:
    if len(numbers) == 1:
        return f"{numbers[0]}"
    return f"({make_equation(*numbers[:-1])}) * x + {numbers[-1]}"
