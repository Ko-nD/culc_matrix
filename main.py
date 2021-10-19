from classes import *


if __name__ == '__main__':
    # print(Matrix.get_from_list([[1,2,3], [4,5,6]]) - Matrix.get_from_list([[4,5,6], [1,2,3]]))
    # print(Matrix.get_from_list([[1,2,3], [2,5,6], [1, 1, 1]]).det())
    a = Matrix.get_from_list([[5,1,],[3,4]])
    other = [[5],[6]]
    c = 0.001
    print(a.jacoby(other, c)[1])
    
