class Node :

    def __init__(self ,  data):
        self.data= data
        self.next=None

    
class NewNode :
    first = Node(-1)
    def start (data):
        newnode = Node(data)
        if (NewNode.first.next==None):
 
            NewNode.first.next = newnode

                
        else:
            current = NewNode.first
            while(current.next!=None):

                current=current.next
            current.next=newnode    
        
    def display():
        current= NewNode.first
        while(current.next!=None):
            current= current.next
            print(current.data)


            
class main:
    
    NewNode.start(1)    
    NewNode.start(2)
    NewNode.start(3)
    NewNode.start(4)
    NewNode.display()
