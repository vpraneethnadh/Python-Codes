n = int(input("Enter any Number: "))

print("Digit\tFrequency")

for i in range(0, 10):
    c = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        if digit == i:
            c = c + 1
        temp = temp // 10
    if c > 0:
        print(i, "\t", c)
