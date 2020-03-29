# Необходимо написать функцию для проверки корректности пароля. Функция принимает в качестве параметра пароль
# который необходимо проверить и возвращает True если пароль верный, иначе False.

# Правила которым должен соответствовать пароль:
# 	a. длина пароля должна быть больше или равна 8 символам
# 	b. пароль должен содержать символы латинского алфавита верхнего и нижнего регистров
# (a - z и  A - Z обязательно должны присутствовать оба регистра)
# 	c. пароль должен содержать цифры от 0 до 9 (минимум 1 символ)
# 	d. пароль должен содержать специальные символы: @ # % & _ (минимум 1 символ)
# Можно использовать функции isnumeric(), isupper(), islower().

inp = input('Введите пароль: ')

def isPassCor(password):
    res = True
    if not (len(password) >= 8):
        print('Длина пароля должна быть минимум в восемь символов.')
        res = False
    if not any(i.isnumeric() for i in password):
        print('В пароле должна содержаться как минимум одна цифра.')
        res = False
    if not any(i.isupper() for i in password):
        print('Должен содержаться как минимум один большая символ.')
        res = False
    if not any(i.islower() for i in password):
        print('Должен содержаться как минимум один маленький символ.')
        res = False
    if not any(i in ['@', '#', '%', '&', '_'] for i in password):
        print('Пароль должен содержаться один из следующиз спец.символов: (@, #, %, &, _).')
        res = False
    return res

print('Пароль соответствует требованиям.' if isPassCor(inp) == True else 'Пароль не соответствует требованиям.')


# Or:

# def isPassCor(password):
#     isLen = True if len(password) >= 8 else False
#     isUp, isLow, isNum, isSymb = False, False, False, False
#     for i in password:
#         if i.isnumeric() == True:
#             isNum = True
#         if i.isupper() == True:
#             isUp = True
#         if i.islower() == True:
#             isLow = True
#         if i in ['@', '#', '%', '&', '_']:
#             isSymb = True
#     if isLen == True and isUp == True and isLow == True and isNum == True and isSymb == True:
#         return True
#     else:
#         return False
    
# print('Пароль соответствует требованиям!' if isPassCor(inp) == True else 'Пароль не соответствует требованиям!')