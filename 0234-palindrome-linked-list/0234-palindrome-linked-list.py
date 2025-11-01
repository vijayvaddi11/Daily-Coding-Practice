# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
        
        #reverse second LL
        prev=None
        curr=slow
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        #compare both fast and slow
        first=head
        second=prev
        while second:
            if first.val != second.val:
                return False
            first=first.next
            second=second.next
        return True



        
        