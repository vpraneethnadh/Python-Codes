def search(arr,x):
    for i in arr:

        if i==x:
            return 1
            break
    return 0

from array import *

arr=array('i',[])

n=int(input("ENTER THE LENGTH OF THE STRING: "))

for i in range(0,n,1):
    x=int(input("ENTER THE NUMBER: "))
    arr.append(x)

print(arr)
x=int(input("ENTER ANY NUMBER: "))

if search(arr,x)==1:
    print("ELEMENT FOUND")
else:
    print("ELEMENT NOT FOUND")
