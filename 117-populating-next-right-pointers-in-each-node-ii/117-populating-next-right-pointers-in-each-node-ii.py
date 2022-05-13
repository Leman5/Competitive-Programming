"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque()
        level = []
        level.append(root)
        q.append(level)
        
        while len(q)!=0:
            nodes = q.popleft()
            level = []
            for i in range(len(nodes)):
                if nodes[i]:
                    if nodes[i].left: level.append(nodes[i].left)
                    if nodes[i].right: level.append(nodes[i].right)
                if i+1 < len(nodes) and nodes[i]:
                    nodes[i].next = nodes[i+1]
            if len(level) > 0:
                q.append(level)
        return root