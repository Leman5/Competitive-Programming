# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum1 = 0
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        global ans
        ans = 0
        global depth
        depth = 0
        
        def solve(node,curr):
            if node.left==None and node.right==None:
                global ans
                global depth
                if curr==depth: #if current depth equals our stored depth
                    ans+=node.val # that means we have some leaves added, so add again
                if curr>depth: # if current depth > stored depth, so there are deeper leaves present
                    ans = node.val #so update the ans with the new value of this new deeper leave
                    depth = curr #update the stored depth as it has increased now
                return
            else:
                if node.left:
                    solve(node.left,curr+1) 
                if node.right:
                    solve(node.right,curr+1) 
        
        solve(root,0)
        return ans