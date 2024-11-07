class parent:
    def display(self):
        print("Parent Class...")

class child(parent):
    def display(self):
        print("Sub Class...")

c=child()
c.display()