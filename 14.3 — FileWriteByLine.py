# Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.
# Каждая введённая строка, в файле, должна начинаться с новой строки.

lst = []
while True:
    inp = input()
    if inp != '':
        lst.append(inp)
    else:
        break 

print(lst)

file = open('14.2.txt', 'w', encoding='utf-8')
for line in lst:
    file.write(line)
    file.write('\n')

file.close()