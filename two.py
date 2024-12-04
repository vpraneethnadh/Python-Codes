class train:

    def __init__(self):

        self.pasname = input("ENTER THE PASSENGER NAME: ")
        self.pasage = int(input("ENTER THE AGE OF THE PASSENGER: "))
        self.km = int(input("ENTER THE KM PASSENGER IS TRAVELLING: "))

        self.final_fare = 0
        self.discount = 0
        self.fare = 0

    def cal(self):

        if self.km <= 100:
            self.fare = 100

        elif self.km <= 200:
            self.fare = 100 + (self.km - 200) * 2

        elif self.km <= 300:
            self.fare = 100 + 200 + (self.km - 300) * 3

        elif self.km <= 400:
            self.fare = 100 + 200 + 300 + (self.km - 400) * 4

        elif self.km <= 500:
            self.fare = 100 + 200 + 300 + 400 + (self.km - 500) * 5

        else:
            self.fare = 100 + 200 + 300 + 400 + 500 + (self.km - 600) * 6



        if self.pasage <= 10:
            self.discount = (50 * self.fare) / 100

        elif self.pasage >= 50:
            self.discount = (25 * self.fare) / 100

        else:
            self.discount = 0


        self.final_fare = self.fare - self.discount

    def display(self):

        print("PASSENGER NAME: ", self.pasname)
        print("PASSENGER AGE: ", self.pasage)
        print("KILOMETERS TRAVELLING: ", self.km)
        print("DISCOUNT OBTAINED: ", self.discount)
        print("FARE WITHOUT DISCOUNT: ", self.fare)
        print("FINAL TICKET FARE: ", self.final_fare)


t1 = train()

t1.cal()
t1.display()
