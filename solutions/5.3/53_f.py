class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a: int | float, b: int | float, c: int | float) -> tuple:
    """Принимает три рациональных числа как параметры:
    коэффициенты уравнения и возвращающую его корни
    в виде кортежа из двух значений.
    """
    if not all(isinstance(num, (int, float)) for num in (a, b, c)):
        raise TypeError

    if not a:
        if not b:
            if not c:
                raise InfiniteSolutionsError
            raise NoSolutionsError
        root = -c / b
        return (root,)

    discriminant = b**2 - 4 * a * c

    if discriminant >= 0:
        bigger_root = (-b + discriminant**0.5) / (2 * a)
        smaller_root = (-b - discriminant**0.5) / (2 * a)
        return smaller_root, bigger_root

    raise NoSolutionsError
