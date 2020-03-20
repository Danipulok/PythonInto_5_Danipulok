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
    isLen = True if len(password) >= 8 else False
    isUp, isLow, isNum, isSymb = False, False, False, False
    for i in password:
        if i.isnumeric() == True:
            isNum = True
        if i.isupper() == True:
            isUp = True
        if i.islower() == True:
            isLow = True
        if i in ['@', '#', '%', '&', '_']:
            isSymb = True
    if isLen == True and isUp == True and isLow == True and isNum == True and isSymb == True:
        return True
    else:
        return False
    
print('Пароль соответствует требованиям!' if isPassCor(inp) == True else 'Пароль не соответствует требованиям!')
    