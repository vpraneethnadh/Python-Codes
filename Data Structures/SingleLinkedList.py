class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def insertatbeg(self,n):
        temp = node(n)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            temp.next = self.head
            self.head = temp
        self.len += 1
    
    def insertatend(self,n):
        temp = node(n)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            while self.tail.next != None:
                self.tail = self.tail.next
            self.tail.next = temp
        self.len += 1

    def insertatpos(self,n,pos):
        if pos <= 0 or pos > self.len:
            print("Invalid Position value")
            return
        if pos == 1:
            self.insertatbeg(n)
        else:
            temp = node(n)
            self.tail = self.head
            while pos - 1 > 0:
                self.tail = self.tail.next
                pos -= 1
            temp.next = self.tail.next
            self.tail.next = temp
        self.len += 1

    def deleteatbeg(self):
        if self.head == None:
            print("List is empty")
            return
        else:
            self.head = self.head.next
        self.len -= 1

    def deleteatend(self):
        if self.head == None:
            print("List is empty")
            return
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
        self.len -= 1

    def deleteatpos(self,pos):
        if pos <= 0 or pos > self.len:
            print("Invalid Position value")
            return
        else:
            if pos == 1:
                self.deleteatbeg()
            else:
                temp = self.head
                while pos - 1 > 0:
                    temp = temp.next
                    pos -= 1
                temp.next = temp.next.next
        self.len -= 1

    def printNode(self):
        if self.head == None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    
if __name__ == "__main__":
    s1 = SingleLinkedList()
    s1.insertatbeg(10)
    s1.insertatbeg(20)
    s1.insertatbeg(30)
    s1.printNode()

    s1.insertatend(40)
    s1.insertatend(50)
    s1.insertatend(60)
    s1.printNode()

    s1.insertatpos(5,3)
    s1.printNode()

    s1.deleteatbeg()
    s1.printNode()

    s1.deleteatend()
    s1.printNode()

    s1.deleteatpos(2)
    s1.printNode()