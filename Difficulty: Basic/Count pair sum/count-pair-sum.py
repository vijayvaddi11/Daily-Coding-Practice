#User function Template for python3

class Solution:
    def countPairs(self,arr1, arr2, x):
        #code here.
        target = set(x-j for j in arr2)
        count=0
        for i in arr1:
            if i in target:
                count+=1
        return count        