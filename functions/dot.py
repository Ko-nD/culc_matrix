def dot(first, second):
    # считываем кол-во строк и столбцов матриц
    m1, n1 = first.shape() # m - строки, n - столбцы
    m2, n2 = second.shape()
    assert n1 == m2, 'Не правильная размерность матриц'

    mtrx = [[0 for i in range(n2)] for j in range(m1)]
    for i in range(m1): # кол-во строк первой
        for j in range(n2): # кол-во столбцов второй
            summ = 0
            for index in range(n1): # n1 == m2
                summ += first[i][index] * second[index][j] 
            mtrx[i][j] = summ

    return mtrx
