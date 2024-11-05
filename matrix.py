from numpy import *

arr1=array([
            [1,2,3,7,8,9],
            [4,5,6,10,11,12]
          ])

#converting 2-dimentional array into 1-dimentional array
arr2=arr1.flatten()
print(arr2)

#converting 1-dimentional array into 2-dimentional array for that we use a function called reshape(length,breadth)
arr3=arr2.reshape(3,4)
print(arr3)

#converting 1-dimentional array into 3-dimentional array which have two 2-dimentional array(length,breadth,height)
#in this we have two 1-dimentional array two rows each and three values in each one

arr3=arr2.reshape(2,2,3)
print(arr3)

print(arr1.dtype)
print(arr1.size)
print(arr1.ndim)
print(arr1.shape)

#matrix
#we can write matrix in diffrent forms one is the top one and the othe is the folloing one
m=matrix('1 2 3 6 ; 4 5 6 7')
print(m)

#to convert the above matrix into 4 rows and 2 coloums
n=matrix('1 2 ; 3 6 ; 4 5 ; 6 7')
print(n)
#for 3X3 matrix
a=matrix('1 2 3 ; 6 4 5 ; 1 6 7 ')
print(a)

#to print only the diagnal elements of the matrix we have a function called diagnal()
print(diagonal(a))
# to add and multiply two matrices
m1=matrix('1 2 3 ; 6 4 5 ; 1 6 7 ')
m2=matrix('1 2 3 ; 6 4 5 ; 1 6 7 ')
m3=m1+m2
print(m3)

m4=m1*m2
print(m4)
