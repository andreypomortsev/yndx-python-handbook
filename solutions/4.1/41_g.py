def can_eat(horsey: tuple, victim: tuple) -> bool:
    x1, y1 = horsey
    x2, y2 = victim
    hor = abs(x2 - x1) == 1 and abs(y2 - y1) == 2
    vert = abs(x2 - x1) == 2 and abs(y2 - y1) == 1
    return hor or vert
