# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        first = l1
        second = l2
        result = l3
        sum  = 0
        while(first and second):
            sum += first.val + second.val
            result.val = sum%10
            
            if(first.next or second.next):
                result.next = ListNode()
            elif(sum>9):
                result.next = ListNode(val=1)
            
            if(sum>9):
                sum = 1
            else:
                sum = 0
            first = first.next
            second = second.next
            result = result.next
        while(first):
            sum += first.val
            result.val = sum%10
            
            if(first.next):
                result.next = ListNode()
            elif(sum>9):
                result.next = ListNode(val=1)
            
            if(sum>9):
                sum = 1
            else:
                sum = 0
            first = first.next
            result = result.next
            
            
        while(second):
            sum += second.val
            result.val = sum%10
            
            if(second.next):
                result.next = ListNode()
            elif(sum>9):
                result.next = ListNode(val=1)
            
            if(sum>9):
                sum = 1
            else:
                sum = 0
            second = second.next
            result = result.next
            
            
            
        return l3