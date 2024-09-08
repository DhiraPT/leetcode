# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(node, lnode):
            if not lnode:
                return True
            if not node:
                return False
            if node.val == lnode.val:
                return dfs(node.left, lnode.next) or dfs(node.right, lnode.next)
            return False

        def transverse(node):
            if not node:
                return False
            if dfs(node, head):
                return True
            return transverse(node.left) or transverse(node.right)

        return transverse(root)