from array import *

arr=array('i',[])

n=int(input("ENTER THE LENGTH OF THE STRING: "))

for i in range(0,n,1):
    x=int(input("ENTER THE NEXT NUMBER: "))
    arr.append(x)
print(arr)

min=arr[0]
pos=0
for i in range(1,n,1):
    if min>arr[i]:
        min=arr[i]
        pos=i

print("SMALLEST NUMBER: ",min)
print("POSITION: ",pos+1)