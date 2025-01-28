from threading import Lock
from typing import Dict

IN_STOK_LOCK = Lock()
RECIPIES = {
    "Эспрессо": {"coffee": 1, "milk": 0, "cream": 0},
    "Капучино": {"coffee": 1, "milk": 3, "cream": 0},
    "Макиато": {"coffee": 2, "milk": 1, "cream": 0},
    "Кофе по-венски": {"coffee": 1, "milk": 0, "cream": 2},
    "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
    "Кон Панна": {"coffee": 1, "milk": 0, "cream": 1},
}


def check_ingredients(ingredients: Dict[str, int]) -> bool:
    """Проверка достаточности ингредиентов для напитка"""
    return all(
        in_stock.get(ingredient, 0) >= quantity  # noqa F821
        for ingredient, quantity in ingredients.items()
    )


def update_stock(ingredients: Dict[str, int]) -> None:
    """Обновление ингредиентов в остатках"""
    for ingredient, quantity in ingredients.items():
        in_stock[ingredient] -= quantity  # noqa F821


def order(*preferences) -> str:
    # Lock the in_stock to prevent race conditions.
    with IN_STOK_LOCK:
        for drink in preferences:
            ingredients = RECIPIES.get(drink, None)

            if ingredients and check_ingredients(ingredients):
                update_stock(ingredients)
                return drink

    return "К сожалению, не можем предложить Вам напиток"
