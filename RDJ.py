
n = int(input("Enter a Number: "))
list=[]

for i in range(1,n+1):
    for j in range(1,i):
        if (i%j == 0) :
            list.append(i)

print(list)