"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        res = []
        stack = deque([root])
        last_node = None

        while stack:
            node = stack[-1]
            if node.children and last_node not in node.children:
                for child in reversed(node.children):
                    stack.append(child)
            else:
                res.append(node.val)
                last_node = stack.pop()

        return res