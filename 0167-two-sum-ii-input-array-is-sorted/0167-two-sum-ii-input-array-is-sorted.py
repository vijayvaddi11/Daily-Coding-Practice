class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        start=0
        end=n-1

        while start<end:
            add_result = numbers[start]+numbers[end]
            if add_result == target:
                return [start+1, end+1]
            elif add_result > target:
                end-=1
            elif add_result < target:
                start+=1
