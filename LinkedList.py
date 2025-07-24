#SingleLinkedList
class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class LinkedList:
  def __init__(self):
    self.head=None
  def iab(self,data):
    newnode=Node(data)
    newnode.next=self.head
    self.head=newnode
    print(f"{data} inserted from begin.")
  def display(self):
    current=self.head
    if not current:
      print("LL-Empty")
      return
    while current:
      print(current.data,end='---')
      current=current.next
    print("none")



ll=LinkedList()
while True:
  print("\n LinkedList- Insert At Begin....")
  print("1.insert")
  print("2.display")
  print("3.exit")
  choice=input("enter your choice:")
  if choice=='1':
    data=int(input("enter your choice:"))
    ll.iab(data)
  elif choice=='2':
      ll.display()
  elif choice=='3':
      print("exit the operation....")
      break
  else:
      print("enter only ...1/2/3")
