def gcd(a: int, b: int) -> int:
    """
    Calculates the greatest common divisor (GCD) of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The GCD of the two integers.
    """
    while b:
        a, b = b, a % b
    return a
