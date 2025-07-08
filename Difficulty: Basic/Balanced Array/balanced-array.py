#User function Template for python3


class Solution:
    # Function to find the minimum value required to balance the array.
    def min_value_to_balance(self, arr):
        # code here
        len_arr=len(arr)
        half_val=len_arr//2
        ar1=[]
        ar2=[]
        for i in range(len(arr)):
            if i<half_val:
                ar1.append(arr[i])
            else:
                ar2.append(arr[i])
        return abs(sum(ar1)-sum(ar2))
            