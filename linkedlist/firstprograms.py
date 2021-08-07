class Node:
    def __init__(self, data,next):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):     #__init__ cl level built in method
        self.head =None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    def isempty(self):     # isempty is our own defined method. so we will not use __isempty__
        # return self.size == 0
        return self.head == None

    def addlast(self,data):
        newest = Node(data,None)  #node is calling here .when we pass the data in node it will store in newest variable
        if self.isempty():
            self.head = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self.size += 1
        
    def addfirst(self,data):
        # newest = Node(data,None)
        # newest.next=self.head
        # self.head=newest
        if self.isempty():
            self.head=newest
            self.tail=newest
        else:
            newest.next=self.head
            self.head=newest
        self.size +=1
            
    
    def  search(self,key):
        p=self.head
        index=0
        while p:
            if p.data==key:
                return index
            p=p.next
            index += 1
        return -1
        
    def display(self):
        p = self.head
        while p:
            print(p.data,end = '-->')
            p=p.next
        print()
L = LinkedList()
L.addlast(7)
L.addlast(4)
L.addlast(12)
L.addlast(8)
L.addlast(3)


L.display()
print('size:',len(L))
i=L.search(8)
print('Result:',i)
L.addfirst(15)

L.display()
print('size:',len(L))
L.addfirst(25)

L.display()
print('size:',len(L))

L.addlast(35)


L.display()
print('size:',len(L))
L.addfirst(2)

L.display()
print('size:',len(L))
        
    
    