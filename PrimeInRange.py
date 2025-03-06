def isPrime(n):
    n1 = 0
    for i in range(1, n):
        if(n % i == 0):
            n1 += 1
    if(n1 < 2):
        return True
    else:
        return False

def PrimeRange(n):
    for i in range(1, n):
        if isPrime(i):
            print(i)

# print(isPrime(4))
print(PrimeRange(5))
print(PrimeRange(10))