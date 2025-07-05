# Function should return an integer value
class Solution:
    def convertFive(self, n):
        # Code here
        str_n=str(n)
        output=''
        for i in str_n:
            if i=='0':
                output+='5'
            else:
                output+=i
        return output    