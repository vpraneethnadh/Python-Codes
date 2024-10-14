from modules import *

while True:

    print("""
    1.SUM OF TWO NUMBERS
    2.DIFFERENCE OF TWO NUMBERS
    3.MULTIPLICATION OF TWO NUMBERS
    4.DIVISION OF TWO NUMBERS
    5.INTEGER DIVISION OF TWO NUMBERS
    6.SUM OF DIGITS OF A NUMBER
    7.REVERSE OF A NUMBER
    8.FACTORIAL OF A NUMBER
    9.EVEN OR ODD NUMBER
    10.EXIT/QUIT
    """)

    m = int(input("ENTER ANY NUMBER OF YOUR CHOICE: "))
    if m == 1:
        a = int(input("ENTER FIRST NUMBER"))
        b = int(input("ENTER SECOND NUMBER"))
        c = add(a, b)
        print(c)

    if m == 2:
        a = int(input("ENTER FIRST NUMBER"))
        b = int(input("ENTER SECOND NUMBER"))
        c = sub(a, b)
        print(c)

    if m == 3:
        a = int(input("ENTER FIRST NUMBER"))
        b = int(input("ENTER SECOND NUMBER"))
        c = mul(a, b)
        print(c)

    if m == 4:
        a = int(input("ENTER FIRST NUMBER"))
        b = int(input("ENTER SECOND NUMBER"))
        c = div(a, b)
        print(c)

    if m == 5:
        a = int(input("ENTER FIRST NUMBER"))
        b = int(input("ENTER SECOND NUMBER"))
        c = idiv(a, b)
        print(c)

    if m == 6:
        n = int(input("ENTER ANY NUMBER: "))
        s = sumofdigits(n)
        print(s)

    if m == 7:
        n = int(input("ENTER ANY NUMBER: "))
        r = reverse(n)
        print(r)

    if m == 8:
        n = int(input("ENTER ANY NUMBER: "))
        f = factorial(n)
        print(f)

    if m == 9:
        n = int(input("ENTER ANY NUMBER: "))
        if evenodd(n) == 0:
            print("IT IS AN EVEN NUMBER")
        else:
            print("IT IS AN ODD NUMBER")

    if m == 10:
        print("DONE! THANKYOU")
        exit(0)
        break
