class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        dublicate_nums = nums.copy()
        nums.extend(dublicate_nums)
        return nums


