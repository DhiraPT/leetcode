# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node = root
        parent = None
        while node and key != node.val:
            parent = node
            if key < node.val:
                node = node.left
            else:
                node = node.right

        if not node:
            return root

        if not node.left or not node.right:
            new_node = node.right if not node.left else node.left

            if not parent:
                return new_node

            if node == parent.left:
                parent.left = new_node
            else:
                parent.right = new_node

        else:
            successor_parent = node
            successor = node.right
            while successor.left:
                successor_parent = successor
                successor = successor.left

            node.val = successor.val

            if successor_parent != node:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        return root