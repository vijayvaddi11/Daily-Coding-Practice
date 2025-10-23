class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        l=0
        r=n-2

        ans=0

        while l<=r:
            mid=(l+r)//2
            if arr[mid]< arr[mid+1]:
                l=mid+1
            else:
                ans=mid
                r=mid-1
        return ans