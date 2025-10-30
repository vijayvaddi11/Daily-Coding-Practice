# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # p1=head
        # p2=head

        # for i in range(n):
        #     p1=p1.next
        
        # if p1==None:
        #     head=head.next
        #     return head

        # while p1.next!=None:
        #     p1=p1.next
        #     p2=p2.next
        # p2.next=p2.next.next
        # return head


        l=1
        curr=head
        while curr.next!=None:
            curr=curr.next
            l+=1
            
        # if only one node and we remove it
        if l == 1 and n == 1:
            return None

        # if we need to remove the first node
        if n == l:
            return head.next
        
        start=head
        for i in range(l-n-1):
            start=start.next
        start.next=start.next.next
        return head


