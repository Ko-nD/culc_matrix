from classes import *


arr = Matrix([
            [1,2,9,4],
            [2,5,9,4],
            [0,8,7,4],
            [0,0,1,2]
])

print('Класс\n',arr)
print('Размерность', arr.shape())
print('len() выводит количество строк',len(arr)) 
print('Можем обращаться к строке и к символу arr[1]:{}, arr[1][0]:{}'.format( arr[1], arr[1][0]))
print()
print('сложение и тд +=2\n', arr + 2)
print('Матрица - матрица\n', arr - arr)
print('Лучшая строка для определителя', arr.best_line())
print('Определитель Рекурсией', arr.det())

arr1 = Matrix([
    [3, -1, 2],
    [4, 2, 0],
    [-5, 6, 1]
])

arr2 = Matrix([
    [8, 1],
    [7, 2],
    [2, -3]
])
print(Matrix.dot(arr1, arr2) + 7)
arr1.write_csv()


#print(Matrix.do_equation(input('Вводите матрицы Заглавными латинскими буквами:\n')))