# Написать функцию, которая принимает в качестве параметра целое, многозначное число. Функция должна вернуть 
# сумму произведений каждой цифры на её порядковый номер. 

# Например:
# 	есть число 874658734
# 	8 имеет порядковый номер 1,
# 	7 - 2
# 	4 - 3
# 	6 - 4
# 	5 - 5 и т. д.
# 	необходимо посчитать: 8 * 1 + 7 * 2 + 4 * 3 + 6 * 4 + 5 * 5 ..... 
# 	Задачу надо решить с использование list comprehension и функции sum() в ОДНУ строку.

inp = int(input('Введите число: '))

def sumByRate(number):
    
    res = sum([[x for x in range(1, len(str(number))+1)][j] * [int(i) for i in str(number)][j] for j in range(len(str(number)))])
    # res = sum([int(str(number)[i]) * (i + 1) for i in range(len(str(number)))])
    return res

print('Сумма с заданными параметрами:', sumByRate(inp))
