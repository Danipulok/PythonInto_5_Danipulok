# n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. 
# Сколько яблок достанется каждому школьнику? 
# Сколько яблок останется в корзинке? 
# Программа получает на вход числа `n` и `k` и должна вывести искомое количество яблок (два числа).

n = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок: "))

if (k>=n):
    print('{} яблок каждому школьнику.'.format(n//k))
    print('{} яблок останется в корзине.'.format(n-k*(n//k)))
else:
    print('0 яблок каждому школьнику.')
    print('{} яблок останется в корзине.'.format(k))