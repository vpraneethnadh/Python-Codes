import numpy as np
# (i)
def solve(matrix):
   m = len(matrix)
   if m == 1: return matrix[0][0]

   count = 0
   for i in range(m):
      count += matrix[i][i]
      count += matrix[i][-1 - i]

   if m % 2 == 1: count -= matrix[m // 2][m // 2]

   return count
# (ii)
def row(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(0, rows):
        sumRow = 0
        for j in range(0, cols):
            sumRow = sumRow + matrix[i][j]
        print("Sum of " + str(i + 1) + " row: " + str(sumRow))

    for i in range(0, rows):
        sumCol = 0
        for j in range(0, cols):
            sumCol = sumCol + matrix[j][i]
        print("Sum of " + str(i + 1) + " column: " + str(sumCol))

# (iv)
def product(mat, n):
    d1 = 0
    d2 = 0

    for i in range(n):
        d1 += mat[i][i]
        d2 += mat[i][n - i - 1]


    return d1 * d2


matrix = [[1,2],[3,4]]
matrix2 = [[7,10],[15,22]]

print(solve(matrix))
print(solve(matrix2))

print(row(matrix))
print(row(matrix2))

print(np.diff(matrix))
print(np.diff(matrix2))

# (iii)

if __name__ == '__main__':
    x = len(matrix)
    y = len(matrix2)
    print(product(matrix, x))
    print(product(matrix2, y))