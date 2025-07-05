#User function Template for python3

class Solution:

    def solve(self, a):
        # code here
        st=''
        vowels=['a','e','i','o','u']
        for i in a:
            if i not in vowels:
                if i not in st:
                    st+=i
        len_st=len(st)        
        if len_st%2!=0:
            return 'HE!'
        else:
            return 'SHE!'