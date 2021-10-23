from classes import *


if __name__ == '__main__':

    m = Matrix.get_from_list([[1,0] ,[2,1]]) # матрица
    other = [[5],[6]] # свободные члены
    c = 0.001 # точность
    print(m.solve(m, [[1],[2]], 0.01))

    a = Matrix.union(m, Matrix.get_from_list([[1],[2]]), Matrix.unit(len(m)))
    a.convert(type_=Fraction)
    print(a.method_Jordano_Gauss())

