# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d = dict()
        while(headA):
            d[headA] = 'Visited'
            headA = headA.next
        while(headB):
            if(headB in d.keys()):
                return headB
            headB = headB.next
        return None
        