# Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).
# Небольшая подсказка. В этой задаче вам понадобится:
#     - список
#     - метод `revers()` (или срез [::-1], или вместо `revers()` использовать `insert()` тогда не придётся разворачивать 
#     список), чтоб развернуть список, метод `join()`
#     - строка `ascii_uppercase` из модуля `string` (её можно получить если сделать импорт `from string import 
#     ascii_uppercase`), она содержит все буквы латинского алфавита.

from string import ascii_uppercase

inp = int(input('Введите десятичное число: '))
toNumSys = int(input('Введитие, в какую систему счисления перевести (2-36): '))

def numSys(decim, targetNumSys):
    alf = ascii_uppercase
    res = ''
    while decim != 0:
        if (decim % targetNumSys < 10):
            res += str(decim % targetNumSys)
        else:
            res += str(alf[(decim % targetNumSys) - 10])
        decim //= targetNumSys
    res = res[::-1]
    return res

print('Результат:', numSys(inp, toNumSys))

# Или:

# inp = int(input('Введите десятичное число: '))
# toNumSys = int(input('Введитие, в какую систему счисления перевести (2-36): '))

# def numSys(decim, targetNumSys):
#     lst_ost = []
#     while decim != 0:
#         decim_n = decim
#         if (decim_n % targetNumSys < 10):
#             lst_ost.append(decim_n % targetNumSys)
#         elif (decim_n % targetNumSys == 10):
#             lst_ost.append('A')
#         elif (decim_n % targetNumSys == 11):
#             lst_ost.append('B')
#         elif (decim_n % targetNumSys == 12):
#             lst_ost.append('C')
#         elif (decim_n % targetNumSys == 13):
#             lst_ost.append('D')
#         elif (decim_n % targetNumSys == 14):
#             lst_ost.append('E')
#         elif (decim_n % targetNumSys == 15):
#             lst_ost.append('F')
#         elif (decim_n % targetNumSys == 16):
#             lst_ost.append('G')
#         elif (decim_n % targetNumSys == 17):
#             lst_ost.append('H')
#         elif (decim_n % targetNumSys == 18):
#             lst_ost.append('I')
#         elif (decim_n % targetNumSys == 19):
#             lst_ost.append('J')
#         elif (decim_n % targetNumSys == 20):
#             lst_ost.append('K')
#         elif (decim_n % targetNumSys == 21):
#             lst_ost.append('L')
#         elif (decim_n % targetNumSys == 22):
#             lst_ost.append('M')
#         elif (decim_n % targetNumSys == 23):
#             lst_ost.append('N')
#         elif (decim_n % targetNumSys == 24):
#             lst_ost.append('O')
#         elif (decim_n % targetNumSys == 25):
#             lst_ost.append('P')
#         elif (decim_n % targetNumSys == 26):
#             lst_ost.append('Q')
#         elif (decim_n % targetNumSys == 27):
#             lst_ost.append('R')
#         elif (decim_n % targetNumSys == 28):
#             lst_ost.append('S')
#         elif (decim_n % targetNumSys == 29):
#             lst_ost.append('T')
#         elif (decim_n % targetNumSys == 30):
#             lst_ost.append('U')
#         elif (decim_n % targetNumSys == 31):
#             lst_ost.append('V')
#         decim //= targetNumSys
#     lst_ost = lst_ost[::-1]
#     res = ''.join(str(element) for element in lst_ost)
#     return res

# print(numSys(inp, toNumSys))