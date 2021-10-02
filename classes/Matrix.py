import copy


class Matrix:
    
    def __init__(self, n, m=False):
        
        __slots__ = 'matrix'
# ==========================Создание===========================================     
        if isinstance(n, list):
            length = len(n[0])
#             Задать списком
            for i in n:
                assert length == len(i), 'Не прямоугольная матрица'
                  
            self.matrix = n
            del length
        else:
#             Задать размером
            assert n > 0 , 'Неверные данные'
            assert m > 0 , 'Неверные данные'
            assert isinstance(n, int), 'Неверные данные'
            assert isinstance(m, int), 'Неверные данные'
            
            if n >= 0 and m >= 0: 
                self.matrix = [[0 for j in range(m)] for i in range(n)]
                
# ========================Транспонирование=====================================   
    def T(self):
        
        matrix_T = [[0 for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        
        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                matrix_T[i][j] = self.matrix[j][i]
        return Matrix(matrix_T)
    
# ========================Размер Матрицы=======================================

    def shape(self):
        return [len(self.matrix), len(self.matrix[0])]
    
# =======================Изменение элементов матрицы===========================

    def __getitem__(self,key):
        return self.matrix[key]
    
    def __setitem__(self,key,value):
        self.matrix[key] = value
        

# ========================Длина================================================

    def __len__(self):
        return len(self.matrix)
    
# ==========================Сложение=========================================== 

    def __add__(self, other):
        # Копирование для того чтобы не изменять self
        help_m = copy.deepcopy(self)
        help_oth = copy.deepcopy(other)
        # Если число, то каждому элементу + other  
        if isinstance(other, float) or isinstance(other, int):
            for i in range(len(self)):
                for j in range(len(self[0])):
                    help_m[i][j] = help_m[i][j] + other 
        # Иначе соответствующие элементы 
        else:
            if help_m.shape() == help_oth.shape():
                for i in range(len(self)):
                    for j in range(len(self[0])):
                        help_m[i][j] = help_m[i][j] + help_oth[i][j]
            else:
                assert 1 == 0, 'Неправильная размерность матрицы'
            
            
        return help_m
    
    def __radd__(self, other):
        
        help_m = copy.deepcopy(self)
        help_oth = copy.deepcopy(other)

        if isinstance(other, float) or isinstance(other, int):
            for i in range(len(self)):
                for j in range(len(self[0])):
                    help_m[i][j] = help_m[i][j] + other 
                    
        return help_m
    
# =======================Вычитание=============================================

    def __sub__(self, other):
        
        help_m = copy.deepcopy(self)
        help_oth = copy.deepcopy(other)

        if isinstance(other, float) or isinstance(other, int):
            for i in range(len(self)):
                for j in range(len(self[0])):
                    help_m[i][j] = help_m[i][j] - other 
                    
        else:
            if help_m.shape() == help_oth.shape():
                for i in range(len(self)):
                    for j in range(len(self[0])):
                        help_m[i][j] = help_m[i][j] - help_oth[i][j]
            else:
                assert 1 == 0, 'Неправильная размерность матрицы'
            
        return help_m
    
    def __rsub__(self, other):
        
        help_m = copy.deepcopy(self)
        help_oth = copy.deepcopy(other)

        if isinstance(other, float) or isinstance(other, int):
            for i in range(len(self)):
                for j in range(len(self[0])):
                    help_m[i][j] = other - help_m[i][j]
                    
        return help_m
        
 # =======================Умножение============================================

    def __mul__(self, other):
        
        help_m = copy.deepcopy(self)
        help_oth = copy.deepcopy(other)

        if isinstance(other, float) or isinstance(other, int):
            for i in range(len(self)):
                for j in range(len(self[0])):
                    help_m[i][j] = help_m[i][j] * other 
                    
        else:
            if help_m.shape() == help_oth.shape():
                for i in range(len(self)):
                    for j in range(len(self[0])):
                        help_m[i][j] = help_m[i][j] * help_oth[i][j]
            else:
                assert 1 == 0, 'Неправильная размерность матрицы'
            
        return help_m
    

    def __rmul__(self, other):
        
        help_m = copy.deepcopy(self)
        help_oth = copy.deepcopy(other)

        if isinstance(other, float) or isinstance(other, int):
            for i in range(len(self)):
                for j in range(len(self[0])):
                    help_m[i][j] = help_m[i][j] * other 
                        
        return help_m


# =======================Деление целочисленное=================================
    def __floordiv__(self, other):
        
        help_m = copy.deepcopy(self)
        help_oth = copy.deepcopy(other)

        if isinstance(other, float) or isinstance(other, int):
            for i in range(len(self)):
                for j in range(len(self[0])):
                    help_m[i][j] = help_m[i][j] // other 
                    
        else:
            if help_m.shape() == help_oth.shape():
                for i in range(len(self)):
                    for j in range(len(self[0])):
                        help_m[i][j] = help_m[i][j] // help_oth[i][j]
            else:
                assert 1 == 0, 'Неправильная размерность матрицы'
            
        return help_m
    


    def __rfloordiv__(self, other):
        
        help_m = copy.deepcopy(self)
        help_oth = copy.deepcopy(other)

        if isinstance(other, float) or isinstance(other, int):
            for i in range(len(self)):
                for j in range(len(self[0])):
                    help_m[i][j] =  other // help_m[i][j]  
                    
        return help_m


# ================================Деление======================================
    def __truediv__(self, other):
        
        help_m = copy.deepcopy(self)
        help_oth = copy.deepcopy(other)

        if isinstance(other, float) or isinstance(other, int):
            for i in range(len(self)):
                for j in range(len(self[0])):
                    help_m[i][j] = help_m[i][j] / other 
                    
        else:
            if help_m.shape() == help_oth.shape():
                for i in range(len(self)):
                    for j in range(len(self[0])):
                        help_m[i][j] = help_m[i][j] / help_oth[i][j]
            else:
                assert 1 == 0, 'Неправильная размерность матрицы'
            
        return help_m
    
    def __rtruediv__(self, other):
        
        help_m = copy.deepcopy(self)
        help_oth = copy.deepcopy(other)

        if isinstance(other, float) or isinstance(other, int):
            for i in range(len(self)):
                for j in range(len(self[0])):
                    help_m[i][j] = other / help_m[i][j] 
                    
         
        return help_m
    
# ====================Нахождение лучшей строки=================================
    def best_line(self):
        
        h_dict = {}
        maxim = 0
        for k, v in enumerate(self):
            maxim = v.count(0)
            sp = [i for i in h_dict.values()]


            if len(h_dict) != 0:
                if sp[0][0] == maxim:
                    h_dict[k] = [maxim , sum(map(abs, v))]

                if sp[0][0] < maxim:
                    h_dict = {}
                    h_dict[k] = [maxim, sum(map(abs, v))]
            else:
                h_dict[k] = [maxim, sum(map(abs, v))]
#         minim = 2**64
#         for k, v in h_dict.items():
#             if minim > v[1]:
#                 minim = v[1]
#         sp = [k for k, v in h_dict.items() if v[1] != minim ]
#         for i in sp:
#             del h_dict[i]

        return list(h_dict.keys())[0]  


    # ========================Удаление Элемента=========================
    def __delitem__(self, key):
        del self.matrix[key]

# ======================Рекурсивный определитель===============================
    def det(self):
        assert self.shape()[0] == self.shape()[1], 'Не квадратная'
        line = self.best_line()
        summ = 0
        if self.shape() == [1,1]:
            return self[0][0]
        else:
            for ind, elem in enumerate(self[line]):
                if elem != 0:
                    matr = copy.deepcopy(self)
                    for i in range(len(matr)):
                        del matr[i][ind]
                    del matr[line]
                    summ += ((-1) ** (ind + line)) * (matr.det()) * elem           
            return summ
            
                
    def __str__(self):
        string = ''
        for line in self.matrix:
        
            string += ', '.join([str(i) for i in line])
            string += '\n'
        return string


# скалярное умножение матриц
    @staticmethod
    def dot(first, second):
        # считываем кол-во строк и столбцов матриц
        m1, n1 = first.shape() # m - строки, n - столбцы
        m2, n2 = second.shape()
        assert n1 == m2, 'Не правильная размерность матриц'

        mtrx = Matrix(m1, n2)
        for i in range(m1): # кол-во строк первой
            for j in range(n2): # кол-во столбцов второй
                summ = 0
                for index in range(n1): # n1 == m2
                    summ += first[i][index] * second[index][j] 
                mtrx[i][j] = summ

        return mtrx




    # считывание матричного уравнения и его решение 
    @staticmethod
    def do_equation(equation: str):
        alph = 'ABCDEFGHIJKLNOPQRSTUVWXYZ' # за исключением M
        dict_mtrx = {}
        for elem in equation: # считываем вместо букв - матрицы
            if elem in alph and elem not in dict_mtrx:
                dict_mtrx[elem] = Matrix.get_by_console(elem)

        for key in dict_mtrx.keys(): # меняем буквы на матрицы 
            equation = equation.replace(key, f'dict_mtrx["{key}"]')

        try: 
            return eval(equation)
        except:
            return 'Посчитать не удалось'


    # консольное считывание матрицы
    @staticmethod
    def get_by_console(name: str):
        m = int(input(f'Введите кол-во строк матрицы {name}:\n'))
        n = int(input(f'Введите кол-во столбцов матрицы {name}:\n'))
        mtrx = Matrix(m, n)
        for i in range(m):
            for j in range(n):
                # пока принимаем только числа
                mtrx[i][j] = float(input(f'Введите элемент a({i+1}, {j+1}):\n'))
        return mtrx

