# Дан текст, состоящий из нескольких строк. Выведите слово, которое в этом тексте встречается чаще всего. 
# Если таких слов несколько, выведите последнее.
# Задачу необходимо решить с использованием словаря.

inp = input('Введите текст: ')
lst = inp.split(' ')
dct = {}
max_ = 0
max_i = '0'

for element in lst:
    if element in dct:
        dct[element] += 1
    else:
        dct[element] = 1

for element in dct:
    if dct[element] >= max_:
        max_ = dct[element]
        max_i = element

print(max_i)