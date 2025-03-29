def removeMultiple(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]==list[j]:
                del(list[i])
    print(list)

list1 = [1,2,3,4,5,4]
list2 = [1,2,3,4,5,6]

removeMultiple(list1)
removeMultiple(list2)