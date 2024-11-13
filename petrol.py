print("""WELCOME TO OUR PETROL BUNK"
      PETROL COSTS: Rs.123.46
      DIESEL costs: Rs.120.98
      
      CHOOSE 1 FOR PETROL 
      CHOOSE 2 FOR DIESEL""")

choice = int(input("ENTER 1/2 OF YOUR CHOICE: "))

while True:
    if choice == 1:
        print("""YOU HAVE CHOSEN PETROL
                CHOOSE 1 FOR FULL TANK
                CHOOSE 2 FOR PETROL AS PER MONEY
                CHOOSE 3 FOR PETROL AS PER LITRES""")

        choice2 = int(input("ENTER 1/2/3 OF YOUR CHOICE: "))
        while True:
            if choice2 == 1:
                n = int(input("ENTER THE TOTAL NUMBER OF LITERS SUFFICIENT TO YOUR VEHICLE: "))
                bill = n * 123.46
                print("YOUR TOTAL BILL IS: ", bill)
                print("THANKYOU!,VISIT AGAIN")

                break
            if choice2 == 2:
                amount = float(input("ENTER THE MONEY: "))
                x = (amount * 1000) // 123.46
                print("TOTAL NUMBER OF LITRES: ", x / 1000)
                print("THANKYOU!,VISIT AGAIN")

                break
            if choice2 == 3:
                litre = int(input("ENTER HOW MANY LITRES DO YOU WANT: "))
                x = (123.46 * (litre * 1000)) // 1000
                print("TOTAL COST: ", x)
                print("THANKYOU!,VISIT AGAIN")

                break

        break

    else:
        print("""YOU HAVE CHOSEN DIESEL
                        CHOOSE 1 FOR FULL TANK
                        CHOOSE 2 FOR DIESEL AS PER MONEY
                        CHOOSE 3 FOR DIESEL AS PER LITRES""")

        choice3 = int(input("ENTER 1/2/3 OF YOUR CHOICE: "))
        while True:
            if choice3 == 1:
                d = int(input("ENTER THE TOTAL NUMBER OF LITERS SUFFICIENT TO YOUR VEHICLE: "))
                bill = d * 120.98
                print("YOUR TOTAL BILL: ", bill)
                print("THANKYOU!,VISIT AGAIN")

                break
            if choice3 == 2:
                amount = float(input("ENTER tHE MONEY: "))
                x = (amount * 1000) // 110.98
                print("TOTAL NUMBER OF LITRES: ", x / 1000)
                print("THANKYOU!,VISIT AGAIN")

                break
            if choice3 == 3:
                litre = int(input("ENTER HOW MANY LITRES DO YOU WANT: "))
                x = (120.98 * (litre * 1000)) // 1000
                print("TOTAL COST: ", x)
                print("THANKYOU!,VISIT AGAIN")

                break

        break
