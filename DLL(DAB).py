class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def iae(self, data): 
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode
        newnode.prev = temp
        print(f"{data} inserted at the end.")


    def dab(self):
        if self.head is None:
            print("Cannot perform delete operation on an empty list.")
            return
        print(f"Deleted: {self.head.data}")
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def display(self):
        temp = self.head
        print("Doubly Linked List:")
        while temp:
            print(temp.data, end="<->")
            temp = temp.next
        print("None")

dll = DoublyLinkedList()

n = int(input("Enter the number of elements to insert at the end: "))
print("--- Inserting at End ---")
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    dll.iae(val)
dll.display()

d = int(input("\n enter how many times you want to perform delete at beginning op: "))
print("--- Deleting from Beginning ---")
for _ in range(d):
  dll.dab()
  dll.display()