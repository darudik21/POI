import random


def power(x, y, p):
    res = 1

    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p

        y = y >> 1
        x = (x * x) % p

    return res


def miillerTest(d, ni):
    a = 2 + random.randint(1, ni - 4)

    x = power(a, d, ni)

    if x == 1 or x == ni - 1:
        return True

    while d != ni - 1:
        x = (x * x) % ni
        d *= 2

        if x == 1:
            return False
        if x == ni - 1:
            return True

    return False


def isPrime(ni, ki):
    if ni <= 1 or ni == 4:
        return False
    if ni <= 3:
        return True
    d = ni - 1
    while d % 2 == 0:
        d //= 2

    for i in range(ki):
        if not miillerTest(d, ni):
            return False

    return True



k = 4
n = int(input('Введите число: '))
if isPrime(n, k):
    print(n,' - Простое число')
else:
    print(n, ' - Составное число')