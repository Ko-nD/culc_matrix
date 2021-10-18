from .meta import SingletonValue
from .Fraction import Fraction


class ComplexFraction(metaclass=SingletonValue):
    """
        Класс обертка для дробных расчетов над комплексными числами
    """
    def __init__(self, real: Fraction, img: Fraction):
        self.real = real
        self.img = img

    @staticmethod
    def to_complex_fraction(x):
        if type(x) == ComplexFraction:
            return x
        if type(x) == Fraction:
            return ComplexFraction(x, Fraction.to_fraction(0))
        if type(x) == int or type(x) == float:
            return ComplexFraction(Fraction.to_fraction(x), Fraction.to_fraction(0))
        if type(x) == complex:
            return ComplexFraction(Fraction.to_fraction(x.real), Fraction.to_fraction(x.imag))
        raise NotImplementedError(f'Type {type(x)} is not supported')

    def compute(self):
        return complex(self.real.compute(), self.img.compute())

    def __add__(self, other):
        another = ComplexFraction.to_complex_fraction(other)
        return ComplexFraction(self.real+another.real, self.img+another.img)

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        return ComplexFraction(-self.real, -self.img)

    def __mul__(self, other):
        another = ComplexFraction.to_complex_fraction(other)
        return ComplexFraction(
            self.real * another.real - self.img * another.img,
            self.real * another.img + another.real * self.img
        )

    def __rmul__(self, other):
        return self * other

    def __pow__(self, power, modulo=None):  # сложная логика, лень писать
        return pow(self.compute(), power, modulo)

    def __rpow__(self, other):
        return pow(other, self.compute())
