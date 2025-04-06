def monotic(arr):
    inc = dec = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            inc = True
        elif arr[i] < arr[i - 1]:
            dec = True
        if inc and dec:
            return False
    return True
        

arr = [6,5,4,4]
arr2 = [5,15,20,10]

print(monotic(arr))
print(monotic(arr2))