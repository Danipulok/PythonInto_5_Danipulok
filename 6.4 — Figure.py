# При помощи вложенных циклов (можно for, можно while) нарисовать следующие фигуру, изображённую ниже. 
# Пользователь вводит с клавиатуры высоту фигуры.

#             *
#           * * *
#         * * * * *
#       * * * * * * *
#     * * * * * * * * *
#   * * * * * * * * * * *
# * * * * * * * * * * * * *
#   *         *         *
#     *       *       *
#       *     *     *
#         *   *   *
#           * * *
#             *

while (True):
    inp = int(input('Введите высоту: '))
    if (inp <= 0) or (inp %2 == 0):
        print('Ошибка. Необходимо ввести нечётное натуральное число.')
        continue
    else:
        break

# Верхняя часть
cnt = 1 # количество звёздочек 
n = inp//2 # переменная

for i in range(inp//2+1):
    for _ in range(n):
        print(' ', end = '')    
    for _ in range(cnt):
        print('*', end = '')    
    print()
    n -= 1
    cnt += 2
    
# Нижняя часть
cnt = cnt//2 + cnt%1  # кол-во пробелов посередине
cnt -= 3
n = 1 # переменная

#Основа
for _ in range(1, inp//2):
    for _ in range(n):
        print(' ', end = '')
    print('*', end = '')
    for _ in range(cnt):
        print(' ', end = '')
    print('*', end = '')
    for _ in range(cnt):
        print(' ', end = '')
    print('*')    
    n += 1
    cnt -= 1

#Последняя строка
for _ in range(n): 
    print(' ', end = '')
print('*')