class Solution:
    def lowerBound(self,nums,target):
        n= len(nums)

        l=0
        r=n-1
        ans=n

        while l<=r:
            mid=(l+r)//2
            if nums[mid]>=target:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans

    def upperBound(self,nums,target):
        n=len(nums)

        l=0
        r=n-1
        ans=n
        
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>target:
                ans = mid
                r=mid-1
            else:
                l=mid+1
        return ans
        

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lowerBound(nums,target)
        ub = self.upperBound(nums,target)
        set1= set(nums)
        if target in set1:
            if lb != ub-1:
                return [lb,ub-1]
            elif lb == ub-1:
                return [lb,ub-1]
        else:
            return [-1,-1]

