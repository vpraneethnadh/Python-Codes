def MultiplicationOfArrDividedbyn(arr,n):
    mul = 1
    for i in range(len(arr)):
        mul *= arr[i]
    return mul % n

arr = [100,10,5,25,35,14]
n = 11

arr2 = [100,10]
n2 = 5

print(MultiplicationOfArrDividedbyn(arr,n))
print(MultiplicationOfArrDividedbyn(arr2,n2))