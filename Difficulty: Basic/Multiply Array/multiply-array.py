#User function Template for python3

class Solution:
    def longest(self, arr, n):
        #Code Here
        count=1
        for i in range(n):
             count*=arr[i]
        return count     
            
    
    
