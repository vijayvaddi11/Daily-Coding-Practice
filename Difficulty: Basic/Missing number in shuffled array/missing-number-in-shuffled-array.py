#User function Template for python3


class Solution:
    def findMissing(self, arr1,arr2):
        # code here
        missing=0
        for num in arr1+arr2:
            missing^=num
        return missing    