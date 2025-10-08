class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        words.reverse()
        return " ".join(words)





#manual it can be further optimised
#class Solution:
#    def reverseWords(self, s: str) -> str:
        # c=[]
        # d=''
        # for i in s.strip():
        #     if i==" ":
        #         if d:
        #             c.append(d)
        #             d=''
        #     else:
        #         d+=i
        # if d:
        #     c.append(d)

        # result=''   
        # for i in range(len(c)-1,-1,-1):
        #     result+=c[i]
        #     if i!=0:
        #         result+=" "
        # return result        