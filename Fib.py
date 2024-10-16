'''
def fib(n):
    a=0
    b=1
    if n==1:
        print(0)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c,end=" ")
fib(10)

def fact(n):
    for i in range(1,n,1):
        n=n*i
    print(n)

fact(5)


import sys

sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())
i=0

def greet():
    global i
    i+=1
    print("HELLO",i)
    greet()

greet()

def fact(n):
    if n==0:
        return 1

    return n*fact(n-1)

result=fact(5)
print(result)

f=lambda a:a*a*a
n=int(input("ENTER ANY NUMBER: "))
result=f(n)
print(result)

f=lambda a,b:a+b
x=int(input("ENTER THE FIRST NUMBER: "))
y=int(input("ENTER THE SECOND NUMBER: "))
result=f(x,y)
print(result)
'''
#def is_even(n):
#    return n%2!=0
from functools import reduce

nums=[8,11,6,9,5,3,4,7,10,2]

even=list(filter(lambda n: n%2==0 ,nums))

double=list(map(lambda n: n*2,nums))

sum=reduce(lambda a,b:a+b,nums)

print(even)
print(double)
print(sum)
