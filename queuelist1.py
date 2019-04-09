
# made the class which defines the node 

class Node:
    #i inialized the class 
    def __int__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    # i defined he inaltizser, set it to itself and created an empty list
    def __int__(self):
        self.items =[]
        
      #im checking to see if my list is empty ,   
    def isEmpty(self):
        return self.items ==[]
    
    #adding something to my queue
    def enqueue(self, item):
        self.items.insert(0, item)
   
    def dequeue(self):
        self.items.pop()
        
        #im checking to see if my stack is empty or not
    def size(self):
        return len(self.items)
    
    def printqueue(self):
        for items in self.items:
            print(items)

    
q = Queue()
print(q.isEmpty())
q.enqueue(1)    
q.enqueue(10) 
   
# creates the class







