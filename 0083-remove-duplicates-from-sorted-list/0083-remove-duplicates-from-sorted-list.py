# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        if curr==None or curr.next==None:
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
            
