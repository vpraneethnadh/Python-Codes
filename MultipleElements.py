def multiple(list):
    for i in range(len(list)):
        for j in range(i + 1,len(list)):
            if list[i] == list[j]:
                return True
    return False

list1 = [1,2,3,4,5,4]
list2 = [1,2,3,4,5,6]

print(multiple(list1))
print(multiple(list2))