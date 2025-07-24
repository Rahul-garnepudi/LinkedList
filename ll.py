
def __init__(s,data):
        s.data=data
        s.next= None
class Linkedlist:
    def __init__(s):
        s.head= None
    def i_a_b(s,data):
        newnode=Node(data)
        if not s.head:
            s.head=newnode
            return
        current=s.head
        while current.next:
            current=current.next
        current.next=newnode
    def deletebegin(s):
        if s.head==None:
            print("empty=ll")
        else:
            print("deleted node from begining:",s.head.data)
            s.head=s.head.next
       
    def display(s):
        current=s.head
        if not current:
            print("linked list is empty")
            return
        while current:
            print(current.data,end="---")
            current=current.next
        print(None)
       
       
l1=Linkedlist()
while True:
    print("\n Linkedlist- Insert at begin...")
    print("1. Insert")
    print("2. Display")
    print("3. delete")
    print("4. Exit")
    choice=input("enter choice")
    if choice=='1':
        data=int(input("inserted value"))
        l1.i_a_b(data)
    elif choice=="2":
        l1.display()
    elif choice=="3":
        l1.deletebegin()
    elif choice=="4":
        print("exit the operation")
        break
    else:
        print("invalid choice")
