def rev(n):
    m=n
    s=0
    r=0
    while(n!=0):
        r=n%10
        n=n//10
        s=(s*10)+r
    return s

    if (m==s):
        return 1
    else:
        return 0

n=int(input("ENTER ANY VALUE: "))
if (rev(n)==1):
    print("pal")
else:
    print("np")

