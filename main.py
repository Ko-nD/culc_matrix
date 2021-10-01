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



