# В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, 
# сколько раз оно встречалось в этом тексте.
# Задачу необходимо решить с использованием словаря.

from pprint import pprint

inp = input('Введите строку: ')
lst = inp.split(' ')
dct = {}

for element in lst:
    if element in dct:
        dct[element] += 1
    else:
        dct[element] = 1

pprint(dct)