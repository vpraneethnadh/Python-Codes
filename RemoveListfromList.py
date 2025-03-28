def delList(lst):
    res = []
    for i in lst:
        if i:
            res.append(i)
    print(res)

lst = [[1, 2], [], [3, 4], [], [5]]
delList(lst)
