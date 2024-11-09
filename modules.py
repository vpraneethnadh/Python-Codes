def sumofdigits(n):
    s = 0
    while n != 0:
        r = n % 10
        n = n // 10
        s = s + r
    return s


def reverse(n):
    s = 0
    while n != 0:
        r = n % 10
        n = n // 10
        s = (s * 10) + r

    return s


def factorial(n):
    s = 1
    for i in range(1, n + 1, 1):
        s = s * i

    return s


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def idiv(a, b):
    return a // b

def evenodd(n):
    if n % 2 == 0:
        return 0
    else:
        return 1

