class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        last_previous=self.fib(n-1)    
        previous=self.fib(n-2)
        return last_previous+previous
    