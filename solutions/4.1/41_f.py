from typing import Set


def modern_print(phrase: str, cache: Set[str] = set()) -> None:
    if phrase in cache:
        return None
    cache.add(phrase)
    print(phrase)
