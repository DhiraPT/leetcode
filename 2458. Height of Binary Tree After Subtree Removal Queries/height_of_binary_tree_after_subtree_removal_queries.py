# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        node_level_height = {}
        level_heights = defaultdict(list)

        def dfs(node, level):
            if not node:
                return 0
            height = max(dfs(node.left, level + 1), dfs(node.right, level + 1))
            node_level_height[node.val] = (level, height)
            level_heights[level].append(height)
            return height + 1

        dfs(root, 0)

        for heights in level_heights.values():
            heights.sort(reverse=True)

        res = []
        for q in queries:
            l, h = node_level_height[q]
            heights = level_heights[l]
            if heights[0] == h:
                res.append(node_level_height[root.val][1] - h + (heights[1] if len(heights) > 1 else -1))
            else:
                res.append(node_level_height[root.val][1])

        return res