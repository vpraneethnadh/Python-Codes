def prime(n):
    n1 = 0
    for i in range(1, n):
        if(n % i == 0):
            n1 += 1
    if(n1 < 2):
        return True
    else:
        return False

print(prime(5))
print(prime(10))