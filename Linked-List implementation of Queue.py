#Linked-List implementation of Queue

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.length=0
    
    def push(self,x):
        newNode=Node(x)
        self.length+=1
        if self.front is None:
            self.front=newNode
            self.rear=newNode
        else:
            self.rear.next=newNode
            self.rear=newNode
    
    def pop(self):
        if self.front is None:
            return -1
        self.length-=1
        x=self.front.data
        self.front=self.front.next
        return x
        
    def getFront(self):
        if self.front is None:
            return -1
        return self.front.data
        
    def size(self):
        return self.length
        
