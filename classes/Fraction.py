from .meta import Singleton


class Fraction(metaclass=Singleton):
    """
        Класс для расчетов в обычных дробях
    """

    @staticmethod
    def __gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def reduce(a, b):
        gcd = Fraction.__gcd(a, b)
        return a // gcd, b // gcd

    def __init__(self, numerator: int, denominator: int):
        self.numerator, self.denominator = Fraction.reduce(numerator, denominator)

    @staticmethod
    def to_fraction(x):
        if type(x) == Fraction:
            return x
        if type(x) == int:
            return Fraction(x, 1)
        if type(x) == float:
            a, b = str(x).split('.')
            denominator = 10 ** len(b)
            return Fraction(int(a)*denominator + int(b), denominator)
        raise NotImplementedError(f'Type {type(x)} is not supported')

    def compute(self):
        return self.numerator / self.denominator

    def __add__(self, other):
        another = Fraction.to_fraction(other)
        return Fraction(
            self.numerator * another.denominator + another.numerator * self.denominator,
            self.denominator * another.denominator
        )

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        another = Fraction.to_fraction(other)
        return Fraction(self.numerator * another.numerator, self.denominator * another.denominator)

    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __truediv__(self, other):
        another = Fraction.to_fraction(other)
        return Fraction(self.numerator * another.denominator, self.denominator * another.numerator)

    def __rtruediv__(self, other):
        return self / other

    def __pow__(self, power, modulo=None):
        return Fraction(pow(self.numerator, power, modulo), pow(self.denominator, power, modulo))

    def __rpow__(self, other):
        return other ** self.compute()