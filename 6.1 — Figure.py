# При помощи вложенных циклов (можно for, можно while) нарисовать следующие фигуру, изображённую ниже. 
# Пользователь вводит с клавиатуры высоту фигуры.

#             *
#           *   *
#         *       *
#       *           *
#     *               *
#   *                   *
# * * * * * * * * * * * * *

while (True):
    inp = int(input('Введите высоту: '))
    if (inp <= 0):
        print('Ошибка. Необходимо ввести натуральное число.')
        continue
    else:
        break  
    
cnt = 1 # номер строки минус один
n = inp - 1 # переменная
     
#Первая строка
for _ in range(n):
    print(' ', end = '')
print('*')

#Основа
for _ in range(1, inp-1):
    for _ in range(n-1):
        print(' ', end = '')
    print('*', end = '')
    for _ in range(cnt):
        print(' ', end = '')
    print('*')
    n -= 1
    cnt += 2

#Последняя строка
for _ in range(2*inp-1):
    print('*', end = '')