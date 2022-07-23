# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = right = None
        rs = right
        ls = left
        while(head != None):
            if(head.val>=x):
                if(right):
                    right.next = ListNode(head.val)
                    right = right.next
                else:
                    right = ListNode(head.val)
                    rs = right
            else:
                if(left):
                    left.next = ListNode(head.val)
                    left = left.next
                else:
                    left = ListNode(head.val)
                    ls = left
            head = head.next
        if(left):
            left.next = rs
            return ls
        else:
            return rs
            
                