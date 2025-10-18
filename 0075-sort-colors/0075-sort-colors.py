class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=0
        left=0
        right=n-1

        while i<=right:
            if nums[i]==1:
                i+=1
            elif nums[i]==0:
                nums[left],nums[i]=nums[i],nums[left]
                i+=1
                left+=1
            else:
                nums[i],nums[right]=nums[right],nums[i]
                right-=1

        return nums        