class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums

        # Tc-O(n)
        # Sc-O(1) no extra list created

        