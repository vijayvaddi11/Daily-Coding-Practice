class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start=0
        for i in range(1,len(nums)):
            if nums[start]%2!=0 and nums[i]%2==0:
                nums[start],nums[i]=nums[i],nums[start]
                start+=1
            elif nums[start]%2==0:
                start+=1
        return nums