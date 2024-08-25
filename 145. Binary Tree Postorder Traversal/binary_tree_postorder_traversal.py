# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = deque()
        res = []
        last_node = None

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack[-1]
                if root.right and last_node != root.right:
                    root = root.right
                else:
                    stack.pop()
                    res.append(root.val)
                    last_node = root
                    root = None

        return res