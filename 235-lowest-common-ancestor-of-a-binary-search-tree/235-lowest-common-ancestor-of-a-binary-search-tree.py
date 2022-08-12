# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def traverse(root,p,q):
            if(not root):
                return
            # if(p==root.val or q==root.val):
            #     return root 
            if(p<root.val and q<root.val):
                return traverse(root.left,p,q)
            if(p>root.val and q>root.val):
                return traverse(root.right,p,q)
            return root
            
        return traverse(root,p.val,q.val)