class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # Always push to stack1
        self.stack1.append(x)

    def pop(self) -> int:
        # Move elements to stack2 if it's empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Pop from stack2 (front of queue)
        return self.stack2.pop()

    def peek(self) -> int:
        # Move elements if needed
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Return front element (top of stack2)
        return self.stack2[-1]

    def empty(self) -> bool:
        # Queue is empty only if both stacks are empty
        return not self.stack1 and not self.stack2



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()