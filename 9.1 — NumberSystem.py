# Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).
# Небольшая подсказка. В этой задаче вам понадобится:
#     - список
#     - метод `revers()` (или срез [::-1], или вместо `revers()` использовать `insert()` тогда не придётся разворачивать 
#     список), чтоб развернуть список, метод `join()`
#     - строка `ascii_uppercase` из модуля `string` (её можно получить если сделать импорт `from string import 
#     ascii_uppercase`), она содержит все буквы латинского алфавита.

inp = int(input('Введите десятичное число: '))
toNumSys = int(input('Введитие, в какую систему счисления перевести (2-36): '))

def numSys(decim, targetNumSys):
    lst_ost = []
    while decim // targetNumSys != 0:
        decim_n = decim
        lst_ost.append(decim_n // targetNumSys)
        decim = decim - decim // targetNumSys
    return lst_ost

print(numSys(inp, toNumSys))



        