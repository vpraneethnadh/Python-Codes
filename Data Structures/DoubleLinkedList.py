class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def insertatbeg(self,n):
        temp = Node(n)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            temp.next = self.head
            self.head = temp
            temp = self.head
        self.len += 1

    def insertatend(self,n):
        temp = Node(n)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            while self.tail.next != None:
                self.tail = self.tail.next
            temp.prev = self.tail
            self.tail.next = temp
        self.len += 1

    def insertatpos(self,n,pos):
        if pos <= 0 or pos > self.len:
            print("Invalid Position")
            return
        else:
            temp = Node(n)
            if pos == 1:
                self.insertatbeg(n)
            else:
                self.tail = self.head
                while pos - 1 > 0:
                    self.tail = self.tail.next
                    pos -= 1
                temp.prev = self.tail
                temp.next = self.tail.next
                self.tail.next.prev = temp
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
            print("Invalid Position")
            return
        else:
            if pos == 1:
                self.deleteatbeg()
            else:
                self.tail = self.head
                while pos - 1 > 0:
                    self.tail = self.tail.next
                    pos -= 1
                self.tail.next = self.tail.next.next
                self.tail.next.prev = self.tail
        self.len -= 1

    def printNode(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

    def reverse(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            while temp != None:
                print(temp.data, end=" -> ")
                temp = temp.prev
            print("None")


if __name__ == "__main__":
    d1 = DoubleLinkedList()
    d1.insertatbeg(10)
    d1.insertatbeg(20)
    d1.insertatbeg(30)
    d1.printNode()

    d1.insertatend(40)
    d1.insertatend(50)
    d1.insertatend(60)
    d1.printNode()

    d1.insertatpos(45,4)
    d1.printNode()

    d1.deleteatbeg()
    d1.printNode()

    d1.deleteatend()
    d1.printNode()

    d1.deleteatpos(3)
    d1.printNode()

    d1.reverse()