for i in range(65,113):
    if i<=90:
        print(chr(i),end=" ")
        if (i-64)%8==0:print("")
    if i>90 and i<=96:
        print(chr(i-26),end=" ")
        if (i-90)%6==0:print("")
    if i>96:
        print(chr(i-26),end=" ")
        if (i-96)%8==0:print("")