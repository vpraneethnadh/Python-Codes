def difference(arr, n):
    d1 = 0
    d2 = 0

    for i in range(0, n):

        for j in range(0, n):
            if (i == j):
                d1 += arr[i][j]

            if (i == n - j - 1):
                d2 += arr[i][j]

    return abs(d1 - d2)


def printCornerElement(arr):
    n = len(arr)

    m = len(arr[0])

    print("left top corner :", arr[0][0])
    print("right top corner :", arr[0][m - 1])
    print("left bottom corner :", arr[n - 1][0])
    print("right bottom corner :", arr[n - 1][m - 1])

    corner_sum = (arr[0][0] + arr[0][m - 1] + arr[n - 1][0] + arr[n - 1][m - 1])

    print("\nCorner elements Sum :", corner_sum)

n = 3

arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

print("Diagnol Difference is: ",difference(arr, n))

res = [sum(idx) / len(idx) for idx in zip(*arr)]

res = sum(res) / len(res)

print("Matrix Mean : " + str(res))
printCornerElement(arr)
