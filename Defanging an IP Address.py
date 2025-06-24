#1108. Defanging an IP Address
#Problem Link: https://leetcode.com/problems/defanging-an-ip-address/description/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        for i in address:
            if i =='.':
                address =address.replace('.','[.]')  
                break  
        return address
