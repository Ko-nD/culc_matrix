from classes import *


if __name__ == '__main__':
    # print(Matrix.get_from_list([[1,2,3], [4,5,6]]) - Matrix.get_from_list([[4,5,6], [1,2,3]]))
    # print(Matrix.get_from_list([[1,2,3], [2,5,6], [1, 1, 1]]).det())
    m = Matrix.get_from_list([[3, 4], [5, 2]])
    print(get_eigen_values(m))
