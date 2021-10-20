from .Matrix import *
from .Fraction import *
from .ComplexFraction import *
from .SparseMatrix import *
from .Symbol import *


def get_eigen_values(matrix: Matrix, step=0.001, eps=0.001):
    lambda_ = Symbol()
    new_matrix = matrix - SparseMatrix.get_diag_matrix(matrix.n, matrix.m, lambda_)
    func = new_matrix.det().get_function()
    result = []
    for i in range(1000000):
        if abs(func(i * step)) < eps:
            result.append(i * step)
        if abs(func(-i * step)) < eps:
            result.append(-i * step)
    return result
