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
    if isPal:
        print("Palindrome")
    else:
        print("Not a Palindrome")

n = "malayalam"
palindrome(n)

n1 = "abcd"
palindrome(n1)