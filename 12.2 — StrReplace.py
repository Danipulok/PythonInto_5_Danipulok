# Имеется строка вида: AABABBAABBBAB. Необходимо написать функцию которая заменит буквы A на B, а B, соответственно, на A.
# Замену можно производить ТОЛЬКО используя функцию replace(). 
# В результате применения функции к исходной строке, функция должна вернуть строку: BBABAABBAAABA

string = 'AABABBAABBBAB'

def StrRepl(string):
    new_str = ''
    # for i in range(len(string)):
    #     if string[i] == 'A':
    #         new_str += string[i].replace('A', 'B')
    #     else:
    #         new_str += string[i].replace('B', 'A')
    lst = [string[i].replace('A', 'B') if string[i] == 'A' else string[i].replace('B', 'A') for i in range(len(string))]
    return new_str.join(lst)
    # return new_str
 
print(StrRepl(string))