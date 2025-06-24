#2011. Final Value of Variable After Performing Operations
#problem link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X=0
        for i in operations:
            if i=='X++' or i=='++X':
                X+=1
            else:
                X-=1
        return X 
