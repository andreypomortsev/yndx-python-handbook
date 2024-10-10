def answer(func: callable) -> str:

    def wrapper(*args, **kwargs) -> str:
        return f"Результат функции: {func(*args, **kwargs)}"

    return wrapper
