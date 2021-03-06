# По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N.
# Выведите показатель степени и саму степень.
# Операцией возведения в степень, а так же функцией возведения в степень пользоваться НЕЛЬЗЯ!

# Например:
# 50          5 32            2 ** 5 = 32
# 10          3 8             2 ** 3 = 8
# 8           3 8             2 ** 3 = 8
# 7           2 4             2 ** 2 = 4
# 1           0 1             2 ** 0 = 1
# 2           1 2             2 ** 1 = 2
# 3           1 2             2 ** 1 = 2
# 4           2 4             2 ** 2 = 4
# 5           2 4             2 ** 2 = 4
# 100         6 64            2 ** 6 = 64
# 1025        10 1024         2 ** 10 = 1024
# 15431543    23 8388608      2 ** 23 = 8388608

inp_orig = int(input('Введите число: '))

inp = inp_orig
count = 0
while inp >= 2:    
    inp //= 2
    count += 1    

inp_2 = inp_orig
inp_1 = inp_orig 
square = 1
while(True):
    while inp_1 > 1:
        # if inp_1 > 100000000:
        #     inp_1 /= 33554432
        # if inp_1 > 10000000:
        #     inp_1 /= 4194304
        # if inp_1 > 1000000:
        #     inp_1 /= 262144    
        # if inp_1 > 100000:
        #     inp_1 /= 32768
        # if inp_1 > 10000:
        #     inp_1 /= 4096
        # if inp_1 > 1000:
        #     inp_1 /= 256
        # if inp_1 > 100:
        #     inp_1 /= 32
        # if inp_1 > 1:
        #     inp_1 /= 2
        inp_1 /= 2
    if inp_1 == 1:
        square = inp_2
        break
    else:
        inp_2 -= 1
        inp_1 = inp_2
              
print('Наибольшая степень двойки: {} — {}'.format(count,square), end = ' ')