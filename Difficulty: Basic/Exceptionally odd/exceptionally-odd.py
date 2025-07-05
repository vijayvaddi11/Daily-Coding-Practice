#User function Template for python3

class Solution:
    def getOddOccurrence(self, arr, n):
        # code here 
        count=0
        for i in arr:
            count^=i
        return count