class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # n=len(numbers)
        # start=0
        # end=n-1

        # while start<end:
        #     add_result = numbers[start]+numbers[end]
        #     if add_result == target:
        #         return [start+1, end+1]
        #     elif add_result > target:
        #         end-=1
        #     elif add_result < target:
        #         start+=1

        n = len(numbers)
        dict1={}
        for i in range(n):
            res=target-numbers[i]
            if res not in dict1:
                dict1[numbers[i]]=i
            else:
                return [dict1[res]+1,i+1]    





