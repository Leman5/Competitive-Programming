# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if(root==None):
            return
        def traverse(root):
            if(not root):
                return None
            
            leftT = traverse(root.left)
            rightT = traverse(root.right)
            if(leftT):
                leftT.right = root.right
                root.right = root.left
                root.left = None
            last = rightT or leftT or root
            return last
        traverse(root)
        