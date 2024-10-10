from typing import Optional


class Fraction:
    def __init__(self, *numbers) -> None:
        if isinstance(numbers[0], str):
            if "/" in numbers[0]:
                self._numerator, self._denominator = map(
                    int, numbers[0].split("/")
                )
            else:
                self._numerator = int(numbers[0])
                self._denominator = 1
        else:
            if len(numbers) == 2:
                self._numerator, self._denominator = numbers
            else:
                self._numerator = numbers[0]
                self._denominator = 1
        self._gcd_check()

    def numerator(self, number: Optional[int] = None) -> Optional[int]:
        if not number:
            return abs(self._numerator)

        sign = -1 if self._numerator < 0 else 1
        self._numerator = number * sign
        self._gcd_check()

    def denominator(self, number: Optional[int] = None) -> Optional[int]:
        if not number:
            return self._denominator

        self._denominator = number
        self._gcd_check()

    def reverse(self) -> "Fraction":
        return Fraction(self._denominator, self._numerator)

    def _gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def _gcd_check(self) -> None:
        gcd = self._gcd(self._numerator, self._denominator)

        if gcd != 0:
            self._numerator //= gcd
            self._denominator //= gcd

    def _ensure_fraction(self, value) -> "Fraction":
        if isinstance(value, (int, str)):
            return Fraction(value)
        elif isinstance(value, Fraction):
            return value
        else:
            raise TypeError(
                f"Неподдерживаемый тип: {type(value)}. \
            Допускаются int, str, или Fraction."
            )

    def __str__(self) -> str:
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self) -> str:
        return f"Fraction('{self._numerator}/{self._denominator}')"

    def __neg__(self) -> "Fraction":
        return Fraction(-self._numerator, self._denominator)

    def __add__(self, other) -> "Fraction":
        other = self._ensure_fraction(other)
        new_numerator = (
            self._numerator * other._denominator
            + other._numerator * self._denominator
        )
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other: "Fraction") -> "Fraction":
        other = self._ensure_fraction(other)
        new_numerator = (
            self._numerator * other._denominator
            - other._numerator * self._denominator
        )
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)

    def __iadd__(self, other: "Fraction") -> "Fraction":
        other = self._ensure_fraction(other)
        self._numerator = (
            self._numerator * other._denominator
            + other._numerator * self._denominator
        )
        self._denominator *= other._denominator
        self._gcd_check()
        return self

    def __isub__(self, other: "Fraction") -> "Fraction":
        other = self._ensure_fraction(other)
        self._numerator = (
            self._numerator * other._denominator
            - other._numerator * self._denominator
        )
        self._denominator *= other._denominator
        self._gcd_check()
        return self

    def __mul__(self, other: "Fraction") -> "Fraction":
        other = self._ensure_fraction(other)
        new_numerator = self._numerator * other._numerator
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        other = self._ensure_fraction(other)
        return self * other.reverse()

    def __imul__(self, other: "Fraction") -> "Fraction":
        other = self._ensure_fraction(other)
        self._numerator *= other._numerator
        self._denominator *= other._denominator
        self._gcd_check()
        return self

    def __itruediv__(self, other: "Fraction") -> "Fraction":
        other = self._ensure_fraction(other)
        self._numerator *= other._denominator
        self._denominator *= other._numerator
        self._gcd_check()
        return self

    def __gt__(self, other: "Fraction") -> bool:
        other = self._ensure_fraction(other)
        return not self <= other

    def __lt__(self, other: "Fraction") -> bool:
        other = self._ensure_fraction(other)
        return not self >= other

    def __ge__(self, other: "Fraction") -> bool:
        other = self._ensure_fraction(other)
        return (self._numerator * other._denominator) >= (
            other._numerator * self._denominator
        )

    def __le__(self, other: "Fraction") -> bool:
        other = self._ensure_fraction(other)
        return (self._numerator * other._denominator) <= (
            other._numerator * self._denominator
        )

    def __eq__(self, other: "Fraction") -> bool:
        other = self._ensure_fraction(other)
        return (
            self._numerator == other._numerator
            and self._denominator == other._denominator
        )

    def __ne__(self, other: "Fraction") -> bool:
        other = self._ensure_fraction(other)
        return not self == other
