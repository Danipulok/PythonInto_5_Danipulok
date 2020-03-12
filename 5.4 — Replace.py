# Дана строка. Замените в этой строке все появления буквы `h` на букву `H`,
# кроме первого и последнего вхождения.

inp = input('Введите строку:')
i_1 = inp.find('h')
i_2 = inp.rfind('h')
inp_H = inp.replace('h','H')

print('Результативная строка: ', end = '')
print(inp[:i_1+1], end = '')
print(inp_H[i_1+1:i_2], end = '')
print(inp[i_2:], end = '')