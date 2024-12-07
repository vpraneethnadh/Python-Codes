'''
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        s=1
        for i in range(1,n+1,1):
           s=s*i
        print(s)

n=int(input("ENTER NAY NUMBER: "))
factorial(n)
'''

def fab(n):
    k=1
    i=1
    j=0
    while(k<=n):
        k=i+j
        print(k,end=" ")
        i=j
        j=k

n=int(input("ENTER ANY NUMBER: "))
fab(n)