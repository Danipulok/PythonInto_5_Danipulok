# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, 
# которому этот месяц принадлежит (зима, весна, лето или осень).

def season(month):
    if month in [1,2,12]:
        return('Win')
    if 3 <= month <= 5:
         return('Spr')
    if 6 <= month <= 8:
        return('Sum')
    if 9 <= month <= 11:
        return('Aut')
    else:
        return('Error')

while(True):
    inp = int(input('Введите номер месяца: '))
    if season(inp) == 'Win':
        print('Время года — Зима')
        break
    elif season(inp) == 'Spr':
        print('Время года — Весна')
        break
    elif season(inp) == 'Sum':
        print('Время года — Лето')
        break
    elif season(inp) == 'Aut':
        print('Время года — Осень')
        break
    else:
        print("Ошибка. Пожалуйста, введите число от 1 до 12.")
        continue
