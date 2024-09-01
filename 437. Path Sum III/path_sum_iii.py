# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val
            count = prefix_sums.get(curr_sum - targetSum, 0)
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1

            count += dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
            prefix_sums[curr_sum] -= 1

            return count

        prefix_sums = {0: 1}

        return dfs(root, 0)