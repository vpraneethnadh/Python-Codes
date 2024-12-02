class result:

    def __init__(self):
        self.name = input("ENTER THE NAME OF THE STUDENT: ")
        self.correct = int(input("ENTER THE NUMBER OF CORRECT ANSWERS: "))

        self.percentage = 0

        self.total = 10

    def cal(self):
        self.percentage = (self.correct / self.total) * 100

    def display(self):
        print("STUDENT NAME: ", self.name)
        print("TOTAL NUMBER OF QUESTIONS: ", self.total)
        print("TOTAL NUMBER OF CORRECT ANSWERS: ", self.correct)
        print("RESULT IN PERCENTAGE: ", self.percentage, "%")


r1 = result()

r1.cal()
r1.display()
