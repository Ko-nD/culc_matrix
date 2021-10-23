from .Matrix import *
from .Fraction import *
from .ComplexFraction import *
from .SparseMatrix import *
from .Symbol import *


def get_eigen_values(matrix: Matrix, step=0.001, eps=0.001, iterations=1000000):
    """
    Функция для вычисления собственных значений матрицы на промежутке (-1000;1000)
    (только для действительного аргумента)
    :param matrix: матрица, для которой необходимо вычислить собственные значения
    :param step: шаг вычислений
    :param eps: число, значение меньше которого является нулем
    :param iterations: количество итерация для вычисления собственных значений
    :return: список собственных значений
    """
    lambda_ = Symbol()
    new_matrix = matrix - SparseMatrix.get_diag_matrix(matrix.n, matrix.m, lambda_)
    func = new_matrix.det().get_function('x')
    result = []
    for i in range(iterations):
        if abs(func(i * step)) < eps:
            result.append(i * step)
        if abs(func(-i * step)) < eps:
            result.append(-i * step)
    return result


def derivative(func, delta=1e-4):
    def hold_complex_value(x, mode):
        if type(x) == complex or type(x) == ComplexFraction:
            return x + complex(delta, delta) if mode else x - complex(delta, delta)
        return x + delta if mode else x - delta
    return lambda x: func(hold_complex_value(x, 1)) - func(hold_complex_value(x, 0)) / (2 * delta)


def gradient_descent(previous_value, func, step_rate=0.001, complex_=False):
    if complex_:
        return complex(
            previous_value.real - step_rate *
                derivative(lambda x: func(x.real, previous_value.imag))(previous_value.real),
            previous_value.imag - step_rate *
                derivative(lambda x: func(previous_value.real, x.imag))(previous_value.imag)
        )
    return previous_value - step_rate * derivative(func)(previous_value)


# TODO: метод не доработан
def get_eigen_value(matrix, eps=0.001, iterations=100000, complex_=False):
    """
    Находит одно собственное значение собственной матрицы
    :param matrix: матрица
    :param eps: число, значение меньше которого является нулем
    :param iterations: количество итерация для вычисления собственного значения
    :param complex_: флаг, обозначающий является ли матрица комплексной
    :return:
    """
    def is_null(function, val):
        return abs(function(val.real, val.imag)) > eps if complex_ else abs(function(val)) > eps
    lambda_ = Symbol('x + y * (0+1j)' if complex_ else 'x')
    new_matrix = matrix - SparseMatrix.get_diag_matrix(matrix.n, matrix.m, lambda_)
    args = 'xy' if complex_ else 'x'
    func = abs(new_matrix.det()).get_function(*args)
    x = 0
    i = 0
    while is_null(func, x) and i < iterations:
        x = gradient_descent(x, func, complex_=complex_)
    return x
