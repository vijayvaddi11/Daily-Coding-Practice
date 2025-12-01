class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_n = len(nums)
        dict1={}

        for i in range(len_n):
            required_num = target-nums[i]
            if required_num not in dict1:
                dict1[nums[i]]=i
            else:
                return [dict1[required_num],i]


