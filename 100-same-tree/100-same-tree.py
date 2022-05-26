# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(p == q and p ==None):
            return True
        elif(not p or not q ):
            return False
        if(p.val != q.val):
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)