#User function Template for python3

class Solution:
    def printGfg(self, n):
        # Code here
        #using reccursion
        if n==0:
            return
        print(n,end=' ')
        self.printGfg(n-1)
