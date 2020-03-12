# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью 
# кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.

from math import sqrt

def square(side):
    perim = int(side*4)
    square = int(side*side)
    diag = int(side*sqrt(2))
    return [perim, square, diag]

inp = int(input('Введите сторону квадрата: '))
print('''
Периметр квадрата — {}
Площадь квадрата — {}
Диагональ квадрата — {}     
    '''.format(
        (square(inp)[0]),
        (square(inp)[1]),
        (square(inp)[2])
        )
    )