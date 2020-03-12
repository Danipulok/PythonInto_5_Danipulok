# Пользователь вводит, отдельно, строку `s` и один символ `ch`. 
# Необходимо выполнить поиск в строке `s` всех символов `ch`.
# Для решения можно использовать только функцию `find`(rfind), операторы  if и while.

inp = input('Введите строку:')
fnd = input('Введите искомый символ:')

i = 0
cnt = 0
 
while(True):
    i = inp.find(fnd, i)
    if i == -1 or i == (len(inp)-1):
        if i == (len(inp)-1):
            cnt += 1
            break
        else:
            break
    else:
        cnt += 1
        i = inp.find(fnd, i+1)

print('В строке было найдено {} искомых символов.'.format(cnt))