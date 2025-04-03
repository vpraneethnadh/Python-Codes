def sort(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

list = [1,3,2,5,4]
list2 = sort(list)

print("Smallest Element:", list2[0])
print("Largest Element:", list2[-1])