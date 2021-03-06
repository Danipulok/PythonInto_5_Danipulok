# Написать функцию, циклически сдвигающую целое число на N разрядов вправо или влево, в зависимости от третьего 
# параметра функции. Функция должна принимать три параметра: в первом параметре передаётся число для сдвига, второй 
# параметр задаёт количество разрядов для сдвига (по умолчанию сдвиг на 1 разряд), 3-й булевский параметр задаёт 
# направление сдвига (по умолчанию влево (False)).

def CyclicShift(inp, rate = 1, dir = False):
    inp = str(inp)
    if dir == False:
        res = inp[len(inp)-rate : len(inp)] + inp[: len(inp)-rate]
    else:
        res = inp[rate : len(inp)] + inp[: rate]
    return res

inp = int(input('Введите число: '))
rate = int(input('Введите кол-во разрядов, на которое хотите сдвинуть: '))
while (True):
    dir_ = input('В какую сторону выполнить сдвиг? ("+" — вправо, "-" — влево): ')
    if (dir_ == '+'):
        dir_ = False
        break
    elif (dir_ == '-'):
        dir_ = True
        break
    else:
        print('Ошибка. Введите "+" или "-".')
        continue

res = CyclicShift(inp, rate, dir_)
print(res)