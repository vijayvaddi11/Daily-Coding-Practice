#Linked-List implimentation of stack
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        self.length=0
    def push(self,x):
        newNode=Node(x)
        self.length+=1
        if self.top is None:
            self.top=newNode
        else:
            newNode.next=self.top
            self.top=newNode
    def pop(self):
        if self.length==0:
            return -1
        else:
            x=self.top.data
            self.length-=1
            self.top=self.top.next
            return x
    def getTop(self):
        if self.top is None:
            return -1
        else:
            x=self.top.data
            return x
    def size(self):
        return self.length
        
            
stack=Stack()
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(9)


print(stack.size())
print(stack.pop())
print(stack.getTop())
