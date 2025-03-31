def evenOdd(list):
    even = []
    odd = []
    for i in range(len(list)):
        if(list[i] % 2 == 0):
            even.append(list[i])
        else:
            odd.append(list[i])
    print(even)
    print(odd)

list = [1,2,3,4,5,6,7,8,9,10]
print(evenOdd(list))