class employee:
    def __init__(self, name, num, salary):
        self.name = name
        self.num = num
        self.salary = salary

    def display(self):
        print("EMPLOYEE NAME: ", self.name)
        print("EMPLOYEE NUMBER: ", self.num)
        print("EMPLOYEE SALARY: ", self.salary)


class manager(employee):
    def __init__(self, name, num, salary):
        super().__init__(name, num, salary)
        self.extra = 0
        self.emp_sal = 0

    def calculate(self):
        self.extra = (self.salary * 20) // 100
        self.emp_sal = self.extra + self.salary

    def display(self):
        print("MANAGER SALARY: ", self.emp_sal)


class technical(employee):
    def __init__(self, name, num, salary):
        super().__init__(name, num, salary)
        self.extra = 0
        self.tech_sal = 0

    def calculate(self):
        self.extra = (self.salary * 10) // 100
        self.tech_sal = self.extra + self.salary

    def display(self):
        print("TECHNICAL SALARY: ", self.tech_sal)


e1 = technical("ABC", 1001, 10000)
e1.calculate()
e1.display()

e2 = manager("AAA", 1002, 20000)
e2.calculate()
e2.display()
