class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def iab(self, data):  # Insert At Beginning
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode

    def display(self):
        temp = self.head
        print("Doubly Linked List:")
        while temp:
            print(temp.data, end="<->")
            temp = temp.next
        print("None")

dll = DoublyLinkedList()
n = int(input("Enter the number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    dll.iab(val)
dll.display()
