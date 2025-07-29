class Node:
  def __init__(self,data):
    self.data=data
    self.prev=None
    self.next=None
class DoublyLinkedList:
  def __init__(self):
    self.head=None
  def iab(self, data): 
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode

  def dab(self):
    if not self.head:
     print("cant perform delete operation")
    print(f"deleted: {self.head.data}")
    self.head=self.head.next
    if self.head:
        self.head.prev=None



  def display(self):
    temp=self.head
    print("Doubly Linked List:")
    while temp:
      print(temp.data,end="<->")
      temp=temp.next
    print("None")
dll=DoublyLinkedList()

n=int(input("Enter the number of elements to insert at position:"))
for i in range(n):
  val=int(input(f"Enter element {i+1}:"))
  dll.iab(val)
dll.display()
d=int(input("\n enter how many times you want to perform delete op:"))
for _ in range(d):
  dll.dab()
  dll.display()
