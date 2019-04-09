
# made the class which defines the node 

class Node:
    #i inialized the class 
    def __int__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __int__(self):
        self.root = None
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    
    def setData(self, newdata):
        self.data  = newdata
        
    def setData(self, newnext):
        self.next  = newnext
        #im checking to see if my stack is empty or not
    def isEmpty(self):
        return self.head  == None
    
    def push(self, data):
        newnode = self.Node(data)
        newnode.next = self.root
        self.root = newnode
        
    def pop(self):
        if (self.isEmpty()):
            return "-1"
        temp = self.root =self.root.next
        popped = temp.data
        return pooped
    

    
stack = Stack()
stack.push(10)
    
    
   
# creates the class