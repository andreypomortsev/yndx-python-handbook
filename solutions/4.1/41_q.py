def is_prime(n: int) -> bool:
    """
    Checks if the given number is prime.
    Approach: check for division on 2 and 3,
        then check for division on 6k ± 1.

    Arguments:
        n (int): Number to check for primality.

    Returns:
        bool: True if the given number is prime, otherwise False.
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    sqrt = int(n**0.5) + 1

    while i < sqrt:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True
