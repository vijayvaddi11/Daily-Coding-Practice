class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False
        
        st=[]
        for i in list(s):
            if i =="[" or i == "{" or i =="(":
                st.append(i)
            else:
                if len(st)==0:
                    return False
                top=st.pop()
                if i ==")" and top!="(":
                    return False
                elif i=="}" and top!="{":
                    return False
                elif i=="]" and top!="[":
                    return False

        if len(st)==0:
            return True
        else:
            return False 


        