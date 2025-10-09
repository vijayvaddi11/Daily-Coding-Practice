class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n= len(nums)
        dict1={}

        for i in range(n):
            require_num = target - nums[i]
            if require_num not in dict1:
                dict1[nums[i]]=i
            else:
                return [dict1[require_num],i]