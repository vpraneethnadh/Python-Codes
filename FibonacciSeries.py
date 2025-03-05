def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)
fib(10)