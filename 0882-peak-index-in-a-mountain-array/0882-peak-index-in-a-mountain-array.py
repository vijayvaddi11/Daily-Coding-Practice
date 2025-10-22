class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n= len(arr)
        ans=arr[0]
        index=0
        for i in range(1,n):
            if arr[i] > ans:
                ans = arr[i]
                index=i
        return index
