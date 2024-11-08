from typing import Optional


class Fraction:
    def __init__(self, *numbers) -> None:
        if isinstance(numbers[0], str):
            self._numerator, self._denominator = map(
                int, numbers[0].split("/")
            )
        else:
            self._numerator, self._denominator = numbers
        self.__gcd_check()

    def numerator(self, number: Optional[int] = None) -> Optional[int]:
        if not number:
            return abs(self._numerator)

        sign = -1 if self._numerator < 0 else 1
        self._numerator = number * sign
        self.__gcd_check()

    def denominator(self, number: Optional[int] = None) -> Optional[int]:
        if not number:
            return self._denominator

        self._denominator = number
        self.__gcd_check()

    def __gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def __gcd_check(self) -> None:
        gcd = self.__gcd(self._numerator, self._denominator)
        if gcd != 0:
            self._numerator //= gcd
            self._denominator //= gcd

    def __str__(self) -> str:
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self) -> str:
        return f"Fraction('{self._numerator}/{self._denominator}')"

    def __neg__(self) -> "Fraction":
        return Fraction(-self._numerator, self._denominator)

    def __add__(self, other: "Fraction") -> "Fraction":
        new_numerator = (
            self._numerator * other._denominator
            + other._numerator * self._denominator
        )
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)

    def __iadd__(self, other: "Fraction") -> "Fraction":
        self._numerator = (
            self._numerator * other._denominator
            + other._numerator * self._denominator
        )
        self._denominator *= other._denominator
        self.__gcd_check()
        return self

    def __sub__(self, other: "Fraction") -> "Fraction":
        new_numerator = (
            self._numerator * other._denominator
            - other._numerator * self._denominator
        )
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)

    def __isub__(self, other: "Fraction") -> "Fraction":
        self._numerator = (
            self._numerator * other._denominator
            - other._numerator * self._denominator
        )
        self._denominator *= other._denominator
        self.__gcd_check()
        return self
