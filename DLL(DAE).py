class Node:
  def __init__(self,data):
    self.data=data
    self.prev=None
    self.next=None
class DoublyLinkedList:
  def __init__(self):
    self.head=None
  def iae(self, data):
        newnode = Node(data)
        if self.head is None: 
          self.head=newnode
          return
        temp=self.head
        while temp.next:
          temp=temp.next
        temp.next=newnode
        newnode.prev=temp

  def dae(self):
    if self.head is None:
      print("cant perform delete in an empty list....")
      return
    temp=self.head
    while temp.next:
      temp=temp.next
    print(f"deleted: {temp.data}")
    if temp.prev:
      temp.prev.next=None
    else:
      self.head=None


  def display(self):
    temp=self.head
    print("Doubly Linked List:")
    while temp:
      print(temp.data,end="<->")
      temp=temp.next
    print("None")
dll=DoublyLinkedList()

n=int(input("Enter the number of elements to insert at end:"))
for i in range(n):
  val=int(input(f"Enter element {i+1}:"))
  dll.iae(val) 
dll.display()
d=int(input("\n enter how many times you want to perform delete op:"))
for _ in range(d):
  dll.dae()
  dll.display()