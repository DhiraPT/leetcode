# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left, length):
            if not node:
                return length

            if is_left:
                return max(dfs(node.right, False, length + 1), dfs(node.left, True, 0))
            else:
                return max(dfs(node.left, True, length + 1), dfs(node.right, False, 0))

        return max(dfs(root.left, True, 0), dfs(root.right, False, 0))