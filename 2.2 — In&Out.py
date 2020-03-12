# Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере (пробелы важны!). 

# Первая строка содержит следующее значение, а вторая строка содержит предыдущее значение введёного числа.
# Пример вывода:
# Please enter an integer number: 1234
# The next number for the number 1234 is 1235.
# The previous number for the number 1234 is 1233.
# или
# Please enter an integer number: 0
# The next number for the number 0 is 1.
# The previous number for the number 0 is -1.

# Вывод программы должен соответствовать примеру!

a = input('Please enter an integer number: ')
b = int(a)+1
print('The next number for the number ' + a + ' is ' + str(b) + '.')
b = int(a)-1
print('The previous number for the number ' + a + ' is ' + str(b) + '.')