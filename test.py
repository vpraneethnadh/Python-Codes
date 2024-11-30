from numpy import *

arr=array([1,2,3,4,5])
print(sum(arr))
print(min(arr))
print(max(arr))
print(sin(arr))
print(cos(arr))
print(tan(arr))
print(sort(arr))

a=array([1,2,3,4,5])
b=array([6,7,8,9,10])
print(concatenate([a,b]))

c=array([2,6,8,10])
d=c
print(c)
print(d)

print(id(c))
print(id(d))

arra=array([2,6,8,1,3])
arrb=arra.view()

print(arra)
print(arrb)

print(id(arra))
print(id(arrb))
