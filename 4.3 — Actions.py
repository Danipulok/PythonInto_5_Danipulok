# Программа запрашивает ввод последовательности целых чисел, пока не будет введён 0. 
# Как только будет введён 0 (ноль), программа должна посчитать и вывести на экран:

# - количество введённых чисел (завершающий 0 не считается)
# - их сумму
# - среднее арифметическое (не считая завершающего числа 0)
# - определить максимальное и минимальное значение
# - определить количество чётных и не чётных элементов в последовательности

count, count_1, count_2, sum_, min_, max_= 0, 0, 0, 0, 0, 0 
while (True): 
    inp = int(input("Введите число: "))
    if int(inp) != 0:
        count += 1
        sum_ += inp
        if (min_ > inp):
            min_ = inp
        if (max_ < inp):
            max_ = inp
        if (inp % 2 == 0):
            count_2 += 1
        if (inp % 1 == 0):
            count_1 += 1
    else:
        break
print(''' 
{} — Количество введённых чисел.
{} — Сумма.
{} — Среднее арифметическое.
{} — Максимальное значение.
{} — Минимальное значение.
{} — Количество чётных элементов.
{} — Количество нечётных элементов.'''
.format(count, sum_, sum_/count, max_, min_, count_2, count_1))

# count, count_1, count_2, sum_, = 0, 0, 0, 0
# list_ = []
# print('Введите числа: ')
# while True:
#     inp = int(input())
#     if inp == 0:
#         break        
#     else:
#         list_.append(inp) 
# print(list_)
    
# max_, min_ = list_[0], list_[0]
# for i in range(len(list_)):
#     # print('{} is beaing checked'.format(list_[i]))
#     sum_ += list_[i]
#     if (min_ > list_[i]):
#         min_ = list_[i]
#         # print('min is {}'.format(min_))
#     if (max_ < list_[i]):
#         max_ = list_[i]
#         # print('max is {}'.format(max_))
#     if (list_[i] % 2 == 0):
#         count_2 += 1
#         # print('{} is %2, count_2 = {}'.format(list_[i], count_2))
#     if (list_[i] % 2 != 0):
#         count_1 += 1
#         # print('{} is %1, count_1 = {}'.format(list_[i], count_1))
    
# print(list_)    
# print(''' 
# {} — Количество введённых чисел.
# {} — Сумма.
# {} — Среднее арифметическое.
# {} — Максимальное значение.
# {} — Минимальное значение.
# {} — Количество чётных элементов.
# {} — Количество нечётных элементов.'''
# .format(len(list_), sum_, sum_/len(list_), max_, min_, count_2, count_1))