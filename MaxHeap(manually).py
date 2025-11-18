class MaxHeap:
    def __init__(self):
        self.h=[]
    def push(self,x):
        self.h.append(x)
        self._up(len(self.h)-1)
    def _up(self,i):
        while i>0 and self.h[(i-1)//2]<self.h[i]:
            parent=(i-1)//2
            self.h[parent],self.h[i]=self.h[i],self.h[parent]
            i=parent
    def pop(self):
        if len(self.h) ==0:
            return None
        self.h[0],self.h[-1]=self.h[-1],self.h[0]
        val=self.h.pop()
        if self.h:
            self._down(0)
        return val
    def _down(self,i):
        size=len(self.h)
        while True:
            left=2*i+1
            right=2*i+2
            large_val=i
            if left<size and self.h[left]>self.h[large_val]:
                large_val=left
            if right<size and self.h[right]>self.h[large_val]:
                large_val=right
            
            if large_val==i:
                break
            self.h[i],self.h[large_val]=self.h[large_val],self.h[i]
            i=large_val
    
