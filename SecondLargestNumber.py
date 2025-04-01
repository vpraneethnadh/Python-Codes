def sort(list):
    for i in range(len(list)):
        for j in range(i+1, len(list), 1):
            if list[i] < list[j]:
                list[i], list[j] = list[j], list[i]
    return list

list = [5,3,4,1,2]
list2 = sort(list)
print("Second Largest Element:",list2[1])

