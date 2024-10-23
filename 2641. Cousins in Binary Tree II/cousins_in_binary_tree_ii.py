# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([])
        queue.append(root)

        prev_sum = root.val
        while queue:
            length = len(queue)
            curr_sum = 0
            for i in range(length):
                node = queue.popleft()
                left_val, right_val = node.left.val if node.left else 0, node.right.val if node.right else 0
                if node.left:
                    curr_sum += node.left.val
                    if node.right:
                        node.left.val += right_val
                    queue.append(node.left)
                if node.right:
                    curr_sum += node.right.val
                    if node.left:
                        node.right.val += left_val
                    queue.append(node.right)
                node.val = prev_sum - node.val
            prev_sum = curr_sum

        return root