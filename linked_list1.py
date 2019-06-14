class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=Node()
    def appendAtEnd(self,element):
        newnode=Node(element)
        current=self.head
        while current.next!=None:
            current=current.next
        current.next=newnode
    def getSize(self):
        current=self.head
        length=0
        while current.next!=None:
            length+=1
            current=current.next
        return length
    def printList(self):
        current=self.head
        while current.next!=None:
            current=current.next
            print(current.data,end=" ")
        print("\n")
    def appendAtBeginning(self,element):
        newnode=Node(element)
        current=self.head.next
        self.head.next=newnode
        newnode.next=current 
    def deleteFirstNode(self):
        self.deleteNodeAtIndex(0)
    def deleteLastNode(self):
        self.deleteNodeAtIndex(self.getSize()-1)
    def deleteNodeAtIndex(self,index):
        current=self.head
        if(index>self.getSize()):
            print("Out Of Bounds")
            exit(1)
        i=0
        while i<=index:
            if(i==index):
                current.next=current.next.next
            current=current.next
            i+=1
        pass
    def getAtIndex(self,index):
        i=0
        current=self.head.next
        while i<=index:
            if(i==index):
                return current.data
            current=current.next
            i+=1
    def updateAtIndex(self,index,element):
        if(index>self.getSize()):
            print("Out Of Bounds")
            exit(1)
        i=0
        current=self.head
        while i<=index:
            current=current.next
            i+=1
        print(current.data)
        current.data=element
    def createCycle(self):
        index=1
        i=0
        current=self.head
        while current.next!=None:
            current=current.next
        elementcycle=self.head
        while i<=index:
            elementcycle=elementcycle.next
            i+=1
        current.next=elementcycle   
    
    #Hare and the tortoise approach.

    def checkCycleAndPrintHeadIfExists(self):
        hare=self.head
        tortoise=self.head
        iscycle=False
        while(hare.next!=None):
            if(hare.data==tortoise.data and hare.data!=None and tortoise.data!=None):
                iscycle=True
                break
            hare=hare.next.next
            print("Hare",hare.data)
            tortoise=tortoise.next
            print("Tortoise",tortoise.data)
        if(iscycle==False):
            return iscycle
        distance=0
        tortoise=tortoise.next
        while(tortoise.next!=hare.next):
            tortoise=tortoise.next
            distance+=1
        print("Length of cycle is ",distance)
        p1=self.head
        p2=self.head
        start=0
        while start<=distance:
            start+=1
            p2=p2.next
        print(p2.data)
        while(p1.next!=p2.next):
            p1=p1.next
            p2=p2.next
        print(p1.next.data)
        return iscycle
ll=LinkedList()
print(ll)
ll.appendAtEnd(5)
ll.appendAtEnd(7)
ll.getSize()
ll.printList()
ll.appendAtBeginning(3)
ll.appendAtBeginning(300)
ll.getSize()
ll.printList()
ll.deleteLastNode() 
ll.printList()
print(ll.getAtIndex(0))
ll.updateAtIndex(2,100)
ll.appendAtEnd(71)
ll.appendAtEnd(73)
ll.appendAtEnd(37)
ll.appendAtEnd(17)
ll.appendAtEnd(72)
ll.appendAtEnd(27)
ll.appendAtEnd(117)
ll.printList()
# print(ll.checkCycle())
ll.createCycle()
# ll.printList()
print(ll.checkCycleAndPrintHeadIfExists())





