# parent = (i-1)//2
# left_child = 2*i+1
# right_chilld = 2*i+2


class MinHeap:
    def __init__(self):
        self.h=[]
    def push(self,x):
        self.h.append(x)
        self._up(len(h)-1)
    def _up(self,i):
        while i>0 and self.h[(i-1)//2]>self.h[i]:
            parent=(i-1)//2
            self.h(parent),self.h[i]=self.h[i],self.h[parent]
            i=parent
    def pop(self):
        if len(self.h) ==0:
            return None
        self.h[0],self.h[-1]=self.h[-1],self.h[0]
        val=self.h.pop()
        self._down(0)
        return val
    def _down(self,i):
        size=len(self.h)
        while True:
            left = 2*i+1
            right = 2*i+2
            smallest=i
            if left<size and self.h[left]<self.h[smallest]:
                smallest=left
            if right<size and self.h[right]<self.h[smallest]:
                smallest=right
            
            if smallest==i:
                break
            self.h[i],self.h[smallest]=self.h[smallest],self.h[i]
            i=smallest
