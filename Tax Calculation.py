n = int(input("Enter the salary of the person(0-10,00,000): "))

if n <= 250000:
    tax = 37500 + (15/100)*(n-100000)
elif n <= 500000:
    tax = 12500 + (10/100)*(n-300000)
elif n <= 750000:
    tax = (5/100)*(n)
elif n <= 1000000:
    tax = 0

print(tax)