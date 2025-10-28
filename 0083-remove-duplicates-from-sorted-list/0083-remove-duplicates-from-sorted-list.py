# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head

        curr =head
        while curr!=None and curr.next!=None:
            #dublicate
            if curr.val == curr.next.val:
                curr.next=curr.next.next
            #not a dublicate
            else:
                curr=curr.next
        return head
            
