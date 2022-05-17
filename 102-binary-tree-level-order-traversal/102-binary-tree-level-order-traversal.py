# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        visited = []
        queue = []
        if(not root):
            return queue
        queue.append(root)
        while(queue):
            ans = []
            l = len(queue)
            for i in range(l):
                ans.append(queue[0].val)
                u = queue[0]
                if(u.left):
                    queue.append(u.left)
                if(u.right):
                    queue.append(u.right)
                queue.pop(0)
            visited.append(ans)
        return visited
        
        