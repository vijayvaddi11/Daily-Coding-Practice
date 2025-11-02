# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a=headA
        b=headB

        l1=0
        while a:
            l1+=1
            a=a.next
        
        l2=0
        while b:
            l2+=1
            b=b.next

        #trim a and b to equal 
        a=headA
        b=headB
        if l1>l2:
            for _ in range(l1-l2):
                a=a.next
        else:
            for _ in range(l2-l1):
                b=b.next
        
        while a and b:
            if a==b:
                return a
            a=a.next
            b=b.next
        return None
