n = input("ENTER ANY WORD: ")
l = len(n)

i=0
k=l-1
while(i<=l-1):
    for j in range(1,k,1):
        print("-")
    for t in range(0,i,1):
        print(n[t])
    print("\n")
    i=+1
    k=-1