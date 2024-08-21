# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def calculate(node):
            if node.val == 2:
                return calculate(node.left) or calculate(node.right)
            elif node.val == 3:
                return calculate(node.left) and calculate(node.right)
            else:
                return node.val

        return calculate(root)