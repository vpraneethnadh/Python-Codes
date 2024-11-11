class electricity:

    def __init__(self):

        self.mtno=int(input("ENTER THE METER NUMBER: "))
        self.name=input("ENTER THE OWNER NAME: ")
        self.old_units=int(input("ENTER THE OLD UNITS: "))
        self.new_units=int(input("ENTER THE NEW UNITS: "))

        self.units=0
        self.bill=0

    def cal(self):

        self.units = self.new_units - self.old_units

        if self.units <= 100:
            self.bill=units * 1

        elif self.units <= 200:
            self.bill=100 + (self.units - 100) * 2

        elif self.units <= 300:
            self.bill=100 + 200 + (self.units - 300) * 3

        elif self.units <= 400:
            self.bill=100 + 200 + 300 + (self.units - 400) * 4

        elif self.units <= 500:
            self.bill=100 + 200 + 300 + 400 + (self.units - 500) * 5

        else:
            self.bill = 100 + 200 + 300 + 400 + 500 + (self.units - 600) * 6

    def display(self):

        print("OWNER NAME: ",self.name)
        print("METER NUMBER: ",self.mtno)
        print("OLD UNITS: ",self.old_units)
        print("NEW UNITS: ",self.new_units)
        print("UNITS: ",self.units)
        print("BILL: ",self.bill)

e1 = electricity()

e1.cal()
e1.display()
