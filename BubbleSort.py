def bsort(k, n):
    for i in range(n - 1):
        if (k[i] < k[i + 1]):
            t = k[i]
            k[i] = k[i + 1]
            k[i + 1] = t
    if n - 1 > 1:
        bsort(k, n - 1)


k = [1, 10, 4, 3, 5, 2]
n = len(k)
a = bsort(k, n)
print(a)
