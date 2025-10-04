class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_n=1
        sum_n=0
        for i in str(n):
            product_n*=int(i)
            sum_n+=int(i)
        return product_n-sum_n    
