def freq(lst):
    print("Element\tFrequency")
    counted = set()
    for i in range(len(lst)):
        if lst[i] not in counted:
            n = 0
            for j in range(i + 1, len(lst)):
                if lst[j] == lst[i]:
                    n += 1
            print(lst[i], "\t", n + 1)
            counted.add(lst[i])

lst = [1, 2, 3, 4, 5, 1, 3, 5, 3]
freq(lst)
