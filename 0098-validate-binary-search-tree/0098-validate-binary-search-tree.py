# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
                    
        def check(root,l,r):
            if(root is None):
                return True
            
            if (not(root.val<r and root.val>l)):
                return False
            
            return (check(root.right,root.val,r) and check(root.left,l,root.val))
        
        return check(root,-2**31-1,2**31+1)