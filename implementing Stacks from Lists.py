#list implimentation of stack
class Stack:
    def __init__(self):
        self.st=[]
        self.length=0
    def push(self,x):
        self.length+=1
        self.st.append(x)
    def pop(self):
        if len(self.st)==0:
            return -1
        self.length-=1
        x=self.st[-1]
        self.st.pop()
        return x
    def top(self):
        if len(self.st)==0:
            return -1
        x=self.st[-1]
        return x
    def size(self):
        return self.length

stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.size())
print(stack.pop())

print(stack.top())

