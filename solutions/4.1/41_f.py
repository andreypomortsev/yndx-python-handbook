from typing import Set


def modern_print(phrase: str, cache: Set[str] = set()) -> None:
    if phrase in cache:
        return
    cache.add(phrase)
    print(phrase)
