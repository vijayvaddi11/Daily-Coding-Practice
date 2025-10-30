# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow = head
        # fast = head

        # while fast != None and fast.next != None:
        #     slow = slow.next
        #     fast = fast.next.next
        
        # return slow
        
        curr=head
        l=1
        while curr.next!=None:
            curr=curr.next
            l+=1
        
        n=l//2
        if n%2==0:
            l+=1
        
        st=head
        for i in range(n):
            st=st.next
        
        return st