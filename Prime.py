from array import *
arr=array('i',[])

n=int(input("ENTER THE LENGTH OF THE STRING: "))

for i in range(0,n,1):
    x=int(input("ENTER THE NEXT NUMBER: "))
    arr.append(x)
print(arr)

for j in range(0,n,1):
    a=arr[j]
    c=0
    for e in range(1,a+1,1):
        if a%e==0:
            c=c+1
    if c==2:
        print(a)