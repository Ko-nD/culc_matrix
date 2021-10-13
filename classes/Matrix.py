class Matrix:
    def __init__(self, n=1, m=1):
        __slots__ = 'matrix'
        assert n > 0, 'Неверные данные'
        assert m > 0, 'Неверные данные'
        assert isinstance(n, int), 'Неверные данные'
        assert isinstance(m, int), 'Неверные данные'

        if n >= 0 and m >= 0:
            self.n = n
            self.m = m
            self.matrix = [[0 for j in range(m)] for i in range(n)]

    @staticmethod
    def get_from_list(list_):
        if not Matrix.__check_shape(list_):
            raise Exception("Ошибка: строки разной длины")
        matrix = Matrix()
        matrix.matrix = list_
        matrix.n = len(list_)
        matrix.m = len(list_[0])
        return matrix

    @staticmethod
    def __check_shape(list_):
        c = len(list_[0])
        for i in range(1, len(list_)):
            if c != len(list_[i]):
                return False
        return True

    @staticmethod
    def get_minor(mtrx, i, j):
        return [row[:j] + row[j+1:] for row in (mtrx[:i]+mtrx[i+1:])]

    def transpose(self):
        matrix_T = [[0 for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]

        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                matrix_T[i][j] = self.matrix[j][i]

        return Matrix.get_from_list(matrix_T)

    def shape(self):
        return len(self.matrix), len(self.matrix[0])

    def __getitem__(self, key):
        return self.matrix[key]

    def __setitem__(self, key, value):
        self.matrix[key] = value

    def __len__(self):
        return len(self.matrix)

    def __get_op(self, other, op):
        n, m = self.shape()
        if isinstance(other, float) or isinstance(other, int) or isinstance(other, complex):
            result = [[op(other, self[i][j]) for j in range(m)] for i in range(n)]
        else:
            if self.shape() == other.shape():
                result = [[op(other[i][j], self[i][j]) for j in range(m)] for i in range(n)]
            else:
                raise BaseException('Неправильная размерность матрицы')
        return Matrix.get_from_list(result)

    def __add__(self, other):
        return self.__get_op(other, lambda x, y: x + y)

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(self, Matrix) and isinstance(other, Matrix):
            return Matrix.dot(self, other)
        return self.__get_op(other, lambda x, y: x * y)

    def __rmul__(self, other):
        if isinstance(self, Matrix) and isinstance(other, Matrix):
            return Matrix.dot(self, other)
        return self * other

    def __sub__(self, other):
        return self + (-1) * other

    def __rsub__(self, other):
        return self + (-1) * other

    def __floordiv__(self, other):
        return self.__get_op(other, lambda x, y: x // y)

    def __rfloordiv__(self, other):
        return self // other

    def __truediv__(self, other):
        return self.__get_op(other, lambda x, y: x / y)

    def __rtruediv__(self, other):
        return self / other

    def __best_line(self):
        """Нахождение лучшей строки для вычисления определителя"""
        h_dict = {}
        for k, v in enumerate(self):
            maxim = v.count(0)
            sp = [i for i in h_dict.values()]
            if len(h_dict) != 0:
                if sp[0][0] == maxim:
                    h_dict[k] = [maxim, sum(map(abs, v))]
                elif sp[0][0] < maxim:
                    h_dict = {k: [maxim, sum(map(abs, v))]}
            else:
                h_dict[k] = [maxim, sum(map(abs, v))]
        return list(h_dict.keys())[0]

    def __delitem__(self, key):
        del self.matrix[key]

    def det(self):
        """ Рекурсивный определитель """
        n, m = self.shape()
        assert n == m, 'Не квадратная'
        if n == 1:
            return self[0][0]
        if n == 2:
            return self[0][0] * self[1][1] - self[0][1] * self[1][0]

        line = self.__best_line()
        summ = 0
        for j, elem in enumerate(self[line]):
            if elem != 0:
                summ += ((-1) ** (j + line)) * Matrix.get_from_list(self.get_minor(self, i=line, j=j)).det() * elem
        return summ

    def swap_rows(self, i1: int, i2: int):
        """
        Меняет строки с индексами i1 и i2 местами
        :param i1: индекс 1-ой строки 
        :param i2: индекс 2-ой строки
        """
        self[i1], self[i2] = self[i2], self[i1]

    def devide_row_by_number(self, i, devider, j=0):
        """
        Деление i-ой строки на число devider начиная с j-го элемента
        :param i: индекс строки 
        :param devider: делитель строки
        :param j: индекс элемента строки с которого начинается(включительно) деление
        :return: 
        """
        assert devider != 0, 'Деление строки на ноль'
        for j in range(j, self.shape()[1]):
            self[i][j] /= devider 

    def combine_rows(self, i1, i2, k, j=0):
        """
        Вычитание из i1-ой строки i2-ую строку умноженную на число k начиная с j-го элемента
        :param i1: индекс строки из которой вычитают
        :param i2: индекс вычитаемой строки
        :param k: множитель строки с индексом i2
        :param j: индекс элемента строки с которого начинается(включительно) вычитание 
        :return:
        """
        for j in range(j, self.shape()[1]):
            self[i1][j] -= k * self[i2][j] 

    def get_index_max_elem_in_col(self, j=0):
        """
        получение индекса строки максимального элемента на j-ой позиции
        :param j: позиция макс. элемента 
        :return: int - индекс строки с макс. элементом на j-ой позиции
        """
        m, n = self.shape()
        assert 0 <= j <= n, 'Столбца с таким номером не существует'
        max_elem = 0
        for i in range(m):
            elem = abs(self[i][j])
            if elem > max_elem:
                max_elem = elem
                index = i
        return index

    # приведение матрицы к верхней треугольной
    def upper_triangular(self):
        m, n = self.shape()
        for i in range(m):
            # i совпадает с нужным j, так как идём поп диагонали
            index = self.get_index_max_elem_in_col(i)
            if i != index:
                self.swap_rows(i, index)
            self.devide_row_by_number(i, self[i][i], j=i)
            for i2 in range(i, m-1):
                self.combine_rows(i2+1, i, self[i2+1][i], j=i)

    # обратный ход (для Гаусса) применяется к верхним треугольным матрицам
    def reverse_course(self):
        m, n = self.shape()
        X_arr = [0] * m
        for i in range(m - 1, -1, -1):
            X_arr[i] = self[i][-1] - sum(x * a for x, a in zip(X_arr[i+1:n], self[i][i+1:n]))
        return X_arr
    
    def method_Gauss(self): #пока нет проверок, т.к. не понятно как объединять матрицы будем
        self.upper_triangular()
        answer = self.reverse_course()
        print(*(f"x{i+1} = {elem}" for i, elem in enumerate(answer)), sep='\n')
        return answer

    # норма по строке
    def norm_by_row(self):
        """
        Вычисление нормы по строке
        :return: норма по строке
        """
        m, n = self.shape()
        max_norm = 0
        for i in range(m):
            row_sum = 0 
            for j in range(n):
                row_sum += abs(self[i][j])
            if row_sum > max_norm:
                max_norm = row_sum
        return max_norm

    def norm_by_col(self):
        """
        Вычисление нормы по столбцу
        :return: норма по столбцу
        """
        m, n = self.shape()
        max_norm = 0
        for j in range(n):
            col_sum = 0 
            for i in range(m):
                col_sum += abs(self[i][j])
            if col_sum > max_norm:
                max_norm = col_sum
        return max_norm

    def norm_by_euclid(self):
        """
        Вычисление Евклидовой нормы (корень квадратный из суммы квадратов всех элементов матрицы)
        :return: Евклидова норма
        """
        m, n = self.shape()
        norm = 0
        for i in range(m):
            for j in range(n):
                norm += self[i][j] ** 2
        return norm ** (1/2) 

    def __str__(self):
        string = ''
        for line in self.matrix:
            string += ', '.join([str(i) for i in line])
            string += '\n'
        return string

    def write_csv(self, path='./data/', file_name='result.csv', delimiter=' '):
        """ Запись матрицы в цсв """
        with open(path + file_name, 'w') as f:
            for row in self:
                print(delimiter.join(map(repr, row)), file=f)
        print('Матрица успешно записана!')

    @staticmethod
    def dot(first, second):
        """ Cкалярное умножение матриц """
        # считываем кол-во строк и столбцов матриц
        m1, n1 = first.shape()  # m - строки, n - столбцы
        m2, n2 = second.shape()
        assert n1 == m2, 'Неправильная размерность матриц'

        mtrx = Matrix(m1, n2)
        for i in range(m1):  # кол-во строк первой
            for j in range(n2):  # кол-во столбцов второй
                summ = 0
                for index in range(n1):  # n1 == m2
                    summ += first[i][index] * second[index][j]
                mtrx[i][j] = summ

        return mtrx

    @staticmethod
    def do_equation(equation: str):
        """ Считывание матричного уравнения и его решение """
        alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        arr_mtrx = ''
        for i, elem in enumerate(equation):  # считываем вместо букв - матрицы
            if elem in alph and elem not in arr_mtrx:
                arr_mtrx += elem
                exec(f'{elem}=Matrix.get_by_console("{elem}")')
        try:
            return eval(equation)
        except:
            return 'Посчитать не удалось'

    @staticmethod
    def get_by_console(name = ''):
        """ Консольное считывание матрицы """
        m = int(input(f'Введите кол-во строк матрицы {name}:\n'))
        n = int(input(f'Введите кол-во столбцов матрицы {name}:\n'))
        mtrx = Matrix(m, n)
        for i in range(m):
            for j in range(n):
                # пока принимаем только числа
                mtrx[i][j] = float(input(f'Введите элемент {name.lower()}({i + 1}, {j + 1}):\n'))
        return mtrx

    @staticmethod
    def read_csv(path='./data/', file_name='matrix.csv', delimiter=' '):
        """ Чтение матрицы из цсв """
        return Matrix.get_from_list(
            [[float(token) for token in line.split(delimiter)] for line in open(path + file_name)]
        )

    @staticmethod
    def write_matrix_to_csv(matrix, path='./data/', file_name='result.csv', delimiter=' '):
        """ Запись матрицы в цсв """
        with open(path + file_name, 'w') as f:
            for row in matrix:
                print(delimiter.join(map(repr, row)), file=f)
        print('Матрица успешно записана!')
