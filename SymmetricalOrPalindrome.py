def palindrome(str):
    i = 0
    j = len(str) - 1
    isPal = True
    while i < j:
        if str[i] != str[j]:
            isPal = False
            break
        i += 1
        j -= 1
    return isPal

def symmetrical(str):
    leng = len(str)
    mid = leng // 2
    str1 = ""
    str2 = ""
    for i in range(mid):
        str1 += str[i]
    for i in range(mid - 1, leng):
        str2 += str[i]
    return str1 == str2

def symorPal(str):
    if palindrome(str) == True:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")    
    if symmetrical(str) == True:
        print("It is Symmetrical")
    else:
        print("It is not Symmetrical")

n1 = "knoko"
n2 = "amaama"

symorPal(n1)
symorPal(n2)
    