class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_amount = 0
        l = 0
        r = len(height) - 1
        while l < r:
            if height[l] < height[r]:
                max_amount = max(max_amount, height[l] * (r - l))
                l += 1
            else:
                max_amount = max(max_amount, height[r] * (r - l))
                r -= 1
        return max_amount