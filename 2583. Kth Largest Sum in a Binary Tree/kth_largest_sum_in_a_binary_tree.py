# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([])
        queue.append((root, 0))

        level_sums = []
        curr_level = 0
        curr_level_sum = 0
        while queue:
            node, level = queue.popleft()
            if level != curr_level:
                heapq.heappush(level_sums, -curr_level_sum)
                curr_level = level
                curr_level_sum = 0
            curr_level_sum += node.val
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        heapq.heappush(level_sums, -curr_level_sum)

        if len(level_sums) < k:
            return -1

        while k > 1:
            heapq.heappop(level_sums)
            k -= 1

        return -heapq.heappop(level_sums)