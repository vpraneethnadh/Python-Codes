class student:

    def __init__(self):

        self.name = input("ENTER THE NAME OF THE STUDENT: ")
        self.m1 = int(input("ENTER THE FIRST MARKS: "))
        self.m2 = int(input("ENTER THE SECOND MARKS: "))
        self.m3 = int(input("ENTER THE THIRD MARKS: "))

        self.tot = 0
        self.avg = 0
        self.grades = 'a'

    def cal(self):

        self.tot = self.m1 + self.m2 + self.m3

        self.avg = self.tot / 3

        if self.avg >= 90:
            self.grades = 'A'

        elif self.avg >= 80:
            self.grades = 'B'

        elif self.avg >= 70:
            self.grades = 'C'

        elif self.avg >= 60:
            self.grades = 'D'

        elif self.avg >= 50:
            self.grades = 'E'

        else:
            self.grades = 'F'

    def display(self):

        print("STUDENT NAME: ", self.name)
        print("MARKS OBTAINED: ", self.tot)
        print("AVERAGE: ", self.avg)
        print("GRADE: ", self.grades)


s1 = student()
s1.cal()
s1.display()
