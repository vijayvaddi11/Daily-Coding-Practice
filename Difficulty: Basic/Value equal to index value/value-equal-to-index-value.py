#User function Template for python3
class Solution:
    # Function to find values in array equal to their indices
    def valueEqualToIndex(self, arr):
        li=[]
        for i in range(len(arr)):
            index=i+1
            if index==arr[i]:
                li.append(index)
        return li        