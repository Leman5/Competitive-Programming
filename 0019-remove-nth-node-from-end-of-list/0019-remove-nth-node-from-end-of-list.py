# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        temp = head
        for i in range(n):
            temp = temp.next
        start = dummy
        while temp:
            start = start.next
            temp = temp.next
        # if(start):
        start.next = start.next.next
        # else:
        #     return None
        return dummy.next