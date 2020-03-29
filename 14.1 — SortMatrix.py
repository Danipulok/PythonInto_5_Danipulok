# Написать функцию сортировки двухмерного списка МхМ (матрицы)

# Значение М - задаётся пользователем, с клавиатуры. Может быть любым целым, положительным числом, больше 5.
# Функция должна:
# 1. найти сумму элементов столбцов и отсортировать столбцы по возрастанию этих сумм
# 2. отсортировать каждый нечётный столбец по возрастанию значений снизу
# вверх, а каждый чётный столбец по возрастанию значений сверху вниз.

# Также, ваша программа должна иметь функцию вывода данного списка на экран. 
# При выводе, внизу каждого столбца должна выводиться сумма элементов этого столбца.

# Что можно использовать:
# 1. для создания списка использовать ТОЛЬКО 'list comprehension' и
# генератор случайных чисел. Диапазон случайных чисел для заполнения
# списка от 1 до 50. Список должен создаваться однострочным
# выражением.
# 2. Можно использовать ТОЛЬКО ДВА списка. Первый это двухмерный список
# размером МхМ, второй, вспомогательный, одномерный список размером
# М. Использование других списков (или коллекций) НЕДОПУСТИМО.
# 3. Можно использовать ТОЛЬКО ОДНУ переменную М для хранения размера
# списка, плюс переменные циклов for.
# 4. Для сортировки можно использовать алгоритм пузырьковой сортировки.
# Использование встроенных функций сортировки - НЕДОПУСТИМО (да и не
# получится их использовать)!
# 5. Решение должно включать ТОЛЬКО ДВЕ функции: функцию сортировки (по
# правилам описанным выше) и функцию вывода на экран.
# Задача считается решённой верно при условии соблюдения всех требований.

import random

size = int(input('Введите размер матрицы: '))
matrix = [[random.randint(1, 50) for i in range(size)] for i in range(size)]

def PrintMatrix(size, matrix, status):

    if status == 0:
        status = ' Before sort:'
    else:
        status = ' After sort:'
    
    # Upper string
    print()
    print('\u256D', end = '')  # ╭
    print('\u2500'*((size*4)+1), end = '')  # ─
    print('\u256E')  # ╮

    # 'Before sort' or 'After sort' string
    print('\u250A', end = '')  # ┊
    print('' + str(status), end = '')
    print(' ' * ((size*4)-len(status)+1), end = '')
    print('\u250A')  # ┊

    # Border after 'Before sort' or 'After sort'
    print('\u251C', end = '')  # ├
    print('\u2500'*((size*4)+1), end = '')  # ─
    print('\u2524')  # ┤

    # Print Matrix
    for i in range(size):
        print('\u250A', end='')  # ┊
        for j in range(size):
            print('{:>4}'.format(matrix[i][j]), end = '')
        print('', '\u250A')

    # Border before 'Sum'
    print('\u251C', end = '')  # ├
    print('\u2500'*((size*4)+1), end = '')  # ─
    print('\u2524')  # ┤

    # Making list of sums of colums
    sum_ = 0  # sum of the coloumn
    lst = []  # list of sums of coloumns
    for j in range(size):
        for i in range(size):
            sum_ += matrix[i][j]
        lst.append(sum_)
        sum_ = 0

    # Print sum of colums
    print('\u250A', end = '')  # ┊
    for i in lst:
        print('{:>4}'.format(i), end = '')
    print(' \u250A')  # ┊

    # Last string
    print('\u2570',end = '')  # ╰
    print('\u2500'*((size*4)+1), end = '')  # ─
    print('\u256F') # ╯

def SortMatrix(size, matrix):

    # Making list of sums of colums
    sum_ = 0  # sum of the coloumn
    lst = []  # list of sums of coloumns
    for j in range(size):
        for i in range(size):
            sum_ += matrix[i][j]
        lst.append(sum_)
        sum_ = 0

    # Sort colomns and list
    for _ in range(size):
        flag = True
        for col in range(size-1):
            if lst[col] > lst[col+1]:
                for elem in range(size):
                    matrix[elem][col], matrix[elem][col+1] = matrix[elem][col+1], matrix[elem][col]
                lst[col], lst[col+1] = lst[col+1], lst[col]
                flag = False
        if flag:
            break

    # Sort elements in colomns
    for col in range(size):
        for j in range(size):
            for i in range(size-1):
        
                if j%2 == 1:  # нечётная
                    flag = True
                    if matrix[i][j] > matrix[i+1][j]:
                        matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]
                        flag = False
                    if flag:
                        continue
            
                else: # чётная
                    flag = True
                    if matrix[i][j] < matrix[i+1][j]:
                        matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]
                        flag = False
                    if flag:
                        continue

PrintMatrix(size, matrix, 0)
SortMatrix(size, matrix)
PrintMatrix(size, matrix, 1)