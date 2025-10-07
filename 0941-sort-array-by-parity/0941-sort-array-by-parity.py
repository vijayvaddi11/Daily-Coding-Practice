class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[start],nums[i]=nums[i],nums[start]
                start+=1

        return nums



'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        
        if n<=1:
            return nums

        start =0
        for i in range(1,n):
            if nums[start]%2==0:
                start+=1
            else:
                if nums[i]%2==0:
                    nums[start],nums[i]=nums[i] ,nums[start]
                    start+=1
        return nums
        
'''        