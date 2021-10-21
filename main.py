from classes import *


if __name__ == '__main__':
    # print(Matrix.get_from_list([[1,2,3], [4,5,6]]) - Matrix.get_from_list([[4,5,6], [1,2,3]]))
    # print(Matrix.get_from_list([[1,2,3], [2,5,6], [1, 1, 1]]).det())
    a = Matrix.get_from_list([[5,1],[3,4]])
    other = [[5],[6]]
    c = 0.001
    # print(a.method_jacoby(other, c)[1])

    m = Matrix.get_from_list([[1,0] ,[2,1]])
    # m = Matrix.union(m,Matrix.unit(len(m)))
  
    # print(m)
    # print('========')
    # m.method_Jordano_Gauss()
    # print('========')
    print(m.unification([[1],[2]], 0.01))
    # print(Matrix.union(m, Matrix.get_from_list([[1],[2]]), Matrix.unit(len(m))))
    

